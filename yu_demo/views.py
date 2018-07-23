# -*- coding: utf-8 -*-
from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_request

def test1(request):
    client = get_client_by_request(request)
    client.set_bk_api_ver('v2')
    kwargs = {}
    result = client.cc.search_business(kwargs)
    return render_mako_context(request, '/yudemo/inf.html', {
        'bk_biz_list': result.get('data').get('info')
    })

#@csrf_exempt
#@login_exempt
def get_app_info(request):
    # 从环境配置获取APP信息，从request获取当前用户信息
    client = get_client_by_request(request)
    client.set_bk_api_ver('v2')
    kwargs = {}
    result = client.cc.search_business(kwargs)
    return render_mako_context(request, '/yudemo/inf.html', {
        'bk_biz_list': result.get('data').get('info')
    })
