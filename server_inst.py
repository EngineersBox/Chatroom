from uuid import uuid4
import hashlib
import encryption

clients = {}
adresses = {}

class con_handlers:

    def accept_cons(client=None):
        clients.update(client)

    def client_handler():
        pass

    def send_data(msg):
        pass

class server:

    def __init__(self, instanceId=uuid4()):
        self.instanceId = instanceId
        self.passwd = hashlib.sha256(str(uuid4()).encode("utf-8")).hexdigest()
        self.msgKey = encryption.keyGen.newKey()
        self.clients = {}
        self.addresses = {}

    def getInstanceId(self):
        return self.instanceId

    def getPasswd(self):
        return self.passwd

testServer = server()
print(testServer.getPasswd())

f = encryption.keyGen.newKey()
print(f)
tok = encryption.msgEnc.encMsg(f, "test message")
print(tok)
msg = encryption.msgEnc.decMsg(f, tok)
print(msg)
