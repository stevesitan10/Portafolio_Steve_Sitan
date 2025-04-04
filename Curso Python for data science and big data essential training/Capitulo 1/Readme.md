# Funciones básicas para tiempo
-time.time()       # Devuelve el tiempo actual en segundos desde la época (1 de enero de 1970)
-time.sleep(s)     # Suspende la ejecución del programa durante 's' segundos
-time.ctime([sec]) # Convierte un tiempo en segundos a una cadena de texto (formato local)

# Estructuras de tiempo
-time.gmtime([sec])    # Convierte segundos a struct_time en UTC
-time.localtime([sec]) # Convierte segundos a struct_time en hora local
-time.mktime(t)        # Convierte struct_time a segundos desde la época

# Formateo de tiempo
-time.strftime(format[, t]) # Formatea struct_time según el formato especificado
-time.strptime(string, format) # Analiza una cadena según el formato y devuelve struct_time

# Rendimiento y precisión
-time.perf_counter() # Devuelve el valor del contador de rendimiento (alta resolución)
-time.process_time() # Devuelve el tiempo de CPU del proceso actual
-time.monotonic()    # Devuelve un valor de tiempo monótono (no afectado por ajustes del sistema)

# Para medir tiempos precisos
-time.perf_counter_ns() # Como perf_counter() pero devuelve nanosegundos
-time.monotonic_ns()    # Como monotonic() pero devuelve nanosegundos
-time.process_time_ns() # Como process_time() pero devuelve nanosegundos

# Información de zona horaria
-time.timezone  # Desplazamiento de la zona horaria local en segundos al oeste de UTC
-time.tzname    # Tupla de nombres de zona horaria (no DST, DST)
-time.daylight  # Si se define una corrección DST
