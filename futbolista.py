from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):
    _listaFutbolistas=[]

    def __init__(self,nombre,edad,altura,sexo,añosPracticando, golesMarcados,tarjetasRojas,piernaHabil):
        Deportista.__init__(self,añosPracticando)
        Persona.__init__(self,nombre,edad,altura,sexo)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        Futbolista._listaFutbolistas.append(self)
    
    def getNombre(self):
        return Persona.getNombre(self)
    
    def getEdad(self):
        return Persona.getEdad(self)
    
    def getSexo(self):
        return Persona.getSexo(self)
    
    def getAltura(self):
        return Persona.getAltura(self)
    
    def getAñosPracticando(self):
        return Deportista.getAñosPracticando(self)
    
    def getDeporte(self):
        return Deportista.getDeporte(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    
    @staticmethod
    def getListaFutbolistas(cls):
        return cls._listaFutbolistas
    
    def SetNombre(self,nombre):
        Persona.setNombre(self,nombre)
    
    def setEdad(self,edad):
        Persona.setEdad(self,edad)
    
    def setSexo(self,sexo):
        Persona.setSexo(self,sexo)
    
    def setAltura(self,altura):
        Persona.setAltura(self,altura)
    
    def setAñosPraticando(self,añosPracticando):
        Deportista.setAñosPracticando(self,añosPracticando)
    
    def setDeporte(self,deporte):
        Deportista.setDeporte(self,deporte)
    
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados=golesMarcados
    
    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil=piernaHabil
    
    @staticmethod
    def setListaFutbolistas(cls,listaFutbolistas):
        cls._listaFutbolistas=listaFutbolistas
    
    def __str__(self):
        return f"Mi nombre es {Persona.getNombre(self) } soy profesional en el deporte {Deportista.getDeporte(self)} Tengo {Persona.getEdad(self)} años de edad y llevo {Deportista.getAñosPracticando(self)} años en el deporte"