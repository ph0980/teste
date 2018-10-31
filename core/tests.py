from django.test import TestCase
from django.shortcuts import render
from .views import *

# Create your tests here.
test__index():
    request='index'
    assert index(request) == render(request,'index.html')

