from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home (request):
    return render(request,"index.html")


def result (request):
    cls = joblib.load('./CardHolder/finalized_model.sav')
    list = []
    list.append(request.POST['education'])
    list.append(request.POST['gender'])
    list.append(request.POST['marital'])
    list.append(request.POST['id'])
    list.append(request.POST['limit_bal'])
    list.append(request.POST['education'])
    list.append(request.POST['marital'])

    list.append(request.POST['pay1'])
    list.append(request.POST['pay2'])
    list.append(request.POST['pay3'])
    list.append(request.POST['pay4'])
    list.append(request.POST['pay5'])
    list.append(request.POST['pay6'])

    list.append(request.POST['bill1'])
    list.append(request.POST['bill2'])
    list.append(request.POST['bill3'])
    list.append(request.POST['bill4'])
    list.append(request.POST['bill5'])
    list.append(request.POST['bill6'])

    list.append(request.POST['pamt1'])
    list.append(request.POST['pamt2'])
    list.append(request.POST['pamt3'])
    list.append(request.POST['pamt4'])
    list.append(request.POST['pamt5'])
    list.append(request.POST['pamt6'])

    ans = cls.predict([list])

    print(list)

    return render(request,"result.html",{'ans':ans})
