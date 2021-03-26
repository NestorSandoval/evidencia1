articulos = [];

print("********** MENU **********")

while (True):
    print("1. Registrar una venta")
    print("2. Consultar una venta")
    print("3. Salir")
    opcion = int(input("ingrese una opcion: "))
    
    if opcion == 1:
        print("\REGISTRAR COMESTICO\n")
        descripcion = input('Descripcion del producto: ');
        cantidad = int(input('Cantidad de productos: '));
        precio = int(input('Precio del producto: '));        
        
        total = cantidad * precio;
        
        articulos.append({'descripcion': descripcion, 'cantidad': cantidad, 'precio': precio, 'total': total});
        
    if opcion == 2:
        montoTotalArticulos = 0
        
        print('\n****CONSULTAR VENTAS****\n');
        print("\n")
        print("{:>20} {:>20} {:>20} {:>20}".format("DESCRIPCION","CANTIDAD","PRECIO","TOTAL"))
        print("{:>20} {:>20} {:>20} {:>20}".format("-----------------", "-----------------", "-----------------","-----------------",))
        for articulo in articulos:
            print("{:>20} {:>20} {:>20} {:>20}".format(articulo['descripcion'], articulo['cantidad'], articulo['precio'], articulo['total']))
            montoTotalArticulos = montoTotalArticulos + articulo['total']
        print("{:>20} {:>20} {:>20} {:>20}".format("", "", "", montoTotalArticulos))
        print("\n")
          

    
    if opcion == 3:
        break;
    