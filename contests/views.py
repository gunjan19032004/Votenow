from accounts.utils import decode_data
from django.shortcuts import render, redirect

<<<<<<< HEAD

from .forms import UploadQrcodeForm
=======
from .forms import UploadQrcodeForm, CreateContestForm
>>>>>>> contestform
from .models import *

import cv2 as cv
import numpy as np
import os

def home(request):
    context = {}
    return render(request,'contests/index.html', context)

def verify(request):
    if request.method == 'POST':
        
        form = UploadQrcodeForm(request.POST, request.FILES)
        if form.is_valid():
            qrcode_str = request.FILES['qrcode'].read()
            npimg = np.fromstring(qrcode_str, np.uint8)
            im = cv.imdecode(npimg, cv.IMREAD_COLOR)
            det = cv.QRCodeDetector()
            retval, points, straight_qrcode = det.detectAndDecode(im)
            email = decode_data(retval)
            print(email)
            return redirect('contest:home')
    else:
        form = UploadQrcodeForm()
        context = {'form':form}
        return render(request, 'contests/verify.html', context)
        

def contest(request):
    if request.method == 'POST':
        form= CreateContestForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateContestForm()
        context = {'forms':form}
        return render(request, 'contests/contest.html', context)