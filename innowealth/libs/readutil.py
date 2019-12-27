import os
import codecs
import configparser

proDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
configPath = os.path.join(os.path.join(proDir, 'conf'), "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


if __name__ == '__main__':
    readconfig = ReadConfig()
    print(readconfig.get_http('base_url'))
