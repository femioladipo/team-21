from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from surveys.models import User, Response, Survey, SurveyQuestions, Question, UserSurvey
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return HttpResponse("Testing...")

@csrf_exempt
def survey_questions(request, forSurvey='all'):
    if request.method == 'GET':
        json_questions = fetchQuestions(forSurvey)
        print(json_questions)
        return JsonResponse(json_questions, safe=False)
    elif request.method == 'POST':
        # username = request.POST.get('username')
        # print(username)
        response_json = json.loads(request.body)
        print(response_json)
        user_name = response_json.get("user", "guest")
        surveyT = response_json.get("survey", "s_title")
        qid = response_json.get("qid", "1")
        rsp = response_json.get("response", "answer")

        usr = None
        resp = None
        survey_q = None
        try:
            usr = User.objects.get(username=user_name)
            resp = Response.objects.get(response_text=rsp)
            survey_q = SurveyQuestions.objects.filter(survey__title=surveyT, question=qid)[0]
        except:
            usr = User.objects.all()[0]
            resp = Response.objects.all()[0]
            survey_q = SurveyQuestions.objects.filter(survey__title=surveyT, question=qid)[0]

        userData = UserSurvey.objects.create(user=usr, survey_question=survey_q, response=resp)

        return HttpResponse("Working")

def surveys(request, survey='all'):
    json_surveys = fetchSurveys()
    print(json_surveys)
    return JsonResponse(json_surveys, safe=False)

def fetchSurveys():
    query = []
    query = Survey.objects.all()

    objList = []
    
    for data in query:
        objList.append({'title': data.title})

    json_query = json.dumps(objList)
    return json_query

def fetchQuestions(forSurvey='all'):
    query = []
    if forSurvey=='all':
        query = SurveyQuestions.objects.all()
    else:
        surveyId = -1
        try:
            surveyId = Survey.objects.get(title=forSurvey).id
        except Survey.DoesNotExist:
            surveyId = -1

        if surveyId >= 0:  
            query = SurveyQuestions.objects.filter(survey=surveyId)

    objList = []
    
    for data in query:
        objList.append({
            'id': data.question.id,
            'qtext': data.question.question_text,
            'qtype': data.question.qtype,
            })

    json_query = json.dumps(objList)
    return json_query


