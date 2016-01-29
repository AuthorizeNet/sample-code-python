import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def charge_tokenized_credit_card():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	creditCard = apicontractsv1.creditCardType()
	creditCard.cardNumber = "4111111111111111"
	creditCard.expirationDate = "2020-12"
	creditCard.cryptogram = "EjRWeJASNFZ4kBI0VniQEjRWeJA="

	payment = apicontractsv1.paymentType()
	payment.creditCard = creditCard

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "authCaptureTransaction"
	transactionrequest.amount = Decimal ('1.5')
	transactionrequest.payment = payment

	createtransactionrequest = apicontractsv1.createTransactionRequest()
	createtransactionrequest.merchantAuthentication = merchantAuth
	createtransactionrequest.refId = "MerchantID-0001"
	createtransactionrequest.transactionRequest = transactionrequest

	createtransactioncontroller = createTransactionController(createtransactionrequest)
	createtransactioncontroller.execute()

	response = createtransactioncontroller.getresponse()

	if (response.messages.resultCode=="Ok"):
		print "SUCCESS"
		print "Message Code : %s" % response.messages.message[0].code
		print "Message text : %s" % response.messages.message[0].text
		print "Transaction ID : %s" % response.transactionResponse.transId
	else:
		print "ERROR"
		print "Message Code : %s" % response.messages.message[0].code
		print "Message text : %s" % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	charge_tokenized_credit_card()