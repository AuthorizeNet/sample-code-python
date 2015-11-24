from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *
from authorizenet.apicontractsv1 import bankAccountType, accountTypeEnum

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'


payment = apicontractsv1.paymentType()

bankAccountType = apicontractsv1.bankAccountType()
accountType = apicontractsv1.bankAccountTypeEnum
bankAccountType.accountType = accountType.checking
bankAccountType.routingNumber = "125000024"
bankAccountType.accountNumber = "12345678"
bankAccountType.nameOnAccount = "John Doe"

transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType = "refundTransaction"
transactionrequest.amount = Decimal ('2.55')
transactionrequest.payment = payment
transactionrequest.payment.bankAccount = bankAccountType


createtransactionrequest = apicontractsv1.createTransactionRequest()
createtransactionrequest.merchantAuthentication = merchantAuth
createtransactionrequest.refId = "MerchantID-0001"

createtransactionrequest.transactionRequest = transactionrequest
createtransactioncontroller = createTransactionController(createtransactionrequest)
createtransactioncontroller.execute()

response = createtransactioncontroller.getresponse()

if (response.messages.resultCode=="Ok"):
    print "Transaction ID : %s" % response.transactionResponse.transId
    print response.transactionResponse.messages.message[0].description
else:
    print "response code: %s" % response.messages.resultCode
    print response.messages.message[0].text
