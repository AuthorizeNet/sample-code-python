import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def update_split_tender_group():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey


	updateSplitTenderGroup = apicontractsv1.updateSplitTenderGroupRequest()
	updateSplitTenderGroup.merchantAuthentication = merchantAuth
	updateSplitTenderGroup.splitTenderId = "115901"
	enum = apicontractsv1.splitTenderStatusEnum
	updateSplitTenderGroup.splitTenderStatus = enum.voided


	updateSplitTenderController = updateSplitTenderGroupController(updateSplitTenderGroup)
	updateSplitTenderController.execute()

	response = updateSplitTenderController.getresponse()


	if (response.messages.resultCode=="Ok"):
	    print response.messages.message[0].text
	else:
	    print "response code: %s" % response.messages.resultCode
	    print response.messages.message[0].text

	return response

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	update_split_tender_group()