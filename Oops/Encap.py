class Mobile:
    __model=""   #private
    __price=0.0
    __ram=0
    __internal=0
    def setModel(self,mod=""):
        self.__model=mod
    def getModel(self):
        return self.__model
    def setPrice(self,pri=""):
        self.__Price=pri
    def getPrice(self):
        return self.__Price
    def setRam(self,ra=""):
        self.__ram=ra
    def getRam(self):
        return self.__ram
    def setInternal(self,inte=""):
        self.__internal=inte
    def getInternal(self):
        return self.__internal                
M=Mobile()
M.setModel("Iphone")
M.setPrice(690000.0)
M.setRam(128)
M.setInternal(128)
print(M.getModel(),M.getPrice(),M.getRam(),M.getInternal())
