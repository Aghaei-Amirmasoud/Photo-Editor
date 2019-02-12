from random import randint
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import default_storage
from PIL import Image
from shalgham import settings
import glob, os
import pathlib



def index(request):
    return render(request, 'fileuploader/index.html', {
        'lst': [1, 2, 3, 4, 5, 'salam'],
    })


def upload(request):
    try :
        photo_url = default_storage.save('file.jpg', request.FILES['fileToUpload'])
        context = {'image' : photo_url}
        request.session['Url'] = photo_url;
        return render(request, 'fileuploader/edit.html', context)
    except :
        return HttpResponse('No photo chosen')


def gray(request):
    try :
        img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
        img_grayed= img.convert("L")
        img_grayed.save(os.path.join(settings.MEDIA_ROOT,  request.session['Url']))
        context = {'image' : request.session['Url']}
        return render(request, 'fileuploader/edit.html', context)
    except :
        return HttpResponse('No photo uploaded')


def crop(request):
    try :
        img = Image.open(os.path.join(settings.MEDIA_ROOT,  request.session['Url']))
        img_croped = img.crop((int(request.POST.get('box1')), int(request.POST.get('box2')), int(request.POST.get('box3')), int(request.POST.get('box4'))))
        img_croped.save(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
        context = {'image' : request.session['Url']}
        return render(request, 'fileuploader/edit.html', context)
    except :
        return HttpResponse('chek: 1-image was not uploaded  2-you entered string  3-you entered nothing'
        + ' 4-crop parameter shoud not be greater than width and height'
        + ' 5-first parameter should be >= third'
        + ' 6-forth parameter should be >= second'
        )

def resize(request):
    try :
        img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
        img_resized = img.resize((int(request.POST.get('rebox1')), int(request.POST.get('rebox2'))))
        img_resized.save(os.path.join(settings.MEDIA_ROOT,  request.session['Url']))
        context = {'image' : request.session['Url']}
        return render(request, 'fileuploader/edit.html', context)
    except :
        return HttpResponse('chek: 1-image was not uploaded  2-you entered string  3-you entered nothing'
        + ' 4-width and height size must be greater than zero'
        + ' 5-number you entered is tooo high!!'
        )

def rotate(request):
    try :
        img = Image.open(os.path.join(settings.MEDIA_ROOT,  request.session['Url']))
        img_rotated = img.rotate(int(request.POST.get('rtbox1')), expand=1)
        img_rotated.save(os.path.join(settings.MEDIA_ROOT ,  request.session['Url']))
        context = {'image' : request.session['Url']}
        return render(request, 'fileuploader/edit.html', context)
    except :
        return HttpResponse('chek: 1-image was not uploaded  2-you entered string  3-you entered nothing')





def remove(request):
    return redirect('/')

def share(request):
    img = Image.open(os.path.join(settings.MEDIA_ROOT, request.session['Url']))
    img.save(os.path.join(settings.SHARE_ROOT, request.session['Url']))
    path = os.path.join(settings.SHARE_ROOT)
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    lst_image = []
    for file in range(len(files)-1,-1,-1):
        lst_image.append(files[file])
    return render(request, 'fileuploader/sharepanel.html', {
        'lst_image': lst_image,
        })
