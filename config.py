# Description: Configuration file for the application

import customtkinter


Configuration = {
    "appearance_mode": "system"
    ,"color_theme": "blue"   
    ,"init_width_ratio": 1/3
    ,"init_height_ratio": 1/3
    ,"app_title": "Windows DeskArrange"
    ,"app_sidebar_title": "Windows DeskArrange"
}


def init_app_config(app_instance):
    customtkinter.set_appearance_mode(Configuration["appearance_mode"])
    customtkinter.set_default_color_theme(Configuration["color_theme"])