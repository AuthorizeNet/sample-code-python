from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

getCustomerPaymentProfile = apicontractsv1.getCustomerPaymentProfileRequest()
getCustomerPaymentProfile.merchantAuthentication = merchantAuth
getCustomerPaymentProfile.customerProfileId = "36731856"
getCustomerPaymentProfile.customerPaymentProfileId = "33211899"

getCustomerPaymentProfileController = getCustomerPaymentProfileController(getCustomerPaymentProfile)
getCustomerPaymentProfileController.execute()

response = getCustomerPaymentProfileController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully retrieved a payment profile with profile id %s and customer id %s" % (getCustomerPaymentProfile.customerProfileId, getCustomerPaymentProfile.customerProfileId)	
else:
	print "response code: %s" % response.messages.resultCode
	print "Failed to get payment profile information with id %s" % getCustomerPaymentProfile.customerPaymentProfileId
