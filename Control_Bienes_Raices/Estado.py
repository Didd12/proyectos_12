class Estado:
    def __init__(self, nombre, fecha):
        self.__nombre  = nombre
        self.__fecha   = fecha
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        return self.__nombre
    
    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self, fecha):
        return self.__fecha
        