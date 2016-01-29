import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def create_customer_payment_profile(customerProfileId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	creditCard = apicontractsv1.creditCardType()
	creditCard.cardNumber = "4111111111111111"
	creditCard.expirationDate = "2020-12"

	payment = apicontractsv1.paymentType()
	payment.creditCard = creditCard

	profile = apicontractsv1.customerPaymentProfileType()
	profile.payment = payment

	createCustomerPaymentProfile = apicontractsv1.createCustomerPaymentProfileRequest()
	createCustomerPaymentProfile.merchantAuthentication = merchantAuth
	createCustomerPaymentProfile.paymentProfile = profile
	createCustomerPaymentProfile.customerProfileId = customerProfileId

	controller = createCustomerPaymentProfileController(createCustomerPaymentProfile)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
		print "Successfully created a customer payment profile with id: %s" % response.customerPaymentProfileId
	else:
		print "Failed to create customer payment profile %s" % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	create_customer_payment_profile(constants.customerProfileId)