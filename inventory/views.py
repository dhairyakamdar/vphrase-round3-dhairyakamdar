from django.shortcuts import render,redirect,get_object_or_404 
from .forms import *
from .models import *
#from django.forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')



def display_mobiles(request):
    items = phone.objects.all()
    context = {
        'items' : items,
    }

    return render(request, 'index.html', context)


def add_device(request,cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect ('index')

    else:
        form = cls()
        return render (request, 'add_new.html', {'form':form})

def add_mobile(request):
    return add_device(request,mobileform)


def edit_device(request,pk,model,cls):
    item = get_object_or_404(model,pk=pk)

    if request.method == "POST":
        form =mobileform(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form' : form})

def edit_mobile(request,pk):
    return edit_device(request,pk,phone,mobileform)

def del_mobile(request,pk):
    phone.objects.filter(id=pk).delete()

    items=phone.objects.all()
    
    context ={
        'items' : items
    }
    return render(request, 'index.html',context)


# def search(request):
#     if request.method == 'GET' :
#         mobile_name = request.GET.get('search')
#         try :
#             status=mobile.objects.filter(name__icontains=mobile_name)
#         except mobile.DoesNotExist:
#             status=None
#         return render(request,"search.html",{"books":status})
#     else :
#         return render(request,"search.html",{})

# def search(request):

#     if request.method == 'GET':
#         form = new_form(request.POST)
#         if form.is_valid():
#             search_query = request.GET.get('search', None)
#             if search_query:
#                 mobile = mobile.objects.filter(name__icontains=search_query)
                
