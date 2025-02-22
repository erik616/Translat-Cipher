import time, os, sys, encrypt, decrypt

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style

from tkinter.filedialog import askopenfilename
import datetime
import pathlib


def main():
    app = ttk.Window("Transposition File Cipher")
    app.geometry("500x500")
    app.maxsize(width=800, height=800)
    FileTranslatEngine(app)
    style = Style(theme="solar")
    app.mainloop()


class FileTranslatEngine(ttk.Frame):
    searching = False

    def __init__(self, master):
        super().__init__(master, padding=15)
        self.pack(fill=BOTH, expand=YES)

        # application variables
        self.path_var = ttk.StringVar(value='C:/')
        self.type_var = ttk.StringVar(value='encrypt')
        self.key_var = ttk.IntVar(value=0)

        # header and labelframe option container
        option_text = "Search file .txt"
        self.option_lf = ttk.Labelframe(self, text=option_text, padding=15)
        self.option_lf.pack(fill=X, expand=YES, anchor=N)

        self.create_path_row()
        self.create_type_row()
        self.create_key_row()
        self.create_button_row()
        self.create_text_result()

    def create_path_row(self):
        """Add path row to labelframe"""
        path_row = ttk.Frame(self.option_lf)
        path_row.pack(fill=X, expand=YES)
        path_lbl = ttk.Label(path_row, text="Path", width=8)
        path_lbl.pack(side=LEFT, padx=(15, 0))
        path_ent = ttk.Entry(path_row, textvariable=self.path_var)
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)
        browse_btn = ttk.Button(
            master=path_row,
            text="Browse",
            command=self.on_browse,
            width=8
        )
        browse_btn.pack(side=LEFT, padx=5)

    def create_type_row(self):
        """Add type row to labelframe"""
        type_row = ttk.Frame(self.option_lf)
        type_row.pack(fill=X, expand=YES, pady=15)
        type_lbl = ttk.Label(type_row, text="Type", width=8)
        type_lbl.pack(side=LEFT, padx=(15, 0))

        encrypt_opt = ttk.Radiobutton(
            master=type_row,
            text="Encrypt",
            variable=self.type_var,
            value="encrypt"
        )
        encrypt_opt.pack(side=LEFT)

        decrypt_opt = ttk.Radiobutton(
            master=type_row,
            text="Decrypt",
            variable=self.type_var,
            value="decrypt"
        )
        decrypt_opt.pack(side=LEFT, padx=15)

    def create_key_row(self):
        key_row = ttk.Frame(self.option_lf)
        key_row.pack(fill=X, expand=YES)
        key_lbl = ttk.Label(key_row, text="Key", width=8)
        key_lbl.pack(side=LEFT, padx=(15, 0))
        key_ent = ttk.Entry(key_row, textvariable=self.key_var)
        key_ent.pack(side=LEFT, fill=BOTH, padx=5)

    def create_button_row(self):
        btn_row = ttk.Frame(self.option_lf)
        btn_row.pack(fill=X, expand=YES, pady=15)
        btn = ttk.Button(
            master=btn_row,
            text="Translated",
            command=self.on_translate,
            bootstyle=OUTLINE,
            width=100
        )
        btn.pack(side=LEFT, padx=5)

    def create_text_result(self):
        self.textbox = ttk.ScrolledText(
            master=self,
            width=100,
        )
        self.textbox.pack(side=TOP, pady=15)

    def on_translate(self):
        """Search for a term based on the search type"""
        search_path = self.path_var.get()
        key = self.key_var.get()

        if search_path != '' and key != 0:
            self.file_translated()

    def on_browse(self):
        """Callback for directory browse"""
        path = askopenfilename(title="Browse directory", filetypes=[("text files", "*.txt")])
        if path:
            self.path_var.set(path)

    def file_translated(self):
        file = self.path_var.get()
        mode = self.type_var.get()
        key = self.key_var.get()

        global translated
        fileObj = open(file, 'r')
        content = fileObj.read()
        fileObj.close()

        if mode == 'encrypt':
            translated = encrypt.encryptMessage(key, content)
        elif mode == 'decrypt':
            translated = decrypt.decryptMessage(key, content)

        self.key_var.set(0)
        name = file[file.find('/'):]
        outputFileName = f"{name[:name.find('.')]}.{mode}ed.txt"

        rote_path = f"{file[:file.find('.')]}.{mode}ed.txt"
        message = f"----File saved in------\n\n{rote_path}\n\n=========\n\n"

        with open(outputFileName, 'w') as outputfile:
            outputfile.write(translated)
            self.textbox.delete('1.0', END)
            self.textbox.insert(END, message)
            self.textbox.insert(END, translated)


if __name__ == '__main__':
    main()
