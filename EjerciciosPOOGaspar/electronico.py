from producto import Producto
class Electronico(Producto):
    def __init__(self,nombre,precio,cantidad,marca,modelo): #se llama al constructor y se definen los atributos que funcionaran como parametros
        super().__init__(nombre,precio,cantidad) #se heredan los atributos de la clase Producto
        #se inicializan los atributos
        self.marca = marca
        self.modelo = modelo
        

    def getMarca(self):  #Metodo para obtener la marca   
            return self.marca

    def getModelo(self): #Metodo para obtener el modelo   
            return self.modelo  
    
    def mostrar_informacion_electronico(self): #metodo que realiza el print que vera el usuario
       print ("\nLos datos de su producto son: " + "\n" +"\nNombre: "+ str(self.getNombre()) + "\n" +"\nPrecio: "+ str(self.getPrecio()) + "\n" +"\nCantidad: "+ str(self.getCantidad()) + "\n" + "\nMarca:"+ str(self.getMarca())+ "\n" +"\nModelo:" + str(self.getModelo())) 
      


