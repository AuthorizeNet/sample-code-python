from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

request = apicontractsv1.ARBCancelSubscriptionRequest()
request.merchantAuthentication = merchantAuth
request.refId = "Sample"
request.subscriptionId = "2945617"

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