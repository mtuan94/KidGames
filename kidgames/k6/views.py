from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os

from xml.dom import minidom
import xml.etree.ElementTree as ET

dataPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/config/data.xml'
staticPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/static'
#elementtree
#root[cat id][quess id][...]
def index(request):
    tree = ET.parse(dataPath);
    root = tree.getroot();
    url = '/k6/q1/config.png'
    return render(request,"k6.html",{
    	"url": url,
        "question_string": root[1][0][0].text,
        "answeer": root[1][0][1].text,
        "audio_url": root[1][0][2].text,
        "photo1_url" : root[1][0][3][0].text,
        "photo1_pos" : root[1][0][3][0].attrib.values,
        "photo2_url" : root[1][0][3][1].text,
        "photo2_pos" : root[1][0][3][1].attrib.values
        });
