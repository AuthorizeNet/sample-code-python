from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

paypal = apicontractsv1.payPalType()
paypal.successUrl = "http://www.merchanteCommerceSite.com/Success/TC25262"
paypal.cancelUrl = "http://www.merchanteCommerceSite.com/Success/TC25262"
paypal.payerID = "LM6NCLZ5RAKBY"

payment = apicontractsv1.paymentType()
payment.payPal = paypal

transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.priorAuthCaptureTransaction
transactionrequest.refTransId = "2245591700"
transactionrequest.payment = payment

request = apicontractsv1.createTransactionRequest()
request.merchantAuthentication = merchantAuth
request.refId = "Sample"
request.transactionRequest = transactionrequest

controller = createTransactionController(request)
controller.execute()

response = controller.getresponse()

if (response.messages.resultCode=="Ok"):
    print "SUCCESS"
    print "Message Code : %s" % response.messages.message[0].code
    print "Message text : %s" % response.messages.message[0].text
    print "Auth code : %s " % response.transactionResponse.authCode
    if (response.transactionResponse.responseCode == "1" ):
        print "Description : %s " % response.transactionResponse.messages.message[0].description
        print "Transaction ID : %s " % response.transactionResponse.transId
else:
    print "ERROR"
    print "Message Code : %s" % response.messages.message[0].code
    print "Message text : %s" % response.messages.message[0].text