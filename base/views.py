from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
# Create your views here.
def getToken(request):
    appId = "ea5472b2c2ad450397a718fa2e13d4e9"
    appCertificate = "3f1bd0b48c364a3184955a184428c0d2"
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    role = 1 # - default is 1 for admin
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid}, safe=False)

def lobby(request):
    return render(request, 'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')