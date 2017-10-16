from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from books.models import Book

def search_form(request):
    return render_to_response('search_form.html')

"""
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        books=Book.objects.filter(title__icontains=q)   #获取标题里包含q的书籍，不区分大小写
        return render_to_response('search_results.html',
                                  {'books':books,'query':q})
        #message='You searched for %s' % request.GET['q']
    else:
        return render_to_response('search_form.html',{'error':True})
        #return HttpResponse('Please submit a search term.')
        #message='You submitted an empty form.'
    #return HttpResponse(message)
"""
def search(request):
    #error = False
    errors=[]
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            #error = True
            errors.append('enter a search term.')
        elif len(q) > 10:
            errors.append('please enter at most 10 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})















