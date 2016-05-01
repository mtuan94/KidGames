from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os

from xml.dom import minidom
import xml.etree.ElementTree as ET

dataPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/config/data.xml'
staticPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/static'

def index(request):
    tree = ET.parse(dataPath);
    root = tree.getroot();
    url = 	'/k5/q1/config.png'
    return render(request,"k5.html",{"data": root[0][0].text});
