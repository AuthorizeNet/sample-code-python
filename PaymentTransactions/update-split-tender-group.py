from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'


updateSplitTenderGroup = apicontractsv1.updateSplitTenderGroupRequest()
updateSplitTenderGroup.merchantAuthentication = merchantAuth
updateSplitTenderGroup.splitTenderId = "115901"
enum = apicontractsv1.splitTenderStatusEnum
updateSplitTenderGroup.splitTenderStatus = enum.voided


updateSplitTenderController = updateSplitTenderGroupController(updateSplitTenderGroup)
updateSplitTenderController.execute()

response = updateSplitTenderController.getresponse()


if (response.messages.resultCode=="Ok"):
    print response.messages.message[0].text
else:
    print "response code: %s" % response.messages.resultCode
    print response.messages.message[0].text
