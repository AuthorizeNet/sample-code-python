import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *

def get_unsettled_transaction_list():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	unsettledTransactionListRequest = apicontractsv1.getUnsettledTransactionListRequest()
	unsettledTransactionListRequest.merchantAuthentication = merchantAuth

	unsettledTransactionListController = getUnsettledTransactionListController(unsettledTransactionListRequest)

	unsettledTransactionListController.execute()

	unsettledTransactionListResponse = unsettledTransactionListController.getresponse()

	if unsettledTransactionListResponse is not None:
		if unsettledTransactionListResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
			print('Successfully got unsettled transaction list!')

			for transaction in unsettledTransactionListResponse.transactions.transaction:
				print('Transaction Id : %s' % transaction.transId)
				print('Transaction Status : %s' % transaction.transactionStatus)
				print('Amount Type : %s' % transaction.accountType)
				print('Settle Amount : %s' % transaction.settleAmount)

			if unsettledTransactionListResponse.messages:
				print('Message Code : %s' % unsettledTransactionListResponse.messages.message[0].code)
				print('Message Text : %s' % unsettledTransactionListResponse.messages.message[0].text)
		else:
			if unsettledTransactionListResponse.messages:
				print('Failed to get unsettled transaction list.\nCode:%s \nText:%s' % (unsettledTransactionListResponse.messages.message[0].code,unsettledTransactionListResponse.messages.message[0].text))

	return unsettledTransactionListResponse

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	get_unsettled_transaction_list()