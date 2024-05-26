from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
import json

def vatandas_chatbox(request):
    return render(request, 'chatbox.html')

# -------------------- Chatbox Fonksiyonları --------------------
with open("gemini_key.txt") as keyfile:
    key = keyfile.read()

genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

@csrf_exempt
def chat_with_gemini(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        prompt = data.get('prompt', '')

        response = model.generate_content(prompt)

        return JsonResponse({'response': response.text})