def suma(resultado = 0):
	
	print("Si quieres dejar de introducir numeros, presiona 'S' \n")

	x = 0
	print(" ",resultado)
	x = input('+ ')

	try:
		while True:
			resultado = float(x) + resultado

			print("------ ")
			print(" ",resultado)
			x = input('+ ')
	except ValueError:
		print("No has introducido un numero")
	finally:
		print("Tu resultado es: ", resultado)
		return resultado
		
def resta(resultado = 0):
	
	print("Si quieres dejar de introducir numeros, presiona 'S' \n")

	x = 0
	print(" ",resultado)
	x = input("- ")

	try:
		while True:
			resultado = resultado - float(x)
			print("------ ")
			print(" ",resultado)
			x = input("- ")
	except ValueError:
		print("No has introducido un numero")
	finally:
		print("Tu resultado es: ", resultado)
		return resultado

def multi(resultado = 1):

	print("Si quieres dejar de introducir numeros, presiona 'S' \n")
	x = 0
	print(" ",resultado)
	x = input("* ")


	try:
		while True:
			resultado = resultado * float(x)
			print("------ ")
			print(" ",resultado)
			x = input("* ")
	except ValueError:
		print("No has introducido un numero")
	finally:
		print("Tu resultado es: ", resultado)
		return resultado

def division(resultado = 1):

	print("Si quieres dejar de introducir numeros, presiona 'S' \n")
	x = 0
	print(" ",resultado)
	x = input("/ ")


	try:
		while True:
			try:
				resultado = resultado / float(x)
				print("------ ")
				print(" ",resultado)
				x = input("/ ")
				
			except ZeroDivisionError:
				print('No Puedes dividir entre 0: ')
				print(" ",resultado)
				x = input("/ ")
	except ValueError:
		print("No has introducido un numero")
	finally:
		print("Tu resultado es: ", resultado)
		return resultado

print('''******************************************

	Bienvenido a la calculadora

******************************************


''')

bandera = True

resultado = 0

while bandera == True:
	print('''

	Ingresa el numero de operacion que quieres Realizar, para finalizar, presiona 'S'


		Operaciones:

			1. Suma


			2. Resta


			3. Multiplicacion


			4. Division 


	Para borrar tu resultado acumulado presiona 0  	''')

	opcion = input()

	if opcion == '1':
		
		resultado = suma(resultado)

	elif opcion == '2':
		
		resultado = resta(resultado)

	elif opcion == '3':

		resultado = multi(resultado)

	elif opcion == '4':

		resultado = division(resultado)

	elif opcion == '0':

		resultado = 0

		print('''

		>>>RESULTADO ACUMULADO BORRADO<<<

		''')

	else:

		print(''' *************************
 ADIOS
 ************************''')
		bandera = False


