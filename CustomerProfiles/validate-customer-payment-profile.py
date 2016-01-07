import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def validate_customer_payment_profile(customerProfileId, customerPaymentProfileId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

	validateCustomerPaymentProfile = apicontractsv1.validateCustomerPaymentProfileRequest()
	validateCustomerPaymentProfile.merchantAuthentication = merchantAuth
	validateCustomerPaymentProfile.customerProfileId = customerProfileId
	validateCustomerPaymentProfile.customerPaymentProfileId = customerPaymentProfileId
	validateCustomerPaymentProfile.validationMode = "testMode"

	validateCustomerPaymentProfileCntrlr = validateCustomerPaymentProfileController(validateCustomerPaymentProfile)
	validateCustomerPaymentProfileCntrlr.execute()

	response = validateCustomerPaymentProfileCntrlr.getresponse()

	if (response.messages.resultCode=="Ok"):
		print response.messages.message[0].text
	else:
		print "ERROR :  Validate Customer Payment Profile: Invalid response"
		print "response code: %s %s" % {response.messages.message[0].code, response.messages.message[0].text}

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	validate_customer_payment_profile()