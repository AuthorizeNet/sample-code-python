from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

validateCustomerPaymentProfile = apicontractsv1.validateCustomerPaymentProfileRequest()
validateCustomerPaymentProfile.merchantAuthentication = merchantAuth
validateCustomerPaymentProfile.customerProfileId = "36731856"
validateCustomerPaymentProfile.customerPaymentProfileId = "33211899"
validateCustomerPaymentProfile.validationMode = "testMode"

validateCustomerPaymentProfileCntrlr = validateCustomerPaymentProfileController(validateCustomerPaymentProfile)
validateCustomerPaymentProfileCntrlr.execute()

response = validateCustomerPaymentProfileCntrlr.getresponse()

if (response.messages.resultCode=="Ok"):
	print response.messages.message[0].text
else:
	print "ERROR :  Validate Customer Payment Profile: Invalid response"
	print "response code: %s %s" % {response.messages.message[0].code, response.messages.message[0].text}
