import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

def charge_customer_profile(customerProfileId, paymentProfileId, amount):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

	# create a customer payment profile
	profileToCharge = apicontractsv1.customerProfilePaymentType()
	profileToCharge.customerProfileId = customerProfileId
	profileToCharge.paymentProfile = apicontractsv1.paymentProfile()
	profileToCharge.paymentProfile.paymentProfileId = paymentProfileId

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "authCaptureTransaction"
	transactionrequest.amount = amount
	transactionrequest.profile = profileToCharge


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
	charge_customer_profile()
