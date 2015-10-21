from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.files import File

from models import Profile, Content

#write db info to README.md to present as cv
def index(request):
    profile = Profile.objects.get(id=1)
    intro = Content.objects.all().filter(category='intro')
    work_exp = Content.objects.all().filter(category='work_exp')
    education = Content.objects.all().filter(category='education')
    footnote = Content.objects.all().filter(category='footnote')
    template = loader.get_template('readme.template')
    context = RequestContext(request, {
        'profile': profile,
        'intro': intro,
        'work_exp': work_exp,
        'education': education,
        'footnote': footnote,
    })
    cv_output = template.render(context)
    with open('README.md', 'w') as f:
		myfile = File(f)
		myfile.write(cv_output)
		myfile.closed
		f.closed
    return HttpResponse('<img src="http://desktopclub.ru/files/wallpapers/source/desktopclub.ru_cartoons_yozhik_v_tumane_6226_1024x768.jpg" alt="jozik v tumane">')