from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

transactionDetailsRequest = apicontractsv1.getTransactionDetailsRequest()
transactionDetailsRequest.merchantAuthentication = merchantAuth
transactionDetailsRequest.transId = "2239287784"

transactionDetailsController = getTransactionDetailsController(transactionDetailsRequest)

transactionDetailsController.execute()

transactionDetailsResponse = transactionDetailsController.getresponse()

if transactionDetailsResponse is not None:
	if transactionDetailsResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
		print('Successfully got transaction details!')

		print('Transaction Id : %s' % transactionDetailsResponse.transaction.transId)
		print('Transaction Type : %s' % transactionDetailsResponse.transaction.transactionType)
		print('Transaction Status : %s' % transactionDetailsResponse.transaction.transactionStatus)
		print('Auth Amount : %s' % transactionDetailsResponse.transaction.authAmount)
		print('Settle Amount : %s' % transactionDetailsResponse.transaction.settleAmount)

		if transactionDetailsResponse.messages:
			print('Message Code : %s' % transactionDetailsResponse.messages.message[0].code)
			print('Message Text : %s' % transactionDetailsResponse.messages.message[0].text)
	else:
		if transactionDetailsResponse.messages:
			print('Failed to get transaction details.\nCode:%s \nText:%s' % (transactionDetailsResponse.messages.message[0].code,transactionDetailsResponse.messages.message[0].text))
