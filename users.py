from uuid import uuid4
import permissions as pm

#Standard permissions
member = pm.permissions("member")
moderator = pm.permissions("moderator")
admin = pm.permissions("admin")
owner = pm.permissions("owner")

class user:

    def __init__(self, name, uid=uuid4(), perms=member):
        self.name = name
        self.uid = uid
        if isinstance(perms, pm.permissions) == True:
            self.perms = perms
        else:
            self.perms = member

    def getName(self):
        return self.name

    def setName(self, newName):
        if self.name != newName:
            self.name = newName

    def getUid(self):
        return self.uid

    def setUid(self, newUid):
        if self.uid != newUid:
            self.uid = newUid

    def renewUid(self):
        self.uid = uuid4()

    def getPermTitle(self):
        return self.perms.getTitle()

    def getPermType(self):
        return self.perms

    def setPermType(self, newPerms):
        if isinstance(newPerms, pm.permissions) == True:
            self.perms = newPerms

testMember = user("member", perms=member)
testMod = user("mod", perms=moderator)
testAdmin = user("admin", perms=admin)
testOwner = user("owner", perms=owner)

print(testMember.getUid())
print(testMember.getName())
print(testMember.getPermTitle())
print(testMember.getPermType().getValue("add_friend"))
