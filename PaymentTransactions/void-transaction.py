import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

def void_transaction(refTransId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'


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
	    print "Transaction ID : %s" % response.transactionResponse.transId
	    print response.transactionResponse.messages.message[0].description
	else:
	    print "response code: %s" % response.messages.resultCode
	    print response.transactionResponse.errors.error[0].errorText

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	void_transaction()