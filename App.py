import customtkinter
import tkinter
import tkinter.messagebox

from config import init_app_config, Configuration
from ViewCardBase import ViewCardBase


class App(customtkinter.CTk):
    def __init__(self):
        init_app_config(self)
        super().__init__()

        self.title(Configuration["app_title"])

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        

        self.sidebar_frame = customtkinter.CTkFrame(self, width=80, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nswe", columnspan=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text=Configuration["app_sidebar_title"], font=customtkinter.CTkFont(size=12, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=12, pady=(12, 10))
        # self.sidebar_frame.pack(side="left", fill="y")

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, fg_color="green",font=customtkinter.CTkFont( weight="bold"))
        self.sidebar_button_1.grid(row=1, column=0, pady=(5, 0))
        self.sidebar_button_1.configure(text="Create backup")

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, fg_color="#b39204",font=customtkinter.CTkFont( weight="bold"))
        self.sidebar_button_2.grid(row=2, column=0, pady=(5, 0))
        self.sidebar_button_2.configure(text="View backups")
        self.sidebar_button_2.configure(text_color_disabled="#bfbfbf")


        
        # self.my_frame = MyFrame(master=self, width=300, height=200)
        # self.my_frame.grid(row=0, column=0, padx=20, pady=20)
       
        # self.radio_var = tkinter.IntVar(value=0)
      
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        
        
        # customtkinter.CTkRadioButton(master=self.radiobutton_frame
        # self.card1 = ViewCardBase(self,width=80)
        # self.card1.grid(row=0, column=0, padx=12, pady=(12, 10))

        # self.card2 = customtkinter.CTkFrame(self, width=80, corner_radius=0)
        # self.card2.grid(row=0, column=1, padx=12, pady=(12, 10), sticky="nswe")



        self.main_frame = customtkinter.CTkScrollableFrame(self, width=80, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, rowspan=4, sticky="nswe", columnspan=1)


        self.iconSizing_frame = customtkinter.CTkFrame(master=self.main_frame)    
        self.iconSizing_frame.grid(row=0, column=3, padx=(10, 10), pady=(10, 0), sticky="nsew") #, columnspan=1,rowspan=1)
        self.iconSizing_label = customtkinter.CTkLabel(master=self.iconSizing_frame, text="Size of icons", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.iconSizing_label.grid(row=0, column=2, columnspan=1, padx=10, pady=(0,15), sticky="")
        self.iconSizing_slider = customtkinter.CTkSlider(master=self.iconSizing_frame, from_=0, to=100, command=self.iconSizing_slider_event)
        self.iconSizing_slider.grid(row=1, column=2, columnspan=1, padx=10, pady=(0,15), sticky="")
        
        

        self.geometry(f"{int(self.winfo_screenwidth()*Configuration['init_width_ratio'])}x{int(self.winfo_screenheight()*Configuration['init_height_ratio'])}+{int(self.winfo_screenwidth()*Configuration['init_width_ratio']/2)}+{int(self.winfo_screenheight()*Configuration['init_height_ratio']/2)}")


    def sidebar_button_event(self):
        print("Button clicked")
    def iconSizing_slider_event(self, value):
        print("Slider moved. Value: ", value)

#how to run app (with venv:)
# python -m venv venv