from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os

from xml.dom import minidom
import xml.etree.ElementTree as ET
import random
import logging

dataPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/config/data.xml'
staticPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/static'
QuestionList = [0,1]

def index(request):
    tree = ET.parse(dataPath);
    root = tree.getroot();
    randowmQuestion = random.choice([0,1]);
    return render(request,"k6.html",{
    	"url": "url",
        "question_number": "1",
        "question_string": root[1][randowmQuestion][0].text,
        "answeer": root[1][randowmQuestion][1].text,
        "audio_url": root[1][randowmQuestion][2].text,
        "photo1_url" : root[1][randowmQuestion][3][0].text,
        "photo1_pos" : root[1][randowmQuestion][3][0].attrib.values,
        "photo2_url" : root[1][randowmQuestion][3][1].text,
        "photo2_pos" : root[1][randowmQuestion][3][1].attrib.values
        });

def loadmore(request):
    answeered = int(request.GET["answeered"]);
    quesExist = QuestionList[:];
    quesExist.remove(answeered);
    randowmQuestion = random.choice(quesExist);
    tree = ET.parse(dataPath);
    root = tree.getroot();
    return render(request,"k6Ajax.html",{
        "url": "url",
        "question_number": "2",
        "question_string": root[1][randowmQuestion][0].text,
        "answeer": root[1][randowmQuestion][1].text,
        "audio_url": root[1][randowmQuestion][2].text,
        "photo1_url" : root[1][randowmQuestion][3][0].text,
        "photo1_pos" : root[1][randowmQuestion][3][0].attrib.values,
        "photo2_url" : root[1][randowmQuestion][3][1].text,
        "photo2_pos" : root[1][randowmQuestion][3][1].attrib.values
        });