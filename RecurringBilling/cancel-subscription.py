import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def cancel_subscription(subscriptionId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

	request = apicontractsv1.ARBCancelSubscriptionRequest()
	request.merchantAuthentication = merchantAuth
	request.refId = "Sample"
	request.subscriptionId = subscriptionId

	controller = ARBCancelSubscriptionController(request)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
	    print "SUCCESS"
	    print "Message Code : %s" % response.messages.message[0].code
	    print "Message text : %s" % response.messages.message[0].text
	else:
	    print "ERROR"
	    print "Message Code : %s" % response.messages.message[0].code
	    print "Message text : %s" % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	cancel_subscription()