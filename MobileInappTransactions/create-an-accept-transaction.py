import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def create_an_accept_transaction():

	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	opaquedata = apicontractsv1.opaqueDataType()
	opaquedata.dataDescriptor = "COMMON.ACCEPT.INAPP.PAYMENT"
	opaquedata.dataValue = "9471471570959063005001"

	paymentOne = apicontractsv1.paymentType()
	paymentOne.opaqueData = opaquedata

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.authCaptureTransaction
	transactionrequest.amount = Decimal('151')
	transactionrequest.payment = paymentOne

	request = apicontractsv1.createTransactionRequest()
	request.merchantAuthentication = merchantAuth
	request.refId = "Sample"
	request.transactionRequest = transactionrequest

	controller = createTransactionController(request)
	controller.execute()

	response = controller.getresponse()

	if response is not None:
		if response.messages.resultCode == "Ok":
			if response.transactionResponse.responseCode == 1:
				print ('Successfully created transaction with Transaction ID: %s' % response.transactionResponse.transId);
				print ('Description: %s' % response.transactionResponse.messages.message[0].description);
				print ('AUTH Code : %s' % response.authCode)
			else:
				print ('Failed Transaction.');
				if hasattr(response.transactionResponse, 'errors') == True:
					print ('Error Code:  %s' % str(response.transactionResponse.errors.error[0].errorCode));
					print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText);
		else:
			print ('Failed Transaction.');
			if hasattr(response, 'transactionResponse') == True and hasattr(response.transactionResponse, 'errors') == True:
				print ('Error Code: %s' % str(response.transactionResponse.errors.error[0].errorCode));
				print ('Error message: %s' % response.transactionResponse.errors.error[0].errorText);
			else:
				print ('Error Code: %s' % response.messages.message[0]['code'].text);
				print ('Error message: %s' % response.messages.message[0]['text'].text);
	else:
		print ('Null Response.');

	return response

if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
	create_an_accept_transaction()
