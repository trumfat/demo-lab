from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

from mysite.demo_lab.models import vInfra
from mysite.demo_lab.models import Emails

from django.core.mail import EmailMessage
import requests

def version(request):
    r = requests.get("https://10.10.5.81/api/initial-data?format=json", auth=("admin", "avi123"), verify=False)
    data = r.json()

