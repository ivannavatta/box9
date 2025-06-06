#arrays
names = []
company_performance = []
company_potential = []
auto_performance = []
auto_potential = []

#funcion para agregar empleados, y califiquen su performance y su potencial de crecimiento.
def add_employed() :
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
            print(f"{i+1}. {names[i]} | Auto-Performance: {auto_performance[i]}, Auto-Potencial: {auto_potential[i]}")
        print()

#funcion que sirve para que los empleados puedan actualizar sus datos
def update_data():
    employed = input("Ingrese su nombre y apellido: ")
    while employed == "" :
        employed = input("Ingrese su nombre y apellido: ")   
    for i in range(len(names)):
        employed_name = names[i]
        if employed_name == employed:
            print(f"name: {names[i]}")
            print(f"Auto-Performance: {auto_performance[i]}")
            print(f"Auto-Potencial: {auto_potential[i]}")
            updated_info = int(input("Desea actualizar todos los campos? (Si, precione 1. No, precione -1): "))
            while updated_info > 1 or updated_info < -1 :
                updated_info = int(input("Desea actualizar todos los campos? (Si, precione 1. No, precione -1): "))
            if updated_info == 1:
                update_performance = int(input("Ingrese su nueva performance: "))
                while update_performance < 1 or update_performance > 5:
                    update_performance = int(input("Ingrese su nueva performance: "))
                auto_performance[i] = update_performance
                update_potential = int(input("Ingrese su nuevo potencial: "))
                while update_potential < 1 or update_potential > 5:
                    update_potential = int(input("Ingrese su nueva potencial: "))
                auto_potential[i] = update_potential
            elif updated_info == -1:
                updated_info = int(input("Desea actualizar su performance o su potencial? (Performance, 1. Potencial, 2): "))
                while updated_info > 2 or updated_info < 1:
                    updated_info = int(input("Desea actualizar su performance o su potencial? (Performance, 1. Potencial, 2): "))
                if updated_info == 1:
                    update_performance = int(input("Ingrese su nueva performance: "))
                    while update_performance < 1 or update_performance > 5 :
                        update_performance = int(input("Ingrese su nueva performance: "))
                    auto_performance[i] = update_performance
                    return
                elif updated_info == 2:
                    update_potential = int(input("Ingrese su nuevo potencial: "))
                while update_potential < 1 or update_potential > 5:
                    update_potential = int(input("Ingrese su nuevo potencial: "))
                auto_potential[i] = update_potential
                
            return
    print("Empleado no encontrado")

def best_employee():
    if names == []:
        print("No hay empleados cargados.")
        return
    else :
        best_score=  -1
        best_employee = ""
        print("Mejor empleado:")
        for i in range(len(names)):
            score= auto_performance[i] * auto_potential[i]
            print(f"{names[i]} | Auto-Performance: {auto_performance[i]}, Auto-Potencial: {auto_potential[i]}, Puntaje: {score}")
            if score > best_score:
                best_score = score
                best_employee = names[i]

    print(f"El mejor empleado es: {best_employee} con un puntaje de {best_score}")        
# funcion main que sirve como "menu" para que el usario elija que desea realizar.
def main():
    run = int(input("Desea correr el programa? (si, presione 1. no, presione -1): "))
    while run != -1:
        if run == 1:
            print("Opcion 1, cargar resultados")
            print("Opcion 2, agregar empleado")
            print("Opcion 3, actualizar datos")
            print("Opcion 4, mejor empleado")
            print("Opcion 5, salir")

            option = int(input("Ingrese una opcion: "))
            if option == 1:
                shows_employed()
            elif option == 2:
                add_employed()
            elif option == 3:
                update_data()
            elif option == 4:
                best_employee()
            elif option == 5:  
                print("Fin del programa")
                break
            else:
                print("Opcion invalida")
        else:
            print("Opcion invalida")
            run = int(input("Desea correr el programa? (si, presione 1. no, presione -1): "))



#ejecuta la funcion.
main()
