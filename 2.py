import random


#crear un diccionario
mi_dicccionario = {}

#llenar el diccionario
mi_dicccionario["Bolívar"] = "Cartagena"
mi_dicccionario["Santander"] = "Bucaramanga"
mi_dicccionario["Nariño"] = "Pasto"
mi_dicccionario["Risaralda"] = "Pereira"
mi_dicccionario["Cesar"] = "Valledupar"
mi_dicccionario["Boyacá"] = "Tunja"
mi_dicccionario["Tolima"] = "Ibagué"
mi_dicccionario["Quindío"] = "Armenia"

#crear el ciclo
while True:
    print('Departamentos de colombia')
    for departamento in mi_dicccionario:
        print(departamento)
        
        
        #apartamento random
        departamento_azar = random.choice(list(mi_dicccionario.keys()))
        
        #peticion
        intentos = 0
        while intentos < 3:
            respuesta_user = input(f"Ingrese la capital de {departamento_azar} (o escriba 'salir' para terminar la ejecucion )" ).strip()
            if respuesta_user.lower() == 'salir':
                exit()  #salir del programa
                
            elif respuesta_user == mi_dicccionario[departamento_azar]:
                print("Correcto!")
                break #salir del ciclo si a cierta
            else:
                print("Respuesta incorrecta. INTENTA OTRA VEZ")
                print("La primera letra es con Mayuscula")
                intentos +=1
        else:
            print("Has pertido tus tres oportunidades.   ")
            # Eliminar el departamento adivinado para no repetirlo
    del mi_dicccionario[departamento_azar]
    
    
    
    