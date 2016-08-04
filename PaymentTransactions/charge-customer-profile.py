import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def charge_customer_profile(customerProfileId, paymentProfileId, amount):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

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
		print ("Transaction ID : %s" % response.transactionResponse.transId)
	else:
		print ("response code: %s" % response.messages.resultCode)

	return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
	charge_customer_profile(constants.customerProfileId, constants.customerPaymentProfileId, constants.amount)
