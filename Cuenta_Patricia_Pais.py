class Cuenta:
   def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
   def mostrar(self):
        return self.titular, self.cantidad
   def ingresa_cantidad(self,cantida):
       if cantida>0: 
             self.cantidad=cantida
             return self.cantidad
       else: return self.cantidad 
   def retira_cantidad(self):
       self.cantidad -= float(input("Ingrese cantidad a retirar: ")) 
       return self.cantidad 
cuenta1=Cuenta("Pato",0)
cuenta1.ingresa_cantidad(float(input("Ingrese cantidad a depositar: ")))
datos=cuenta1.mostrar()
print("Nombre: " + str(datos[0]) + "\nSaldo: " + str(datos[1]) )
print("Saldo Actualizado: " + str(cuenta1.retira_cantidad()))