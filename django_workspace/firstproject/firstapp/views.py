from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'firstapp/main.html')


# 3. movie실행 => firstapp/movie.html 띄움
def movie(request):
    return render(request, 'firstapp/movie.html')


def details1(request):
    return render(request, 'firstapp/details1.html')

def details2(request):
    return render(request, 'firstapp/details2.html')


def details3(request):
    return render(request, 'firstapp/details3.html')

