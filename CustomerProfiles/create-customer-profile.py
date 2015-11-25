from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
import random

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'


createCustomerProfile = apicontractsv1.createCustomerProfileRequest()
createCustomerProfile.merchantAuthentication = merchantAuth
createCustomerProfile.profile = apicontractsv1.customerProfileType('jdoe' + str(random.randint(0, 10000)), 'John2 Doe', 'jdoe@mail.com')

createCustomerProfileController = createCustomerProfileController(createCustomerProfile)
createCustomerProfileController.execute()

response = createCustomerProfileController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully created a customer profile with id: %s" % response.customerProfileId
else:
	print "Failed to create customer payment profile %s" % response.messages.message[0].text
