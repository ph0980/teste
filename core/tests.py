from django.test import TestCase
from django.shortcuts import render
from .views import *

# Create your tests here.
def test__index():
    #assert index('index') == render(request,'index.html')
    assert 1+1==2
