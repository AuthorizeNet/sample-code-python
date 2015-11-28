from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

createCustomerProfileFromTransaction = apicontractsv1.createCustomerProfileFromTransactionRequest()
createCustomerProfileFromTransaction.merchantAuthentication = merchantAuth
createCustomerProfileFromTransaction.transId = '2238147175'

createCustomerProfileFromTransactionController = createCustomerProfileFromTransactionController(createCustomerProfileFromTransaction)
createCustomerProfileFromTransactionController.execute()

response = createCustomerProfileFromTransactionController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully created a customer profile with id: %s from transaction id: %s" % {response.customerProfileId, createCustomerProfileFromTransaction.transId}
else:
	print "Failed to create customer payment profile from transaction %s" % response.messages.message[0].text
