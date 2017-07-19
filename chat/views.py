from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from .models import Comments, User
 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseServerError

from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
 
import redis
 
@login_required
def home(request):
	print(request.session.session_key)
	session = Session.objects.get(session_key=request.session.session_key)
	user_id = session.get_decoded().get('_auth_user_id')
	print(user_id)
	comments = Comments.objects.select_related().all()[0:100]
	return render(request, 'home.html', locals())

def node_api(request):
	try:
		#Get User from sessionid
		message = request.POST.get('comment')

		session = Session.objects.get(session_key=request.POST.get('session'))
		user_id = session.get_decoded().get('_auth_user_id')
		user = User.objects.get(id=user_id)

		#Create comment
		Comments.objects.create(user=user, text=message)

		#Once comment has been created post it to the chat channel
		r = redis.StrictRedis(host='localhost', port=6379, db=0)
		r.publish('chat', user.username + ': ' + request.POST.get('comment'))

		return HttpResponse("Everything worked :)")
	except Exception as e:
		return HttpResponseServerError(str(e))



