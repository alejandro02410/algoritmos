from django.shortcuts import render
from . models import endNum


def muestra_datos(request):
    consulta = endNum.objects.all()
    contexto = {'data': consulta}
    return render(request, 'prueba2/index.html',contexto)

#def calculaSuma(l):
 #   listaSuma=[]
  #  for i in l:
   #     r = i.x1 + i.x2 + i.x3
    #    listaSuma.append(r)
    #return listaSuma

