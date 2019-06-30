from django.http import Http404

def check_topic_owner(request, topic):
	if request.user != topic.owner:
		raise Http404