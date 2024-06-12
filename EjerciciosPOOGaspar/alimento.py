from producto import Producto

class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):   #se llama al constructor y se definen los atributos
        super().__init__(nombre, precio, cantidad) #se heredan los atributos de la clase Producto
        self.fecha_expiracion = fecha_expiracion # se inicializa el atributo 

    def get_fecha_expiracion(self):   #Metodo para obtener la fecha de caducidad   
        return self.fecha_expiracion
    
    def mostrar_informacion_alimento(self): #metodo que realiza el print que vera el usuario
       print ("\nLos datos de su producto son: " + "\n" +"\nNombre: "+ str(self.getNombre()) + "\n" +"\nPrecio: "+ str(self.getPrecio()) + "\n" +"\nCantidad: "+ str(self.getCantidad()) + "\n" + "\nFecha de expiración: " + str(self.get_fecha_expiracion())) 


