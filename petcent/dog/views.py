from django.shortcuts import render,redirect
from .models import Dog,Review
from django.shortcuts import get_object_or_404
from .forms import ReviewForm

# Create your views here.

def doghome(request):
    searchTerm=request.GET.get('searchDog')
    if searchTerm:
        dogs=Dog.objects.filter(title=searchTerm)
    else:
        dogs=Dog.objects.all()
    return render(request,'doghome.html',{'searchTerm':searchTerm,'dogs':dogs})

def dogdetail(request,dog_id):
    dog=get_object_or_404(Dog,pk=dog_id)
    return render(request,'dogdetail.html',{'dog':dog})

def createdogreview(request,dog_id):
    dog = get_object_or_404(Dog,pk=dog_id)
    if request.method=='GET':
        return render(request,'createdogreview.html',{'form':ReviewForm,'dog':dog})
    else:
        try:
            form=ReviewForm(request.POST)
            newReview=form.save(commit=False)
            newReview.user=request.user
            newReview.dog=dog
            newReview.save()
            return redirect('dogdetail',newReview.dog.id)
        except ValueError:
            return render(request,'createdogreview.html',{'form':ReviewForm,'error':'非法数据'})

