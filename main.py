#arrays
names = []
company_performance = []
company_potential = []
auto_performance = []
auto_potential = []

#funcion para agregar empleados, y califiquen su performance y su potencial de crecimiento.
def add_empoyed() :
    employed = input("Ingrese su nombre y apellido: ")
    while employed == "" :
        employed = input("Ingrese su nombre y apellido: ")
    performance = int(input("Ingrese su perfomance dentro de la empresa: "))
    while performance < 1 or performance > 5:
        performance = int(input("Ingrese su perfomance dentro de la empresa: "))
    potential = int(input("Ingrese su potencial de crecimiento dentro de la empresa: "))
    while potential < 1 or potential > 5:
        potential = int(input("Ingrese su potencial de crecimiento dentro de la empresa: "))

    names.append(employed)
    auto_performance.append(performance)
    auto_potential.append(potential)

    print(f"{employed}, agregado correctamente")

#mostrar los empleados cargados.
def shows_employed():
    if names == []:
        print("No hay empleados cargados.")
    else:
        print("Empleados cargados:")
        for i in range(len(names)):
            print(f"{i+1}. {names[i]} | Performance: {auto_performance[i]}, Potencial: {auto_potential[i]}")
        print()

# funcion main que sirve como "menu" para que ul usario elija que desea realizar.
def main():
    run = int(input("Desea correr el programa? (si, precione 1. no, precione -1) "))
    while run != -1:
        if run == 1:
            print("Opcion 1 cargar resultados")
            print("Opcion 2 agregar empleado")
            print("Opcion 3, salir")

            option = int(input("Ingrese una opcion: "))
            if option == 1:
                shows_employed()
            elif option == 2:
                add_empoyed()
            elif option == 3:
                print("Fin del programa")
                break
            else:
                print("Opcion invalida")
        else:
            print("Opcion invalida")
            run = int(input("Desea correr el programa? (si, precione 1. no, precione -1) "))


#ejecuta la funcion.
main()
