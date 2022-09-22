from django.shortcuts import render

# Create your views here.


def endNum(request):
    consulta = endNum.objects.all()
    contexto = {'datos ': consulta}
    return render(request, 'prueba2/index.html',)

def calculaSuma(l):
    listaSuma=[]
    for i in l:
        r = i.x1 + i.x2 + i.x3
        listaSuma.append(r)
    return listaSuma
