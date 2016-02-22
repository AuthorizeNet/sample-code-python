import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def void(refTransId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	paypal = apicontractsv1.payPalType()

	payment = apicontractsv1.paymentType()
	payment.payPal = paypal

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.voidTransaction
	transactionrequest.refTransId = refTransId
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
	    if (response.transactionResponse.responseCode == "1" ):
	        print "Transaction ID : %s " % response.transactionResponse.transId
	        print "Description : %s " % response.transactionResponse.messages.message[0].description
	else:
	    print "ERROR"
	    print "Message Code : %s" % response.messages.message[0].code
	    print "Message text : %s" % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	void(constants.transactionId)