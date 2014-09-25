from django.http import HttpResponse

from django.template import Context
from django.template.loader import get_template

from mysite.demo_lab.models import vInfra
from mysite.demo_lab.models import Emails

from django.core.mail import EmailMessage
import requests
import time

def hello(request):
	return HttpResponse("Hello World")

def avi(request):
	avi_ctrl = vInfra.objects.get(name="vCenter Avi")
	email_receivers = Emails.objects.all()
	email_list = ''
	version = ''
	first = True
	for entry in email_receivers:
		if first:
			email_list = email_list + str(entry)
			first = False
		else:
			email_list = email_list + ', ' + str(entry)

	try: 
		r = requests.get('https://%s/api/virtualservice-inventory-summary/?step=5&limit=360'%avi_ctrl.ip, auth=('admin','avi123'), verify=False, timeout=3)
		data = r.json()
		if data['count']>=4:
			health = 'I feel lucky!'
			for hs in data['results']:
				if hs['realtime_scores']['health_score'] < 10: 
					health = 'I have a bad feeling about this!'
					break
		else:
			health = 'I have a bad feeling about this!'
		r = requests.get('https://%s/api/initial-data?format=json'%avi_ctrl.ip, auth=('admin','avi123'), verify=False, timeout=1)
		data = r.json()
		version = str(data['version']['Version']) + ' B' +  str(data['version']['build']) + ', ' + str(data['version']['Date'])

	except:
		health = 'Something bad happened!'
		
	t = get_template('avi.html')

	html = t.render(Context({'ip': avi_ctrl.ip, 'email_receivers': email_list, 'health_status': health, 'version': version}))

	return HttpResponse(html)

def update(request):
	message = "Successfully updated!"
	if 'ip' in request.GET and 'passwd' in request.GET:
		password = request.GET['passwd']
		if password == "avinetworks":
			avi_ctrl = vInfra.objects.get(name="vCenter Avi")
			avi_ctrl.ip = request.GET['ip']
			avi_ctrl.save()
			send_update_email(avi_ctrl.ip)
		else:
			message = "Invalid password. Go away!"
	else:
		message = "Trying to hack? Goood luck with that ^^;"
	t = get_template('generic.html')
	html = t.render(Context({"message": message}))

	return HttpResponse(html)

def send_update_email(ip):
	email_list = Emails.objects.all()
	for email in email_list:
		receiver = str(email)
		body = """A new Avi Controller IP is %s. 

To unsubscribe this E-mail, click http://10.10.5.64/unsubscribe/?email=%s""" %(ip, receiver)


		email = EmailMessage("[Auto Alert] Demo system update", body, to=[receiver])
		email.send()

	return()

def remove_email(email):
	try:
		entry= Emails.objects.get(email=email)
		entry.delete()
		message = "%s is unsubscribed" %email
	except:
		if email == '':
			message = "The E-mail field is empty"
		else :	
			message = "%s does not exist" %email

	return message

def add_email(email):
	if Emails.objects.filter(email=email).exists() :
		message = "%s already exists" %email
	else :
		if email != '':
			entry = Emails(email=email)
			entry.save()
			message = "%s is added to the subscription list" %email
		else:
			message = "The E-mail field is empty"

	return message

def subscribe(request):
	if request.GET['action'] == 'subscribe':
		message = add_email(request.GET['email'])
	else:
		message = remove_email(request.GET['email'])

	t = get_template('generic.html')
	html = t.render(Context({"message": message}))

	return HttpResponse(html)

def avi_version(request):
    r = requests.get("https://10.10.5.81/api/initial-data?format=json", auth=("admin", "avi123"), verify=False)
    data = r.json()
    version = str(data['version']['Version']) + ' B' +  str(data['version']['build']) + ', ' + str(data['version']['Date'])

    return HttpResponse(version)

def avi_health(request):
    time.sleep(0)
    return HttpResponse("I've a good feeling about this.")

