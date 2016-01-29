import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def authorization_only():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	paypal = apicontractsv1.payPalType()
	paypal.successUrl = "http://www.merchanteCommerceSite.com/Success/TC25262"
	paypal.cancelUrl = "http://www.merchanteCommerceSite.com/Success/TC25262"

	payment = apicontractsv1.paymentType()
	payment.payPal = paypal

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.amount = Decimal('55.00')
	transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.authOnlyTransaction
	transactionrequest.payment = payment

	request = apicontractsv1.createTransactionRequest()
	request.merchantAuthentication = merchantAuth
	request.refId = "Sample"
	request.transactionRequest = transactionrequest

	controller = createTransactionController(request)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
	    print "SUCCESS"
	    print "Message Code : %s" % response.messages.message[0].code
	    print "Message text : %s" % response.messages.message[0].text
	    print "Secure acceptance URL : %s " % response.transactionResponse.secureAcceptance.SecureAcceptanceUrl
	    print "Transaction ID : %s " % response.transactionResponse.transId
	else:
	    print "ERROR"
	    print "Message Code : %s" % response.messages.message[0].code
	    print "Message text : %s" % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	authorization_only()
