from django.shortcuts import render

# In order to show the form on views
from .forms import EmailForm, JoinForm
from .models import Join
import uuid

def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id

def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

# Create your views here.
def home(request):
    # This is issong Regular Django Forms

    # print("-------------------------------------------------------------------")
    # print(request)
    # print("-------------------------------------------------------------------")
    # print(request.POST)
    # print("-------------------------------------------------------------------")
    # print(request.COOKIES)
    # print("-------------------------------------------------------------------")
    # # print(request.META)
    # print(request.META.get("REMOTE_ADDR"))
    # print(request.META.get("HTTP_X_FORWARDED_FOR"))
    # print("-------------------------------------------------------------------")
    # print("")
    # # print("Email: %s" % request.POST["email"])
    # print("SessionID: %s" % request.COOKIES["sessionid"])
    # print("csrftoken: %s" % request.COOKIES["csrftoken"])
    # print("")
    # form = EmailForm(request.POST or None)
    # queryset = Join.objects.all()
    # if form.is_valid():
    #     email = form.cleaned_data['email']
    #     print (form.cleaned_data['email'])
    #     new_join, created = Join.objects.get_or_create(email=email)
    #     print(new_join, created)
    #     print(new_join.timestamp)
    # context = {"form": form, "queryset": queryset}

    #   This is using model forms

    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        # above line say, dont save it yet, as we might do something here
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
        # redirect here

        # new_join.ip_address = get_ip(request)

        # below line says save it now
        # new_join.save()


    context = {"form": form}
    template = 'home.html'
    return render(request, template, context)
