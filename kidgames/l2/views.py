from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import os

from xml.dom import minidom
import xml.etree.ElementTree as ET
import random

dataPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/config/data.xml'
staticPath = os.path.normpath(os.path.join(os.path.dirname(__file__),'..')) + '/static'
QuestionList = [0,1,2]

def index(request):
    tree = ET.parse(dataPath);
    root = tree.getroot();
    randowmQuestion = random.choice(QuestionList);
    return render(request,"l2.html",{
    	"url": "url",
        "question_number": root[5][randowmQuestion][0].text,
        "question_string": root[5][randowmQuestion][1].text,
        "answeer": root[5][randowmQuestion][2].text,
        "audio_url": root[5][randowmQuestion][3].text,
        "photo1_url" : root[5][randowmQuestion][4][0].text,
        "photo2_url" : root[5][randowmQuestion][4][1].text,
        "photo3_url" : root[5][randowmQuestion][4][2].text,
        "photo4_url" : root[5][randowmQuestion][4][3].text,
        });

def loadmore(request):
    answeered = int(request.GET["answeered"]);
    quesExist = QuestionList[:];
    quesExist.remove(answeered);
    randowmQuestion = random.choice(quesExist);
    tree = ET.parse(dataPath);
    root = tree.getroot();
    return render(request,"l2Ajax.html",{
        "url": "url",
        "question_number": root[5][randowmQuestion][0].text,
        "question_string": root[5][randowmQuestion][1].text,
        "answeer": root[5][randowmQuestion][2].text,
        "audio_url": root[5][randowmQuestion][3].text,
        "photo1_url" : root[5][randowmQuestion][4][0].text,
        "photo2_url" : root[5][randowmQuestion][4][1].text,
        "photo3_url" : root[5][randowmQuestion][4][2].text,
        "photo4_url" : root[5][randowmQuestion][4][3].text,
        });