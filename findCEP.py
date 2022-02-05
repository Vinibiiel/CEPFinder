from pycep_correios import get_address_from_cep, WebService

class searchCEP():
    def __init__(self,CEP):
        self.__cep = CEP

    def consulting(self): # Query using the CEP, what is the adress
        try:
            # Call the library to research
            self.__endereco = get_address_from_cep(self.__cep, webservice=WebService.APICEP) 
            
            return self.__endereco # If has a Adress for the CEP, return a Object that contains the adress data
        except:
            return False
    
    