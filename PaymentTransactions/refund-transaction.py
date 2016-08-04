import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def refund_transaction(refTransId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	creditCard = apicontractsv1.creditCardType()
	creditCard.cardNumber = "0015"
	creditCard.expirationDate = "XXXX"

	payment = apicontractsv1.paymentType()
	payment.creditCard = creditCard

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "refundTransaction"
	transactionrequest.amount = Decimal ('2.55')
	#set refTransId to transId of a settled transaction
	transactionrequest.refTransId = refTransId
	transactionrequest.payment = payment


	createtransactionrequest = apicontractsv1.createTransactionRequest()
	createtransactionrequest.merchantAuthentication = merchantAuth
	createtransactionrequest.refId = "MerchantID-0001"

	createtransactionrequest.transactionRequest = transactionrequest
	createtransactioncontroller = createTransactionController(createtransactionrequest)
	createtransactioncontroller.execute()

	response = createtransactioncontroller.getresponse()

	if (response.messages.resultCode=="Ok"):
	    print ("Transaction ID : %s" % response.transactionResponse.transId)
	else:
	    print ("response code: %s" % response.messages.resultCode)
	    print ("Message code: %s" % response.messages.message[0]['code'].text)
	    print ("Message text: %s" % response.messages.message[0]['text'].text)
	    print ("Transaction Error Code: %s" % response.transactionResponse.errors.error[0].errorCode)
	    print ("Transaction Error Text: %s" % response.transactionResponse.errors.error[0].errorText)

	return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
	refund_transaction(constants.transactionId)
