from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from books.models import Book
from books.models import Author
def search_form(request):
    return render_to_response('search_form.html')



def search_results(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        aid = Author.objects.get(name=q)
        books=Book.objects.filter(authorid=aid.authorid)
        return render_to_response('search_results.html',
            {'books': books, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')


def information(request):
        t = request.GET['id']
        book=Book.objects.get(title=t)
        a=Author.objects.get(authorid= book.authorid)
        return render_to_response('information.html',{'book':book,'author':a})

def delete(request):
        ti = request.GET['id']
        book=Book.objects.get(title=ti)
        book.delete()
        return render_to_response('delete.html')

def renew(request):   
    
   
    if 'id' in request.GET and request.GET['id']: 
        tt = request.GET['id']
        book=Book.objects.get(title=tt)
        return render_to_response('renew.html',{'book':book})       
    else:
            pu=request.GET['pu']
            bn=request.GET['bn']
            pud=request.GET['pud']
            pr=request.GET['pr']
            na=request.GET['na']
          
            bk=Book.objects.get(title=bn)
            ar=Author.objects.get(authorid= bk.authorid)
            ar.name=na
            ar.authorid+=1 
            ar.save()

            bk.publisher=pu
            bk.price=pr
            bk.publication_date=pud
            bk.authorid+=1
            bk.save()
            return render_to_response('delete.html')
def new(request):
    if 'na' in request.GET and request.GET['na']:
            pu=request.GET['pu']
            bn=request.GET['bn']
            pud=request.GET['pud']
            pr=request.GET['pr']
            na=request.GET['na']
            ag=request.GET['ag']
            co=request.GET['co']
            ib=request.GET['ib']
            ai=request.GET['ai']
            a2=Author(name=na,authorid=ai,country=co,age=ag)
            a2.save()
            b2=Book(authorid=ai,title=bn,isbn=ib,price=pr,publisher=pu,publication_date=pud)
            b2.save()
            return render_to_response('delete.html')
    else:
        return  render_to_response('new.html')
            
        
            
