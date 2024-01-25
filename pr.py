import customtkinter as CTk


expenses = {
        "food_for_month": 10000,
        "cloth_for_month": 10000,
        "transport": 4000,
        "books_price": 500,
        "communal_payments": 5000,
        "others": 10000
    }

expenses_one_time = {
        "phone": 20000,
        "tablet": 20000,
    }


class ToplevelWindow(CTk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")
        self.label = CTk.CTkLabel(self, text="Изменение параметров")
        self.label.pack(padx=20, pady=20)


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("900x580")
        self.title("Семейный бюджет")
        self.resizable(False, False)
        self.toplevel_window = None
        self.scholarship = 0
        self.inflation = 0.006
        self.all_expenses = 0
        self.balance = 0

        self.entry_1 = CTk.CTkEntry(self, placeholder_text="Введите общую зарплату родителей", width=300)
        self.entry_1.grid(row=0, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.entry_2 = CTk.CTkEntry(self, placeholder_text="Введите количество месяцев", width=300)
        self.entry_2.grid(row=2, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.button_2 = CTk.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
                                          text="Ребёнок студент", command=self.student)
        self.button_2.grid(row=10, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        #self.button_1 = CTk.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
        #                              text="Изменить данные о расходах", command=self.open_toplevel(), width=100)
        #self.button_1.grid(row=0, column=6, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")
        # Этот кусок кода запускает отдельное окно, в котором можно изменять изнаячально заданные расходы,
        # Почему-то событие происходит без нажатия кнопки
        # Но в задании нет функции изменения этих параметров, так что я оставлю пока так. В перспективе дальнейшего
        # развития..

        self.button_3 = CTk.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
                                      text="Ребёнок школьник", command=self.school_boy)
        self.button_3.grid(row=8, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.button_4 = CTk.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
                                      text="Рассчитать", command=self.calculate)
        self.button_4.grid(row=6, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.button_5 = CTk.CTkButton(self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),
                                      text="Платное обучение", command=self.pay_study)
        self.button_5.grid(row=12, column=2, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.textbox = CTk.CTkTextbox(self, width=450)
        self.textbox.grid(row=6, column=6, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.appearance_mode_option_menu = CTk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_option_menu.grid(row=12, column=6, padx=20, pady=(10, 10))

    def student(self):
        expenses["room_price_month"] = 1000
        self.scholarship = 2000

    def pay_study(self):
        self.scholarship = 0
        expenses_one_time["stud_price"] = 90000

    def school_boy(self):
        self.scholarship = 0
        if "room_price_month" in expenses.keys():
            expenses.pop("room_price_month")
        if "stud_price" in expenses_one_time.keys():
            expenses_one_time.pop("stud_price")

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
        else:
            self.toplevel_window.focus()

    def print_result(self):
        if self.balance > 0:
            self.textbox.insert("0.0", "Денег хватает\n\n" + f'Баланс составит {self.balance}')
        else:
            self.textbox.insert("0.0", "Недостаток денег\n\n" + f'Баланс составит {self.balance}')

    def calculate(self):
        try:
            self.textbox.delete("1.0", "end")
            salary = int(self.entry_1.get())
            month_count = int(self.entry_2.get())
            for value in expenses.values():
                self.all_expenses += value * month_count
            for value in expenses_one_time.values():
                self.all_expenses += value

            self.balance = ((salary * month_count) - (salary * month_count * self.inflation)) - self.all_expenses
            self.print_result()
            self.all_expenses = 0
        except ValueError:
            self.textbox.insert("0.0", "Ошибка ввода значений")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        CTk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()
