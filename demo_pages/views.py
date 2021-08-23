from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.generic.base import TemplateView
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.

data={
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

@csrf_exempt
def test(request):
    if request.method=="GET":
        return JsonResponse({
            "test_msg":"success",
            "method":request.method
        })
    return JsonResponse({
        "test_msg":"failed",
        "method":request.method
    })

class TestView(View):
    def get(self, request):
        return HttpResponse("its get method")    
    def post(self, request):
        return HttpResponse("its post method")
    def put(self, request):
        return HttpResponse("its put method")
    def delete(self, request):
        return HttpResponse("its delete method")

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TestView, self).dispatch(request, *args, **kwargs)


def index(request):   
    return render(request, 'index.html', context=data)


class IndexPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(data)
        return context


def page2(request):
    return render(request, 'page2.html')