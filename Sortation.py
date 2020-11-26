class Sortation:
    def __init__(self,data,fulcrum,selection = [0],attribute = {"priority":True,"exact":False,"precise":True,"order":True}):
        self.__failed            = True
        self.__data_size         = 0
        self.__data              = data if self.__dataValidation(data) else None
        self.__fulcrum           = fulcrum if self.__fulcrumValidation(fulcrum) else None
        self.__selection         = selection if self.__selectionValidation(selection) else [0]
        self.__attribute         = attribute if self.__attributeValidation(attribute) else None
        if(self.__data and self.__fulcrum and self.__selection and self.__attribute):
            if (isinstance(self.__fulcrum,str) and self.__fulcrum.strip()) or isinstance(self.__fulcrum,int):
                self.__fulcrum = str(self.__fulcrum)
                self.__failed = False
            
    def __selectionValidation(self,selection):
        result = True
        if not selection == [0]:
            if len(selection) <= self.__data_size:
                for i in range(0,len(selection)):
                    if isinstance(selection[i],int) and selection[i] < self.__data_size:
                        if not (isinstance(self.__data[0][selection[i]],str) or (isinstance(self.__data[0][selection[i]],int) and ((isinstance(self.__fulcrum,str) and self.__fulcrum.isdigit()) or isinstance(self.__fulcrum,int)))):
                            result = False
                            break
                    else:
                        result = False
                        break
            else:
                result = False
        return result
    
    def __fulcrumValidation(self,fulcrum):
        return fulcrum and ((isinstance(fulcrum,str) and fulcrum.strip()) or isinstance(fulcrum,int))
    
    def __attributeValidation(self,attribute):
        return attribute and attribute.get('priority') != None and attribute.get('exact') != None and attribute.get('order') != None and attribute.get('precise') != None
    
    def __dataValidation(self,data):
        result = True
        if data and isinstance(data,list) and isinstance(data[0],list) and len(data[0]) > 0:
            self.__data_size = len(data[0])
            for i in range(0,len(data)):
                j = len(data[i])
                if (isinstance(data[i],list) and  j > 0 and j == self.__data_size):
                    for k in range(0,j):
                        if not type(data[i][k]) == type(data[0][k]):
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
    
    def sort(self):
        if not self.__failed:
            self.__data.sort(key = self.__candidacy)
    
    def data(self):
        return self.__data
    
    def failed(self):
        return self.__failed
            
    def __candidacy(self,intry):
        result = 0
        j = 10 ** len(self.__selection) if self.__attribute.get('priority') else 1
        for i in self.__selection:
            result += j * self.__compare(str(intry[i]))
            j /= 10 if j != 1 else 1
        return result
    
    def __compare(self,text):
        result = 0
        l1 = self.__fulcrum
        l2 = text
        for i in range(33,48):
            l1 = l1.replace(chr(i), " ")
            l2 = l2.replace(chr(i), " ")
        l1 = l1.split(" ")
        l2 = l2.split(" ")
        l1 = [i for i in l1 if i]
        l2 = [i for i in l2 if i]
        s  = 0
        for i in range(0,len(l1)):
            for j in range(s,len(l2)):
                dif = self.__correspond(l2[j], l1[i])
                result += dif
                if self.__attribute.get("order"):
                    s = j + 1
                    if dif > 0:
                        break
        return result
    
    def __correspond(self,text1,text2):
        result = (len(text1) if (text1.strip() == text2.strip()) else 0) if (self.__attribute.get('exact')) else (len(text1) if (text1.find(text2) != -1) else 0) if (self.__attribute.get("precise")) else -1
        if result == -1:
            result = 0
            for i in range(0,len(text2) if len(text1) > len(text2) else len(text1)):
                if(text1[i] == text2[i]):
                    result += 1;
        return result
    
    def priority(self):
        return self.__attribute.get('priority')
    
