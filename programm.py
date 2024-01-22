from tkinter import ttk

objects = ['button', 'label', 'entry', 'text', 'combobox', 'create_window', 'loop_window']
script = ""

while True:
    object_for_gen = input("Что вы хотите добавить? ")
    if object_for_gen.lower() in objects:
        for i in range(len(objects)):
            if object_for_gen.lower() == 'button':
                name_for_btn = input("Введите название кнопки: ")
                label_for_btn = input("Введите текст для кнопки: ")
                width_for_btn = input("Введите ширину кнопки: ")
                height_for_btn = input("Введите высоту кнопки: ")
                x_for_btn = input("Введите расположение x: ")
                y_for_btn = input("Введите расположение y: ")
                command_for_btn = input("Назначьте команду для кнопки: ")
                script = script + f"{name_for_btn} = Button(window, text = '{label_for_btn}', command = {command_for_btn})\n{name_for_btn}.place(width = {width_for_btn}, height = {height_for_btn}, x = {x_for_btn}, y = {y_for_btn})\n"
                print(script)
                break
            elif object_for_gen.lower() == 'label':
                name_for_lbl = input("Введите название текста: ")
                label_for_lbl = input("Введите текст для отображения: ")
                width_for_lbl = input("Введите ширину текста: ")
                height_for_lbl = input("Введите высоту текста: ")
                x_for_lbl = input("Введите расположение x: ")
                y_for_lbl = input("Введите расположение y: ")
                font_for_lbl = input("Введите настройку шрифта*: ")

                if font_for_lbl == "":
                    script = script + f"{name_for_lbl} = Label(window, text = '{label_for_lbl}')\n{name_for_lbl}.place(width = {width_for_lbl}, height = {height_for_lbl}, x = {x_for_lbl}, y = {y_for_lbl})\n"
                else:
                    script = script + f"{name_for_lbl} = Label(window, text = '{label_for_lbl}', font = {font_for_lbl})\n{name_for_lbl}.place(width = {width_for_lbl}, height = {height_for_lbl}, x = {x_for_lbl}, y = {y_for_lbl})\n"
                print(script)
                break
            elif object_for_gen.lower() == 'entry':
                name_for_entry = input("Введите название поля: ")
                width_for_entry = input("Введите ширину поля: ")
                height_for_entry = input("Введите высоту поля: ")
                x_for_entry = input("Введите расположение x: ")
                y_for_entry = input("Введите расположение y: ")
                font_for_entry = input("Введите настройку шрифта*: ")
                
                if font_for_entry == "":
                    script = script + f"{name_for_entry} = Entry(window)\n{name_for_entry}.place(width = {width_for_entry}, height = {height_for_entry}, x = {x_for_entry}, y = {y_for_entry})\n"
                else:
                    script = script + f"{name_for_entry} = Entry(window, font = {font_for_entry})\n{name_for_entry}.place(width = {width_for_entry}, height = {height_for_entry}, x = {x_for_entry}, y = {y_for_entry})\n"
                print(script)
                break
            elif object_for_gen.lower() == 'text':
                name_for_text = input("Введите название поля: ")
                width_for_text = input("Введите ширину поля: ")
                height_for_text = input("Введите высоту поля: ")
                x_for_text = input("Введите расположение x: ")
                y_for_text = input("Введите расположение y: ")
                font_for_text = input("Введите настройку шрифта*: ")

                if font_for_text == "":
                    script = script + f"{name_for_text} = Text(window)\n{name_for_text}.place(width = {width_for_text}, height = {height_for_text}, x = {x_for_text}, y = {y_for_text})\n"
                else:
                    script = script + f"{name_for_text} = Text(window, font = {font_for_text})\n{name_for_text}.place(width = {width_for_text}, height = {height_for_text}, x = {x_for_text}, y = {y_for_text})\n"
                print(script)
                break
            elif object_for_gen.lower() == 'combobox':
                name_for_cb = input("Введите название списка: ")
                width_for_cb = input("Введите ширину списка: ")
                height_for_cb = input("Введите высоту списка: ")
                x_for_cb = input("Введите расположение x: ")
                y_for_cb = input("Введите расположение y: ")
                values_for_cb = input("Введите значения (напр., [1,2,3]): ")

                script = script + f"{name_for_cb} = ttk.Combobox(window, values = {values_for_cb})\n{name_for_cb}.place(width = {width_for_cb}, height = {height_for_cb}, x = {x_for_cb}, y = {y_for_cb})\n"
                print(script)

                break
            elif object_for_gen.lower() == 'create_window':
                geometry = input("Введите размер окна (\"300x300\"): ")
                script = f"from tkinter import *\nfrom tkinter import ttk\nwindow = Tk()\nwindow.geometry({geometry})\nwindow.title('TkGen')\n"
                print(script)
                break
            elif object_for_gen.lower() == 'loop_window':
                script = script + f"window.mainloop()"

                print(script)
                break