from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.


def test(request):
    return JsonResponse({
        "test_msg":"success"
    })


def index(request):
    context={
        "name":"guru",
        "FullName":"Guruprasad BR",
        "city":"banglore",
        "programming_skills":[
            {
                "language":"javascript",
                "skill":"good"
            },
            {
                "language":"python",
                "skill":"good"
            },
            {
                "language":"c#",
                "skill":"beginner"
            },
            {
                "language":"c++",
                "skill":"moderate"
            }
        ]
    }

    return render(request, 'index.html', context=context)


def page2(request):
    return render(request, 'page2.html')