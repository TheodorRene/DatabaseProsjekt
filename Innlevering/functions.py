from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk


class GuiTools(ABC):

    @abstractmethod
    def empty_ent(ent):
        empty = [el.delete(0,"end") for el in ent]


    @abstractmethod
    def pack_widgets(widgets):
        pack = [el.pack() for el in widgets]

