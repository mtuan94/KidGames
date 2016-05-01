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
    url = '/k6/q1/config.png'
    return render(request,"k6.html",{
    	"url": url,
        "question_string": root[0][1][0].text,
        "photo1_url" : root[0][1][2][0].text,
        "photo1_pos" : root[0][1][2][0].attrib.values,
        "photo2_url" : root[0][1][2][1].text,
        "photo2_pos" : root[0][1][2][1].attrib.values
        });
