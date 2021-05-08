# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
# import dialogflowcx
import os
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Order
import argparse
import uuid
from django.contrib.auth.forms import UserCreationForm 
from google.cloud.dialogflowcx_v3beta1.services.agents import AgentsClient
from google.cloud.dialogflowcx_v3beta1.services.sessions import SessionsClient
from google.cloud.dialogflowcx_v3beta1.types import session
#from dialogflow_v2 import dialogflow_v2 as Dialogflow
# Create your views here.
from django.contrib import messages 
from .forms import UserRegistrationForm
@require_http_methods(['GET'])
def index_view(request):
    return render(request, 'chathome.html')

def home_view(request):
    return render(request, 'home.html')

def reg_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # user.profile.email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            messages.success(request,"Account Created for %s is created. Login!" %username)
            return redirect('login') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form':form})

def convert(data):
    if isinstance(data, bytes):
        return data.decode('ascii')
    if isinstance(data, dict):
        return dict(map(convert, data.items()))
    if isinstance(data, tuple):
        return map(convert, data)

    return data

@csrf_exempt
@require_http_methods(['POST'])
def chat_view(request):
    print('Body', request.body)
    input_dict = convert(request.body)
    input_text = json.loads(input_dict)['text']

    GOOGLE_AUTHENTICATION_FILE_NAME = "AppointmentScheduler.json"
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

    project_id = "ivr-bot-goug"
    location_id = "global"
    agent_id = "c09ce1a3-c00d-452e-8781-f2b679f14a61"
    session_id = "1234567891"
    # context_short_name = "does_not_matter"
    agent = f"projects/{project_id}/locations/{location_id}/agents/{agent_id}"
    # context_name = "projects/" + GOOGLE_PROJECT_ID + "/agent/sessions/" + session_id + "/contexts/" + \
    #            context_short_name.lower()

    # parameters = dialogflow.types.struct_pb2.Struct()
    #parameters["foo"] = "bar"

    # context_1 = dialogflow.types.context_pb2.Context(
    #     name=context_name,
    #     lifespan_count=2,
    #     parameters=parameters
    # )
    # query_params_1 = {"contexts": [context_1]}

    language_code = 'en-us'
    
    response =  detect_intent_texts(agent, session_id, input_text, language_code)
 
    return HttpResponse(response.query_result.response_messages, status=200)

def detect_intent_texts(agent, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_path = f"{agent}/sessions/{session_id}"
    print(f"Session path: {session_path}\n")
    client_options = None
    agent_components = AgentsClient.parse_agent_path(agent)
    location_id = agent_components["location"]
    if location_id != "global":
        api_endpoint = f"{location_id}-dialogflow.googleapis.com:443"
        print(f"API Endpoint: {api_endpoint}\n")
        client_options = {"api_endpoint": api_endpoint}
    session_client = SessionsClient(client_options=client_options)
    text_input = session.TextInput(text=text)
    query_input = session.QueryInput(text=text_input, language_code=language_code)
    request = session.DetectIntentRequest(
        session=session_path, query_input=query_input
    )
    response = session_client.detect_intent(request=request)

    print("=" * 20)
    print(f"Query text: {response.query_result.text}")
    response_messages = [
        " ".join(msg.text.text) for msg in response.query_result.response_messages
    ]
    print(f"Response text: {' '.join(response_messages)}\n")
    return response

# def detect_intent_with_parameters(project_id, session_id, query_params, language_code, user_input):
#     """Returns the result of detect intent with texts as inputs.

#     Using the same `session_id` between requests allows continuation
#     of the conversaion."""
#     session_client = dialogflow.SessionsClient()

#     session = session_client.session_path(project_id, session_id)
#     print('Session path: {}\n'.format(session))

#     #text = "this is as test"
#     text = user_input

#     text_input = dialogflow.types.TextInput(
#         text=text, language_code=language_code)

#     query_input = dialogflow.types.QueryInput(text=text_input)

#     response = session_client.detect_intent(
#         session=session, query_input=query_input,
#         query_params=query_params
#     )

#     print('=' * 20)
#     print('Query text: {}'.format(response.query_result.query_text))
#     print('Detected intent: {} (confidence: {})\n'.format(
#         response.query_result.intent.display_name,
#         response.query_result.intent_detection_confidence))
#     print('Fulfillment text: {}\n'.format(
#         response.query_result.fulfillment_text))

#     return response
    

def about(request):
    return render(request, 'chat/about.html')
