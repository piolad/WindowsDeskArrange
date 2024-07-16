import customtkinter

from config import init_app_config, Configuration
from ViewCardBase import ViewCardBase

class App(customtkinter.CTk):
    def __init__(self):
        init_app_config(self)
        super().__init__()
        self.title(Configuration["app_title"])

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        

        self.sidebar_frame = customtkinter.CTkFrame(self, width=80, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nswe", columnspan=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=Configuration["app_sidebar_title"], font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=12, pady=(12, 10))
        self.sidebar_frame.pack(side="left", fill="y")

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, fg_color="green",font=customtkinter.CTkFont( weight="bold"))
        self.sidebar_button_1.grid(row=1, column=0, pady=(5, 0))
        self.sidebar_button_1.configure(text="Create backup")

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, fg_color="#b39204",font=customtkinter.CTkFont( weight="bold"))
        self.sidebar_button_2.grid(row=2, column=0, pady=(5, 0))
        self.sidebar_button_2.configure(text="View backups")
        self.sidebar_button_2.configure(state="disabled", text_color_disabled="#bfbfbf")

        self.card1 = ViewCardBase(self)
        

        self.geometry(f"{int(self.winfo_screenwidth()*Configuration['init_width_ratio'])}x{int(self.winfo_screenheight()*Configuration['init_height_ratio'])}+{int(self.winfo_screenwidth()*Configuration['init_width_ratio']/2)}+{int(self.winfo_screenheight()*Configuration['init_height_ratio']/2)}")

    def sidebar_button_event(self):
        print("Button clicked")


#how to run app (with venv:)
# python -m venv venv