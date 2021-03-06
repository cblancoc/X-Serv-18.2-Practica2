from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from models import Table
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def form(request):
    if request.method == "GET":
        out = ""
        form = '<form action="" method="POST">'
        form += 'URL a acortar: <input type="text" name="real_url">'
        form += '<input type="submit" value="Enviar">'
        form += '</form>'

        out += form
        list = Table.objects.all()
        if list:
            out += "The previous searches are: "
            out += "<html><body><ul>\n"
            for i in list:
                out += "<li><a href=" + str(i.id) + ">"
                out += i.real_url + "</a></li>\n"
            out += "</ul></body></html>"
        else:
            out += "There are no previous searches on this page"
            out += "</ul></body></html>"
        return HttpResponse(out)
    elif request.method == "PUT" or request.method == "POST":
        out = ""
        url = request.body
        url = url.split("real_url=")[1]
        if url == "":
            return HttpResponseBadRequest("Empty url")
        elif not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        else:
            url = url.split("%3A%2F%2F")[0]
        try:
            new = Table.objects.get(real_url=request.body)
        except Table.DoesNotExist:
            new = Table(real_url=url)
            new.save()

        out += ("<html><body>" + "URL buscada: "
                + "<a href=" + url + ">" + url + "</href></br>"
                + "URL acortada: " + "<a href=" + str(new.id) + ">"
                + str(new.id) + "</href></br>" + "</body></html>")
        return HttpResponse(out)


def redirect(request, resource):
    try:
        url = Table.objects.get(id=resource)
    except Table.DoesNotExist:
        return HttpResponseNotFound("Page not found")
    return HttpResponseRedirect(url.real_url)
