class Cola:
    def __init__(self):
        self.__elementos = []

    def arrive(self, value):
        self.__elementos.append(value)

    def atention(self):
        if self.size() > 0:
            return self.__elementos.pop(0)

    def size(self):
        return len(self.__elementos)

    def on_front(self):
        if self.size() > 0:
            return self.__elementos[0]

    def move_to_end(self):
        if self.size() > 0:
            aux = self.atention()
            self.arrive(aux)
            return aux
    
    def eliminar_notificaciones_facebook(self):
        self.__elementos = [notificacion for notificacion in self.__elementos if notificacion.app != 'Facebook']

    def mostrar_notificaciones_twitter_con_python(self):
        for notificacion in self.__elementos:
            if notificacion.app == 'Twitter' and 'Python' in notificacion.mensaje:
                print(f"{notificacion.app} - {notificacion.mensaje}")

    def pila_temporal_entre_horas(self, hora_inicio, hora_fin):
        pila_temporal = Cola()
        for notificacion in self.__elementos:
            if hora_inicio <= notificacion.hora <= hora_fin:
                pila_temporal.arrive(notificacion)
        return pila_temporal

class Notificacion:
    def __init__(self, hora, app, mensaje):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje

cola_notificaciones = Cola()
cola_notificaciones.arrive(Notificacion("11:30", "Twitter", "mensaje_1"))
cola_notificaciones.arrive(Notificacion("12:45", "Facebook", "mensaje_2"))
cola_notificaciones.arrive(Notificacion("13:15", "Twitter", "Python"))
cola_notificaciones.arrive(Notificacion("14:30", "Facebook", "Mensaje_4"))
cola_notificaciones.arrive(Notificacion("15:50", "Instagram", "Mensaje_5"))

cola_notificaciones.eliminar_notificaciones_facebook()

cola_notificaciones.mostrar_notificaciones_twitter_con_python()

pila_temporal = cola_notificaciones.pila_temporal_entre_horas("11:43", "15:57")

print("Notificaciones temporales:")
while pila_temporal.size() > 0:
    notificacion_temporal = pila_temporal.atention()
    print(f"{notificacion_temporal.app} - {notificacion_temporal.mensaje}")