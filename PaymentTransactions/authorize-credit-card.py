import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def authorize_credit_card(amount):

	# Create a merchantAuthenticationType object with authentication details
	# retrieved from the constants file
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	# Create the payment data for a credit card
	creditCard = apicontractsv1.creditCardType()
	creditCard.cardNumber = "4111111111111111"
	creditCard.expirationDate = "2020-12"
	creditCard.cardCode = "123"

	# Add the payment data to a paymentType object
	payment = apicontractsv1.paymentType()
	payment.creditCard = creditCard
	
	# Create order information
	order = apicontractsv1.orderType()
	order.invoiceNumber = "10101"
	order.description = "Golf Shirts"
	
	# Set the customer's Bill To address
	customerAddress = apicontractsv1.customerAddressType()
	customerAddress.firstName = "Ellen"
	customerAddress.lastName = "Johnson"
	customerAddress.company = "Souveniropolis"
	customerAddress.address = "14 Main Street"
	customerAddress.city = "Pecan Springs"
	customerAddress.state = "TX"
	customerAddress.zip = "44628"
	customerAddress.country = "USA"
	
	# Set the customer's identifying information
	customerData = apicontractsv1.customerDataType()
	customerData.type = "individual"
	customerData.id = "99999456654"
	customerData.email = "EllenJohnson@example.com"
	
	# Add values for transaction settings
	duplicateWindowSetting = apicontractsv1.settingType();
	duplicateWindowSetting.settingName = "duplicateWindow"
	duplicateWindowSetting.settingValue = "600"

	# Create a transactionRequestType object and add the previous objects to it.
	transactionrequest = apicontractsv1.transactionRequestType()
	transactionrequest.transactionType = "authOnlyTransaction"
	transactionrequest.amount = amount
	transactionrequest.payment = payment
	transactionrequest.order = order
	transactionrequest.billTo = customerAddress
	transactionrequest.customer = customerData
	transactionrequest.transactionSettings = duplicateWindowSetting

	# Assemble the complete transaction request
	createtransactionrequest = apicontractsv1.createTransactionRequest()
	createtransactionrequest.merchantAuthentication = merchantAuth
	createtransactionrequest.refId = "MerchantID-0001"
	createtransactionrequest.transactionRequest = transactionrequest
	# Create the controller
	createtransactioncontroller = createTransactionController(createtransactionrequest)
	createtransactioncontroller.execute()

	response = createtransactioncontroller.getresponse()

	if response is not None:
		# Check to see if the API request was successfully received and acted upon
		if response.messages.resultCode == "Ok":
			# Since the API request was successful, look for a transaction response
			# and parse it to display the results of authorizing the card
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
		# Or, print errors if the API request wasn't successful
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
	authorize_credit_card(constants.amount)
