from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

batchStatisticsRequest = apicontractsv1.getBatchStatisticsRequest()
batchStatisticsRequest.merchantAuthentication = merchantAuth
batchStatisticsRequest.batchId = "4532808"

batchStatisticsController = getBatchStatisticsController(batchStatisticsRequest)

batchStatisticsController.execute()

batchStatisticsResponse = batchStatisticsController.getresponse()

if batchStatisticsResponse is not None:
	if batchStatisticsResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
		print('Successfully got batch statistics!')

		print('Batch Id : %s' % batchStatisticsResponse.batch.batchId)
		print('Batch Settlement State : %s' % batchStatisticsResponse.batch.settlementState)
		print('Batch Payment Method : %s' % batchStatisticsResponse.batch.paymentMethod)

		for statistic in batchStatisticsResponse.batch.statistics.statistic:
			print('Account Type : %s' % statistic.accountType)
			print('Charge Amount : %s' % statistic.chargeAmount)
			print('Refund Amount : %s' % statistic.refundAmount)
			print('Decline Count : %s' % statistic.declineCount)

		if batchStatisticsResponse.messages:
			print('Message Code : %s' % batchStatisticsResponse.messages.message[0].code)
			print('Message Text : %s' % batchStatisticsResponse.messages.message[0].text)
	else:
		if batchStatisticsResponse.messages:
			print('Failed to get batch statistics.\nCode:%s \nText:%s' % (batchStatisticsResponse.messages.message[0].code,batchStatisticsResponse.messages.message[0].text))
