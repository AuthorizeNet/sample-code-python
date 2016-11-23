import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def refund_transaction(refTransId):
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	creditCard = apicontractsv1.creditCardType()
	creditCard.cardNumber = "0015"
	creditCard.expirationDate = "XXXX"

	payment = apicontractsv1.paymentType()
	payment.creditCard = creditCard

	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "refundTransaction"
	transactionrequest.amount = Decimal ('2.55')
	#set refTransId to transId of a settled transaction
	transactionrequest.refTransId = refTransId
	transactionrequest.payment = payment


	createtransactionrequest = apicontractsv1.createTransactionRequest()
	createtransactionrequest.merchantAuthentication = merchantAuth
	createtransactionrequest.refId = "MerchantID-0001"

	createtransactionrequest.transactionRequest = transactionrequest
	createtransactioncontroller = createTransactionController(createtransactionrequest)
	createtransactioncontroller.execute()

	response = createtransactioncontroller.getresponse()

	if response is not None:
		if response.messages.resultCode == "Ok":
			if hasattr(response.transactionResponse, 'messages') == True:
				print ('Successfully created transaction with Transaction ID: %s' % response.transactionResponse.transId);
				print ('Transaction Response Code: %s' % response.transactionResponse.responseCode);
				print ('Message Code: %s' % response.transactionResponse.messages.message[0].code);
				print ('Description: %s' % response.transactionResponse.messages.message[0].description);
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
	refund_transaction(constants.transactionId)
