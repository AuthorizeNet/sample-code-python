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
	creditCard.cardNumber = "4111111111111111"
	creditCard.expirationDate = "2020-12"

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
	    print "Transaction ID : %s" % response.transactionResponse.transId
	else:
	    print "response code: %s" % response.messages.resultCode

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	refund_transaction(constants.transactionId)