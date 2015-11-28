from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

getCustomerProfileIds = apicontractsv1.getCustomerProfileIdsRequest()
getCustomerProfileIds.merchantAuthentication = merchantAuth

getCustomerProfileIdsController = getCustomerProfileIdsController(getCustomerProfileIds)
getCustomerProfileIdsController.execute()

response = getCustomerProfileIdsController.getresponse()

if (response.messages.resultCode=="Ok"):
	print "Successfully retrieved customer ids:"
	for identity in response.ids.numericString:
		print identity
else:
	print "response code: %s" % response.messages.resultCode
