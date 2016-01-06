import os, sys

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

def get_customer_profile_ids():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = '5KP3u95bQpv'
	merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

	getCustomerProfileIds = apicontractsv1.getCustomerProfileIdsRequest()
	getCustomerProfileIds.merchantAuthentication = merchantAuth

	controller = getCustomerProfileIdsController(getCustomerProfileIds)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
		print "Successfully retrieved customer ids:"
		for identity in response.ids.numericString:
			print identity
	else:
		print "response code: %s" % response.messages.resultCode

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	get_customer_profile_ids()
