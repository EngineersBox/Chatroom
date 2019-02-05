import json
import fileconfig
import configparser
from os.path import dirname, abspath

#Globals
dir_path = dirname(abspath(__file__))

class json_config:

    def getData(dirname, data_filter, data_set):
        with open(dirname) as json_file:
            data = json.load(json_file)
            for p in data[data_filter]:
                return p[data_set]

class cfg(fileconfig.Config):

    filename = dir_path + "/config/perms.ini"
    def __init__(self, key, **kwargs):
        self.key = key
        self.__dict__.update(kwargs)

class ini_config:

    def getValue(key, keyarg): #Read from perms.ini
        ret_val = cfg(key).__dict__
        return ret_val.get(keyarg)

    def writeValue(key, perm, permState): #Write to perms.ini
        config = configparser.ConfigParser()
        config.read(dir_path + "/config/perms.ini")
        if key not in config:
            config.add_section(key)
            config.set(key, perm, permState)
        else:
            config.set(key, perm, permState)

        with open(dir_path + "/config/perms.ini", 'w+') as configfile:
            config.write(configfile)

class permissions:

    def __init__(self, title, ex_perms={}):
        self.title = title
        self.tier = 0
        try:
            self.tier = ini_config.getValue(self.title, "tier")
        except KeyError:
            ini_config.writeValue(self.title, "inherits", "user_config")
            ini_config.writeValue(self.title, "prefix", self.title.capitalize())
        if len(ex_perms) > 0:
            for key in ex_perms:
                try:
                    ini_config.writeValue(self.title, key, ex_perms.get(key))
                except TypeError:
                    print("Type Error: Key \u0022" + key + "\u0022 with value \u0022" + str(ex_perms.get(key)) + "\u0022 is not of type string")
                    continue
                if key == "tier":
                    self.tier = ex_perms.get(key)

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        if self.title != newTitle:
            self.title = newTitle

    def getTier(self):
        return self.tier

    def setTier(self, newTier=int):
        self.tier = newTier

    def getExPerms(self):
        return self.ex_perms

permList = {"test1": [12, "cheese", 4], "test2": "val2", "tier": "2"}
testPerm = permissions("cheese", ex_perms=permList)
print(testPerm.getTier())
