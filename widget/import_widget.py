import customtkinter as ctk
from tkinter import filedialog as fd
import os
from config import AppStyles as st # Importa la classe di configurazione

class ImportSection:
    def __init__(self, master):
        self.master = master
        
        # Creazione del frame principale
        self.frame = ctk.CTkFrame(master)
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        # Configurazione della griglia del frame principale
        self.frame.grid_rowconfigure((0, 1), weight=1)
        self.frame.grid_columnconfigure((0, 1, 2), weight=1, uniform="column")
        
        # Titolo della sezione
        self.import_title_label = ctk.CTkLabel(self.frame, text="Import Files", font=st.HEADER_FONT)
        self.import_title_label.grid(row=0, column=0, columnspan=3, padx=15, pady=(0, 10), sticky="nsew")
        
        # Pulsanti per l'importazione
        self.import_model_button = ctk.CTkButton(self.frame, text="Import Model (.pt)", font=st.BUTTON_FONT,command=self.select_model_file, corner_radius=10)
        self.import_model_button.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.import_dataloader_button = ctk.CTkButton(self.frame, text="Import DataSet (.py)", font=st.BUTTON_FONT, command=self.import_dataset, corner_radius=10)
        self.import_dataloader_button.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.import_dataset_button = ctk.CTkButton(self.frame, text="Import Data File (.csv)", font=st.BUTTON_FONT, command=self.import_datafile, corner_radius=10)
        self.import_dataset_button.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

        # Creazione di un frame per le etichette e i pulsanti di rimozione
        self.file_frame = ctk.CTkFrame(self.frame)
        self.file_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")
        self.file_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.file_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        # Etichette e pulsanti di rimozione per mostrare i file selezionati
        self.model_file_label = ctk.CTkLabel(self.file_frame, text="No Model selected", font=st.TEXT_FONT)
        self.model_file_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.model_remove_button = ctk.CTkButton(self.file_frame, text="X", command=self.remove_model_file, width=10, height=10, corner_radius=10)
        self.model_remove_button.grid(row=0, column=2, padx=(0, 10), pady=5, sticky="e")
        
        self.dataset_file_label = ctk.CTkLabel(self.file_frame, text="No DataSet selected", font=st.TEXT_FONT)
        self.dataset_file_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.dataset_remove_button = ctk.CTkButton(self.file_frame, text="X", command=self.remove_dataset_file, width=10, height=10, corner_radius=10)
        self.dataset_remove_button.grid(row=1, column=2, padx=(0, 10), pady=5, sticky="e")
        
        self.data_file_label = ctk.CTkLabel(self.file_frame, text="No Data File selected", font=st.TEXT_FONT)
        self.data_file_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        self.data_remove_button = ctk.CTkButton(self.file_frame, text="X", command=self.remove_data_file, width=10, height=10, corner_radius=10)
        self.data_remove_button.grid(row=2, column=2, padx=(0, 10), pady=5, sticky="e")
        
        # Variabili per i percorsi dei file
        self.selected_model_file = None
        self.dataset_file_path = None
        self.data_file_path = None

    def select_model_file(self):
        filetypes = (
            ('Model files', '*.pt'),
        )

        filename = fd.askopenfilename(
            title='Select Model File',
            initialdir='.',
            filetypes=filetypes
        )
        
        if filename:
            self.selected_model_file = filename
            self.model_file_label.configure(text=f"Model: {os.path.basename(filename)}", font=st.TEXT_FONT)

    def import_dataset(self):
        filetypes = (
            ('DataSet files', '*.py'),
        )

        filename = fd.askopenfilename(
            title='Select DataSet file',
            initialdir='.',
            filetypes=filetypes
        )
        
        if filename:
            self.dataset_file_path = filename
            self.dataset_file_label.configure(text=f"DataSet: {os.path.basename(filename)}", font=st.TEXT_FONT)

    def import_datafile(self):
        filetypes = (
            ('Data Files', '*.csv'),
        )

        filename = fd.askopenfilename(
            title='Select Data File',
            initialdir='.',
            filetypes=filetypes
        )
        
        if filename:
            self.data_file_path = filename
            self.data_file_label.configure(text=f"Data File: {os.path.basename(filename)}", font=st.TEXT_FONT)
    
    def remove_model_file(self):
        self.selected_model_file = None
        self.model_file_label.configure(text="No Model selected", font=st.TEXT_FONT)
        
    def remove_dataset_file(self):
        self.dataset_file_path = None
        self.dataset_file_label.configure(text="No DataSet selected", font=st.TEXT_FONT)
        
    def remove_data_file(self):
        self.data_file_path = None
        self.data_file_label.configure(text="No Data File selected", font=st.TEXT_FONT)
   
    # Metodi per ottenere i percorsi dei file
    def get_model_file(self):
        print(self.selected_model_file)
        return self.selected_model_file

    def get_dataset_file(self):
        return self.dataset_file_path

    def get_data_file(self):
        return self.data_file_path