from datetime import datetime
import random
import math

#Definir cuantos cupos tiene el parqueadero en motos y carros
print("////BIENVENIDO AL SISTEMA DE PARQUEADEROS GALVIS////"  )
print("----------------------------------------------------")
camp_cars = None
camp_motorcycles = None

while camp_cars is None or camp_cars <= 0:
    try:
        camp_cars = int(input('Ingresa la cantidad de parqueaderos para carros: '))
        if camp_cars <= 0:
            print("Ingresa un número positivo mayor que cero.")
    except ValueError:
        print("Por favor ingresa un número válido.")

while camp_motorcycles is None or camp_motorcycles <= 0:
    try:
        camp_motorcycles = int(input('Ingresa la cantidad de parqueaderos para motos: '))
        if camp_motorcycles <= 0:
            print("Ingresa un número positivo mayor que cero.")
    except ValueError:
        print("Por favor ingresa un número válido.")


#Definir los campos del parqueadero
name_camp_cars = []
name_camp_moto = []

while int(len(name_camp_cars)) < camp_cars:
    name_camp_cars.append({"place": str(input('Ingresa el nombre del campo del parqueadero de carro: ')),'avalible':True})

while int(len(name_camp_moto)) < camp_motorcycles:
    name_camp_moto.append({'place': str(input('Ingresa el nombre del campo del parqueadero de moto: ')),'avalible':True})
               
#Definir tarifa de cobro por tiempo
cost_frac_car = 2000
cost_frac_moto = 1000

#Registrar entrada de vehicula o cobrar parqueadero
register_car = []
register_motorcycle =[]

while True:
#recorrer un for dentro de una lista para consultar los diccionarios que hay
    place_free_moto = [x['place'] for x in name_camp_moto if x['avalible'] == True]
    place_free_car = [x['place'] for x in name_camp_cars if x['avalible'] == True]
    print('lugares disponibles:',place_free_car,place_free_moto)

    print('¿QUÉ OPCIÓN DESEAS REALIZAR?')
    options = input('1. Registrar nuevo vehículo\n2. Registrar salida de vehículo\n3. Salir.\nOpción >: ')
     
    #Opcion para registrar Moto
    if options == '1':
        if len(place_free_moto) > 0 or len(place_free_car) > 0:
            type_vehicule = input('¿QUÉ TIPO DE VEHÍCULO DESEAS REGISTRAR?\n1. Moto\n2. Carro\nOpción >: ')
            if type_vehicule == '1' and len(place_free_moto) > 0:
                placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO >: '))
                hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                place_random = random.choice(place_free_moto)
                register_motorcycle.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})
                for x in name_camp_moto:
                    if x['place'] == place_random:
                        x['avalible'] = False
                print('El registro de vehículos es el siguiente: ', register_motorcycle)
                print("\n")

            #registrar carro
            elif type_vehicule == '2' and len(place_free_car) > 0:
                placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHÍCULO >: '))
                hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                place_random = random.choice(place_free_car)
                register_car.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})
                for x in name_camp_cars:
                    if x['place'] == place_random:
                        x['avalible'] = False
                print('El registro de vehículos es el siguiente: ', register_car)
                print("\n")
            elif len(place_free_moto) == 0:
                print('PARQUEADERO DE MOTOS LLENO')
            elif len(place_free_car) == 0:
                print('PARQUEADERO DE CARROS LLENO')
            else:
                print('POR FAVOR INTRODUCE UNA SELECCIÓN VÁLIDA')
        else:
            print('PARQUEADERO LLENO, ESPERA QUE SALGA UN VEHÍCULO')

    #cobrar parqueadero    
    elif options == '2':
        option_cash = input('POR FAVOR DIGITA EL TIPO DE VEHÍCULO A COBRAR\n1. Moto\n2. Carro\nOpción: ')
        if option_cash == '1':
            placa_pay = str(input('POR FAVOR DIGITA LA PLACA A COBRAR: '))
            if any(x['placa'] == placa_pay and x['Action'] == 'Entro' for x in register_motorcycle):
                hour_inside = [x['hour_inside'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro'][0]
                place_out = [x['place'] for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro'][0]
                hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
                total = datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(str(hour_inside), '%Y-%m-%d %H:%M')
                total = total.total_seconds() / 60
                total = math.ceil(total)
                total = total * cost_frac_moto
                print('Tu valor a pagar de parqueo es => ', total)

                #liberar parqueadero
                for x in name_camp_moto:
                    if x['place'] == str(place_out):
                        x['avalible'] = True
                for x in register_motorcycle:
                    if x['placa'] == placa_pay:
                        x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                        x['pay_all'] = total
                        x['Action'] = 'saliendo'
                print('Los vehículos motorizados registrados son los siguientes: ', register_motorcycle)
                print("\n")
            else:
                print('LA PLACA CONSULTADA NO FUE ENCONTRADA')

        elif option_cash == '2':
            placa_pay = str(input('POR FAVOR DIGITA LA PLACA A COBRAR: '))
            if any(x['placa'] == placa_pay and x['Action'] == 'Entro' for x in register_car):
                hour_inside = [x['hour_inside'] for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro'][0]
                place_out = [x['place'] for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro'][0]

                 #calcular tiempo de cobro
                hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
                total = datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(str(hour_inside), '%Y-%m-%d %H:%M')
                total = total.total_seconds() / 3600
                total = math.ceil(total)
                total = total * cost_frac_car
                print('Tu valor a pagar de parqueo es => ', total)

                #liberar parqueadero
                for x in name_camp_cars:
                    if x['place'] == str(place_out):
                        x['avalible'] = True
                for x in register_car:
                    if x['placa'] == placa_pay:
                        x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                        x['pay_all'] = total
                        x['Action'] = 'salio'
                print('Los vehículos registrados son los siguientes: ', register_car)
            else:
                print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
        else:
            print('POR FAVOR INTRODUCE UNA SELECCIÓN VÁLIDA')

    elif options.lower() == '3':
        print("Salió del programa")
        break
    else:
        print('POR FAVOR INTRODUCE UNA SELECCIÓN VÁLIDA')