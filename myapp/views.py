from django.shortcuts import render, redirect
from.models import InfoModel
# Create your views here.

def info_list(request):
    info=InfoModel.objects.all()
    context = {
        'info' :info
    }
    return render(render,'index.html',context)


def info_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        InfoModel.objects.create(
            name = name,
            email = email,
            phone = phone

        )

        return redirect('info_list')
    return render(request, 'info_create.html')