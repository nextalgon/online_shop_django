from django.http import HttpResponse
from django.shortcuts import render
from .models import Mahsulot, Toifa
from django.core.paginator import Paginator



def index(request):
    mahsulotlar = Mahsulot.objects.all()
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'kategoriyalar': toifalar, 'mahsulotlar': mahsulotlar})


def category(request, category_id):
    page = request.GET.get('page')
    toifa = Toifa.objects.get(pk=category_id)
    all_mahsulotlar = Mahsulot.objects.filter(toifasi=toifa)
    paginator = Paginator(all_mahsulotlar, 3)
    mahsulotlar = paginator.get_page(page)
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'kategoriyalar': toifalar, 'mahsulotlar': mahsulotlar})

# def one(request):
#     return render(request, 'shop/bir.html')
#     # return HttpResponse('<a href="{% url \'two\'%}"><button>2</button></a>'
#     #                     '<a href="{% url \'three\'%}"><button>3</button></a>'
#     #                     '<a href="{% url \'four\'%}"><button>4</button></a>'
#     #                     '<a href="{% url \'five\'%}"><button>5</button></a>'
#     #                     '<a href="{% url \'six\'%}"><button>6</button></a> <hr><br>'
#     #                     '<h1>Bu sahifa №1!<h1> <br>'
#     #                     '<a href="{% url \'index\'%}"><button>Home</button></a>'
#     #                     '<a href="{% url \'two\'%}"><button>next</button></a>')
#
#
# def two(request):
#     return render(request, 'shop/ikki.html')
#     # return HttpResponse('<a href="{% url \'one\'%}"><button>1</button></a>'
#     #                     '<a href="{% url \'three\'%}"><button>3</button></a>'
#     #                     '<a href="{% url \'four\'%}"><button>4</button></a>'
#     #                     '<a href="{% url \'five\'%}"><button>5</button></a>'
#     #                     '<a href="{% url \'six\'%}"><button>6</button></a> <hr><br>'
#     #                     '<h1>Bu sahifa №2!<h1> <br>'
#     #                     '<a href="{% url \'one\'%}"><button>prev</button></a>'
#     #                     '<a href="{% url \'index\'%}"><button>Home</button></a>'
#     #                     '<a href="{% url \'three\'%}"><button>next</button></a>')
#
#
# def three(request):
#     return render(request, 'shop/uch.html')
#     # return HttpResponse('<a href="{% url \'one\'%}"><button>1</button></a>'
#     #                     '<a href="{% url \'two\'%}"><button>2</button></a>'
#     #                     '<a href="{% url \'four\'%}"><button>4</button></a>'
#     #                     '<a href="{% url \'five\'%}"><button>5</button></a>'
#     #                     '<a href="{% url \'six\'%}"><button>6</button></a> <hr><br>'
#     #                     '<h1>Bu sahifa №3!<h1> <br>'
#     #                     '<a href="{% url \'two\'%}"><button>prev</button></a>'
#     #                     '<a href="{% url \'index\'%}"><button>Home</button></a>'
#     #                     '<a href="{% url \'four\'%}"><button>next</button></a>')
#
#
# def four(request):
#     return render(request, 'shop/turt.html')
#     # return HttpResponse('<a href="{% url \'one\'%}"><button>1</button></a>'
#     #                     '<a href="{% url \'two\'%}"><button>2</button></a>'
#     #                     '<a href="{% url \'three\'%}"><button>3</button></a>'
#     #                     '<a href="{% url \'five\'%}"><button>5</button></a>'
#     #                     '<a href="{% url \'six\'%}"><button>6</button></a> <hr><br>'
#     #                     '<h1>Bu sahifa №4!<h1> <br>'
#     #                     '<a href="{% url \'three\'%}"><button>prev</button></a>'
#     #                     '<a href="{% url \'index\'%}"><button>Home</button></a>'
#     #                     '<a href="{% url \'five\'%}"><button>next</button></a>')
#
#
# def five(request):
#     return render(request, 'shop/besh.html')
#     # return HttpResponse('<a href="{% url \'one\'%}"><button>1</button></a>'
#     #                     '<a href="{% url \'two\'%}"><button>2</button></a>'
#     #                     '<a href="{% url \'three\'%}"><button>3</button></a>'
#     #                     '<a href="{% url \'four\'%}"><button>4</button></a>'
#     #                     '<a href="{% url \'six\'%}"><button>6</button></a> <hr><br>'
#     #                     '<h1>Bu sahifa №5!<h1> <br>'
#     #                     '<a href="{% url \'four\'%}"><button>prev</button></a>'
#     #                     '<a href="{% url \'index\'%}"><button>Home</button></a>'
#     #                     '<a href="{% url \'six\'%}"><button>next</button></a>')
#
#
# def six(request):
#     return render(request, 'shop/olti.html')
#     # return HttpResponse('<a href="{% url \'one\'%}"><button>1</button></a>'
#     #                     '<a href="{% url \'two\'%}"><button>2</button></a>'
#     #                     '<a href="{% url \'three\'%}"><button>3</button></a>'
#     #                     '<a href="{% url \'four\'%}"><button>4</button></a>'
#     #                     '<a href="{% url \'five\'%}"><button>5</button></a> <hr><br>'
#     #                     '<h1>Bu sahifa №6!<h1> <br>'
#     #                     '<a href="{% url \'five\'%}"><button>prev</button></a>'
#     #                     '<a href="{% url \'index\'%}"><button>Home</button></a>')
# def test(request):
#     return HttpResponse("<h1>Siz so'ragan TEST!</h1>")

