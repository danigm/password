from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from siteapp.forms import SiteForm
from siteapp.models import Site

from django.utils import simplejson as json


def stat_site(site):
    site.rate = 0
    site.votes = site.work + site.notwork
    if site.work + site.notwork:
        site.rate = site.work / float(site.votes)

    return site


def index(request):
    if request.method == 'POST':
        searching = request.POST['search']
        return HttpResponseRedirect(reverse(search,
            kwargs={'q': searching}))
    return render_to_response('siteapp/index.html',
            context_instance=RequestContext(request))


def real_search(q):
    sites = [stat_site(site) for site in
                Site.objects.filter(siteurl__contains=q).order_by('-work')]
    return sites


def search(request, q):
    sites = real_search(q)
    form = SiteForm(initial={'siteurl': q})
    context = {'q': q, 'sites': sites, 'form': form}
    return render_to_response('siteapp/search.html',
            context,
            context_instance=RequestContext(request))


def jsonsearch(request, q):
    sites = real_search(q)
    return HttpResponse(serializers.serialize("json", sites),
                        mimetype='application/json')


def real_vote(id, vote):
    site = Site.objects.get(id=id)
    vote = int(vote)
    if vote:
        site.work += 1
    else:
        site.notwork +=1
    site.save()
    return site


def vote(request, id, vote):
    site = real_vote(id, vote)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def jsonvote(request, id, vote):
    site = stat_site(real_vote(id, vote))
    response = {'status': 'ok', 'rate': site.rate, 'votes': site.votes}
    return HttpResponse(json.dumps(response),
                        mimetype='application/json')


def submit(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(index))
    else:
        form = SiteForm()

    context = {'form': form}
    return render_to_response('siteapp/submit.html', 
            context,
            context_instance=RequestContext(request))
