# -*- coding: utf-8 -*-
from common.mymako import render_mako_context, render_json


def test1(request):
    return render_mako_context(request, '/yudemo/inf.html', {})

#@csrf_exempt
#@login_exempt
def get_app_info(request):
    return render_json({
        'name':'test',
        'result':True,
        'data':request.GET.get('name'),
        'message':'success'
    })