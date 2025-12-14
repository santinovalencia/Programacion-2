import tkinter as tk

app = tk.Tk()
palabra = tk.StringVar(app)
entrada = tk.StringVar(app)

app.geometry("400x600")
app.configure(background="blue")
tk.Wm.wm_title(app, "Adivina el numero")

def adivina():
    print("Adivina")

tk.Entry(
    fg="white",
    bg="black",
    justify="center"
        
).pack(
    fill=tk.BOTH,
    expand=True,
)

tk.Button(
    app,
    text="mandar respuesta",
    font=("Courier", 14),
    bg="#00a8e8",
    fg="white",
    command=lambda: print("adivina")
    
).pack(
    fill=tk.BOTH,
    expand=True,
)

