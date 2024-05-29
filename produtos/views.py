from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

# Create your views here.

def cadastrar(request):
    if request.method == "GET":
        erro = request.GET.get("codigo_erro")
        texto = request.GET.get("texto")
        return render(request, "cadastrar.html", {"erro": erro, "texto": texto})
    elif request.method == "POST":
        produto = request.POST["produto"] #ou request.POST.get("produto")
        preco = request.POST.get("preco")

        if len(produto) <= 0:
            return redirect("/produtos/cadastrar/?codigo_erro=1&texto=O nome do produto não pode estar em branco")
        else:
            produto = Produto(
                nome_produto = produto,
                preco_produto = preco
            )

            produto.save()

        return redirect("/produtos/listar/") 

        #return HttpResponse(f"Seu produto {produto} com o preço {preco}, foi cadastrado com sucesso!")
    
def listar(request):
    filtrar_produto = request.GET.get("filtrar_produto")
    
    if filtrar_produto:
        produtos = Produto.objects.filter(nome_produto__icontains=filtrar_produto)
    else:
        produtos = Produto.objects.all()

    return render(request, "listar.html", {"produtos": produtos})

def deletar(request, id):
    produto = Produto.objects.get(id = id)
    produto.delete()

    return redirect("/produtos/listar/")

def alterar(request, id):
    if request.method == 'GET':
        produto = Produto.objects.get(id=id)
        return render(request, 'alterar.html', {'produto': produto})
    if request.method == 'POST':
        nome_produto = request.POST.get('produto')
        preco = request.POST.get('preco')

        produto = Produto.objects.get(id=id)

        produto.nome_produto = nome_produto
        produto.preco_produto = preco

        produto.save()

        return redirect(listar)

