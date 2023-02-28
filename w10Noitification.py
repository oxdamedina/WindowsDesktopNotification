#-------------------------------------------------------------------------------
# Name:       w10Noitification.py
# Purpose:    Notificación Escritorio W10
# Version:    v0.0.1
# Author:     David Alvarez Medina
# Created:    28/02/2023
#-------------------------------------------------------------------------------

# Change Log -------------------------------------------------------------------
#	- v0.0.1: Ejemplo envío notificación de escritorio W10
#-------------------------------------------------------------------------------

import time
from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Ejemplo 1", "Notificación de 10 segundos con iocono", icon_path="custom.ico", duration=10)
toaster.show_toast("Ejemplo 2", "Notificación de 5 segundos sin icono y ejecutada dentro de su propio hilo", icon_path=None, duration=5, threaded=True)

# Wait for threaded notification to finish
while toaster.notification_active(): time.sleep(0.1)
