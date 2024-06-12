from alimento import Alimento #se importa la clase Alimento del archivo alimento.py
from producto import Producto #se importa la clase Producto del arcihvo Producto.py
from electronico import Electronico #se importa la clase Electronico del archivo electronico.py


x= Electronico("xbox360",300,1,"MICROSOFT","2022") #se da valor a cada atributo de la clase Electronico
x.mostrar_informacion_electronico()#se printea la informacion


y= Producto("CPU", 95000, 1) #se da valor a cada atribvuto de la clase Producto
y.mostrar_informacion_producto()#se printea la informacion


z= Alimento("Sanguche Ciabatta",12000,2,"16/12/2002") #se da valor a cada atributo de la clase Alimento
z.mostrar_informacion_alimento()#se printea la informacion

