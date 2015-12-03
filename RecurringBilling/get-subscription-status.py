from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
# Setting the mercahnt details
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'
# Seeting the request
request = apicontractsv1.ARBGetSubscriptionStatusRequest()
request.merchantAuthentication = merchantAuth
request.refId = "Sample"
request.subscriptionId = "294541"
# Executing the controller
controller = ARBGetSubscriptionStatusController(request)
controller.execute()
# Getting the response
response = controller.getresponse()

if (response.messages.resultCode=="Ok"):
	print "SUCCESS:"
	print "Message Code : %s" % response.messages.message[0].code
	print "Message text : %s" % response.messages.message[0].text
	print "Subscription Status : %s" % response.status
else:
	print "ERROR:" 
	print "Message Code : %s" % response.messages.message[0].code
	print "Message text : %s" % response.messages.message[0].text
