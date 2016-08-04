import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def void_transaction(refTransId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey


	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "voidTransaction"
	#set refTransId to transId of an unsettled transaction
	transactionrequest.refTransId = refTransId

	createtransactionrequest = apicontractsv1.createTransactionRequest()
	createtransactionrequest.merchantAuthentication = merchantAuth
	createtransactionrequest.refId = "MerchantID-0001"

	createtransactionrequest.transactionRequest = transactionrequest
	createtransactioncontroller = createTransactionController(createtransactionrequest)
	createtransactioncontroller.execute()

	response = createtransactioncontroller.getresponse()

	if (response.messages.resultCode=="Ok"):
	    print ("Transaction ID : %s" % response.transactionResponse.transId)
	    print (response.transactionResponse.messages.message[0].description)
	else:
	    print ("response code: %s" % response.messages.resultCode)
	    print (response.transactionResponse.errors.error[0].errorText)

	return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
	void_transaction(constants.transactionId)