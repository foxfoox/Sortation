class Sortation:
    def __init__(self,data,fulcrum,selection = [0],priority = True):
        self.__failed    = True
        self.__data      = data
        self.__selection = selection if selection else [0]
        self.__fulcrum   = fulcrum
        self.__data_size = 0
        self.__priority  = priority
        if(self.__dataValidation() and self.__fulcrum and self.__selectionValidation()):
            if (isinstance(self.__fulcrum,str) and self.__fulcrum.strip()) or isinstance(self.__fulcrum,int):
                self.__fulcrum = str(self.__fulcrum)
                self.__failed = False
            
    def sort(self):
        if not self.__failed:
            self.__data.sort(key = self.__candidacy)
    
    def data(self):
        return self.__data
    
    def failed(self):
        return self.__failed
            
    def __candidacy(self,intry):
        result = 0
        j = 10 ** len(self.__selection) if self.__priority else 1
        for i in self.__selection:
            result += j * self.__correspond(str(intry[i]))
            j /= 10 if j != 1 else 1
        return result
    
    def __correspond(self,text):
        result = len(text) if text.strip() == self.__fulcrum.strip() else 0
        if result == 0:
               for i in range(0,len(self.__fulcrum) if len(text) > len(self.__fulcrum) else len(text)):
                   if(text[i] == self.__fulcrum[i]):
                       result += 1;
        return result;
    
    def priority(self):
        return self.__priority
    
    def __selectionValidation(self):
        result = True
        if not self.__selection == [0]:
            if len(self.__selection) <= self.__data_size:
                for i in range(0,len(self.__selection)):
                    if isinstance(self.__selection[i],int) and self.__selection[i] < self.__data_size:
                        if not (isinstance(self.__data[0][self.__selection[i]],str) or (isinstance(self.__data[0][self.__selection[i]],int) and ((isinstance(self.__fulcrum,str) and self.__fulcrum.isdigit()) or isinstance(self.__fulcrum,int)))):
                            result = False
                            break
                    else:
                        result = False
                        break
            else:
                result = False
        return result
    
    def __dataValidation(self):
        result = True
        if self.__data and isinstance(self.__data,list) and isinstance(self.__data[0],list) and len(self.__data[0]) > 0:
            self.__data_size = len(self.__data[0])
            for i in range(0,len(self.__data)):
                j = len(self.__data[i])
                if (isinstance(self.__data[i],list) and  j > 0 and j == self.__data_size):
                    for k in range(0,j):
                        if not type(self.__data[i][k]) == type(self.__data[0][k]):
                            result = False
                            break
                    if result == False:
                        break
                else:
                    result = False
                    break
                
        else:
            result = False
        return result