class Usuario:

    def __init__(self, id:int, nome:str, email:str):
        self.__id=id
        self._nome=nome
        self._email=email

    @property
    def id(self):
        return self.__id 
    
    @id.setter
    def id(self,id:int):
        self.__id=id
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome:str):
        self._nome=nome
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,email:str):
        self._email=email
    
    