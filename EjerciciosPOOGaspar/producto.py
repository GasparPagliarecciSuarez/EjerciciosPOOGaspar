class Producto:
    def __init__(self,nombre,precio,cantidad): #se llama al conructor y se definen los atributos que funcionaran como parametros
        #se incializan los atributos
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
 
    def getNombre (self):   #Metodo para obtener el nombre
        return self.nombre
    
    def getPrecio(self):   #Metodo para obtener el precio
        return self.precio
    
    def getCantidad(self):   #Metodo para obtener la cantidad
        return self.cantidad
    
    def mostrar_informacion_producto(self): #metodo que realiza el print que vera el usuario
       print ("\nLos datos de su producto son: " + "\n" +"\nNombre: "+ str(self.getNombre()) + "\n" +"\nPrecio: "+ str(self.getPrecio()) + "\n" +"\nCantidad: "+ str(self.getCantidad())) #se estructura el print para mostrar al usuario
      