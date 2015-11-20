from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'


getSubscription = apicontractsv1.ARBGetSubscriptionRequest()
getSubscription.merchantAuthentication = merchantAuth
getSubscription.subscriptionId = "2260421"

getSubscriptionController = ARBGetSubscriptionController(getSubscription)
getSubscriptionController.execute()

response = getSubscriptionController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Subscription Name : %s" % response.subscription.name
else:
	print "response code: %s" % response.messages.resultCode