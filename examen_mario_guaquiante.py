# 1. Definicion de funciones de validacion
def val_texto(texto):
    
    if texto.strip() == "":
        return False
    return True

def val_peso(peso):
    return peso > 0

def val_sn(opcion):
    return opcion.lower() in ['s', 'n']

def val_precio(precio):
    return precio > 0

def val_unidades(unidades):
    return unidades >= 0

# 2.Funciones del Sistema
def leer_opcion():
    
    try:
        op = int(input("Ingrese opción: "))
        if 1 <= op <= 6:
            return op
        else:
            return -1
    except ValueError:
        return -1

def unidades_categoria(categoria, productos, stock):
    
    total_unidades = 0
    cat_buscar = categoria.lower()
    
    for codigo in productos:
        
        cat_producto = productos[codigo][1].lower()
        if cat_producto == cat_buscar:
            
            unidades_disp = stock[codigo][1]
            total_unidades += unidades_disp
            
    print(f"El total de unidades disponbles es: {total_unidades}")

def busqueda_precio(p_min, p_max, productos, stock):
    
    resultados = []
    
    for codigo in stock:
        precio = stock[codigo][0]
        unidades = stock[codigo][1]
                
        if p_min <= precio <= p_max and unidades > 0:
            nombre = productos[codigo][0]
            
            formato = f"{nombre}--{codigo}"
            resultados.append(formato)
            
    if len(resultados) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        
        resultados.sort()
        print(f"Los productos encontrados son: {resultados}")

def buscar_codigo(codigo, diccionario):
    
    cod_buscar = codigo.upper()
    for cod in diccionario:
        if cod.upper() == cod_buscar:
            return True
    return False

def obtener_codigo_real(codigo, diccionario):
    
    cod_buscar = codigo.upper()
    for cod in diccionario:
        if cod.upper() == cod_buscar:
            return cod
    return codigo.upper()

def actualizar_precio(codigo, nuevo_precio, stock):
    
    if buscar_codigo(codigo, stock):
        cod_real = obtener_codigo_real(codigo, stock)
        stock[cod_real][0] = nuevo_precio
        return True
    else:
        return False

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades, productos, stock):
    
    if buscar_codigo(codigo, productos):
        return False
    
    cod_real = codigo.upper()
    
    importado_bool = True if es_importado.lower() == 's' else False
    cachorro_bool = True if es_para_cachorro.lower() == 's' else False
    
    # Agregar a diccionarios
    productos[cod_real] = [nombre, categoria, marca, peso_kg, importado_bool, cachorro_bool]
    stock[cod_real] = [precio, unidades]
    return True

def eliminar_producto(codigo, productos, stock):
    
    if buscar_codigo(codigo, productos):
        cod_real = obtener_codigo_real(codigo, productos)
        
        productos.pop(cod_real)
        stock.pop(cod_real)
        return True
    else:
        return False


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

# Diccionarios iniciales
productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10.0, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8.0, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1.0, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2.0, False, False]
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}

# Ciclo principal del Menú
while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")
    
    opcion = leer_opcion()
    
    if opcion == -1:
        print("Debe seleccionar una opción válida")
    
    elif opcion == 1:
        cat = input("Ingrese categoría a consultar: ")
        unidades_categoria(cat, productos, stock)
        
    elif opcion == 2:
        
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    busqueda_precio(p_min, p_max, productos, stock)
                    break
                else:
                    print("Los precios deben ser mayores o iguales a cero y el minimo menor o igual al maximo.")
            except ValueError:
                print("Debe ingresar valores enteros")
                
    elif opcion == 3:
        continuar = 's'
        while continuar.lower() == 's':
            codigo = input("Ingrese codigo del producto: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if nuevo_precio > 0:
                    exito = actualizar_precio(codigo, nuevo_precio, stock)
                    if exito:
                        print("Precio actualizado")
                    else:
                        print("El codigo no existe")
                else:
                    print("El precio debe ser mayor a cero.")
            except ValueError:
                print("El precio debe ser un número entero.")
                
            continuar = input("¿Desea actualizar otro precio (s/n)?: ")
            
    elif opcion == 4:
        codigo = input("Ingrese codigo del producto: ")
        
        if val_texto(codigo):
            if not buscar_codigo(codigo, productos):
                nombre = input("Ingrese nombre: ")
                categoria = input("Ingrese categoría: ")
                marca = input("Ingrese marca: ")
                
                try:
                    peso = float(input("Ingrese peso (kg): "))
                    es_imp = input("¿Es importado? (s/n): ")
                    es_cachorro = input("¿Es para cachorro? (s/n): ")
                    precio = int(input("Ingrese precio: "))
                    unidades = int(input("Ingrese unidades: "))
                    
                    
                    if (val_texto(nombre) and val_texto(categoria) and val_texto(marca) and 
                        val_peso(peso) and val_sn(es_imp) and val_sn(es_cachorro) and 
                        val_precio(precio) and val_unidades(unidades)):
                        
                        exito = agregar_producto(codigo, nombre, categoria, marca, peso, es_imp, es_cachorro, precio, unidades, productos, stock)
                        
                        if exito:
                            print("Producto agregado")
                        else:
                            print("Error al agregar producto.")
                    else:
                        print("Error: Uno o más datos no cumplen con las validaciones.")
                except ValueError:
                    print("Error: El peso debe ser numérico, y el precio/unidades deben ser enteros.")
            else:
                print("El codigo ya existe")
        else:
            print("El codigo no puede estar vacío.")
            
    elif opcion == 5:
        codigo = input("Ingrese codigo a eliminar: ")
        exito = eliminar_producto(codigo, productos, stock)
        if exito:
            print("Producto eliminado")
        else:
            print("El codigo no existe")
            
    elif opcion == 6:
        print("Programa finalizado.")
        break