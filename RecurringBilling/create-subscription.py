from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *
from datetime import *
# Setting the merchant details
merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'
# Setting payment schedule
paymentschedule = apicontractsv1.paymentScheduleType()
paymentschedule.interval = apicontractsv1.CTD_ANON()
paymentschedule.interval.length = 1
paymentschedule.interval.unit = apicontractsv1.ARBSubscriptionUnitEnum.months
paymentschedule.startDate = datetime(2020, 8, 30)
paymentschedule.totalOccurrences = 12
paymentschedule.trialOccurrences = 1
# Giving the credit card info
creditcard = apicontractsv1.creditCardType()
creditcard.cardNumber = "4111111111111111"
creditcard.expirationDate = "2020-12"
payment = apicontractsv1.paymentType()
payment.creditCard = creditcard
# Setting billing information
billto = apicontractsv1.nameAndAddressType()
billto.firstName = "John"
billto.lastName = "Smith"
# Setting subscription details
subscription = apicontractsv1.ARBSubscriptionType()
subscription.name = "Sample Subscription"
subscription.paymentSchedule = paymentschedule
subscription.amount = Decimal('22.29')
subscription.trialAmount = Decimal('0.00')
subscription.billTo = billto
subscription.payment = payment
# Creating the request
request = apicontractsv1.ARBCreateSubscriptionRequest()
request.merchantAuthentication = merchantAuth
request.subscription = subscription
# Creating and executing the controller
controller = ARBCreateSubscriptionController(request)
controller.execute()
# Getting the response
response = controller.getresponse()

if (response.messages.resultCode=="Ok"):
	print "SUCCESS:"
	print "Message Code : %s" % response.messages.message[0].code
	print "Message text : %s" % response.messages.message[0].text
	print "Subscription ID : %s" % response.subscriptionId
else:
	print "ERROR:" 
	print "Message Code : %s" % response.messages.message[0].code
	print "Message text : %s" % response.messages.message[0].text



