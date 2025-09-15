# INICIO
# INGRESO DE DATOS POR EL USUARIO (INGRESA LA FECHA)
fecha_hoy = input("INGRESE LA FECHA DE HOY EN EL SIGUIENTE FORMATO(DIA SEMANA, DD/MM): ")
#SEPARAMOS EL STRING EN DISTINTAS VARIABLES PARA TRABAJARLAS
dia_semana, fecha = fecha_hoy.split(",") 
dia_num, mes_num = fecha.split("/")
dia_num = int(dia_num)
mes_num = int(mes_num)
#VALIDAMOS EL DIA DE LA SEMANA
#DECLARO LA VARIABLE ERROR PARA QUE SI FALLA EL PROGRAMA TERMINE
error = False
dia_semana = dia_semana.capitalize() 
dias_validos = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
if dia_semana not in dias_validos:
    print("ERROR: EL DIA DE LA SEMANA NO ES VÁLIDO")
    error = True
#VALIDAMOS EL NUMERO DEL MES Y SI COINCIDE CON LA CANTIDAD DE DIAS
dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if mes_num not in range(1,13):
    print("ERROR: EL MES NO ESTÁ EN EL RANGO")
    error = True
else: 
    if dia_num < 1 or dia_num > dias_por_mes[mes_num-1]:
        print("ERROR: EL DIA NO CORRESPONDE A UNA FECHA CORRECTA")
        error = True
#SI EL USUARIO ES DE NIVEL INICIAL, INTERMEDIO O AVANZADO VERIFICAMOS SI SE TOMARON EXAMENES Y EL PORCENTAJE DE APROBADOS
if not error:
    examen = ["Lunes", "Martes", "Miercoles"]
    if dia_semana in examen:
        tomaron_examen = input("¿TOMARON EXAMEN? SI/NO: ") 
        tomaron_examen = tomaron_examen.capitalize()
        if tomaron_examen == "Si":
            aprobados_examen = int(input("¿CUANTOS APROBARON?:  "))
            desaprobados_examen = int(input("¿CUANTOS DESAPROBARON?:  "))
            total_examenes = aprobados_examen + desaprobados_examen
            porcentaje_aprobados = (aprobados_examen/total_examenes) * 100
            print(f"EL PORCENTAJE DE APROBADOS ES {porcentaje_aprobados}%")
#SI EL USUARIO ES DE PRÁCTICA HABLADA VERIFICAMOS EL PORCENTAJE DE ASISTENCIA
    if dia_semana == "Jueves":
        porcentaje_asistencia = int(input("INGRESE EL PORCENTAJE DE ASISTENCIA DEL CURSADO: "))
        if porcentaje_asistencia >= 50:
            print("ASISTIO LA MAYORIA")
        else:
            print("NO ASISTIO LA MAYORIA")
#VERIFICAR SI ES EL COMIENZO DE UN CICLO LECTIVO DE INGLES PARA VIAJEROS Y CALCULAR EL ARANCEL
    if dia_semana=="Viernes":
        if dia_num==1 and (mes_num==1 or mes_num==7):
            print("COMIENZO DE UN NUEVO CICLO LECTIVO")
            cantidad_alumnos = int(input("INGRESE LA CANTIDAD DE ALUMNOS: "))
            arancel_por_alumno = int(input("INGRESE EL ARANCEL POR ALUMNO: "))
            ingreso_total = cantidad_alumnos * arancel_por_alumno
            print(f"EL INGRESO TOTAL ES {ingreso_total}$")
        else:
            print("NO COMIENZA CICLO LECTIVO")



