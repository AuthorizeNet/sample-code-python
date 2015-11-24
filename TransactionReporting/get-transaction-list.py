from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

transactionListRequest = apicontractsv1.getTransactionListRequest()
transactionListRequest.merchantAuthentication = merchantAuth
transactionListRequest.batchId = "4551107"

transactionListController = getTransactionListController(transactionListRequest)

transactionListController.execute()

transactionListResponse = transactionListController.getresponse()

if transactionListResponse is not None:
	if transactionListResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
		print('Successfully got transaction list!')

		for transaction in transactionListResponse.transactions.transaction:
			print('Transaction Id : %s' % transaction.transId)
			print('Transaction Status : %s' % transaction.transactionStatus)
			print('Amount Type : %s' % transaction.accountType)
			print('Settle Amount : %s' % transaction.settleAmount)

		if transactionListResponse.messages:
			print('Message Code : %s' % transactionListResponse.messages.message[0].code)
			print('Message Text : %s' % transactionListResponse.messages.message[0].text)
	else:
		if transactionListResponse.messages:
			print('Failed to get transaction list.\nCode:%s \nText:%s' % (transactionListResponse.messages.message[0].code,transactionListResponse.messages.message[0].text))
