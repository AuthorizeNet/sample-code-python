import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')

def get_list_of_subscription():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	sorting = apicontractsv1.ARBGetSubscriptionListSorting()
	sorting.orderBy = apicontractsv1.ARBGetSubscriptionListOrderFieldEnum.id
	sorting.orderDescending = "false"

	paging = apicontractsv1.Paging()
	paging.limit = 1000
	paging.offset = 1

	request = apicontractsv1.ARBGetSubscriptionListRequest()
	request.merchantAuthentication = merchantAuth
	request.refId = "Sample"
	request.searchType = apicontractsv1.ARBGetSubscriptionListSearchTypeEnum.subscriptionInactive
	request.sorting = sorting
	request.paging = paging

	controller = ARBGetSubscriptionListController(request)
	controller.execute()

	response = controller.getresponse()

	if (response.messages.resultCode=="Ok"):
	    print "SUCCESS"
	    print "Message Code : %s" % response.messages.message[0].code
	    print "Message text : %s" % response.messages.message[0].text
	    print "Total Number In Results : %s" % response.totalNumInResultSet
	else:
	    print "ERROR"
	    print "Message Code : %s" % response.messages.message[0].code
	    print "Message text : %s" % response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	get_list_of_subscription()