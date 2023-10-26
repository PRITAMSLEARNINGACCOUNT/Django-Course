from django.http import HttpResponse


def Home_page(request):
    return HttpResponse("This is a home page")


def defination(request):
    return HttpResponse("Pipeline is a structure which has to be made before making a website using django.We are just learning pipeline in django and that's why we are not doing anything great just creating some pipeline and defining them with the number of pipeline.")

def pipeline_1(request):
    return HttpResponse('''This is a first pipeline<br>
                            <a href="http://127.0.0.1:8000/Home_page">Return to Home</a>
                        ''')


def pipeline_2(request):
    return HttpResponse('''This is a second pipeline<br>
                            <a href="http://127.0.0.1:8000/Home_page">Return to Home</a>
                        ''')


def pipeline_3(request):
    return HttpResponse('''This is a third pipeline<br>
                            <a href="http://127.0.0.1:8000/Home_page">Return to Home</a>
                        ''')


def pipeline_4(request):
    return HttpResponse('''This is a fourth pipeline<br>
                            <a href="http://127.0.0.1:8000/Home_page">Return to Home</a>
                        ''')


def pipeline_5(request):
    return HttpResponse('''This is a fifth pipeline<br>
                            <a href="http://127.0.0.1:8000/Home_page">Return to Home</a>
                        ''')
