#########################################################################
# LISTA DIGITAL DE CONTACTOS                                            #
#########################################################################

#########################################################################
# MÓDULOS                                                               #
#########################################################################
import os # para usar system("cls") /clear screen
from fpdf import FPDF #modulo para exportar a pdf
import re # para busqueda de palabras en filtro

#########################################################################
# FUNCIONES                                                             #
#########################################################################
    
#########################################################################
# OPCIÓN REGISTRAR ÁREAS                                                #
#########################################################################

# Obtener datos de un area
# Entradas: lista de áreas, código de área
# Salidas: Si área existe en la lista retorna True y la tupla con sus datos, sino existe retorna False y tupla vacía
def obtener_datos_area(areas, area_telefono):
    for elemento in areas:
        if elemento[0] == area_telefono:
            return True, elemento
    return False, tuple()

# Borra un area
# Entrada: areas, areas_telefono
# Salida: se elimina un area de la lista
def borrar_area(areas, area_telefono):
    for elemento in areas:
        if elemento[0] == area_telefono:
            indice=areas.index(elemento)
            del areas[indice]

# Agregar áreas
# Entradas: lista de áreas
# S: lista de áreas actualizada 
def agregar_areas(areas):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                              REGISTRAR ÁREAS                                │
│                               AGREGAR ÁREAS                                 │""")
            # leer área
            while True:
                try:
                    area_telefono = input("│Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, nombre_del_area = obtener_datos_area(areas, area_telefono)
                        if existe_area:
                            input("│ESTA ÁREA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR ")
                        else:
                            break
                    else:
                        input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
            # leer nombre del área     
            while True:
                nombre_del_area = input("│Nombre del área: ") 
                if len(nombre_del_area) >= 1 and len(nombre_del_area) <= 40:
                    break
                else:
                    input("│EL DATO DEBE TENER ENTRE 1 Y 40 CARACTERES ")
            # leer opción y guardar datos !!!!
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    areas.append((area_telefono, nombre_del_area))
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
                
#CONSULTAR AREAS
#Entradas: lista de áreas
#Salida: El nombre del area
def consultar_areas(areas):
        while True:
            os.system("cls")
            print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                              REGISTRAR ÁREAS                                │
│                              CONSULTAR ÁREAS                                │""")
            # leer área
            while True:
                try:
                    area_telefono = input("│Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, nombre_del_area = obtener_datos_area(areas, area_telefono)
                        if existe_area:
                            print("│Nombre del área: ",nombre_del_area[1],"                                      │")
                            break
                        else:
                            input("│ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE CONSULTAR")
                    else:
                        input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                    
            # leer opción y guardar datos
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR ")
                if opcion == "A":
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#MODIFICAR AREAS
#Entradas: lista de áreas
#Salida: Lista actualizada
def  modificar_areas(areas):
    while True:
            os.system("cls")
            print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                              REGISTRAR ÁREAS                                │
│                              MODIFICAR ÁREAS                                │""")
            # leer área
            while True:
                try:
                    area_telefono = input("│   Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, nombre_del_area = obtener_datos_area(areas, area_telefono)
                        if existe_area:
                            print("│                                    NUEVO VALOR")
                            break
                        else:
                            input("│ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE MODIFICAR")
                    else:
                        input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")

            # leer nombre del área     
            while True:
                print("│Nombre del área: ",nombre_del_area[1],end="          ")
                nombre_del_area = input("") 
                if len(nombre_del_area) >= 0 and len(nombre_del_area) <= 40:
                    if nombre_del_area == "":
                        break
                    borrar_area(areas, area_telefono)
                    break
                else:
                    input("│EL DATO DEBE TENER ENTRE 1 Y 40 CARACTERES ")
            
            # leer opción y guardar datos !!!!
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    areas.append((area_telefono, nombre_del_area))
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
    
#Eliminar Areas
#Entradas: lista de áreas
#Salida: Lista actualizada
def eliminar_areas(areas):
    while True:
            os.system("cls")
            print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                              REGISTRAR ÁREAS                                │
│                              ELIMINAR ÁREAS                                 │""")
            # leer área
            while True:
                try:
                    area_telefono = input("│   Área: ")
                    if area_telefono == "C":
                        return
                    area_telefono = int(area_telefono)
                    if area_telefono >= 1 and area_telefono <= 999:
                        existe_area, nombre_del_area = obtener_datos_area(areas, area_telefono)
                        if existe_area:
                            print("│Nombre del área: ",nombre_del_area[1],"                                      │")
                            break
                        else:
                            input("│ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE ELIMINAR")
                    else:
                        input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                    
            # leer opción y guardar datos
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    borrar_area(areas, area_telefono)
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
                
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

# Obtener datos de un contacto
# Entradas: lista de contactos, numero telefono
# Salidas: Si telefono existe en la lista retorna True y la tupla con sus datos, sino existe retorna False y tupla vacía
def obtener_datos_contacto(contactos, numero_telefono):
    for elemento in contactos:
        if elemento[0] == numero_telefono:
            return True, elemento
    return False, tuple()

# Borra un area
# Entrada: areas, areas_telefono
# Salida: se elimina un area de la lista
def borrar_contacto(contactos, numero_telefono):
    for elemento in contactos:
        if elemento[0] == numero_telefono:
            indice=contactos.index(elemento)
            del contactos[indice]
            
# Agregar contactos
# Entradas: lista de áreas
# S: lista de áreas actualizada 
def agregar_contacto(contactos,areas,TIPOS_TELEFONO,area_por_omision,tipo_telefono_por_omision):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                              AGREGAR CONTACTO                               │""")
            # leer contacto
            while True:
                try:
                    numero_telefono = input("│Telefono:               ")
                    if numero_telefono == "C":
                        return
                    numero_telefono = int(numero_telefono)
                    if numero_telefono >= 99999 and numero_telefono <= 100000000000:
                        existe_numero, nombre_del_contacto = obtener_datos_contacto(contactos, numero_telefono)
                        if existe_numero:
                            input("│ESTE TELÉFONO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR ")
                        else:
                            break
                    else:
                        input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
                except:
                    input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
            # leer numero del área     
            while True:
                area = input("│Área:                   ")
                if area == "C":
                    return
                existe_area, nombre_del_area = obtener_datos_area(areas, int(area))
                if area == "":
                    area = area_por_omision
                    existe_area, nombre_del_area = obtener_datos_area(areas, area)
                    print("│                       ",nombre_del_area[1],"                                             │")
                    break
                elif not existe_area:
                    input("│ESTA ÁREA NO EXISTE ")
                else:
                    print("│                       ",nombre_del_area[1],"                                             │")
                    break
            # leer tipo telefono     
            while True:
                tipo = input("│Tipo teléfono (M,C,T,O):")
                if tipo in TIPOS_TELEFONO or tipo == "":
                    if tipo == "":
                        tipo = tipo_telefono_por_omision
                    break
                else:
                    print("│ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR")
            # leer nombre del contacto     
            while True:
                nombre = input("│Nombre contacto:        ")
                if len(nombre) >= 1 and len(nombre) <= 50:
                    break
                else:
                    input("│EL NOMBRE DEBE TENER ENTRE 1 Y 50 CARACTERES ")
            # leer correo del contacto     
            while True:
                correo = input("│Correo electrónico:     ")
                if "@" in correo and not " " in correo :
                    break
                else:
                    input("│EL CORREO NO DEBE TENER ESPACIOS Y DEBE TENER @ ")
            # leer direccion     
            while True:
                direccion = input("│Dirección física:       ")
                if len(direccion) >= 0 and len(direccion) <= 80:
                    break
                elif len(direccion) == 0:
                    direccion = " "
                    break
                else:
                    input("│EL CORREO DEBE TENER ENTRE 0 Y 80 CARACTERES ")
            # leer fecha ancimiento     
            while True:
                nacimiento = input("│Fecha nacimiento:       ")
                if len(nacimiento)<=6 or nacimiento[2] != '/' or nacimiento[5] != '/':
                    input("│ERROR: LA ESTRUCTURA DE LA FECHA TIENE QUE SER DD/MM/AAAA con el / incluido")
                else:
                    if int(nacimiento[3:5]) > 12:
                        input("│ERROR: EN EL MES SOLO SON VALIDOS NUMEROS DE 01 A 12")
                    else:
                        dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        if len(nacimiento[6:10])!=4:
                            nacimiento= nacimiento[:6]+"0"
                        else:
                            if str(nacimiento[2:4]) == "02" and ((nacimiento[7:10] % 4 == 0 and nacimiento[7:10] % 100 != 0) or nacimiento[7:10] % 400 == 0):
                                dias_por_mes[2] = 29
                        if int(nacimiento[:2]) < 1 or int(nacimiento[:2]) > dias_por_mes[int(nacimiento[3:5])]:
                            input("│ERROR: EN EL DIA ESE NUMEROS NO ES VALIDO")
                        else:
                            break
            # leer Pasatiempos     
            while True:
                pasatiempos = input("│Pasatiempos:            ")
                if len(pasatiempos) >= 0 and len(pasatiempos) <= 60:
                    break
                elif len(pasatiempos) == 0:
                    pasatiempos = " "
                    break
                else:
                    input("│LOS PASATIEMPOS DEBE TENER ENTRE 0 Y 60 CARACTERES ")
            # leer Notas
            while True:
                notas = input("│Notas:                  ")
                if len(notas) >= 0 and len(notas) <= 60:
                    break
                elif len(notas) == 0:
                    notas = " "
                    break
                else:
                    input("│LAS NOTAS DEBE TENER ENTRE 0 Y 60 CARACTERES ")
            
            # leer opción y guardar datos !!!!
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    contactos.append((numero_telefono,area,nombre_del_area,tipo,nombre,correo,direccion,nacimiento,pasatiempos,notas))
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")



# Consultar contactos
# Entradas: lista de contactos
# S: indo contacto 
def consultar_contactos(contactos):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                             CONSULTAR CONTACTO                              │""")

            #Lee contacto
            while True:
                try:
                    numero_telefono = input("│Telefono:               ")
                    if numero_telefono == "C":
                        return
                    numero_telefono = int(numero_telefono)
                    if numero_telefono >= 99999 and numero_telefono <= 100000000000:
                        existe_numero, info_contacto = obtener_datos_contacto(contactos, numero_telefono)
                        if not existe_numero:
                            input("│ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")
                        else:
                            print("│Área:                   ",info_contacto[1])
                            print("│                        ",info_contacto[2][1])
                            print("│Tipo teléfono (M,C,T,O):",info_contacto[3])
                            
                            print("│Nombre contacto:        ",info_contacto[4])
                            print("│Correo electrónico:     ",info_contacto[5])
                            print("│Dirección física:       ",info_contacto[6])
                            print("│Fecha nacimiento:       ",info_contacto[7])
                            print("│Pasatiempos:            ",info_contacto[8])
                            print("│Notas:                  ",info_contacto[9])
                            break
                    else:
                        input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
                except:
                    input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
            # leer opción
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR ")
                if opcion == "A":
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

# Consultar contactos
# Entradas: lista de contactos
# S: indo contacto 
def modificar_contactos(contactos):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                             MODIFICAR CONTACTO                              │""")

            #Lee contacto
            while True:
                try:
                    numero_telefono = input("│Telefono:               ")
                    if numero_telefono == "C":
                        return
                    numero_telefono = int(numero_telefono)
                    if numero_telefono >= 99999 and numero_telefono <= 100000000000:
                        existe_numero, info_contacto = obtener_datos_contacto(contactos, numero_telefono)
                        if not existe_numero:
                            input("│ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")
                        else:
                            print("│Área:                   ",info_contacto[1])
                            print("│                        ",info_contacto[2])
                            print("│Tipo teléfono (M,C,T,O):",info_contacto[3])
                            break
                    else:
                        input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
                except:
                    input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
            # leer nombre del contacto     
            while True:
                nombre = input("│Nombre contacto:        ")
                if len(nombre) >= 1 and len(nombre) <= 50:
                    break
                elif nombre == "":
                    nombre=info_contacto[4]
                    break
                else:
                    input("│EL NOMBRE DEBE TENER ENTRE 1 Y 50 CARACTERES ")
            # leer correo del contacto     
            while True:
                correo = input("│Correo electrónico:     ")
                if "@" in correo and not " " in correo :
                    break
                elif correo == "":
                    correo=info_contacto[5]
                    break
                else:
                    input("│EL CORREO NO DEBE TENER ESPACIOS Y DEBE TENER @ ")
            # leer direccion     
            while True:
                direccion = input("│Dirección física:       ")
                if direccion == "":
                    direccion=info_contacto[6]
                    break
                elif len(direccion) >= 0 and len(direccion) <= 80:
                    break 
                else:
                    input("│EL CORREO DEBE TENER ENTRE 0 Y 80 CARACTERES ")
            # leer fecha ancimiento     
            while True:
                nacimiento = input("│Fecha nacimiento:       ")
                if nacimiento == "":
                    nacimiento=info_contacto[7]
                    break
                elif len(nacimiento)<=6 or nacimiento[2] != '/' or nacimiento[5] != '/':
                    input("│ERROR: LA ESTRUCTURA DE LA FECHA TIENE QUE SER DD/MM/AAAA con el / incluido") 
                else:
                    if int(nacimiento[3:5]) > 12:
                        input("│ERROR: EN EL MES SOLO SON VALIDOS NUMEROS DE 01 A 12")
                    else:
                        dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                        if len(nacimiento[7:10])!=4:
                            nacimiento= nacimiento[:6]+"0"
                        else:
                            if nacimiento[2:4] == 2 and ((nacimiento[7:10] % 4 == 0 and nacimiento[7:10] % 100 != 0) or nacimiento[7:10] % 400 == 0):
                                dias_por_mes[2] = 29
                        if int(nacimiento[:2]) < 1 or int(nacimiento[:2]) > dias_por_mes[int(nacimiento[3:5])]:
                            input("│ERROR: EN EL DIA ESE NUMEROS NO ES VALIDO")
                        else:
                            break
            # leer Pasatiempos     
            while True:
                pasatiempos = input("│Pasatiempos:            ")
                if pasatiempos == "":
                    pasatiempos=info_contacto[8]
                    break
                elif len(pasatiempos) >= 0 and len(pasatiempos) <= 60:
                    break 
                else:
                    input("│LOS PASATIEMPOS DEBE TENER ENTRE 0 Y 60 CARACTERES ")
            # leer Notas
            while True:
                notas = input("│Notas:                  ")
                if notas == "":
                    notas=info_contacto[9]
                    break
                elif len(notas) >= 0 and len(notas) <= 60:
                    break
                else:
                    input("│LAS NOTAS DEBE TENER ENTRE 0 Y 60 CARACTERES ")
            
            # leer opción y guardar datos !!!!
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    nueva_lista=[numero_telefono,info_contacto[1],info_contacto[2],info_contacto[3],nombre,correo,direccion,nacimiento,pasatiempos,notas]
                    borrar_contacto(contactos, numero_telefono)
                    contactos.append(nueva_lista)
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#Eliminar contactos
#Entradas: lista de contactos
#Salida: Lista actualizada
def eliminar_contactos(areas):
    while True:
            os.system("cls")
            print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                             ELIMINAR CONTACTO                               │""")
            # leer contacto
            while True:
                try:
                    numero_telefono = input("│Telefono:               ")
                    if numero_telefono == "C":
                        return
                    numero_telefono = int(numero_telefono)
                    if numero_telefono >= 99999 and numero_telefono <= 100000000000:
                        existe_numero, nombre_del_contacto = obtener_datos_contacto(contactos, numero_telefono)
                        if not existe_numero:
                            input("│ESTE CONTACTO NO ESTÁ REGISTRADO, NO SE PUEDE ELIMINAR")
                        else:
                            break
                    else:
                        input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
                except:
                    input("│ÁTELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
                    
            # leer opción y guardar datos
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    borrar_contacto(contactos, numero_telefono)
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
                

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

# Obtener datos de un grupo
# Entradas: lista de contactos, numero telefono
# Salidas: Si telefono existe en la lista retorna True y la tupla con sus datos, sino existe retorna False y tupla vacía
def obtener_datos_grupo(grupos, nombre_grupo):
    for elemento in grupos:
        if elemento == nombre_grupo:
            return True, elemento
    return False, tuple()

# Borra un area
# Entrada: areas, areas_telefono
# Salida: se elimina un area de la lista
def borrar_grupo(grupos, nombre_grupo):
    for elemento in grupos:
        if elemento == nombre_grupo:
            indice=grupos.index(elemento)
            del grupos[indice]
            
# Agregar contactos
# Entradas: lista de áreas
# S: lista de áreas actualizada 
def agregar_grupos(grupos):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                               AGREGAR GRUPOS                                │""")
            # leer grupo
            while True:
                nombre_grupo = input("│Nombre del grupo:               ")
                if nombre_grupo == "C":
                    return
                existe_grupo, info_grupo = obtener_datos_grupo(grupos, nombre_grupo)
                if existe_grupo:
                        input("│ESTE GRUPO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")
                else:
                        break
            # leer respuesta
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    grupos.append(nombre_grupo)
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

# Agregar contactos a grupo
# Entradas: lista de grupos y contactos
# S: lista grupo 
def agregar_contactos_a_grupo(grupos,contactos,contactos_por_grupos):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                          AGREGAR CONTACTO A GRUPO                           │""")
            
            # leer grupo
            while True:
                nombre_grupo = input("│Nombre del grupo:               ")
                if nombre_grupo == "C":
                    return
                existe_grupo, info_grupo = obtener_datos_grupo(grupos, nombre_grupo)
                if not existe_grupo:
                        input("│ESTE GRUPO NO EXISTE, NO PUEDE AGREGARLE CONTACTOS")
                else:
                        break
            #Lee grupo
            while True:
                try:
                    numero_telefono = input("│Telefono:               ")
                    if numero_telefono == "C":
                        return
                    numero_telefono = int(numero_telefono)
                    if numero_telefono >= 99999 and numero_telefono <= 100000000000:
                        existe_numero, info_contacto = obtener_datos_contacto(contactos, numero_telefono)
                        if not existe_numero:
                            input("│ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE AGREGAR")
                        else:
                            print("│Área:                   ",info_contacto[1])
                            print("│                        ",info_contacto[2][1])
                            print("│Tipo teléfono (M,C,T,O):",info_contacto[3])
                            print("│Nombre contacto:        ",info_contacto[4])
                            break
                    else:
                        input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")
                except:
                    input("│TELEFONO DEBE SER UN ENTERO DE 6 A 11 DIGITOS ")

            # leer opción y guardar datos
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    contactos_por_grupos.append([nombre_grupo,(numero_telefono,info_contacto[2],info_contacto[3],info_contacto[4])])
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

# Modifica nombre grupo
# Entradas: lista de grupos y 
# S: lista grupo 
def modificar_grupos(grupos,contactos_por_grupos):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                               MODIFICAR GRUPO                               │""")
            
            # leer grupo
            while True:
                nombre_grupo = input("│Nombre del grupo:               ")
                if nombre_grupo == "C":
                    return
                existe_grupo, info_grupo = obtener_datos_grupo(grupos, nombre_grupo)
                if not existe_grupo:
                        input("│ESTE GRUPO NO EXISTE, NO PUEDE MODIFICAR")
                else:
                        break
            # leer nombre grupo
            while True:
                nuevo_nombre_grupo = input("│nuevo nombre:               ")
                for elemento in contactos_por_grupos:
                    if not elemento[0] == nuevo_nombre_grupo:
                        eleccion=1
                        print("│GRUPO YA EXISTE, EN CASO DE ACEPTAR LA OPERACIÓN LOS CONTACTOS SE LE AGREGARÁN")
                        break
                eleccion=0
                break
            # leer opción y guardar datos
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    if eleccion==0:
                        borrar_grupo(grupos, nombre_grupo)
                        grupos.append(nuevo_nombre_grupo)
                        for elemento in contactos_por_grupos:
                            if elemento[0] == nombre_grupo:
                                indice=contactos_por_grupos.index(elemento)
                                contactos_por_grupos.append([nuevo_nombre_grupo,elemento[0:]])
                                del contactos_por_grupos[indice]
                        break
                    else:
                        borrar_grupo(grupos, nombre_grupo)
                        for elemento in contactos_por_grupos:
                            if elemento[0] == nombre_grupo:
                                indice=contactos_por_grupos.index(elemento)
                                for i in contactos_por_grupos:
                                    if i[0] == nuevo_nombre_grupo:
                                        indice2=contactos_por_grupos.index(i)
                                        contactos_por_grupos[indice]+=elemento[0:]
                                        del contactos_por_grupos[indice2]
                        break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
                
# Eliminar grupo
# Entradas: lista de grupos 
# S: lista grupo 
def eliminar_grupos(grupos,contactos_por_grupos):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                               ELIMINAR GRUPO                                │""")
            
            # leer grupo
            while True:
                nombre_grupo = input("│Nombre del grupo:               ")
                if nombre_grupo == "C":
                    return
                existe_grupo, info_grupo = obtener_datos_grupo(grupos, nombre_grupo)
                if not existe_grupo:
                        input("│ESTE GRUPO NO EXISTE, NO PUEDE SER ELIMINADO")
                else:
                    break
            # leer opción y actualizar
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    borrar_grupo(grupos, nombre_grupo)
                    for i in contactos_por_grupos:
                        if i[0] == nombre_grupo:
                            indice=contactos_por_grupos.index(i)
                            del contactos_por_grupos[indice]
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

# Eliminar contactos de grupo
# Entradas: lista de grupo y contactos en grupo 
# S: lista grupo 
def eliminar_contactos_de_grupos(grupos,contactos_por_grupos):
        while True:
            os.system("cls")
            print(""""


┌─────────────────────────────────────────────────────────────────────────────┐
│                         LISTA DIGITAL DE CONTACTOS                          │
│                         ELIMINAR CONTACTO DE GRUPO                          │""")
            
            # leer grupo
            while True:
                nombre_grupo = input("│Nombre del grupo:               ")
                if nombre_grupo == "C":
                    return
                existe_grupo, info_grupo = obtener_datos_grupo(grupos, nombre_grupo)
                if not existe_grupo:
                        input("│ESTE GRUPO NO EXISTE, NO PUEDE ELIMINARLE CONTACTOS")
                else:
                    break
            #Lee contacto de grupo
            while True:
                numero_telefono = input("│Telefono:               ")
                if nombre_grupo == "C":
                    return
                for elemento in contactos_por_grupos:
                    for info_contacto in elemento:
                        if info_contacto[0] == int(numero_telefono):
                            print("│Área:                   ",info_contacto[1][0])
                            print("│                        ",info_contacto[1][1])
                            print("│Tipo teléfono (M,C,T,O):",info_contacto[2])
                            print("│Nombre contacto:        ",info_contacto[3])
                            break
                    if info_contacto[0] == int(numero_telefono):
                        break
                if info_contacto[0] == int(numero_telefono):
                        break
                input("│ESTE CONTACTO NO EXISTE EN EL GRUPO, NO PUEDE ELIMINARLO")
            # leer opción y actualizar
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    for elemento in contactos_por_grupos:
                        if elemento[0] == nombre_grupo:
                            for i in elemento[1:]:
                                if i[0] == int(numero_telefono):
                                    indice=elemento.index(i)
                                    del elemento[indice]
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

# FILTROS
# Entradas: dato a filtrar
# Salidas: informacion para el pdf
def lista_con_algo(buscar, para_pdf, indice):
    momentaneo = []
    for contacto in para_pdf:
        contacto_modificado = []
        for i in contacto:
            if isinstance(i, str):
                i = i.replace(" ", "% %")
            contacto_modificado.append(i)
        revisar = str(contacto_modificado[indice]).lower()
        if re.search(buscar.lower(), revisar):
            momentaneo.append(contacto)
    if len(momentaneo) > 0:
        para_pdf.clear()
        para_pdf.extend(momentaneo)

def lista_grupo(buscar, para_pdf, contactos_por_grupos):
    momentaneo = []
    for grupo in contactos_por_grupos:
        if grupo[0].lower() == buscar.lower():
            for contacto in grupo[1:]:
                for contacto_i in para_pdf:
                    if contacto[0] == contacto_i[0] and contacto[1] == contacto_i[1]:
                        momentaneo.append(contacto_i)
    if len(momentaneo) > 0:
        para_pdf.clear()
        para_pdf.extend(momentaneo)

#########################################################################                    
# menú registrar áreas                                                  #

def menu_areas(areas):
    while True:
        os.system("cls")
        print("""



┌─────────────────────────────────────────────────────────────────────────────┐
│                     LISTA DIGITAL DE CONTACTOS                              │
│                           REGISTRAR ÁREAS                                   │
│                                                                             │
│ 1. Agregar áreas                                                            │
│ 2. Consultar áreas                                                          │
│ 3. Modificar áreas                                                          │
│ 4. Eliminar áreas                                                           │
│ 0. Fin                                                                      │""")
        opcion = input("│    OPCIÓN ")
        match opcion: 
            case "1":
                agregar_areas(areas)
            case "2":
                consultar_areas(areas)
            case "3":
                modificar_areas(areas)
            case "4":
                eliminar_areas(areas)  
            case "0":
                break
            case _: 
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#########################################################################                    
# menú Configuración de lista de contactos                              #

def menu_config (areas):
    while True:
            os.system("cls")
            print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                     LISTA DIGITAL DE CONTACTOS                              │
│               CONFIGURACIÓN DE LA LISTA DE CONTACTOS                        │
│                                                                             │""")
            # leer área
            while True:
                try:
                    area_por_omision = input("│   Área por omisión: ")
                    if area_por_omision == "C":
                        return 0, ""
                    area_por_omision = int(area_por_omision)
                    if area_por_omision >= 1 and area_por_omision <= 999:
                        existe_area, nombre_del_area = obtener_datos_area(areas, area_por_omision)
                        if existe_area:
                            print("│                    ",nombre_del_area[1])
                            break
                        else:
                            input("│ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE SELECCIONAR")
                    else:
                        input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                except:
                    input("│ÁREA DEBE SER UN ENTERO ENTRE 1 Y 999 ")
                    
            # Leer tipo de telefono por omision
            while True:
                tipo_telefono_por_omision = input("│   Tipo de teléfono por omisión (M:Móvil, C:Casa, T:Trabajo, O: Otro): ")
                if tipo_telefono_por_omision == "M" or tipo_telefono_por_omision == "C" or tipo_telefono_por_omision == "T" or tipo_telefono_por_omision == "O":
                    break
                else:
                    print("│ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR")
                    
            # leer opción y guardar datos
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    return area_por_omision,tipo_telefono_por_omision
                if opcion == "C":
                    area_por_omision = 0
                    tipo_telefono_por_omision = ""
                    print("│Operación cancelada")
                    return area_por_omision,tipo_telefono_por_omision
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#########################################################################                    
# menú registrar contactos                                              #

def menu_config_contactos (contactos,areas,TIPOS_TELEFONO,area_por_omision,tipo_telefono_por_omision):
    while True:
        os.system("cls")
        print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                     LISTA DIGITAL DE CONTACTOS                              │
│                        REGISTRAR CONTACTOS                                  │
│                                                                             │
│ 1. Agregar contactos                                                        │
│ 2. Consultar contactos                                                      │
│ 3. Modificar contactos                                                      │
│ 4. Eliminar contactos                                                       │
│ 0. Fin                                                                      │""")
        opcion = input("│    OPCIÓN ")
        match opcion: 
            case "1":
                agregar_contacto(contactos,areas,TIPOS_TELEFONO,area_por_omision,tipo_telefono_por_omision)
            case "2":
                consultar_contactos(contactos)
            case "3":
                modificar_contactos(contactos)
            case "4":
                eliminar_contactos(contactos)  
            case "0":
                break
            case _: 
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#########################################################################                    
# menú Administrar grupos de contactos                                  #

def menu_config_grupos (grupos):
    while True:
        os.system("cls")
        print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                     LISTA DIGITAL DE CONTACTOS                              │
│                   ADMINISTRAR GRUPOS DE CONTACTOS                           │
│                                                                             │
│ 1. Agregar grupos                                                           │
│ 2. Agregar contactos a los grupos                                           │
│ 3. Modificar grupos                                                         │
│ 4. Eliminar grupos                                                          │
│ 5. Eliminar contactos de los grupos                                         │
│ 0. Fin                                                                      │""")
        opcion = input("│    OPCIÓN ")
        match opcion: 
            case "1":
                agregar_grupos(grupos)
            case "2":
                agregar_contactos_a_grupo(grupos,contactos,contactos_por_grupos)
            case "3":
                modificar_grupos(grupos,contactos_por_grupos)
            case "4":
                eliminar_grupos(grupos,contactos_por_grupos)
            case "5":
                eliminar_contactos_de_grupos(grupos,contactos_por_grupos)
            case "0":
                break
            case _: 
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")

#########################################################################                    
# menú lista de contactos                                               #

def menu_lista_contactos(contactos,contactos_por_grupos):
    while True:
            os.system("cls")
            print("""


┌─────────────────────────────────────────────────────────────────────────────┐
│                     LISTA DIGITAL DE CONTACTOS                              │
│                        LISTA DE CONTACTOS                                   │
│                                                                             │""")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            #pdf.set_header("CONTACTOS")

            para_pdf=contactos
            print("│FILTROS:")
            indice=0
            nombre_contacto=input("│        Nombre contacto: ")
            if len(nombre_contacto) > 0:
                lista_con_algo(nombre_contacto, para_pdf,indice=4)
                    
            telefono=input("│        Numero telefono: ")
            if len(telefono) > 0:
                lista_con_algo(telefono, para_pdf,indice=0)

            area=input("│        Area: ")
            if len(area) > 0:
                lista_con_algo(area, para_pdf,indice=1)

            fecha_nacimiento=input("│        Fecha de nacimiento: ")
            if len(fecha_nacimiento) > 0:
                lista_con_algo(fecha_nacimiento, para_pdf,indice=7)

            pasatiempos=input("│        Pasatiempos: ")
            if len(pasatiempos) > 0:
                lista_con_algo(pasatiempos, para_pdf,indice=8)

            grupo=input("│        Grupo: ")
            if len(grupo) > 0:
                lista_grupo(grupo, para_pdf,contactos_por_grupos)
                
            # leer opción y guardar datos !!!!
            while True:
                opcion = input("│                     OPCIÓN     <A>ACEPTAR     <C>CANCELAR ")
                if opcion == "A":
                    pdf.cell(0, 10, "Listado de Contactos", ln=True, align='C')
                    pdf.ln(5)
                    for linea in para_pdf:
                        pdf.cell(0, 10, str(linea[4]), ln=True)
                        pdf.cell(0, 10, str(linea[0]), ln=True)
                        pdf.cell(0, 10, str(linea[1]), ln=True)
                        pdf.cell(0, 10, str(linea[2]), ln=True)
                        pdf.cell(0, 10, str(linea[3]), ln=True)
                        pdf.cell(0, 10, str(linea[5]), ln=True)
                        pdf.cell(0, 10, str(linea[6]), ln=True)
                        pdf.cell(0, 10, str(linea[7]), ln=True)
                        pdf.cell(0, 10, str(linea[8]), ln=True)
                        pdf.cell(0, 10, str(linea[9]), ln=True)
                        pdf.ln(5)
                    pdf.output("Contactos.pdf")
                    break
                if opcion == "C":
                    print("│Operación cancelada")
                    break
                input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
                
            
            
          
#########################################################################
# FUNCIÓN PRINCIPAL                                                     #
#########################################################################

# constante de tipos de teléfono: índices pares tienen código, siguiente índice sus descripciones
TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro") 

# inicializar estructuras
areas = [] # lista de áreas de teléfono
contactos = [] # lista con la información de cada contacto
grupos = [] # lista con los nombres de los grupos de contactos
contactos_por_grupos = [] # lista con los contactos asociados a cada grupo de contactos

# datos de configuración
area_por_omision = 0
tipo_telefono_por_omision = ""

# Menú principal
while True:
    os.system("cls")
    print("""



┌─────────────────────────────────────────────────────────────────────────────┐
│                     LISTA DIGITAL DE CONTACTOS                              │
│                                                                             │
│ 1. Registrar áreas                                                          │
│ 2. Configuración de lista de contactos                                      │
│ 3. Registrar contactos                                                      │
│ 4. Administrar grupos de contactos                                          │
│ 5. Lista de contactos                                                       │
│ 6. Ayuda                                                                    │
│ 7. Acerca de                                                                │
│ 0. Fin                                                                      │""")
    opcion = input("│    OPCIÓN ")
    match opcion: 
        case "1":
            menu_areas(areas)
        case "2":
            area_por_omision,tipo_telefono_por_omision = menu_config(areas)
        case "3":
            menu_config_contactos(contactos,areas,TIPOS_TELEFONO,area_por_omision,tipo_telefono_por_omision)
        case "4":
            menu_config_grupos(grupos)
        case "5":
            menu_lista_contactos(contactos,contactos_por_grupos)
        case "6":
            print("│En el .zip del programa puedes encontrar el manual de usuario del programa")
        case "7":
            print("""
│PROGRAMA: LISTA DIGITAL DE CONTACTOS
│VERSION: 1.0
│FECHA CREACION: 15/04/2024
│AUTOR: JOSHUA VALVARDE ARGUEDAS
""")
        case "0":
            break
        case _: # se ejecuta cuando ninguna de las opciones anteriores se ejecutó
            input("│OPCIÓN NO ES PERMITIDA. DAR <INTRO>")
            
print("FIN DEL PROGRAMA")
            


