from typing import Union, Tuple, List, Optional, Any
import customtkinter

class ViewCardBase(customtkinter.CTkFrame):
    def __init__(self,
                 master: Any,
                 width: int = 200,
                 height: int = 200,
                 corner_radius: Optional[Union[int, str]] = None,
                 border_width: Optional[Union[int, str]] = None,

                 bg_color: Union[str, Tuple[str, str]] = "transparent",
                 fg_color: Optional[Union[str, Tuple[str, str]]] = None,
                 border_color: Optional[Union[str, Tuple[str, str]]] = None,

                 background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None,
                 overwrite_preferred_drawing_method: Union[str, None] = None,
                 **kwargs):
        super().__init__(master, width=width, height=height, corner_radius=corner_radius, border_width=border_width,
                            bg_color=bg_color, fg_color=fg_color, border_color=border_color,
                            background_corner_colors=background_corner_colors,
                            overwrite_preferred_drawing_method=overwrite_preferred_drawing_method, **kwargs)
        
        # example: a label and a button
        
        

        # self.label = customtkinter.CTkLabel(self, text="ViewCardBase", font=customtkinter.CTkFont(size=10, weight="bold"))
        # self.label.pack()
        # self.button = customtkinter.CTkButton(self, text="ViewCardBase Button", command=self.button_event)
        # self.button.grid(row=1, column=0)
        # self.button.pack()
        # self.pack()
    
    def button_event(self):
        pass

