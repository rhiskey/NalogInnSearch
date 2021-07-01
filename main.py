import tkinter as tk
from tkinter import filedialog as fd
# Config
# import os
from settings import in_file, out_folder, debug
import logging
import time
from datetime import date
from sys import exit

from Helpers.request import get_valid_inns
from FileWorkers.GetInn import get_inn_list_from_file
from FileWorkers.CreateExcelFile import create_excel_from_response
from Helpers.checkdate import check_date_of_last_modification


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.entry = None
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input_label = tk.Label(self)
        self.input_label["text"] = "Выберите .txt файл со списком ИНН\n(1 ИНН на одной строке):"
        self.input_label.pack()
        #
        # self.entry = tk.Entry(self)
        # self.entry["width"] = 50
        # self.entry.pack()

        self.bt_openfile = tk.Button(self)
        self.bt_openfile["text"] = "Выбрать файл"
        self.bt_openfile["command"] = self.open_file
        self.bt_openfile.pack()

        # self.bt_excel = tk.Button(self)
        # self.bt_excel["text"] = "Создать Excel"
        # self.bt_excel["command"] = self.create_excel
        # # self.bt_excel.pack(side="top")
        # self.bt_excel.pack()

        self.info_label = tk.Label(self)
        self.info_label["text"] = "*Excel файл с результатами\nбудет сохранен в папке с программой"
        self.info_label["fg"] = "red"
        self.info_label.pack()

        # self.quit = tk.Button(self, text="Выход", fg="red",
        #                       command=self.master.destroy)
        # self.quit.pack(side="bottom")

    # UI устарело
    def create_excel(self):
        # entry = tk.Entry(self)
        inn_file = self.entry.get()
        inn_list = get_inn_list_from_file(inn_file)
        response = get_valid_inns(inn_list, 1)
        where_to_save_file = ""
        f_name = create_excel_from_response(response, where_to_save_file)
        # print("hi there, everyone!")

    def open_file(self):
        inn_file = fd.askopenfilename(initialdir="/", title="Выберите файл",
                                      filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        inn_list = get_inn_list_from_file(inn_file)
        response = get_valid_inns(inn_list, 1)
        # TODO
        where_to_save_file = ""
        f_name = create_excel_from_response(response, where_to_save_file)


# def create_excel2(inn_file):
#     # entry = tk.Entry()
#     #inn_file = entry.get()
#     inn_list = get_inn_list_from_file(inn_file)
#     response = get_valid_inns(inn_list)
#     # print(response)
#     where_to_save_file = ""
#     f_name = create_excel_from_response(response, where_to_save_file)
#     #print("hi there, everyone!")


def main():
    # logging.basicConfig(filename='naloginn.log', level=logging.INFO)
    # TODO: change DEBUG -> Error or Info
    log_level = logging.INFO
    if debug == 'true':
        log_level = logging.DEBUG
    if debug == 'false':
        log_level = logging.ERROR

    logging.basicConfig(filename='naloginn.log', format='%(asctime)s - %(levelname)s:%(message)s', level=log_level)
    logging.info('Started v. 0.0.4')

    # # GUI:
    # root = tk.Tk()
    # root.title("Поиск по ИНН")
    # app = Application(master=root)
    # app.mainloop()
    # # root.mainloop()

    # print("Enter path to INN file (.txt):")
    # in_file = str(input())

    # Read IN_FILE and OUT_FILE from config:
    # inn_file = in_file
    # where_to_save_file = out_file

    today = date.today()
    is_month_equal = check_date_of_last_modification(today)

    if is_month_equal:
        logging.debug('Opening file: %s', in_file)
        logging.debug('Folder to save: %s', out_folder)

        inn_list = get_inn_list_from_file(in_file)
        response = get_valid_inns(inn_list, 1)
        # if page>1 do multiple requests, parse results into 1 dictionary
        pages = response.get('pageCount')
        data_l = []
        if pages > 1:
            for i in range(pages):
                # Add response.data
                response = get_valid_inns(inn_list, i + 1)
                # print(response.get('data'))
                data_l.append(response.get('data'))
                time.sleep(1)
        else:
            data_l.append(response.get('data'))
        # print(response.get('innNotFoundCount'))
        logging.info('Not found INN - %s', response.get('innNotFoundCount'))

        # Pass only data
        f_name = create_excel_from_response(data_l, out_folder)
        print('Excel file created! - %s', f_name)
        logging.info('Finished. Out File - %s', f_name)
        exit(0)

        if debug == 'true':
            input()
    else:
        logging.info('Current month is differ from site')
        exit(1)


if __name__ == '__main__':
    main()
