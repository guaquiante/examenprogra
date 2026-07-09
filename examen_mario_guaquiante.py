# 1. Definición de funciones de validación
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

# 2. Funciones del Sistema
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
