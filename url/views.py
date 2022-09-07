from imp import IMP_HOOK
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world")

def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choices(string.ascii_letters) #explaination: https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
                            for x in range(10))
            url = form.cleaned_data["url"]
            new_url = UrlData(url=url, slug=slug)
            new_url.save()
            request.user.urlshort.add(new_url)
            return  redirect('/')
    else:
        form = Url()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)

def UrlRedirect(request, slugs):
    data = UrlData.object.get(slug=slugs)
    return redirect(data.url)