from django.shortcuts import render

# Create your views here.


def endNum(request):
    consulta = endNum.objects.all()
    contexto = {'datos ': consulta}
    return render(request, 'prueba2/index.html',)
