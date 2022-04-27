from django.shortcuts import get_object_or_404, render

from .forms import Remove_Instrument, Add_Instrument
from itertools import chain
from .models import Site, Site_equipment, Deployment, Equipment, Shop_log, Equipment_test
import logging
# Create your views here.

def home(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    return render(request, 'inventory/overview.html', context=context)

def station_detail(request, station_id):
    if request.method == 'POST':
        if 'remove' in request.POST:
            remove_form = Remove_Instrument(request.POST)
            add_form = Add_Instrument()
            if remove_form.is_valid():
                logger.warning(remove_form.cleaned_data)
                deployment = Deployment.objects.get(pk=remove_form.cleaned_data['deployment'])
                deployment.check_out = remove_form.get_datetime()
                deployment.save()
        elif 'add' in request.POST:
            remove_form = Remove_Instrument()
            add_form = Add_Instrument(request.POST)
            if add_form.is_valid():
                logger.warning(add_form.cleaned_data)
                deployment = Deployment(site_eq=Site_equipment.objects.get(pk=add_form.cleaned_data['site_eq']),
                                        instrument=add_form.cleaned_data['instrument'],
                                        check_in=add_form.get_datetime()
                                        )
                deployment.save()

    else:
        add_form = Add_Instrument()
        remove_form = Remove_Instrument()
    site = get_object_or_404(Site, id=station_id)
    equipment = Site_equipment.objects.filter(site=site)
    deployments = Deployment.objects.filter(site_eq_id__in=equipment).order_by('-check_in')
    deployments = [d for d in deployments if d.is_active]
    instruments = [i.instrument for i in deployments]
    tests = Equipment_test.objects.filter(instrument__in=instruments)

    context = {'site': site,
               'equipment': equipment,
               'deployments': deployments,
               'add_form': add_form,
               'remove_form': remove_form}
    return render(request, 'inventory/site_detail.html', context=context)

def station_history(request, station_id):
    site = get_object_or_404(Site, id=station_id)
    equipment = Site_equipment.objects.filter(site=site)
    deployments = Deployment.objects.filter(site_eq_id__in=equipment).order_by('-check_in')
    context = {'site': site,
               'equipment': equipment,
               'deployments': deployments}
    return render(request, 'inventory/site_detail.html', context=context)
logger = logging.getLogger(__name__)

def instrument_detail(request, equipment_pk):
    instrument = get_object_or_404(Equipment, pk=equipment_pk)
    deployments = Deployment.objects.filter(instrument=instrument).order_by('-check_in')
    shop_check_in = Shop_log.objects.filter(instrument=instrument).order_by('-check_in')
    deployments = sorted(chain(deployments, shop_check_in), key=lambda obj: obj.check_in, reverse=True)
    tests = Equipment_test.objects.filter(instrument=instrument).order_by('-test_date')
    add_form = Remove_Instrument()
    context = {
        'instrument': instrument,
        'deployments': deployments,
        'tests': tests,
        'add_form': add_form,
    }
    return render(request, 'inventory/instrument_detail.html', context=context)