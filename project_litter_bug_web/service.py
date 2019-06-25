import smtplib
from datetime import datetime

from django.contrib import messages
from django.utils import timezone

from content.models import Content
from litter.models import Litter
from project_litter_bug_web.forms import ContactForm
from project_litter_bug_web.settings import PLB_EMAIL_USER, PLB_EMAIL_PWD
from script.models import Script


def get_home_data():
    vid_lst = []
    gif_lst = []
    pic_lst = []
    sfx_lst = []

    script_data = Script.objects.get(pk=1)
    litter_id = script_data.litter_id
    status = script_data.status
    download = script_data.download

    life_stats = retrieve_life_stats()
    content_data = Content.objects.filter(litter_id=litter_id)

    for content in content_data:
        if content.type == 'vid':
            vid_lst.append(content.url)
        elif content.type == 'gif':
            gif_lst.append(content.url)
        elif content.type == 'pic':
            pic_lst.append(content.url)
        elif content.type == 'sfx':
            sfx_lst.append(content.url)

    return {
        'litter_id': litter_id,
        'status': status,
        'download': download,
        'vid_lst': vid_lst,
        'gif_lst': gif_lst,
        'pic_lst': pic_lst,
        'sfx_lst': sfx_lst,
        'life_stats': life_stats
    }


def get_results_data(request):
    month = int(request.GET.get('month'))
    day = int(request.GET.get('day'))
    year = int(request.GET.get('year'))
    litter_lst = Litter.objects.filter(created__year=year, created__month=month, created__day=day)
    litter_info = []

    for litter in litter_lst:
        life_weight = get_life_weight(litter.weight, litter.created)
        life_cost = calc_cost_for(life_weight)
        energy_waste = calc_energy_for(life_weight)
        emissions = calc_emissions_for(energy_waste)

        url = to_embedded_format(litter.url)
        litter_info.append({"url": url,
                            "title": litter.title,
                            "weight": litter.weight,
                            "energy_waste": energy_waste,
                            "emissions": emissions,
                            "life_cost": life_cost})

    return {
        'month': month,
        'day': day,
        'year': year,
        'litter_info': litter_info
    }


def retrieve_life_stats():
    total_life_time_weight = 0
    total_weight = 0
    data = dict()

    litter_lst = Litter.objects.all()
    for litter in litter_lst:
        life_weight = get_life_weight(litter.weight, litter.created)
        total_life_time_weight += life_weight
        total_weight += litter.weight

    data['total_energy'] = calc_energy_for(total_life_time_weight)
    data['total_cost'] = calc_cost_for(total_life_time_weight)
    data['total_weight'] = calc_gb_weight_for(total_weight)
    data['total_emissions'] = calc_emissions_for(data['total_energy'])
    data['total_litter'] = Litter.objects.all().count()

    most_recent_litter = Litter.objects.filter().order_by('-created')[:1]
    data['embedded_url'] = to_embedded_format(most_recent_litter[0].url)
    return data


def email_handler(request):
    result = False
    form = ContactForm(request.POST)
    if form.is_valid():
        if send_email(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message']):
            messages.add_message(request, messages.SUCCESS, 'Email successfully sent.')
            result = True
        else:
            messages.add_message(request, messages.ERROR, 'Sorry. Email could not be sent. Please try again.')
    else:
        messages.add_message(request, messages.ERROR, 'Sorry. Form could not be validated. Please try again.')

    return request, result, form


def send_email(name, email, message):
    try:
        email_text = """
        From: %s\n
        Subject: Project Litter Bug - Contact\n    
        Name: %s\n    
        %s
        """ % (email, name, message)
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(PLB_EMAIL_USER, PLB_EMAIL_PWD)
        server.sendmail(email, PLB_EMAIL_USER, email_text)
        server.close()
        return True
    except Exception as e:
        print(e)
        return False


def to_embedded_format(url):
    PREFIX = 'https://www.youtube.com/watch?v='
    offset = len(PREFIX)
    yt_code = url[offset:]
    return 'https://www.youtube.com/embed/' + yt_code + '?modestbranding=1'


def get_life_weight(weight, created):
    sec_to_hr = 360
    life_time = datetime.now(timezone.utc) - created
    return (calc_gb_weight_for(weight) * life_time.total_seconds()) / sec_to_hr


#TODO the fuck is this number?
def calc_gb_weight_for(weight):
    gigabyte = 1073741824
    return round(weight / gigabyte, 4)


def calc_cost_for(weight):
    cost_per_gig = 0.51  # $
    return round(weight * cost_per_gig, 2)


def calc_energy_for(weight):
    pow_per_gig = 5.12  # kWh
    return round(weight * pow_per_gig, 2)


def calc_emissions_for(energy):
    return round(energy * pow(7.07, -4), 2) #metric tons CO2 / kWh
