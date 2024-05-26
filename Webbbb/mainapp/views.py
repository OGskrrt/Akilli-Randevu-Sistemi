from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
import google.generativeai as genai
import json
from .models import Vatandas, Yetkili, Sifreler, Randevu

# -------------------- Genel Fonksiyonlar --------------------
def home(request):
    return render(request, 'mainpage.html')

# -------------------- Vatandaş Fonksiyonları --------------------
@csrf_exempt
def vatandas_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('username')
        password = data.get('password')
        try:
            sifre = Sifreler.objects.get(user_id=user_id)
            if sifre.password == password:
                vatandas = Vatandas.objects.get(id=user_id)
                refresh = RefreshToken.for_user(vatandas)
                return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return JsonResponse({'error': 'Invalid password'}, status=400)
        except Sifreler.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=400)
        except Vatandas.DoesNotExist:
            return JsonResponse({'error': 'Vatandas not found'}, status=400)
    return render(request, 'vatandas_login.html')

def vatandas_register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        vatandas = Vatandas.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone
        )

        Sifreler.objects.create(
            user_id=vatandas.id,
            password=password
        )

        messages.success(request, 'Kayıt başarıyla tamamlandı.')
        return redirect('vatandas_login')
    return render(request, 'vatandas_register.html')

def vatandas_chatbox(request):
    return render(request, 'chatbox.html')

def vatandas_home(request):
    return render(request, 'vatandas_home.html')

def vatandas_logout(request):
    logout(request)
    return redirect('vatandas_login')

def randevu_al(request):
    if request.method == 'POST':
        konu = request.POST.get('konu')
        tarih = request.POST.get('tarih')
        saat = request.POST.get('saat')
        try:
            vatandas = Vatandas.objects.get(id=request.user.id)
        except Vatandas.DoesNotExist:
            return JsonResponse({'error': 'Vatandas not found'}, status=400)

        yetkili = Yetkili.objects.order_by('?').first()

        Randevu.objects.create(
            Vatandas=vatandas,
            Yetkili=yetkili,
            Konu=konu,
            Tarih=tarih,
            Saat=saat
        )

        messages.success(request, 'Randevu başarıyla alındı.')
        return redirect('vatandas_home')

    return render(request, 'randevu_al.html')

# -------------------- Yetkili Fonksiyonları --------------------
@csrf_exempt
def yetkili_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('username')
        password = data.get('password')
        try:
            sifre = Sifreler.objects.get(user_id=user_id)
            if sifre.password == password:
                yetkili = Yetkili.objects.get(id=user_id)
                refresh = RefreshToken.for_user(yetkili)
                return JsonResponse({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            else:
                return JsonResponse({'error': 'Invalid password'}, status=400)
        except Sifreler.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=400)
        except Yetkili.DoesNotExist:
            return JsonResponse({'error': 'Yetkili not found'}, status=400)
    return render(request, 'yetkili_login.html')

def yetkili_home(request):
    return render(request, 'yetkili_home.html')

def randevular(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        randevu_id = request.POST.get('randevuId')
        vatandas_id = request.POST.get('vatandas')
        yetkili_id = request.POST.get('yetkili')
        konu = request.POST.get('konu')
        tarih = request.POST.get('tarih')
        saat = request.POST.get('saat')

        if action == 'add':
            Randevu.objects.create(
                Vatandas=Vatandas.objects.get(id=vatandas_id),
                Yetkili=Yetkili.objects.get(id=yetkili_id),
                Konu=konu,
                Tarih=tarih,
                Saat=saat
            )
        elif action == 'update':
            randevu = get_object_or_404(Randevu, id=randevu_id)
            randevu.Vatandas = Vatandas.objects.get(id=vatandas_id)
            randevu.Yetkili = Yetkili.objects.get(id=yetkili_id)
            randevu.Konu = konu
            randevu.Tarih = tarih
            randevu.Saat = saat
            randevu.save()
        return JsonResponse({'success': True})

    vatandaslar = Vatandas.objects.all()
    yetkililer = Yetkili.objects.all()
    randevular = Randevu.objects.select_related('Vatandas', 'Yetkili').all()
    return render(request, 'yetkili_randevular.html', {'vatandaslar': vatandaslar, 'yetkililer': yetkililer, 'randevular': randevular})

@csrf_exempt
def delete_randevu(request, randevu_id):
    if request.method == 'DELETE':
        randevu = get_object_or_404(Randevu, id=randevu_id)
        randevu.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def randevu_detay(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id)
    return JsonResponse({
        'id': randevu.id,
        'Vatandas': {'id': randevu.Vatandas.id, 'Ad': randevu.Vatandas.Ad, 'Soyad': randevu.Vatandas.Soyad},
        'Yetkili': {'id': randevu.Yetkili.id, 'first_name': randevu.Yetkili.first_name, 'last_name': randevu.Yetkili.last_name},
        'Konu': randevu.Konu,
        'Tarih': randevu.Tarih,
        'Saat': randevu.Saat,
    })

def search_randevular(request):
    term = request.GET.get('term')
    randevular = Randevu.objects.filter(Vatandas__Ad__icontains=term) | Randevu.objects.filter(Yetkili__first_name__icontains=term)
    randevu_list = list(randevular.values('id', 'Vatandas__Ad', 'Vatandas__Soyad', 'Yetkili__first_name', 'Yetkili__last_name', 'Konu', 'Tarih', 'Saat'))
    return JsonResponse({'randevular': randevu_list})

# -------------------- Yönetim Fonksiyonları --------------------
def admin_edit_authority(request):
    yetkililer = Yetkili.objects.all()
    if request.method == 'POST':
        action = request.POST.get('action')
        yetkili_id = request.POST.get('yetkiliid')
        if action == 'add':
            Yetkili.objects.create(
                id=request.POST.get('yetkiliid'),
                first_name=request.POST.get('yetkili_ad'),
                last_name=request.POST.get('yetkili_soyad'),
                specialization=request.POST.get('yetkili_uzmanlikalani'),
                department=request.POST.get('yetkili_bolumu')
            )
        elif action == 'update':
            yetkili = get_object_or_404(Yetkili, id=yetkili_id)
            yetkili.first_name = request.POST.get('yetkili_ad')
            yetkili.last_name = request.POST.get('yetkili_soyad')
            yetkili.specialization = request.POST.get('yetkili_uzmanlikalani')
            yetkili.department = request.POST.get('yetkili_bolumu')
            yetkili.save()
        elif action == 'delete':
            yetkili = get_object_or_404(Yetkili, id=yetkili_id)
            yetkili.delete()
        return redirect('admin_edit_authority')
    return render(request, 'edit_authority.html', {'yetkililer': yetkililer})

def search_authorities(request):
    term = request.GET.get('term')
    yetkililer = Yetkili.objects.filter(first_name__icontains=term) | Yetkili.objects.filter(last_name__icontains=term) | Yetkili.objects.filter(id__icontains=term)
    yetkili_list = list(yetkililer.values_list('id', 'first_name', 'last_name', 'specialization', 'department'))
    return JsonResponse({'yetkililer': yetkili_list})

def admin_edit_citizen(request):
    citizens = Vatandas.objects.all()
    return render(request, 'edit_citizen.html', {'citizens': citizens})

def edit_citizen_detail(request, id):
    citizen = get_object_or_404(Vatandas, id=id)
    if request.method == 'POST':
        citizen.Ad = request.POST.get('Ad')
        citizen.Soyad = request.POST.get('Soyad')
        citizen.DogumTarihi = request.POST.get('DogumTarihi')
        citizen.Cinsiyet = request.POST.get('Cinsiyet')
        citizen.TelefonNumarasi = request.POST.get('TelefonNumarasi')
        citizen.Adres = request.POST.get('Adres')
        citizen.save()
        return redirect('admin_edit_citizen')
    return render(request, 'edit_citizen_detail.html', {'citizen': citizen})


@csrf_exempt
def delete_citizen(request, id):
    citizen = get_object_or_404(Vatandas, id=id)
    if request.method == 'POST':
        citizen.delete()
        return redirect('admin_edit_citizen')
    return render(request, 'edit_citizen.html')


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
