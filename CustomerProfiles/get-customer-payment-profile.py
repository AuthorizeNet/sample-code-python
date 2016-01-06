import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def get_customer_payment_profile(customerProfileId, customerPaymentProfileId):

	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

	getCustomerPaymentProfile = apicontractsv1.getCustomerPaymentProfileRequest()
	getCustomerPaymentProfile.merchantAuthentication = merchantAuth
	getCustomerPaymentProfile.customerProfileId = customerProfileId
	getCustomerPaymentProfile.customerPaymentProfileId = customerPaymentProfileId

	controller = getCustomerPaymentProfileController(getCustomerPaymentProfile)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
		print "Successfully retrieved a payment profile with profile id %s and customer id %s" % (getCustomerPaymentProfile.customerProfileId, getCustomerPaymentProfile.customerProfileId)	
	else:
		print "response code: %s" % response.messages.resultCode
		print "Failed to get payment profile information with id %s" % getCustomerPaymentProfile.customerPaymentProfileId

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	get_customer_payment_profile()
