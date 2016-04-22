from django.shortcuts import render
from django.http import HttpResponse
from order.ys import Order
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.method == "POST":

		try:
			code = request.POST['code']
			if code != 'ysdeneme':
				print "Code error"
				return HttpResponse(status=500)
			print "Starting to order!"
			o = Order()
			o.give()
			print "Order done!"
			return HttpResponse(status = 200)
		except Exception as e:
			print e
			return HttpResponse(status = 500)
	return HttpResponse("Merhaba Dunya")

