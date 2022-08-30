from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    return render(request,"home.html")

@csrf_exempt
def availability(request):
    print("availability called")
    prize = int(request.POST.get("prize"))
    feet = int(request.POST.get("feet"))
    deliveryrange = int(request.POST.get("range"))
    deliverydate = int(request.POST.get("deliverydate"))
    print(type(prize), type(feet), type(deliverydate), type(deliveryrange))
    avilableidols = ""
    if feet < 5 or feet > 30:
        avilableidols = "we are not suerving at this height"
    elif prize < 10000 or prize > 100000:
        avilableidols = "we are not serving at this prize"
    elif deliveryrange > 10:
        return "we are not serving at this radius"
    elif deliverydate < 10:
        avilableidols =  "we cannot delever with in 10 days "
    else:
        avilableidols = "we have 50 idols at your prefference"
    context = {
        "availableidols" : avilableidols
    }
    return render(request, "availableidols.html", context=context)


