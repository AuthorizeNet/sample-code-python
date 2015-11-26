from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

creditcard = apicontractsv1.creditCardType()
creditcard.cardNumber = "4111111111111111"
creditcard.expirationDate = "2020-12"

payment = apicontractsv1.paymentType()
payment.creditCard = creditcard

subscription = apicontractsv1.ARBSubscriptionType()
subscription.payment = payment

request = apicontractsv1.ARBUpdateSubscriptionRequest()
request.merchantAuthentication = merchantAuth
request.refId = "Sample"
request.subscriptionId = "2945620"
request.subscription = subscription

controller = ARBUpdateSubscriptionController(request)
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