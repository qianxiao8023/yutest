# -*- coding: utf-8 -*-

from common.mymako import render_mako_context, render_json


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')

def multiplication_figure(request):
    multiplier = int(request.POST.get('multiplier'))
    multiplicand = int(request.POST.get('multiplicand'))
    mult_result = multiplier * multiplicand
    return render_json({'result':True, 'mult_result':mult_result})
def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')
