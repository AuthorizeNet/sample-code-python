import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *
from authorizenet.apicontractsv1 import bankAccountType, accountTypeEnum

def debit_bank_account():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey


	payment = apicontractsv1.paymentType()

	bankAccountType = apicontractsv1.bankAccountType()
	accountType = apicontractsv1.bankAccountTypeEnum
	bankAccountType.accountType = accountType.checking
	bankAccountType.routingNumber = "125000024"
	bankAccountType.accountNumber = "12345678"
	bankAccountType.nameOnAccount = "John Doe"

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "authCaptureTransaction"
	transactionrequest.amount = Decimal ('2.55')
	transactionrequest.payment = payment
	transactionrequest.payment.bankAccount = bankAccountType


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

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	debit_bank_account()