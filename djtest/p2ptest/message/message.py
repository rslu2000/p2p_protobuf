import p2ptest.p2p as p2p_module
from p2ptest.proto import message_pb2
import hashlib
import time

class Message:
    getdata=set()
    @staticmethod
    def recv(sock):
        serilaMsg=sock.socket.recv(1024)
        try:
            hashdata=hashlib.sha256(serilaMsg).hexdigest()
            if not (hashdata in Message.getdata):
                Message.getdata.add(hashdata)
                print "==== get new message ===="
                print "decode before"
                print serilaMsg
                print "decode after"
                pb2=message_pb2.Message()
                pb2.ParseFromString(serilaMsg)
                print "time: " + pb2.time
                print "message: " pb2.msg
                sock.broadcast(serilaMsg)
        except Exception as e:
            print e

    
    @staticmethod
    def send(body):
        pb2=message_pb2.Message()
        pb2.time=time.time()
        pb2.msg=body
        serilaMsg=pb2.SerializeToString()
        p2p_module.p2p.P2PSocket.broadcast(serilaMsg)
        