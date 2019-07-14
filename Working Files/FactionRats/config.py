def getConfig(key):

    configKeys = {}
    
    config = open("config.txt", "r")

    splitlist = config.read().split("\n")

    for i in splitlist:

        tempList = i.split(" = ")
        configKeys[tempList[0]] = tempList[1] 
        

        
    return(configKeys[key])



