class Persona:
    def __init__(self, nombre, identificacion, edad, contacto, email, direccion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = edad
        self.contacto = contacto
        self.email = email
        self.direccion = direccion

    def __repr__(self):
        return f"Nombre: {self.nombre}, Identificación: {self.identificacion}, Edad: {self.edad}, Contacto: {self.contacto}, Email: {self.email}, Dirección: {self.direccion}"


class Enfermera(Persona):
    def __init__(self, nombre, identificacion, edad, contacto, email, direccion, especialidad, experiencia, horario):
        super().__init__(nombre, identificacion, edad, contacto, email, direccion)
        self.especialidad = especialidad
        self.experiencia = experiencia
        self.horario = horario

    def __repr__(self):
        return super().__repr__() + f", Especialidad: {self.especialidad}, Experiencia: {self.experiencia} años, Horario: {self.horario}"


class Paciente(Persona):
    def __init__(self, nombre, identificacion, edad, contacto, email, direccion, genero, condicion, emergencia, alergias):
        super().__init__(nombre, identificacion, edad, contacto, email, direccion)
        self.genero = genero
        self.condicion = condicion
        self.emergencia = emergencia
        self.alergias = alergias

    def __repr__(self):
        return super().__repr__() + f", Género: {self.genero}, Condición: {self.condicion}, Emergencia: {self.emergencia}, Alergias: {self.alergias}"


def validar_entrada(tipo, mensaje):
    while True:
        entrada = input(mensaje)
        if tipo == 'int':
            try:
                return int(entrada)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif tipo == 'str':
            if entrada.strip() == "":
                print("Este campo no puede estar vacío.")
            else:
                return entrada
        elif tipo == 'gmail':
            if "@" in entrada and "." in entrada:
                return entrada
            else:
                print("Por favor, ingrese un correo electrónico válido.")


def registrar_persona():
    nombre = validar_entrada('str', "Ingrese su nombre completo: ")
    identificacion = validar_entrada('str', "Ingrese su número de identificación profesional si es enfermera sino ingrese su numero de documento: ")
    edad = validar_entrada('int', "Ingrese su edad: ")
    contacto = validar_entrada('str', "Ingrese su número de contacto: ")
    email = validar_entrada('gmail', "Ingrese su correo electrónico: ")
    direccion = validar_entrada('str', "Ingrese su dirección: ")

    return nombre, identificacion, edad, contacto, email, direccion


def registrar_enfermera():
    nombre, identificacion, edad, contacto, email, direccion = registrar_persona()
    especialidad = validar_entrada('str', "Ingrese la especialidad: ")
    experiencia = validar_entrada('int', "Ingrese los años de experiencia: ")
    horario = validar_entrada('str', "Ingrese la disponibilidad horaria: ")

    return Enfermera(nombre, identificacion, edad, contacto, email, direccion, especialidad, experiencia, horario)


def registrar_paciente():
    nombre, identificacion, edad, contacto, email, direccion = registrar_persona()
    genero = validar_entrada('str', "Ingrese el género: ")
    condicion = validar_entrada('str', "Ingrese la enfermedad o condición médica principal: ")
    emergencia = validar_entrada('str', "Ingrese el nombre y número de contacto de una persona en caso de emergencia: ")
    alergias = validar_entrada('str', "Ingrese alergias y medicamentos actuales: ")

    return Paciente(nombre, identificacion, edad, contacto, email, direccion, genero, condicion, emergencia, alergias)


def mostrar_lista(lista):
    for persona in lista:
        print(persona)


def buscar_por_identificacion(lista, identificacion):
    for persona in lista:
        if persona.identificacion == identificacion:
            return persona
    return None


# Implementación del algoritmo de Burbuja
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Comparación por el nombre (posición 0 en cada lista)
            if lista[j].nombre.lower() > lista[j + 1].nombre.lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def registrar_usuario():
    enfermeras = []  # Lista de objetos Enfermera
    pacientes = []   # Lista de objetos Paciente

    while True:
        usuario = input("¿Es usted enfermera o paciente? (enfermera/paciente): ").strip().lower()
        if usuario == 'enfermera':
            enfermeras.append(registrar_enfermera())
            print("Datos de la enfermera registrados exitosamente.")
        elif usuario == 'paciente':
            pacientes.append(registrar_paciente())
            print("Datos del paciente registrados exitosamente.")
        else:
            print("Opción no válida, intente de nuevo.")

        continuar = input("¿Desea registrar a otra persona? (si/no): ").strip().lower()
        if continuar != 'si':
            print("Proceso de registro finalizado.")
            break

    # Ordenar las listas usando Burbuja
    ordenar_burbuja(enfermeras)
    ordenar_burbuja(pacientes)

    # Mostrar los registros ordenados
    print("\nEnfermeras Registradas:")
    mostrar_lista(enfermeras)

    print("\nPacientes Registrados:")
    mostrar_lista(pacientes)

    # Búsqueda por identificación
    identificacion = input("\nIngrese una identificación para buscar: ")
    resultado = buscar_por_identificacion(enfermeras + pacientes, identificacion)
    if resultado:
        print("Persona encontrada:", resultado)
    else:
        print("No se encontró ninguna persona con esa identificación.")


# Ejecutar el programa
registrar_usuario()
