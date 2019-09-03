from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
import tensorflow as tf
import numpy as np
from accent.mlcode import create_mfcc,length_audio

# Create your views here.
def index(request):
    context={'person':'srikanth','age':19}
    return render(request,'accent/index.html',context)

def testing(request):
    return HttpResponse('This is another view ')

def predict(request):
    n='neutralindian1.wav'
    mfcc=[]
    target=[]
    mfcc_len=mlcode.length_audio(n)
    #print(mfcc_len)
    for i in range(0,mfcc_len,3):
        mfcc = mlcode.create_mfcc(n,i)
        mfcc = np.asarray(mfcc)
        mfcc = np.reshape(mfcc,(len(mfcc)*len(mfcc[0])))
        target.append(mfcc)
    target=np.asarray(target)
    md = create_model()
    md.load_weights('C:/Users/Mypc/Downloads/accent classification.h5')
    targ=md.predict(target)    
    print((targ))
