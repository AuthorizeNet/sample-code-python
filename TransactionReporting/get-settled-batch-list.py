import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
constants = imp.load_source('modulename', 'constants.py')
from decimal import *
from datetime import datetime, timedelta

def get_settled_batch_list():
	merchantAuth = apicontractsv1.merchantAuthenticationType()
	merchantAuth.name = constants.apiLoginId
	merchantAuth.transactionKey = constants.transactionKey

	settledBatchListRequest = apicontractsv1.getSettledBatchListRequest()
	settledBatchListRequest.merchantAuthentication = merchantAuth
	settledBatchListRequest.firstSettlementDate = datetime.now() - timedelta(days=31)
	settledBatchListRequest.lastSettlementDate = datetime.now()

	settledBatchListController = getSettledBatchListController(settledBatchListRequest)

	settledBatchListController.execute()

	settledBatchListResponse = settledBatchListController.getresponse()

	if settledBatchListResponse is not None:
		if settledBatchListResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
			print('Successfully got settled batch list!')

			#if hasattr(response, 'batch') == True:
			#mylist = settledBatchListResponse.batchList.batch

			for batchItem in settledBatchListResponse.batchList.batch:
				#print ("LOOK batchItem   = %s" %batchItem)
				print('Batch Id : %s' % batchItem.batchId)
				print('Settlement State : %s' % batchItem.settlementState)
				print('Payment Method : %s' % batchItem.paymentMethod)
				print('Product : %s' % batchItem.product)

				if hasattr(settledBatchListResponse.batchList.batch, 'statistics') == True:
					if hasattr(settledBatchListResponse.batchList.batch.statistics, 'statistic') == True:
# 				if batchItem.statistics:
	 					for statistic in batchItem.statistics.statistic:
	 						print('Account Type : %s' % statistic.accountType)
	 						print('Charge Amount : %s' % statistic.chargeAmount)
	 						print('Refund Amount : %s' % statistic.refundAmount)
	 						print('Decline Count : %s' % statistic.declineCount)
			if settledBatchListResponse.messages:
				print('Message Code : %s' % settledBatchListResponse.messages.message[0]['code'].text)
				print('Message Text : %s' % settledBatchListResponse.messages.message[0]['text'].text)
		else:
			if settledBatchListResponse.messages:
				print('Failed to get settled batch list.\nCode:%s \nText:%s' % (settledBatchListResponse.messages.message[0]['code'].text,settledBatchListResponse.messages.message[0]['text'].text))

	return settledBatchListResponse

if(os.path.basename(__file__) == sys.argv[0].split('/')[-1]):
	get_settled_batch_list()
