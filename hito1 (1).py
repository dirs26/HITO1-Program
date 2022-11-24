productos = {'libro':20,'perfume':70,'gorra':25,'chaqueta':40,'abrigo':330,'zapatillas':110,'gorro':18} #uso un diccionario para establecer precios dentro de una misma línea de código
#Creo estos dos especies de recolectores de información para guardar los productos elegidos por el cliente
lista={} 
carrito={}
class Clientes:# clase cliente en la que se basará la parte principal del prgrama
    def __init__(self) -> None:
        pass
    def interface(self): #Cara principal del programa
        print('------------BIENVENIDO-------------')
        print('Regístrese antes de entrar:')
        def nombre():
            try:
                print(str(input('Escriba un nombre de usuario: ')))
            except:
                print('Introduzca un nombre válido')
                nombre()
        nombre()
        def tlf():
            try: print(int(input('Escriba un número telefónico: ')))
            except:
                print('Introduzca un número...')
                tlf()
        tlf()
        def direccion():
            print('Si no la escribe completa, su paquete no será enviado')
            print(input('Escriba su dirección: '))
        direccion()
        #a partir de aquí hasta el '3.' son las diferentes opciones que tiene el ususario
    def menup(self):
        print('1. Añadir a lista de Deseos ')
        print('2. Añadir al carrito ')
        print('3. Comprar carrito ')
        x=input('Elija que quiere hacer: ')
        match x: # uso de switch case para especificar que se hace con cada una de las opciones dadas, posteriormente matizamos cada caso
            case '1':# Ocurriría la selección de productos para la creación de una lista de deseos
                def listaDeseos():    
                    def producto():
                        for key, value in productos.items():# Obtiene los productos del diccionario 'productos' mencionado en la línea 1 
                            print(key, 'precio: ', value,'€')# decoramos la manera en que se presentan dichos productos
                        try: 
                            p=input('Elija los productos de su preferencia : ')
                            lista[p.lower()]=productos[p.lower()]#Uso .lower para que no importe la manera en la que se escriba el producto, la máquina siempre la entienda
                            for key, value in productos.items():
                                print(key, 'precio: ', value,'€')
                            print(sum(lista.values()))
                        except:
                            print('Elija un producto que se encuentre en la lista...')
                    producto()
                    #presentamos cada una de las opciones luego de haber elegido el primer producto, para que elija que desea hacer
                    print('1. Volver')
                    print('2. Seguir comprando')
                    print('3. Ver lista')
                    y=input('¿Quiere volver, seguir añadiendo productos o ver su Lista de deseos?: ')
                    match y:
                        case '1':
                            print('Volver')
                            self.menup()
                        case'2':
                            listaDeseos()
                        case '3':
                            for key, value in lista.items():    
                                print(key, 'precio: ', value,'€')
                    print('1. Volver')
                    print('2. Seguir comprando')
                    y=input('¿Quiere volver o seguir añadiendo productos?: ')
                    match y:
                        case '1':
                            print('Volver')
                            self.menup()
                        case'2':
                            listaDeseos()
                listaDeseos()
            case '2':
                def carro():      
                    def producto():
                        for key, value in productos.items():    
                            print(key, 'precio: ', value,'€')      
                        try: 
                            p=input('Elija los productos de su preferencia : ')
                            carrito[p.lower()]=productos[p.lower()]
                            for key, value in productos.items():
                                print(key, 'precio: ', value,'€')
                            print(sum(carrito.values()))
                        except:
                            print('Elija un producto que se encuentre en la lista...')
                    producto()
                    print('1. Volver')
                    print('2. Seguir comprando')
                    print('3. Ver carrito')
                    y=input('¿Quiere volver, seguir añadiendo productos o ver el carrito?: ')
                    match y:
                        case '1':
                            print('Volver')
                            self.menup()
                        case'2':
                            carro()
                        case '3':
                            for key, value in carrito.items():    
                                print(key, 'precio: ', value,'€')
                    print('1. Volver')
                    print('2. Seguir comprando')
                    y=input('¿Quiere volver o seguir añadiendo productos?: ')
                    match y:
                        case '1':
                            print('Volver')
                            self.menup()
                        case'2':
                            carro()
                carro()
            case '3':  
                #En el último de los casos se establecerá de qué país es el comprador, si es de España se cobrará el IVA nacional, si no se cobrará un IVA estándar del 8% 
                precioTotal=sum(carrito.values())
                pais=input('De que pais eres: ')
                if pais=='España':
                    print('El iva es del 21%')
                    precioTotalIva=precioTotal*1.21
                    print(f'El precio a pagar + IVA, en España es de: {precioTotalIva}')
                    def finProgram():
                        print('Gracias por confiar en nosostros... ')
                        print('Le enviaremos un SMS con la factura y la información de su pedido')
                    finProgram()
                else:
                    print('El iva es del 8%')
                    precioTotalIva=precioTotal*1.08
                    print(f'El total a pagar + IVA es de {precioTotalIva}')
                    def finProgram():
                        print('Gracias por confiar en nosostros... ')
                        print('Le enviaremos un SMS con la factura y la información de su pedido')
                    finProgram()


                


k=Clientes()
k.interface()
k.menup()

