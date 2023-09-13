import os
import sys
sys.path.insert(0, os.getcwd())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "price_comparison_site.settings")

import django
django.setup()

from search import two

from django.shortcuts import render
from search.models import Product

import numpy as np
import pandas as pd
from django_pandas.io import read_frame

from transformers import TFBertForMaskedLM
from transformers import AutoTokenizer

from collections import Counter


# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def search(request):
    return render(request, 'search/main.html')

def result(request, q):
    request.q_value = q
    print(request.session.get('query'))
    print(q)
    if request.session.get('query') != q:
        request.session['scraped'] = False
    if request.session.get('scraped') != True:
        Product.objects.all().delete()
        two.coupang(q)
        request.session['scraped'] = True
        request.session['query'] = q
    context = {
        'q': q,
        'page': 1,
        'result': Product.objects.all()[:20],
        'length': len(Product.objects.all()),
    }
    return render(request, 'search/result.html', context)

def result2(request, q, page):
    request.q_value = q
    print(request.session.get('query'))
    print(q)
    if request.session.get('query') != q:
        request.session['scraped'] = False
    if request.session.get('scraped') != True:
        Product.objects.all().delete()
        two.coupang(q)
        request.session['scraped'] = True
        request.session['query'] = q
    try:
        if page > len(Product.objects.all()) / 20:
            raise SyntaxError('')
        context = {
            'q': q,
            'page': page,
            'result': Product.objects.all()[(20*(page-1)):((20*(page-1))+20)],
            'length': len(Product.objects.all()),
        }
    except:
        context = {
            'q': q,
            'page': int(len(Product.objects.all())/20)+1,
            'result': Product.objects.all()[len(Product.objects.all())-20:len(Product.objects.all())],
            'length': len(Product.objects.all()),
        }
    finally:
        return render(request, 'search/result.html', context)
    
def result3(request, q):
    request.q_value = q

    qs = Product.objects.all()
    df = read_frame(qs)

    try:
        minstar = request.GET.get('minstar')
        if minstar is None:
            minstar = 0
        else:
            minstar = float(minstar)
    except:
        minstar = 0
    finally:
        pass

    try:
        minprice = request.GET.get('minprice')
        if minprice is None:
            minprice = 0
        else:
            minprice = int(minprice)
    except:
        minprice = 0
    finally:
        pass

    try:
        maxprice = request.GET.get('maxprice')
        if maxprice is None:
            maxprice = 2147483647
        else:
            maxprice = int(maxprice)
    except:
        maxprice = 2147483647
    finally:
        pass

    df2 = df.loc[(pd.to_numeric(df['price']) >= int(minprice)) & (pd.to_numeric(df['price']) <= int(maxprice)) & (pd.to_numeric(df['star']) >= float(minstar))]


    detail = request.GET.get('detail')
    if detail:
        model = TFBertForMaskedLM.from_pretrained('klue/bert-base', from_pt=True)
        tokenizer = AutoTokenizer.from_pretrained("klue/bert-base")
        token1 = Counter(tokenizer(detail)['input_ids'])
        similarity = []
        for idx in df2.index:
            token2 = Counter(tokenizer(df2.loc[idx,'product_name'])['input_ids'])
            intersection = sum((token1 & token2).values())
            union = sum((token1 | token2).values())
            similarity.append(intersection / union if union > 0 else 0.0)
        df2['sim'] = similarity
        df2 = df2.sort_values(by='sim',ascending=False)

        print(df2[:20].to_dict(orient='index'))

    context = {
        'q': q,
        'page': 1,
        'result': df2[:20].to_dict(orient='records'),
        'length': len(df2),
    }
    return render(request, 'search/detail.html', context)