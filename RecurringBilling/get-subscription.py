import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def get_subscription(subscriptionId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey


	getSubscription = apicontractsv1.ARBGetSubscriptionRequest()
	getSubscription.merchantAuthentication = merchantAuth
	getSubscription.subscriptionId = subscriptionId

	getSubscriptionController = ARBGetSubscriptionController(getSubscription)
	getSubscriptionController.execute()

	response = getSubscriptionController.getresponse()

	if (response.messages.resultCode=="Ok"):
		print ("Subscription Name : %s" % response.subscription.name)
	else:
		print ("response code: %s" % response.messages.resultCode)

	return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
	get_subscription(constants.subscriptionId)