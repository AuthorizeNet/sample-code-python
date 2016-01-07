import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

def get_subscription(subscriptionId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'


	getSubscription = apicontractsv1.ARBGetSubscriptionRequest()
	getSubscription.merchantAuthentication = merchantAuth
	getSubscription.subscriptionId = subscriptionId

	getSubscriptionController = ARBGetSubscriptionController(getSubscription)
	getSubscriptionController.execute()

	response = getSubscriptionController.getresponse()

	if (response.messages.resultCode=="Ok"):
		print "Subscription Name : %s" % response.subscription.name
	else:
		print "response code: %s" % response.messages.resultCode

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	get_subscription("1232321")