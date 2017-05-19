#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from p2ptest.p2p import p2p
from p2ptest.message import message as message_module



def JoinNode(request):
    ip=port=""
    try:
        ip=request.GET["ip"]
    except:
        ip="127.0.0.1"
    try:
        port=request.GET["port"]
    except:
        port="8001"
    p2p.P2PJoinStart((ip,int(port)))
    return HttpResponse("JoinNode")

def send(request):
    body=request.body
    
    message_module.Message.send(body)
    return HttpResponse(body)