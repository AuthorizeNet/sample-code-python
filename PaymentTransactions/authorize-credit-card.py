import os, sys
import imp
import random

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def authorize_credit_card():

	amount = str(round(random.random()*100, 2)) 

	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	creditCard = apicontractsv1.creditCardType()
	creditCard.cardNumber = "4111111111111111"
	creditCard.expirationDate = "2020-12"

	payment = apicontractsv1.paymentType()
	payment.creditCard = creditCard

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "authOnlyTransaction"
	transactionrequest.amount = Decimal (amount)
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
	authorize_credit_card()