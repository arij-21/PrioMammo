import tkinter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, filedialog, PhotoImage, Label, Entry, Button, Frame, StringVar, ttk
import os
import csv
from datetime import datetime, timedelta
import tkinter
from tkinter import PhotoImage
from asyncio import windows_events
from tkinter import *
from tkinter import Label, Entry, Button, Checkbutton, messagebox, filedialog, IntVar, StringVar, LabelFrame
import csv
import os
import tkinter as ttk
from customtkinter import CTkButton
from PIL import Image, ImageTk 
import csv
import os
from win32 import win32print
from win32 import win32api
import threading
import requests
from tkcalendar import Calendar
from PIL import Image, ImageTk
from datetime import datetime, timedelta
import re
from tkinter.ttk import Combobox, Style
import pandas as pd
import webbrowser

# Fenêtre principale de l'application
window = tk.Tk()
window.title("My App")
window.geometry("1000x700")

# Load and display the logo image
logo_path = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo200.png")  # Modify the path as per your logo image
logo_label = Label(window, image=logo_path, bg="#fde4f2")
logo_label.place(relx=0.85, rely=0.73, anchor="nw")  # Adjust relx, rely, and anchor as needed


# Chargement et affichage de l'image de fond
image_path = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\maintranss.png")  # Modifiez le chemin selon votre image
bg_image = Label(window, image=image_path)
bg_image.place(relheight=1, relwidth=0.3)

window.configure(bg="#fde4f2")
head_frame = Frame(window, bg="#fde4f2")
head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

def show_login_window():
    window.withdraw()
    # Fenêtre de connexion
    window11 = tk.Toplevel(window)
    window11.title('Se Connecter')
    window11.geometry('800x700')
    window11.configure(bg="#fff")
    window11.resizable(True, True)
    
    
    # Load and display the logo image
    logo_path1 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo100.png")  # Modify the path as per your logo image
    window11.logo_path1 = logo_path1  # Keep a reference to the image object
    logo_label1 = Label(window11, image=logo_path1, bg="#fff")
    logo_label1.place(relx=0.85, rely=0.85, anchor="nw")  # Adjust relx, rely, and anchor as needed

    


    # Fonction pour gérer la connexion
    def connecter():
        username = user.get()
        password = code.get()
        if username == "Agent" and password == "Agent123mammo":
            # Ouverture de la fenêtre pour l'Agent
            open_agent_window()
            window11.destroy()
        elif username == "Medecin" and password == "Medecin456mammo":
            # Ouverture de la fenêtre pour le Médecin
            open_SMS_window()
            window11.destroy()
        elif username == "Admin" and password == "admin789mammo":
            # Ouverture de la fenêtre pour l'admin
            open_admin_window()
            window11.destroy()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")
       
    user_var = StringVar()
    pass_var = StringVar()
    
    
    
    img= PhotoImage(file='sidesign111.png')
    image_label = Label(window11, image=img, bg='white')
    image_label.image = img  # Store the image as an attribute of the label
    image_label.place(x=50, y=50) 
    
    
    
    frame11= Frame(window11, width=390, height=560, bg="#fff")
    frame11.place(x=390, y=20)

    heading= Label(frame11, text='Bienvenue sur votre compte!', fg='#fea6be', bg='#fff', font=('Arial', 15, 'bold'))
    heading.place(x=60, y=5)

    heading= Label(frame11, text='Connectez-vous à votre compte', fg='#606060', bg='#fff', font=('Microsoft YaHei UI Light', 9, 'bold'))
    heading.place(x=84, y=40)

    #######--------------------------------------------------------
    def on_enter(e):
     user.delete(0, 'end')
    
    def on_leave(e):
     name=user.get()
     if name=='':
        user.insert()(0, "Nom d'Utilisateur")    
        
        
    user= Entry(frame11, width=25, fg='#777777', border=0, bg='#fff', font=("Microsoft YaHei UI Light", 11))
    user.place(x=120, y=120)
    user.insert(0, "Nom d'utilisateur")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame11, width=230, height=2, bg='#333333').place(x=60, y=143)

    #######------------------------------------------------------------------

    def on_enter1(e1):
     code.delete(0, "end")
    
    def on_leave1(e1):
     name=code.get() 
     if name=='':
        code.insert(0, "Mot De Passe")   
    
  

    code= Entry(frame11, width=25, fg='#777777', border=0, bg='#fff', font=('Microsoft YaHei UI Light', 11), show='*' )
    code.place(x=120, y=190)
    code.insert(0, 'Mot De Passe')
    code.bind('<FocusIn>', on_enter1)
    code.bind('<FocusOut>', on_leave1)
    Frame(frame11, width=230, height=2, bg='#333333').place(x=60, y=213)
    #########################################################
    
    def close_log():
        window11.destroy()
        

    Button(frame11, pady=10, padx=30, width=10, command=connecter, text='Se Connecter', bg='#fea6be', fg='#fff', border=0, font=('Microsoft YaHei UI Light', 10, 'bold')).place(x=50, y=400)
    Button(frame11, pady=10, padx=30, width=10, text='Quitter', bg='#fea6be', fg='#fff', border=0, font=('Microsoft YaHei UI Light', 10, 'bold'), command=close_log).place(x=230, y=400)

    #label= Label(frame11, text='Vous n’avez un compte?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    #label.place(x=103 , y=465)

    #connecter= Button(frame11, width=6, text='S’inscrire',command=show_sign_up_window, border=0, bg='white', cursor='hand2', fg='#fea6be')
    #connecter.place(x=250, y=465)


def show_sign_up_window():
    window5 = tk.Toplevel(window)
    window5.title("SignUp")
    window5.geometry('1000x600')
    window5.configure(bg="#fff")
    window5.resizable(True, True)
    
    # Load and place image on the left side
    img5 = PhotoImage(file='test55.png')
    image_label = Label(window5, image=img5, bg='white')
    image_label.image = img5  # Store the image as an attribute of the label
    image_label.place(x=40, y=80)
    
    # Load and display the logo image
    logo_path11 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo100.png")  # Modify the path as per your logo image
    window5.logo_path11 = logo_path11  # Keep a reference to the image object
    logo_label11 = Label(window5, image=logo_path11, bg="#fff")
    logo_label11.place(relx=0.89, rely=0.82, anchor="nw")  # Adjust relx, rely, and anchor as needed


    # Create a frame next to the image for text labels
    form_frame = Frame(window5, width=500, height=560, bg='white')
    form_frame.place(x=350, y=20)

    heading5 = Label(form_frame, text='Bienvenue!', fg='#6497b1', bg='#fff', font=('Arial', 20, 'bold'))
    heading5.grid(row=0, column=1, columnspan=2, pady=(10, 20))

    heading55 = Label(form_frame, text='Créer un compte pour personnel', fg='#606060', bg='#fff', font=('Microsoft YaHei UI Light', 12))
    heading55.grid(row=1, column=1, columnspan=2, pady=(0, 20))

    # Matricule 
    mat_label = Label(form_frame, text="Matricule*", bg='white', font=('Arial', 12))
    mat_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    mat_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    mat_entry.grid(row=2, column=1, padx=10, pady=10)

    # First Name
    first_name_label = Label(form_frame, text="Nom*", bg='white', font=('Arial', 12))
    first_name_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    first_name_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    first_name_entry.grid(row=3, column=1, padx=10, pady=10)

    # Last Name
    last_name_label = Label(form_frame, text="Prénom*", bg='white', font=('Arial', 12))
    last_name_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    lastt_name_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    lastt_name_entry.grid(row=4, column=1, padx=10, pady=10)

    # Contact Number
    numero_label = Label(form_frame, text="Numéro de téléphone*", bg='white', font=('Arial', 12))
    numero_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    numero_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    numero_entry.grid(row=5, column=1, padx=10, pady=10)
    # Role
    role_label = Label(form_frame, text="Rôle*", bg='white', font=('Arial', 12))
    role_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    role_var = StringVar()
    role_combobox = Combobox(form_frame, textvariable=role_var, values=["Agent Hospitalier", "Médecin Spécialiste"], state="readonly", font=("Arial", 12))
    role_combobox.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    role_combobox.current(0)  # Set default selection
    # Email
    mail_label = Label(form_frame, text="Adresse E-mail*", bg='white', font=('Arial', 12))
    mail_label.grid(row=7, column=0, padx=10, pady=10, sticky='w')
    mail_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    mail_entry.grid(row=7, column=1, padx=10, pady=10)
    
    # Username
    usern_label = Label(form_frame, text="Nom d'utilisateur*", bg='white', font=('Arial', 12))
    usern_label.grid(row=8, column=0, padx=10, pady=10, sticky='w')
    usern_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    usern_entry.grid(row=8, column=1, padx=10, pady=10)

    # Password
    password_label = Label(form_frame, text="Mot de passe*", bg='white', font=('Arial', 12))
    password_label.grid(row=9, column=0, padx=10, pady=10, sticky='w')
    password_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12), show='*')
    password_entry.grid(row=9, column=1, padx=10, pady=10)

    # Create a style for the Combobox
    style = Style()
    style.map('TCombobox', 
          selectbackground=[('readonly', 'white')],
          selectforeground=[('readonly', 'black')])

    def close_and_show_admin():
        window5.destroy()
        open_admin_window()
 
    # Buttons
    ajout_button = Button(form_frame, text="Ajouter Personnel", bg='#6497b1', fg='white', font=('Arial', 12, 'bold'), border=0, width=20)
    ajout_button.grid(row=10, column=1, padx=20, pady=20)
    quitter= Button(form_frame, width=6, text='Quitter',command=close_and_show_admin, border=0, bg='white', cursor='hand2', fg='#6497b1')
    quitter.place(x=423, y=520)
    
 



def open_admin_window():
    windowA = tk.Toplevel(window)
    windowA.title("Gestion Personnels")
    windowA.geometry("498x280")
    
    # Load and display the logo image
    logo_path11 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo50.png")  # Modify the path as per your logo image
    windowA.logo_path11 = logo_path11  # Keep a reference to the image object
    logo_label11 = Label(windowA, image=logo_path11, bg='#f2baba')
    logo_label11.place(relx=0.01, rely=0.02, anchor="nw")  # Adjust relx, rely, and anchor as needed

    gif_frames = []
    frame_delay = 100  # Default frame delay

    frame_count = 0
    
    def load_gif():
        global frame_delay
        print('Loading GIF...')
        gif_file = Image.open('admin3.gif')

        try:
            while True:
                gif_frames.append(ImageTk.PhotoImage(gif_file.copy()))
                gif_file.seek(gif_file.tell() + 1)
        except EOFError:  # End of frames
            pass

        frame_delay = gif_file.info.get('duration', 100)
        print('GIF loaded.')

        play_gif()
        
    def play_gif():
        nonlocal frame_count
        gif_lb.config(image=gif_frames[frame_count])
        frame_count = (frame_count + 1) % len(gif_frames)
        windowA.after(frame_delay, play_gif)
        
    gif_lb = tk.Label(windowA)
    gif_lb.pack(fill=tk.BOTH, expand=True)  # Allow label to expand with window
    
    # Load GIF in a separate thread
    threading.Thread(target=load_gif).start()
    
    # Ensure the logo is above the GIF
    logo_label11.tkraise()

    # Welcome Frame
    welcome_frame = tk.Frame(windowA, bg='#fff4e4')
    welcome_frame.place(relx=0.5, rely=0.3, width=455, anchor=tk.CENTER)

    welcome_label = tk.Label(welcome_frame, text='Welcome back!', bg='#fff4e4', fg='#66545e', border=0, font=('Microsoft YaHei UI Light', 15, 'bold'))
    welcome_label.pack(pady=10)
    
    #Quote Frame
    #quote_frame = tk.Frame(windowA, bg='#f2baba')
    #quote_frame.place(relx=0.5, rely=0.55, width=455, anchor=tk.CENTER)
    #under_label = tk.Label(quote_frame, text='Bienvenue, Admin ! Vous êtes le pilier de la gestion du personnel', bg='#f2baba', fg='#66545e', border=0, font=('Microsoft YaHei UI Light', 10, 'bold'))
    #under_label.pack(pady=1)
    
    # Functions to close windowA and open other windows
    def close_and_show_sign_up():
        windowA.destroy()
        show_sign_up_window()

    def close_and_show_modify():
        windowA.destroy()
        show_modify_window()

    def close_and_show_delete():
        windowA.destroy()
        show_delete_window()
    
    
    # Frame to contain buttons
    button_frame = tk.Frame(windowA, bg='#f2baba')
    button_frame.place(relx=0.5, rely=0.8, width=466, anchor=tk.CENTER)

    # Buttons
    ajout_button = tk.Button(button_frame, text='Ajouter Personnel', bg='#fff4e4', fg='#66545e', border=1,
                             font=('Microsoft YaHei UI Light', 10, 'bold'), command=close_and_show_sign_up)
    modif_button = tk.Button(button_frame, text='Modifier Personnel', bg='#fff4e4', fg='#66545e', border=1,
                                 font=('Microsoft YaHei UI Light', 10, 'bold'), command=close_and_show_modify)
    supprime_button = tk.Button(button_frame, text='Supprimer Personnel', bg='#fff4e4', fg='#66545e', border=1,
                                 font=('Microsoft YaHei UI Light', 10, 'bold'), command=close_and_show_delete)

    # Use grid to organize buttons in the frame
    ajout_button.grid(row=0, column=0, padx=5, pady=10)
    modif_button.grid(row=0, column=1, padx=5, pady=10)
    supprime_button.grid(row=0, column=2, padx=5, pady=10)



def show_modify_window():
    window5 = tk.Toplevel(window)
    window5.title("Modify")
    window5.geometry('1000x600')
    window5.configure(bg="#fff")
    window5.resizable(True, True)
    
    # Load and place image on the left side
    img5 = PhotoImage(file='modifperr222.png')
    image_label = Label(window5, image=img5, bg='white')
    image_label.image = img5  # Store the image as an attribute of the label
    image_label.place(x=40, y=80)
    
    # Load and display the logo image
    logo_path11 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo100.png")  # Modify the path as per your logo image
    window5.logo_path11 = logo_path11  # Keep a reference to the image object
    logo_label11 = Label(window5, image=logo_path11, bg="#fff")
    logo_label11.place(relx=0.89, rely=0.82, anchor="nw")  # Adjust relx, rely, and anchor as needed


    # Create a frame next to the image for text labels
    form_frame = Frame(window5, width=500, height=560, bg='white')
    form_frame.place(x=350, y=20)

    heading5 = Label(form_frame, text='Bienvenue!', fg='#e23971', bg='#fff', font=('Arial', 20, 'bold'))
    heading5.grid(row=0, column=1, columnspan=2, pady=(10, 20))

    heading55 = Label(form_frame, text='Modifier les données d’un personnel', fg='#606060', bg='#fff', font=('Microsoft YaHei UI Light', 12))
    heading55.grid(row=1, column=1, columnspan=2, pady=(0, 20))

    # Matricule 
    mat_label = Label(form_frame, text="Matricule*", bg='white', font=('Arial', 12))
    mat_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    mat_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    mat_entry.grid(row=2, column=1, padx=10, pady=10)

    # First Name
    first_name_label = Label(form_frame, text="Nom*", bg='white', font=('Arial', 12))
    first_name_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    first_name_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    first_name_entry.grid(row=3, column=1, padx=10, pady=10)

    # Last Name
    last_name_label = Label(form_frame, text="Prénom*", bg='white', font=('Arial', 12))
    last_name_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    lastt_name_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    lastt_name_entry.grid(row=4, column=1, padx=10, pady=10)

    # Contact Number
    numero_label = Label(form_frame, text="Numéro de téléphone*", bg='white', font=('Arial', 12))
    numero_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    numero_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    numero_entry.grid(row=5, column=1, padx=10, pady=10)
    # Role
    role_label = Label(form_frame, text="Rôle*", bg='white', font=('Arial', 12))
    role_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    role_var = StringVar()
    role_combobox = Combobox(form_frame, textvariable=role_var, values=["Agent Hospitalier", "Médecin Spécialiste"], state="readonly", font=("Arial", 12))
    role_combobox.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    role_combobox.current(0)  # Set default selection
    # Email
    mail_label = Label(form_frame, text="Adresse E-mail*", bg='white', font=('Arial', 12))
    mail_label.grid(row=7, column=0, padx=10, pady=10, sticky='w')
    mail_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    mail_entry.grid(row=7, column=1, padx=10, pady=10)
    
    # Username
    usern_label = Label(form_frame, text="Nom d'utilisateur*", bg='white', font=('Arial', 12))
    usern_label.grid(row=8, column=0, padx=10, pady=10, sticky='w')
    usern_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    usern_entry.grid(row=8, column=1, padx=10, pady=10)

    # Password
    password_label = Label(form_frame, text="Mot de passe*", bg='white', font=('Arial', 12))
    password_label.grid(row=9, column=0, padx=10, pady=10, sticky='w')
    password_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12), show='*')
    password_entry.grid(row=9, column=1, padx=10, pady=10)

    # Create a style for the Combobox
    style = Style()
    style.map('TCombobox', 
          selectbackground=[('readonly', 'white')],
          selectforeground=[('readonly', 'black')])

    def closem_and_show_admin():
        window5.destroy()
        open_admin_window()
     
    # Buttons
    continue_button = Button(form_frame, text="Enregistrer Modification", bg='#e23971', fg='white', font=('Arial', 12, 'bold'), border=0, width=20)
    continue_button.grid(row=10, column=1, padx=20, pady=20)
    quitter= Button(form_frame, width=6, text='Quitter',command=closem_and_show_admin, border=0, bg='white', cursor='hand2', fg='#e23971')
    quitter.place(x=423, y=520)



def show_delete_window():
    window5 = tk.Toplevel(window)
    window5.title("Delete")
    window5.geometry('1000x600')
    window5.configure(bg="#fff")
    window5.resizable(True, True)
    
    # Load and place image on the left side
    img5 = PhotoImage(file='suppinter11 (1).png')
    image_label = Label(window5, image=img5, bg='white')
    image_label.image = img5  # Store the image as an attribute of the label
    image_label.place(x=40, y=80)
    
    # Load and display the logo image
    logo_path11 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo100.png")  # Modify the path as per your logo image
    window5.logo_path11 = logo_path11  # Keep a reference to the image object
    logo_label11 = Label(window5, image=logo_path11, bg="#fff")
    logo_label11.place(relx=0.89, rely=0.82, anchor="nw")  # Adjust relx, rely, and anchor as needed


    # Create a frame next to the image for text labels
    form_frame = Frame(window5, width=500, height=560, bg='white')
    form_frame.place(x=350, y=20)

    heading5 = Label(form_frame, text='Bienvenue!', fg='#ff749e', bg='#fff', font=('Arial', 20, 'bold'))
    heading5.grid(row=0, column=1, columnspan=2, pady=(10, 20))

    heading55 = Label(form_frame, text='Supprimer un personnel', fg='#606060', bg='#fff', font=('Microsoft YaHei UI Light', 12))
    heading55.grid(row=1, column=1, columnspan=2, pady=(0, 20))

    # Matricule 
    mat_label = Label(form_frame, text="Matricule*", bg='white', font=('Arial', 12))
    mat_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    mat_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    mat_entry.grid(row=2, column=1, padx=10, pady=10)

    # First Name
    first_name_label = Label(form_frame, text="Nom*", bg='white', font=('Arial', 12))
    first_name_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    first_name_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    first_name_entry.grid(row=3, column=1, padx=10, pady=10)

    # Last Name
    last_name_label = Label(form_frame, text="Prénom*", bg='white', font=('Arial', 12))
    last_name_label.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    lastt_name_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    lastt_name_entry.grid(row=4, column=1, padx=10, pady=10)

    # Contact Number
    numero_label = Label(form_frame, text="Numéro de téléphone*", bg='white', font=('Arial', 12))
    numero_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    numero_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    numero_entry.grid(row=5, column=1, padx=10, pady=10)
    # Role
    role_label = Label(form_frame, text="Rôle*", bg='white', font=('Arial', 12))
    role_label.grid(row=6, column=0, padx=10, pady=10, sticky='w')

    role_var = StringVar()
    role_combobox = Combobox(form_frame, textvariable=role_var, values=["Agent Hospitalier", "Médecin Spécialiste"], state="readonly", font=("Arial", 12))
    role_combobox.grid(row=6, column=1, padx=10, pady=10, sticky='w')
    role_combobox.current(0)  # Set default selection
    # Email
    mail_label = Label(form_frame, text="Adresse E-mail*", bg='white', font=('Arial', 12))
    mail_label.grid(row=7, column=0, padx=10, pady=10, sticky='w')
    mail_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    mail_entry.grid(row=7, column=1, padx=10, pady=10)
    
    # Username
    usern_label = Label(form_frame, text="Nom d'utilisateur*", bg='white', font=('Arial', 12))
    usern_label.grid(row=8, column=0, padx=10, pady=10, sticky='w')
    usern_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12))
    usern_entry.grid(row=8, column=1, padx=10, pady=10)

    # Password
    password_label = Label(form_frame, text="Mot de passe*", bg='white', font=('Arial', 12))
    password_label.grid(row=9, column=0, padx=10, pady=10, sticky='w')
    password_entry = Entry(form_frame, width=30, fg='#777777', border=1, bg='#f0f0f0', font=("Arial", 12), show='*')
    password_entry.grid(row=9, column=1, padx=10, pady=10)

    # Create a style for the Combobox
    style = Style()
    style.map('TCombobox', 
          selectbackground=[('readonly', 'white')],
          selectforeground=[('readonly', 'black')])
    
    def closed_and_show_admin(): 
        window5.destroy()
        open_admin_window()

 
    # Buttons
    continue_button = Button(form_frame, text="Supprimer Personnel", bg='#ff749e', fg='white', font=('Arial', 12, 'bold'), border=0, width=20)
    continue_button.grid(row=10, column=1, padx=20, pady=20)
    quitter= Button(form_frame, width=6, text='Quitter',command=closed_and_show_admin, border=0, bg='white', cursor='hand2', fg='#ff749e')
    quitter.place(x=423, y=520)


def open_ajoutp_window():
    # Fenêtre spécifique pour l'Agent
     ajoutp_window = tk.Toplevel(window)
     ajoutp_window.title("Ajouter Personnel")
     ajoutp_window.geometry("500x500")
     
     def validate_matricule():
         matricule = matriculep_var.get()
         if not matricule.isdigit() or len(matricule) != 8:
             invalid_label_matricule.config(text="Le matricule doit être composé de 8 chiffres.", fg="red")
         else:
             invalid_label_matricule.config(text="")
             
             
     def validate_nom():
         nom = nomp_var.get()
         if not nom.isalpha():
             invalid_label_nom.config(text="Le nom doit contenir uniquement des caractères alphabétiques.", fg="red")
         else:
             invalid_label_nom.config(text="")
             
     # Fonction pour valider le prénom
     def validate_prenom():
         prenom = prenomp_var.get()
         if not prenom.isalpha():
             invalid_label_prenom.config(text="Le prénom doit contenir uniquement des caractères alphabétiques.", fg="red")
         else:
             invalid_label_prenom.config(text="")
             
     def validate_num():
         num = numtelp_var.get()
         if not num.isdigit() or len(num) != 8: 
             invalid_label_num.config(text="Le Numéro de Téléphone est invalide.", fg="red")
         else:
             invalid_label_num.config(text="") 
             
     def validate_email():
         email = adrp_var.get()
         email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
         if not re.match(email_pattern, email):
             invalid_label_adrp.config(text="L'adresse e-mail est invalide.", fg="red")
         else:
             invalid_label_adrp.config(text="")
          
     def validate_password():
         password = password_var.get()
         min_length = 8
    
         # Check password length
         if len(password) < min_length:
            invalid_label_pass.config(text="Le mot de passe doit contenir au moins 8 caractères.", fg="red")
            return

         # Check for uppercase letter, lowercase letter, digit, and special character
         if not re.search(r"[A-Z]", password):
           invalid_label_pass.config(text="Le mot de passe doit contenir au moins une lettre majuscule.", fg="red")
           return

         if not re.search(r"[a-z]", password):
           invalid_label_pass.config(text="Le mot de passe doit contenir au moins une lettre minuscule.", fg="red")
           return

         if not re.search(r"\d", password):
           invalid_label_pass.config(text="Le mot de passe doit contenir au moins un chiffre.", fg="red")
           return

         if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
           invalid_label_pass.config(text="Le mot de passe doit contenir au moins un caractère spécial.", fg="red")
           return

         # If all checks pass
         invalid_label_pass.config(text="")
         
     def validate_username():
         username = username_var.get()
         username_pattern = r"^[a-zA-Z]+$"
    
         if not re.match(username_pattern, username):
           invalid_label_user.config(text="Le nom d'utilisateur ne doit contenir que des lettres majuscules et minuscules.", fg="red")
         else:
           invalid_label_user.config(text="")
           
     def validate_empty_fields():
         if not all((nomp_var.get(), prenomp_var.get(), matriculep_var.get(), adrp_var.get(), numtelp_var.get(), username_var.get(), password_var.get(), rolep_var.get())):
             messagebox.showerror("Error", "Tous les champs de texte doivent être remplis.")
             return False
         elif not matriculep_var.get().isdigit() or len(matriculep_var.get()) != 8:
             messagebox.showerror("Error", "Le matricule doit être composé de 8 chiffres.")
             return False
         elif not nomp_var.get().isalpha():
             messagebox.showerror("Error", "Le nom doit contenir uniquement des caractères alphabétiques.")
             return False
         elif not prenomp_var.get().isalpha():
             messagebox.showerror("Error", "Le prénom doit contenir uniquement des caractères alphabétiques.")
             return False
         elif not numtelp_var.get().isdigit() or len(numtelp_var.get()) !=8:
            messagebox.showerror("Erreur", "Le Numéro de Téléphone est invalide.")
            return False
         return True
     
    # Variables
     nomp_var = StringVar()
     prenomp_var = StringVar()
     matriculep_var = StringVar()
     adrp_var = StringVar()
     numtelp_var= StringVar()
     username_var = StringVar()
     password_var = StringVar()
     rolep_var = StringVar()
     r1_var = StringVar()
     r2_var = StringVar()
     
     
    # Coordonnées Cliniques
     frame_coord_p = LabelFrame(ajoutp_window, text="Coordonnées Cliniques", padx=10, pady=10)
     frame_coord_p.pack(fill="x", padx=20, pady=100)
     
     Label(frame_coord_p, text="Matricule").grid(row=0, column=0, sticky="w")
     matentry = Entry(frame_coord_p, textvariable=matriculep_var)
     matentry.grid(row=0, column=1, sticky="ew", padx=5)
     invalid_label_matricule = Label(frame_coord_p, text="", fg="red")
     invalid_label_matricule.grid(row=0, column=2)

     Label(frame_coord_p, text="Nom").grid(row=2, column=0, sticky="w")
     name_entry=Entry(frame_coord_p, textvariable=nomp_var)
     name_entry.grid(row=2, column=1, sticky="ew", padx=5)
     invalid_label_nom = Label(frame_coord_p, text="", fg="red")
     invalid_label_nom.grid(row=2, column=2)
     
     Label(frame_coord_p, text="Prénom").grid(row=4, column=0, sticky="w")
     last_name_entry=Entry(frame_coord_p, textvariable=prenomp_var)
     last_name_entry.grid(row=4, column=1, sticky="ew", padx=5)
     invalid_label_prenom = Label(frame_coord_p, text="", fg="red")
     invalid_label_prenom.grid(row=4, column=2)     
     
     Label(frame_coord_p, text="Adresse E-mail").grid(row=6, column=0, sticky="w")
     adrp_entry=Entry(frame_coord_p, textvariable=adrp_var)
     adrp_entry.grid(row=6, column=1, sticky="ew", padx=5)
     invalid_label_adrp = Label(frame_coord_p, text="", fg="red")
     invalid_label_adrp.grid(row=6, column=2)
     
     Label(frame_coord_p, text="Numéro De Téléphone").grid(row=8, column=0, sticky="w")
     num_entry=Entry(frame_coord_p, textvariable=numtelp_var)
     num_entry.grid(row=8, column=1, sticky="ew", padx=5)
     invalid_label_num = Label(frame_coord_p, text="", fg="red")
     invalid_label_num.grid(row=8, column=2)
     
     Label(frame_coord_p, text="Nom d'utilisateur").grid(row=10, column=0, sticky="w")
     user_entry=Entry(frame_coord_p, textvariable=username_var)
     user_entry.grid(row=10, column=1, sticky="ew", padx=5)
     invalid_label_user = Label(frame_coord_p, text="", fg="red")
     invalid_label_user.grid(row=10, column=2)
     
     Label(frame_coord_p, text="Mot De Passe").grid(row=12, column=0, sticky="w")
     pass_entry=Entry(frame_coord_p, textvariable=password_var)
     pass_entry.grid(row=12, column=1, sticky="ew", padx=5)
     invalid_label_pass = Label(frame_coord_p, text="", fg="red")
     invalid_label_pass.grid(row=12, column=2)
     
     Label(frame_coord_p, text="Rôle").grid(row=14, column=0, sticky="w")
     r1_var.set(None)
     r1= tk.Radiobutton(frame_coord_p, text="Agent Hospitalier", variable= r1_var, value='Agent Hospitalier').grid(row=14, column=1, sticky="w")
     r2_var.set(None)
     r2= tk.Radiobutton(frame_coord_p, text="Médecin Spécialiste", variable= r2_var, value='Médecin Spécialiste').grid(row=14, column=2, sticky="w")
     
     
     
     
     # Bind validation functions to the KeyRelease event of entry widgets
     matentry.bind("<KeyRelease>", lambda event: validate_matricule())
     name_entry.bind("<KeyRelease>", lambda event: validate_nom())
     last_name_entry.bind("<KeyRelease>", lambda event: validate_prenom())
     adrp_entry.bind("<KeyRelease>", lambda event: validate_email())
     num_entry.bind("<KeyRelease>", lambda event: validate_num())
     pass_entry.bind("<KeyRelease>", lambda event: validate_password())
     
  # Bouton pour sélectionner la lettre scannée
     Button(ajoutp_window, text="Ajouter Personnel").pack(pady=10)

     
             
     





    

def open_agent_window():
    # Fenêtre spécifique pour l'Agent
     agent_window = tk.Toplevel(window)
     agent_window.title("Espace Agent")
     agent_window.geometry("800x800")
     
     # Load and display the logo image
     logo_path11 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo100.png")  # Modify the path as per your logo image
     agent_window.logo_path11 = logo_path11  # Keep a reference to the image object
     logo_label11 = Label(agent_window, image=logo_path11)
     logo_label11.place(relx=0.92, rely=0.85, anchor="nw")  # Adjust relx, rely, and anchor as needed

     
     def validate_matricule():
         matricule = matricule_var.get()
         if not matricule.isdigit() or len(matricule) != 8:
             invalid_label_matricule.config(text="Le matricule doit être composé de 8 chiffres.", fg="red")
         else:
             invalid_label_matricule.config(text="")
            
             
     def validate_age():
         age_dep = imc_var.get()
         if not age_dep.isdigit():
             invalid_label_matricule.config(text="L'âge doit être composé de chiffres.", fg="red")
         else:
             invalid_label_matricule.config(text="")
             
             
     def validate_imc():
         imc = imc_var.get()
         try:
           float_imc = float(imc)
           if float_imc <= 0:  # Check if the value is non-negative
             messagebox.showerror("Error", "L'IMC doit être un nombre positif.")
             return False
         except ValueError:
           messagebox.showerror("Error", "L'IMC doit être un nombre décimal.")
           return False
         return True

                 
    # Implémentez ici la logique spécifique à l'Agent
    # Répertoire pour stocker les lettres scannées et le fichier CSV
     chemin_bureau = os.path.join(os.path.expanduser('~'), 'Desktop')
     dossier_images = os.path.join(chemin_bureau, 'LettresScannees')
     fichier_csv = os.path.join(chemin_bureau, 'PRIO_MAMMO1.csv')

     if not os.path.exists(dossier_images):
      os.makedirs(dossier_images)

     if not os.path.isfile(fichier_csv):
      with open(fichier_csv, 'w', newline='', encoding='utf-8') as file:
           writer = csv.writer(file)
           writer.writerow(['Nom', 'Prénom', 'Matricule', 'Age', 'Numéro De Téléphone', 'L’indice de masse corporelle', 'Traitement Hormonal Contraceptif', 'ATCD P cancer du sein', 'Nodule',
                         'La Puberté Précoce / Menarche Tardive', 'ATCD P cancer de l’ovaire ou de l’endomètre', 'ATCD F cancer du sein ou de l’ovaire', 'Mutation du Gène BRCA1 ou BRCA2',
                         'Aspect peau d’orange', 'Écoulement mamelonnaire sanguinolent', 'Présence d’adénopathie', 'Lettre Scannée', 'Priorité', 'Rendez-vous'])

    # Fonction pour calculer la priorité et le prochain rendez-vous disponible
     def calculer_priorite_et_rdv():
    # Simplification du calcul de priorité
      priorite = 0
      if pubme_var.get() == 1:
        priorite += 2
      if atcdpoe_var.get() == 1:
        priorite += 3
      # Ajoutez d'autres conditions de priorité ici selon les variables cliniques

      # Calcul simplifié du prochain rendez-vous (exemple : le lendemain à 9h)
      prochain_rdv = (datetime.now() + timedelta(days=1)).replace(hour=9, minute=0)
      return priorite, prochain_rdv.strftime('%Y-%m-%d %H:%M')

    # Fonction pour sélectionner une lettre scannée
     def selectionner_lettre():
      fichier = filedialog.askopenfilename(initialdir=chemin_bureau, title="Sélectionner la lettre scannée",
                                         filetypes=[("Fichiers images", ".jpg;.jpeg;*.png"), ("Tous les fichiers", ".")])
      lettre_var.set(fichier)
      
      
      
      
     def validate_empty_fields():
         numtel= numtel_var
         if not all((nom_var.get(), prenom_var.get(), matricule_var.get(), age_var.get(), numtel_var.get(), imc_var.get(), thc_var.get(), atcdps_var.get(), nodule_var.get())):
             messagebox.showerror("Error", "Tous les champs de texte doivent être remplis.")
             return False
         elif not matricule_var.get().isdigit() or len(matricule_var.get()) != 8:
             messagebox.showerror("Error", "Le matricule doit être composé de 8 chiffres.")
             return False
         elif not nom_var.get().isalpha():
             messagebox.showerror("Error", "Le nom doit contenir uniquement des caractères alphabétiques.")
             return False
         elif not prenom_var.get().isalpha():
             messagebox.showerror("Error", "Le prénom doit contenir uniquement des caractères alphabétiques.")
             return False
         elif not age_var.get().isdigit():
             messagebox.showerror("Error", "L'âge ne doit contenir que des caractères numériques.")
             return False
         elif not numtel_var.get().isdigit() or len(numtel_var.get()) !=8:
            messagebox.showerror("Erreur", "Le Numéro de Téléphone est invalide.")
            return False
         elif not validate_imc():
             messagebox.showerror("Error", "L'indice de masse corporelle doit être numérique.")
             return False
         
         return True

    # Fonction pour enregistrer les données et calculer la priorité
     def enregistrer_donnees():
         if not validate_empty_fields():
             return
         matricule = matricule_var.get()
         if not matricule.isdigit() or len(matricule) != 8:
             messagebox.showerror("Error", "Le matricule doit être composé de 8 chiffres.")
             return
         
         priorite, rdv = calculer_priorite_et_rdv()
         with open(fichier_csv, 'a', newline='', encoding='utf-8') as file:
          writer = csv.writer(file)
          writer.writerow([nom_var.get(), prenom_var.get(), matricule_var.get(), age_var.get(), numtel_var.get(),
                         imc_var.get(), thc_var.get(), atcdps_var.get(), nodule_var.get(), pubme_var.get(), atcdpoe_var.get(),
                         atcdf_var.get(), brca_var.get(), peau_var.get(), ecoulement_var.get(), pathie_var.get(),  lettre_var.get(), priorite, rdv])
         messagebox.showinfo("Succès", f"Les informations ont été enregistrées avec succès. Priorité: {priorite}, Rendez-vous: {rdv}")
         agent_window.destroy() 
         
         
     def validate_nom():
         nom = nom_var.get()
         if not nom.isalpha():
             invalid_label_nom.config(text="Le nom doit contenir uniquement des caractères alphabétiques.", fg="red")
         else:
             invalid_label_nom.config(text="")    
             
     # Fonction pour valider le prénom
     def validate_prenom():
         prenom = prenom_var.get()
         if not prenom.isalpha():
             invalid_label_prenom.config(text="Le prénom doit contenir uniquement des caractères alphabétiques.", fg="red")
         else:
             invalid_label_prenom.config(text="")
             
             
     def validate_age():
         age = age_var.get()
         if not age.isdigit():
             invalid_label_age.config(text="L'âge ne doit contenir que des caractères numériques.", fg="red")
         else:
             invalid_label_age.config(text="")
             
     def validate_num():
         num = numtel_var.get()
         if not num.isdigit() or len(num) != 8: 
             invalid_label_num.config(text="Le Numéro de Téléphone est invalide.", fg="red")
         else:
             invalid_label_num.config(text="") 
     
     # Variables
     nom_var = StringVar()
     prenom_var = StringVar()
     matricule_var = StringVar()
     age_var = StringVar()
     numtel_var= StringVar()
     imc_var = StringVar()
     pubme_var = IntVar()
     atcdpoe_var = IntVar()
     thc_var = StringVar()
     atcdps_var = StringVar()
     atcdf_var = IntVar()
     brca_var = IntVar()
     peau_var = IntVar()
     lettre_var = StringVar()
     nodule_var= ttk.StringVar()
     ecoulement_var= IntVar()
     pathie_var= IntVar()

    # Coordonnées Cliniques
     frame_coord_cliniques = LabelFrame(agent_window, text="Coordonnées Cliniques", padx=10, pady=10)
     frame_coord_cliniques.pack(fill="x", padx=20, pady=10)
     
     Label(frame_coord_cliniques, text="Matricule").grid(row=0, column=0, sticky="w")
     matentry = Entry(frame_coord_cliniques, textvariable=matricule_var)
     matentry.grid(row=0, column=1, sticky="ew", padx=5)
     invalid_label_matricule = Label(frame_coord_cliniques, text="", fg="red")
     invalid_label_matricule.grid(row=0, column=2)

     Label(frame_coord_cliniques, text="Nom").grid(row=1, column=0, sticky="w")
     name_entry=Entry(frame_coord_cliniques, textvariable=nom_var)
     name_entry.grid(row=1, column=1, sticky="ew", padx=5)
     invalid_label_nom = Label(frame_coord_cliniques, text="", fg="red")
     invalid_label_nom.grid(row=1, column=2)
     
     Label(frame_coord_cliniques, text="Prénom").grid(row=2, column=0, sticky="w")
     last_name_entry=Entry(frame_coord_cliniques, textvariable=prenom_var)
     last_name_entry.grid(row=2, column=1, sticky="ew", padx=5)
     invalid_label_prenom = Label(frame_coord_cliniques, text="", fg="red")
     invalid_label_prenom.grid(row=2, column=2)     
     
     Label(frame_coord_cliniques, text="Age").grid(row=3, column=0, sticky="w")
     age_entry=Entry(frame_coord_cliniques, textvariable=age_var)
     age_entry.grid(row=3, column=1, sticky="ew", padx=5)
     invalid_label_age = Label(frame_coord_cliniques, text="", fg="red")
     invalid_label_age.grid(row=3, column=2)
     
     Label(frame_coord_cliniques, text="Numéro De Téléphone").grid(row=4, column=0, sticky="w")
     num_entry=Entry(frame_coord_cliniques, textvariable=numtel_var)
     num_entry.grid(row=4, column=1, sticky="ew", padx=5)
     #num_entry.insert(tk.END, "+216")  # Prepopulate the entry with the country code
     #num_entry1.config(state=tk.DISABLED)  # Make the entry non-editable
     invalid_label_num = Label(frame_coord_cliniques, text="", fg="red")
     invalid_label_num.grid(row=4, column=2)
     
     # Bind validation functions to the KeyRelease event of entry widgets
     matentry.bind("<KeyRelease>", lambda event: validate_matricule())
     name_entry.bind("<KeyRelease>", lambda event: validate_nom())
     last_name_entry.bind("<KeyRelease>", lambda event: validate_prenom())
     age_entry.bind("<KeyRelease>", lambda event: validate_age())
     num_entry.bind("<KeyRelease>", lambda event: validate_num())


    # Variables Cliniques
     frame_vars_cliniques = LabelFrame(agent_window, text="Variables Cliniques", padx=10, pady=10)
     frame_vars_cliniques.pack(fill="x", padx=20, pady=20)
     
     Label(frame_vars_cliniques, text="L’indice de masse corporelle").grid(row=0, column=0, sticky="w")
     Entry(frame_vars_cliniques, textvariable=imc_var).grid(row=0, column=1, sticky="ew", padx=5)
     
     Label(frame_vars_cliniques, text="Traitement Hormonal Contraceptif").grid(row=1, column=0, sticky="w")
     Entry(frame_vars_cliniques, textvariable=thc_var).grid(row=1, column=1, sticky="ew", padx=5)
     
     Label(frame_vars_cliniques, text="ATCD P cancer du sein").grid(row=2, column=0, sticky="w")
     Entry(frame_vars_cliniques, textvariable=atcdps_var).grid(row=2, column=1, sticky="ew", padx=5)
     
     Label(frame_vars_cliniques, text="Nodule").grid(row=3, column=0, sticky="w")
     #Entry(frame_vars_cliniques, textvariable=nodule_var).grid(row=3, column=1, sticky="ew", padx=5)
     
     Nodule= ["1cm", "2cm", "3cm", "4cm", "5cm", "+5cm"]
     nodule_var.set(Nodule[0])
     drop= OptionMenu(frame_vars_cliniques, nodule_var, *Nodule)
     drop.grid(row=3, column=1, sticky="ew", padx=5, pady=18)


    
     Label(frame_vars_cliniques, text="La Puberté Précoce / Menarche Tardive").grid(row=4, column=0, sticky="w")
     Checkbutton(frame_vars_cliniques, variable=pubme_var).grid(row=4, column=1, sticky="w", padx=5)
     
     Label(frame_vars_cliniques, text="ATCD P cancer de l’ovaire ou de l’endomètre").grid(row=5, column=0, sticky="w")
     Checkbutton(frame_vars_cliniques, variable=atcdpoe_var).grid(row=5, column=1, sticky="w", padx=5)
     
     Label(frame_vars_cliniques, text="ATCD F cancer du sein ou de l’ovaire").grid(row=6, column=0, sticky="w")
     Checkbutton(frame_vars_cliniques, variable=atcdf_var).grid(row=6, column=1, sticky="w", padx=5)
     
     Label(frame_vars_cliniques, text="Mutation du Gène BRCA1 ou BRCA2").grid(row=7, column=0, sticky="w")
     Checkbutton(frame_vars_cliniques, variable=brca_var).grid(row=7, column=1, sticky="w", padx=5)
     
     Label(frame_vars_cliniques, text="Aspect peau d’orange").grid(row=8, column=0, sticky="w")
     Checkbutton(frame_vars_cliniques, variable=peau_var).grid(row=8, column=1, sticky="w", padx=5)
     
     Label(frame_vars_cliniques, text="Écoulement mamelonnaire sanguinolent").grid(row=9, column=0, sticky="w")
     Checkbutton(frame_vars_cliniques, variable=ecoulement_var).grid(row=9, column=1, sticky="w", padx=5)
     
     Label(frame_vars_cliniques, text="Présence d’adénopathie").grid(row=10, column=0, sticky="w")
     Checkbutton(frame_vars_cliniques, variable=pathie_var).grid(row=10, column=1, sticky="w", padx=5)
     



     # Ajout des widgets dans les cadres pour les variables cliniques
     #entries = [('Âge au premier dépistage', age_premier_depi_var), 
      #     ('Antécédents familiaux de cancer', antecedents_familiaux_var), 
      #     ('Présence de symptômes', symptomes_var), 
       #    ('Résultats préliminaires d’examen', resultats_prelim_var), 
        #   ('Densité mammaire', densite_mammaire_var), 
         #  ('Historique de biopsies mammaires', historique_biopsies_var), 
          # ('Mutations génétiques connues', mutations_genetiques_var), 
           #('Exposition antérieure à la radiothérapie', radiotherapie_var)]

  #   for i, (label, var) in enumerate(entries, start=0):
   #    Label(frame_vars_cliniques, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=2)
    #   if isinstance(var, IntVar):
     #   Checkbutton(frame_vars_cliniques, variable=var).grid(row=i, column=1, sticky="w", padx=5, pady=2)
      # else:
       #  Entry(frame_vars_cliniques, textvariable=var).grid(row=i, column=1, sticky="ew", padx=5, pady=2)

    # Bouton pour sélectionner la lettre scannée
     Button(agent_window, text="Parcourir pour sélectionner la lettre scannée", command=selectionner_lettre).pack(pady=10)

    # Frame to contain the buttons side by side
     button_frame = Frame(agent_window)
     button_frame.pack(pady=20)

     # Buttons arranged horizontally in the frame
     Button(button_frame, text="Ajouter Patient", command=enregistrer_donnees).pack(side='left', padx=10)
     Button(button_frame, text="Enregistrer les modifications").pack(side='left', padx=10)
     Button(button_frame, text="Supprimer Patient").pack(side='left', padx=10)


     
     def close_agent_open_login():
         agent_window.destroy()
         show_login_window()
         
     Button(agent_window, text="Quitter", command=close_agent_open_login).pack(pady=30)





def open_SMS_window():
    window2 = tk.Toplevel(window)
    window2.title("Envoie d'SMS")
    
    # Load and display the logo image
    logo_path11 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo50.png")  # Modify the path as per your logo image
    window2.logo_path11 = logo_path11  # Keep a reference to the image object
    logo_label11 = Label(window2, image=logo_path11, bg='#f9cee7')
    logo_label11.place(relx=0.88, rely=0.64, anchor="nw")  # Adjust relx, rely, and anchor as needed

    gif_frames = []
    frame_delay = 100  # Default frame delay

    def load_gif():
        print('Loading GIF...')
        gif_file = Image.open('gifcrop.gif')

        try:
            while True:
                gif_frames.append(ImageTk.PhotoImage(gif_file.copy()))
                gif_file.seek(gif_file.tell() + 1)
        except EOFError:  # End of frames
            pass

        frame_delay = gif_file.info.get('duration', 100)
        print('GIF loaded.')

        play_gif()

    frame_count = 0

    def play_gif():
        nonlocal frame_count

        gif_lb.config(image=gif_frames[frame_count])
        frame_count = (frame_count + 1) % len(gif_frames)
        window2.after(frame_delay, play_gif)

    gif_lb = tk.Label(window2, text='Hello')
    gif_lb.pack(fill=tk.BOTH, expand=True)  # Allow label to expand with window

    load_gif()
    # Ensure the logo is above the GIF
    logo_label11.tkraise()

    def close_sms_open_doc():
        window2.destroy()
        open_doctor_window()
      


    # SMS Buttons
    sms_cible_button = tk.Button(window2, text='SMS Ciblé', command=close_sms_open_doc, bg='#ff76b7', fg='#fff', border=0,
                                 font=('Microsoft YaHei UI Light', 10, 'bold'))
    sms_cible_button.pack(side=tk.LEFT, padx=(10, 5), pady=10, fill=tk.X, expand=True)

    sms_collectif_button = tk.Button(window2, text='SMS collectif', bg='#ff76b7', fg='#fff', border=0,
                                     font=('Microsoft YaHei UI Light', 10, 'bold'))
    sms_collectif_button.pack(side=tk.RIGHT, padx=(5, 10), pady=10, fill=tk.X, expand=True)




    threading.Thread(target=load_gif).start()
    

def afficher_tableau():
    df = pd.read_csv(r'C:\Users\Arij\Desktop\PRIO_MAMMO.csv')
    
    # Créer une nouvelle fenêtre pour afficher les données
    data_window = tk.Toplevel()
    data_window.title("Données du fichier CSV")

    # Créer un cadre pour la zone de tableau avec barres de défilement
    data_frame = ttk.Frame(data_window)
    data_frame.pack()
    
    # Créer un tableau pour afficher les données avec barres de défilement
    tree = ttk.Treeview(data_frame)
    tree["columns"] = list(df.columns)
    
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, stretch=True)

    hsb = ttk.Scrollbar(data_frame, orient="horizontal", command=tree.xview)
    hsb.pack(side='bottom', fill='x')
    vsb = ttk.Scrollbar(data_frame, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

    for index, row in df.iterrows():
        tree.insert("", 'end', values=list(row))

    tree.pack(expand=True, fill='both')
    




def open_doctor_window():
    # Fenêtre spécifique pour le Médecin
    doctor_window = tk.Toplevel(window)
    doctor_window.title("Espace Médecin")
    doctor_window.geometry("800x800") 
    
    # Load and display the logo image
    logo_path11 = PhotoImage(file=r"C:\Users\Arij\Documents\desktop vs\LOGOPrioMammo100.png")  # Modify the path as per your logo image
    doctor_window.logo_path11 = logo_path11  # Keep a reference to the image object
    logo_label11 = Label(doctor_window, image=logo_path11)
    logo_label11.place(relx=0.92, rely=0.85, anchor="nw")  # Adjust relx, rely, and anchor as needed

    # Implémentez ici la logique spécifique au Médecin
    # Répertoire pour stocker les lettres scannées et le fichier CSV
    chemin_bureau = os.path.join(os.path.expanduser('~'), 'Desktop')
    dossier_images = os.path.join(chemin_bureau, 'LettresScannees')
    fichier_csv = os.path.join(chemin_bureau, 'PRIO_MAMMO1.csv')

    if not os.path.exists(dossier_images):
        os.makedirs(dossier_images)

    if not os.path.isfile(fichier_csv):
        with open(fichier_csv, 'w', newline='', encoding='utf-8') as file:
          writer = csv.writer(file)
          writer.writerow(['Nom', 'Prénom', 'Matricule', 'Age', 'Numéro De Téléphone', 'L’indice de masse corporelle', 'Traitement Hormonal Contraceptif', 'ATCD P cancer du sein', 'Nodule',
                         'La Puberté Précoce / Menarche Tardive', 'ATCD P cancer de l’ovaire ou de l’endomètre', 'ATCD F cancer du sein ou de l’ovaire', 'Mutation du Gène BRCA1 ou BRCA2',
                         'Aspect peau d’orange', 'Écoulement mamelonnaire sanguinolent', 'Présence d’adénopathie', 'Lettre Scannée', 'Date', 'Priorité', 'Rendez-vous'])

    # Fonction pour calculer la priorité et le prochain rendez-vous disponible
    def calculer_priorite_et_rdv():
    # Simplification du calcul de priorité
        priorite = 0
        if pubme1_var.get() == 1:
           priorite += 2
        if atcdpoe1_var.get() == 1:
           priorite += 3
        # Ajoutez d'autres conditions de priorité ici selon les variables cliniques

        # Calcul simplifié du prochain rendez-vous (exemple : le lendemain à 9h)
        prochain_rdv = (datetime.now() + timedelta(days=1)).replace(hour=9, minute=0)
        return priorite, prochain_rdv.strftime('%Y-%m-%d %H:%M')


    # Fonction pour rechercher les informations du patient par matricule
    def rechercher_patient(event=None):
        matricule = matricule1_var.get()
        if not matricule:
            messagebox.showerror("Erreur", "Veuillez saisir le matricule pour rechercher le patient.")
            return
        
        patient_found = False
        with open(fichier_csv, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
               if row['Matricule'] != matricule:
                   continue
               # Affichage des informations du patient correspondant
               nom1_var.set(row['Nom'])
               prenom1_var.set(row['Prénom'])
               age1_var.set(row['Age'])
               numtel_var1.set(row['Numéro De Téléphone'])
               imc1_var.set(row['L’indice de masse corporelle'])
               thc1_var.set(row['Traitement Hormonal Contraceptif'])
               atcdps1_var.set(row['ATCD P cancer du sein'])
               nodule1_var.set(str(row['Nodule']))
               pubme1_var.set(str(row['La Puberté Précoce / Menarche Tardive']))
               atcdpoe1_var.set(str(row['ATCD P cancer de l’ovaire ou de l’endomètre']))
               atcdf1_var.set(str(row['ATCD F cancer du sein ou de l’ovaire']))
               brca1_var.set(str(row['Mutation du Gène BRCA1 ou BRCA2']))
               peau1_var.set(str(row['Aspect peau d’orange']))
               ecoulement1_var.set(str(row['Écoulement mamelonnaire sanguinolent']))
               pathie1_var.set(str(row['Présence d’adénopathie']))
               lettre1_var.set(row['Lettre Scannée'])
               appointment_date = row['Rendez-vous']  # Retrieve the appointment date from the CSV
               print("Retrieved Appointment Date:", appointment_date)  # Print the retrieved appointment date for debugging
               date_entry1.delete(0, 'end')  # Clear any previous entry
               date_entry1.insert(0, appointment_date)  # Set the retrieved appointment date in the entry field
               patient_found = True
               break
            # Si aucun patient correspondant n'est trouvé
            if not patient_found:
             messagebox.showinfo("Information", "Aucun patient trouvé avec ce matricule.")


    def imprimer_lettre():
        lettre = lettre1_var.get()
        if lettre:
        # Logique d'impression de la lettre ici
           messagebox.showinfo("Succès", "La lettre a été imprimée avec succès.")
        else:
           messagebox.showerror("Erreur", "Veuillez sélectionner une lettre à imprimer.")
           
           
    def validate_imc():
         imc1 = imc1_var.get()
         try:
           float_imc1 = float(imc1)
           if float_imc1 <= 0:  # Check if the value is non-negative
             messagebox.showerror("Error", "L'IMC doit être un nombre positif.")
             return False
         except ValueError:
           messagebox.showerror("Error", "L'IMC doit être un nombre décimal.")
           return False
         return True
           
           
    def send_sms():
    # Chemin vers le fichier CSV contenant les données des patients
     fichier_csv = os.path.join(os.path.expanduser('~'), 'Desktop', 'PRIO_MAMMO1.csv')
     try:
        with open(fichier_csv, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Préparation des données pour l'envoi du SMS
                payload = {
                    'type': '55',
                    'sender': 'TunSMS',  # Remplacez par votre sender autorisé
                    'sms': [{'mobile': row['Numéro De Téléphone'], 'sms': f"Bonjour {row['Nom']} {row['Prénom']}, vous avez un rendez-vous le {row['Rendez-vous']}"}]
                }
                headers = {
                    'Authorization': '179mB1VUNfDfyjkdXIfcjyCYbC!OpIIMU7fAA6G1xvf0kWUerZV7eO7qj0ylGJO6kiy=R5VH9BQIpHE6g67uwHBopqvSVf36kT!XZf55',  # Remplacez par votre clé d'API
                    'Content-Type': 'application/json'
                }
                # Envoi du SMS via POST request à l'API
                response = requests.post('https://mystudents.tunisiesms.tn/api/sms', json=payload, headers=headers)
                if response.status_code == 200:
                    print(f"SMS envoyé avec succès à {row['Numéro De Téléphone']}")
                else:
                    print(f"Échec de l'envoi du SMS à {row['Numéro De Téléphone']}: {response.text}")
     except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue lors de l'envoi des SMS: {str(e)}") 
           
    
           
    def validate_fields():
        matricule = matricule1_var.get()
        nom = nom1_var.get()
        prenom = prenom1_var.get()
        age = age1_var.get()
        numtel= numtel_var1.get()
        imc=imc1_var.get()
        thc=thc1_var.get()
        atcdps=atcdps1_var.get() 
        nodule= nodule1_var.get()
        if not all([matricule, nom, prenom, age, numtel, imc, thc, atcdps, nodule]):
           messagebox.showerror("Erreur", "Veuillez remplir tous les champs obligatoires.")
           return False

       # Check additional conditions
        if not (matricule.isdigit() and len(matricule) == 8):
           messagebox.showerror("Erreur", "Le matricule doit contenir exactement 8 chiffres.")
           return False
        elif not nom.isalpha():
           messagebox.showerror("Erreur", "Le nom ne doit ne doit contenir que des lettres.")
           return False
        elif not prenom.isalpha():
           messagebox.showerror("Erreur", "Le prénom ne doit contenir que des lettres.")
           return False
        elif not age.isdigit():
           messagebox.showerror("Erreur", "L'âge doit être un nombre entier.")
           return False
        elif not (numtel.isdigit() and len(numtel)==8):
            messagebox.showerror("Erreur", "Le Numéro de Téléphone est invalide.")
            return False
        elif not validate_imc():
             messagebox.showerror("Error", "L'indice de masse corporelle doit être numérique.")
             return False
        
         
        return True
           
    def afficher_tableau():
        df = pd.read_csv(r'c:\Users\Arij\Desktop\PRIO_MAMMO1.csv')
    
        # Créer une nouvelle fenêtre pour afficher les données
        data_window = tk.Toplevel()
        data_window.title("Données du fichier CSV")

     # Créer un cadre pour la zone de tableau avec barres de défilement
        data_frame = ttk.Frame(data_window)
        data_frame.pack()
    
     # Créer un tableau pour afficher les données avec barres de défilement
        tree = ttk.Treeview(data_frame)
        tree["columns"] = list(df.columns)
    
        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, stretch=True)

        hsb = ttk.Scrollbar(data_frame, orient="horizontal", command=tree.xview)
        hsb.pack(side='bottom', fill='x')
        vsb = ttk.Scrollbar(data_frame, orient="vertical", command=tree.yview)
        vsb.pack(side='right', fill='y')
        tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

        for index, row in df.iterrows():
            tree.insert(values=list(row))

        tree.pack(expand=True, fill='both')
 
        
    # Fonction pour enregistrer les modifications
    def enregistrer_modifications():
        if not validate_fields():
            return
        matricule = matricule1_var.get()
        if not matricule:
            messagebox.showerror("Erreur", "Veuillez rechercher un patient en saisissant le matricule.")
            return

         # Lire toutes les lignes du fichier CSV
        with open(fichier_csv, 'r', newline='', encoding='utf-8') as file:
            lines = list(csv.reader(file))

       # Trouver la ligne correspondant au matricule du patient
        for i, line in enumerate(lines):
            if line[2] == matricule:  # L'indice 2 correspond à la colonne 'Matricule'
                # Mettre à jour les valeurs des champs avec les nouvelles données saisies
                line[0] = nom1_var.get()
                line[1] = prenom1_var.get()
                line[3] = age1_var.get()
                line[4] = numtel_var1.get()
                line[5] = imc1_var.get()
                line[6] = pubme1_var.get()
                line[7] = atcdpoe1_var.get()
                line[8] = thc1_var.get()
                line[9] = atcdpoe1_var.get()
                line[10] = atcdf1_var.get()
                line[11] = brca1_var.get()
                line[13] = peau1_var.get()
                line[14] = lettre1_var.get()
                line[15] = date_entry1.get()
                line[16] = nodule1_var.get()
                line[17] = ecoulement1_var.get()
                line[18] = pathie1_var.get()
                
                break

       # Écrire les modifications dans le fichier CSV
        with open(fichier_csv, 'w', newline='', encoding='utf-8') as file:
             writer = csv.writer(file)
             writer.writerows(lines)
        messagebox.showinfo("Succès", "Les modifications ont été enregistrées avec succès.")
        
        #date_entry1.config(state="normal")
        # Variables
    nom1_var = StringVar()
    prenom1_var = StringVar()
    matricule1_var = StringVar()
    age1_var = StringVar()
    numtel_var1= StringVar()
    imc1_var = StringVar()
    pubme1_var = IntVar()
    atcdpoe1_var = IntVar()
    thc1_var = StringVar()
    atcdps1_var = StringVar()
    nodule1_var = StringVar()
    atcdf1_var = IntVar()
    brca1_var = IntVar()
    peau1_var = IntVar()
    ecoulement1_var = IntVar()
    pathie1_var = IntVar()
    lettre1_var = StringVar()

    # Coordonnées Cliniques
    frame_coord_cliniques = LabelFrame(doctor_window, text="Coordonnées Cliniques", padx=10, pady=10)
    frame_coord_cliniques.pack(fill="x", padx=20, pady=10)

    Label(frame_coord_cliniques, text="Nom").grid(row=1, column=0, sticky="w")
    nom_entry1=Entry(frame_coord_cliniques, textvariable=nom1_var)
    nom_entry1.grid(row=1, column=1, sticky="ew", padx=5)
    invalid_label_nom = Label(frame_coord_cliniques, text="", fg="red")
    invalid_label_nom.grid(row=1, column=2)
    
    Label(frame_coord_cliniques, text="Prénom").grid(row=2, column=0, sticky="w")
    prenom_entry1=Entry(frame_coord_cliniques, textvariable=prenom1_var)
    prenom_entry1.grid(row=2, column=1, sticky="ew", padx=5)
    invalid_label_prenom = Label(frame_coord_cliniques, text="", fg="red")
    invalid_label_prenom.grid(row=2, column=2)
    
    Label(frame_coord_cliniques, text="Matricule").grid(row=0, column=0, sticky="w")
    matricule_entry1 = Entry(frame_coord_cliniques, textvariable=matricule1_var)
    matricule_entry1.grid(row=0, column=1, sticky="ew", padx=5)
    invalid_label_matricule = Label(frame_coord_cliniques, text="", fg="red")
    invalid_label_matricule.grid(row=0, column=2)
    
    
    def obtenir_chemin_lettre_scannée(matricule_patient):
        chemin_fichier_csv2 = 'C:\\Users\\Arij\\Desktop\\PRIO_MAMMO1.csv'
        try:
            with open(chemin_fichier_csv2, mode='r', newline='', encoding='utf-8') as fichier:
                lecteur_csv = csv.DictReader(fichier)
                for ligne in lecteur_csv:
                    if ligne['Matricule'] == matricule_patient:
                        return ligne['Lettre Scannée']
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Le fichier CSV n'a pas été trouvé.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la lecture du fichier CSV : {e}")
        return None
    
    def imprimer_lettre_scannée():
        matricule_patient = matricule_entry1.get() 
        chemin_lettre = obtenir_chemin_lettre_scannée(matricule_patient)
        if chemin_lettre:
            nom_imprimante = win32print.GetDefaultPrinter()  # Utilise l'imprimante par défaut
            try:
                win32api.ShellExecute(0, "print", chemin_lettre, None, ".", 0)
            except Exception as e:
                messagebox.showerror("Erreur d'impression", f"Une erreur s'est produite lors de l'impression: {e}")
        else:
            messagebox.showinfo("Information", "Lettre scannée non trouvée pour le patient spécifié.")


    
    Label(frame_coord_cliniques, text="Age").grid(row=3, column=0, sticky="w")
    age_entry1=Entry(frame_coord_cliniques, textvariable=age1_var)
    age_entry1.grid(row=3, column=1, sticky="ew", padx=5)
    invalid_label_age = Label(frame_coord_cliniques, text="", fg="red")
    invalid_label_age.grid(row=3, column=2)
    
    Label(frame_coord_cliniques, text="Numéro De Téléphone").grid(row=4, column=0, sticky="w")
    num_entry1=Entry(frame_coord_cliniques, textvariable=numtel_var1)
    num_entry1.grid(row=4, column=1, sticky="ew", padx=5)
    #num_entry1.insert(tk.END, "+216")  # Prepopulate the entry with the country code
    #num_entry1.config(state=tk.DISABLED)  # Make the entry non-editable
    invalid_label_num = Label(frame_coord_cliniques, text="", fg="red")
    invalid_label_num.grid(row=4, column=2)

    # Appel à la fonction rechercher_patient lors de la saisie de la matricule
    matricule_entry1.bind("<Return>", rechercher_patient)

    # Variables Cliniques
    frame_vars_cliniques = LabelFrame(doctor_window, text="Variables Cliniques", padx=10, pady=10)
    frame_vars_cliniques.pack(fill="x", padx=20, pady=20) 

    # Ajout des widgets dans les cadres pour les variables cliniques
    Label(frame_vars_cliniques, text="L’indice de masse corporelle").grid(row=0, column=0, sticky="w")
    Entry(frame_vars_cliniques, textvariable=imc1_var).grid(row=0, column=1, sticky="ew", padx=5)
     
    Label(frame_vars_cliniques, text="Traitement Hormonal Contraceptif").grid(row=1, column=0, sticky="w")
    Entry(frame_vars_cliniques, textvariable=thc1_var).grid(row=1, column=1, sticky="ew", padx=5)
     
    Label(frame_vars_cliniques, text="ATCD P cancer du sein").grid(row=2, column=0, sticky="w")
    Entry(frame_vars_cliniques, textvariable=atcdps1_var).grid(row=2, column=1, sticky="ew", padx=5)
     
    Label(frame_vars_cliniques, text="Nodule").grid(row=3, column=0, sticky="w")
     #Entry(frame_vars_cliniques, textvariable=nodule_var).grid(row=3, column=1, sticky="ew", padx=5)
     
    Nodule= ["1", "2", "3", "4", "5", "+5"]
    nodule1_var.set(Nodule[0])
    drop= OptionMenu(frame_vars_cliniques, nodule1_var, *Nodule)
    drop.grid(row=3, column=1, sticky="ew", padx=5, pady=18)
    
    # Label for "cm"
    tk.Label(frame_vars_cliniques, text="cm").grid(row=3, column=2, sticky="ew", padx=5, pady=18)


    Label(frame_vars_cliniques, text="La Puberté Précoce / Menarche Tardive").grid(row=4, column=0, sticky="w")
    Checkbutton(frame_vars_cliniques, variable=pubme1_var).grid(row=4, column=1, sticky="w", padx=5)
     
    Label(frame_vars_cliniques, text="ATCD P cancer de l’ovaire ou de l’endomètre").grid(row=5, column=0, sticky="w")
    Checkbutton(frame_vars_cliniques, variable=atcdpoe1_var).grid(row=5, column=1, sticky="w", padx=5)
     
    Label(frame_vars_cliniques, text="ATCD F cancer du sein ou de l’ovaire").grid(row=6, column=0, sticky="w")
    Checkbutton(frame_vars_cliniques, variable=atcdf1_var).grid(row=6, column=1, sticky="w", padx=5)
     
    Label(frame_vars_cliniques, text="Mutation du Gène BRCA1 ou BRCA2").grid(row=7, column=0, sticky="w")
    Checkbutton(frame_vars_cliniques, variable=brca1_var).grid(row=7, column=1, sticky="w", padx=5)
     
    Label(frame_vars_cliniques, text="Aspect peau d’orange").grid(row=8, column=0, sticky="w")
    Checkbutton(frame_vars_cliniques, variable=peau1_var).grid(row=8, column=1, sticky="w", padx=5)
     
    Label(frame_vars_cliniques, text="Écoulement mamelonnaire sanguinolent").grid(row=9, column=0, sticky="w")
    Checkbutton(frame_vars_cliniques, variable=ecoulement1_var).grid(row=9, column=1, sticky="w", padx=5)
     
    Label(frame_vars_cliniques, text="Présence d’adénopathie").grid(row=10, column=0, sticky="w")
    Checkbutton(frame_vars_cliniques, variable=pathie1_var).grid(row=10, column=1, sticky="w", padx=5)
     

    
    
    # Fonction de validation pour le matricule
    def validate_matricule():
        matricule = matricule1_var.get()
        if not matricule.isdigit() or len(matricule) != 8:
            invalid_label_matricule.config(text="Le matricule doit contenir exactement 8 chiffres.", fg="red")
        else:
            invalid_label_matricule.config(text="")
            
            
    # Fonction de validation pour le nom
    def validate_nom():
        nom = nom1_var.get()
        if not nom.isalpha():
           invalid_label_nom.config(text="Le nom ne doit ne doit contenir que des lettres.", fg="red")
        else:
           invalid_label_nom.config(text="")
           
    def validate_prenom():
        prenom = prenom1_var.get()
        if not prenom.isalpha():
           invalid_label_prenom.config(text="Le prénom ne doit ne doit contenir que des lettres.", fg="red")
        else:
           invalid_label_prenom.config(text="")
           
    def validate_age():
        age = age1_var.get()
        if not age.isdigit():
           invalid_label_age.config(text="L'âge doit être un nombre entier.", fg="red")
        else:
           invalid_label_age.config(text="")
           
    def validate_num():
         num = numtel_var1.get()
         if not num.isdigit() or len(num) != 8:
             invalid_label_num.config(text="Le Numéro de Téléphone est invalide.", fg="red")
         else:
             invalid_label_num.config(text="")       
                
    matricule_entry1.bind("<KeyRelease>", lambda event: validate_matricule())
    nom_entry1.bind("<KeyRelease>", lambda event: validate_nom())
    prenom_entry1.bind("<KeyRelease>", lambda event: validate_prenom())
    age_entry1.bind("<KeyRelease>", lambda event: validate_age())
    num_entry1.bind("<KeyRelease>", lambda event: validate_num())
    
    # Date RDV
    frame_date_rdv = LabelFrame(doctor_window, text="Date De Rendez-Vous", padx=10, pady=10)
    frame_date_rdv.pack(fill="x", padx=20, pady=10)
    
    
    



# Fonction pour afficher le calendrier et sélectionner une date
    def show_date_picker():
      def on_date_select():
        selected_date = cal.selection_get()
        date_entry1.delete(0, 'end')
        date_entry1.insert(0, selected_date.strftime('%Y-%m-%d'))
        cal_window.destroy()

      cal_window = tk.Toplevel(doctor_window)
      cal_window.title("Sélectionner une date")
      cal = Calendar(cal_window, selectmode='day', date_pattern='y-mm-dd')
      cal.pack(padx=10, pady=10)
      Button(cal_window, text="Sélectionner", command=on_date_select).pack(pady=10)

    # Load the calendar icon image
      try:
        calendar_img = calendar_img.resize((32, 32), Image.LANCZOS)
        calendar_photo = ImageTk.PhotoImage(calendar_img)
      except FileNotFoundError as e:
        print(f"Error: {e}")
        calendar_photo = None

     # Create a label with the calendar icon if the image was loaded successfully
      if calendar_photo:
        calendar_icon = tk.Label(cal_window, image=calendar_photo, cursor="hand2")
        calendar_icon.image = calendar_photo  # Keep a reference to avoid garbage collection
        calendar_icon.pack(padx=10, pady=2)
        calendar_icon.bind("<Button-1>", lambda e: on_date_select())
      else:
        calendar_icon = tk.Label(cal_window, text="Calendar Image Not Found", cursor="hand2")
        calendar_icon.pack(padx=10, pady=2)
        calendar_icon.bind("<Button-1>", lambda e: on_date_select())

  # Ajout du champ de date et du bouton pour afficher le calendrier
    Label(frame_vars_cliniques, text="Date de Rendez-vous").grid(row=11, column=0, sticky="w")
    date_entry1 = Entry(frame_vars_cliniques)
    date_entry1.grid(row=11, column=1, sticky="ew", padx=5)
    
    Label(frame_vars_cliniques, text="Priorité").grid(row=12, column=0, sticky="w")
    # Add radio buttons to the frame
    radio1 = tk.Radiobutton(frame_vars_cliniques, text="0", value=0)
    radio1.grid(row=12, column=1, sticky="w")

    radio2 = tk.Radiobutton(frame_vars_cliniques, text="1", value=1)
    radio2.grid(row=12, column=2, sticky="w")


  # Load the calendar icon image
    try:
      calendar_img = Image.open(r"c:\Users\Arij\Documents\desktop vs\calendardate.png")
      calendar_img = calendar_img.resize((32, 32), Image.LANCZOS)
      calendar_photo = ImageTk.PhotoImage(calendar_img)
    except FileNotFoundError as e:
      print(f"Error: {e}")
      calendar_photo = None

  # Create a label with the calendar icon if the image was loaded successfully
    if calendar_photo:
      calendar_icon = tk.Label(frame_vars_cliniques, image=calendar_photo, cursor="hand2")
      calendar_icon.image = calendar_photo  # Keep a reference to avoid garbage collection
      calendar_icon.grid(row=11, column=2, padx=5, pady=5)
      calendar_icon.bind("<Button-1>", lambda e: show_date_picker())
    else:
      calendar_icon = tk.Label(frame_vars_cliniques, text="Calendar Image Not Found", cursor="hand2")
      calendar_icon.grid(row=11, column=2, padx=5, pady=5)
      calendar_icon.bind("<Button-1>", lambda e: show_date_picker())
    #Button(frame_vars_cliniques, text="Choisir Date", command=show_date_picker).grid(row=11, column=2, padx=5, pady=5)
    
    


 # Bouton pour imprimer la lettre sélectionnée
    Button(doctor_window, text="Imprimer la lettre", command=imprimer_lettre_scannée).pack(pady=10)

 # Bouton pour enregistrer les modifications
    save_button = Button(doctor_window, text="Enregistrer les modifications", command=enregistrer_modifications)
    save_button.pack(pady=10) 
    # Bouton pour envoyer les SMS
    #send_sms_button = Button(doctor_window, text="Envoyer SMS", command=send_sms)
    #send_sms_button.pack(pady=10)
    
    def close_med_open_sms():
         doctor_window.destroy()
         open_SMS_window()
    
    def open_outlook():
     chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'  # Update this path if different
     webbrowser.get(chrome_path).open('https://outlook.live.com/mail/0/')     
    #Button(doctor_window, text="Quitter", command=close_med_open_sms).pack(pady=10)
    # Frame to contain the buttons side by side
    button_frame = Frame(doctor_window)
    button_frame.pack(pady=20)

     # Buttons arranged horizontally in the frame
    Button(button_frame, text="Envoyer SMS", command=send_sms).pack(side='left', padx=10)
    Button(button_frame, text="Quitter", command=close_med_open_sms).pack(side='left', padx=10)
    Button(button_frame, text="Consulter", command=afficher_tableau).pack(side='left', padx=10)  
    Button(button_frame, text="Outlook", command=open_outlook).pack(side='left', padx=10)
    #Button(button_frame, text="Enregistrer les modifications", command=enregistrer_modifications).pack(side='left', padx=10)
    # Fonction pour ouvrir la plateforme Outlook
    
    # Charger le logo d'Outlook
    #logo_image = Image.open("Outlook121.png")  # Assurez-vous que le logo est dans le même répertoire ou donnez le chemin complet
   # logo_image = logo_image.resize((50, 50), Image.LANCZOS)  # Redimensionner si nécessaire
    #logo_photo = ImageTk.PhotoImage(logo_image)    

    # Créer un bouton avec le logo d'Outlook et s'assurer que logo_photo ne soit pas récupéré par le garbage collector
    
    #outlook_button.image = logo_photo  # Conserver une référence à l'image
    #outlook_button.pack(pady=10)
  
      


















# Bouton de connexion sur la fenêtre principale
#Button(window, text="Connexion", command=show_login_window, font=("Arial Bold", 25), bg="#CD2990", fg="#ffffff").place(relx=0.6, rely=0.5, anchor="center")
def close_conn_show_login():
    window.destroy()
    show_login_window()

buttonx= CTkButton(master=window, text="Connexion", command=show_login_window, fg_color="#CD2990", hover_color="#E44982", font=("Arial Bold", 25), text_color="#ffffff", width=400, height=70)
buttonx.place(relx=0.6, rely=0.5, anchor="center")

window.mainloop()
