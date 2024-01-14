##############################################################################################################
##   Import Dependencies
##############################################################################################################

import os
import random
from PIL import Image, ImageTk
import tkinter
from tkinter import ttk, filedialog

##############################################################################################################
##   Defining Class
##############################################################################################################

class App:
    def __init__(self, master):
        self.master = master
        self.drawBoard()

    ##############################################################################################################
    ##   Draw Board
    ##############################################################################################################
    def drawBoard(self):
        self.photo_frame = ttk.LabelFrame(self.master, text = "Image", width = 850, height = 650)
        self.photo_frame.pack(side = 'left', padx = 50, fill = 'x', expand = True)
        self.photo_frame.pack_propagate(False) # Keep the frame visible

        self.content_frame = ttk.LabelFrame(self.master, text = "Meta Data", width = 400, height = 350)
        self.content_frame.pack(side = 'left', padx = 20, fill = 'x', expand = True)
        self.content_frame.pack_propagate(False)

        self.image_label = ttk.Label(self.photo_frame)
        self.image_label.pack(anchor = "sw")

        self.open_button = ttk.Button(self.photo_frame, text = "open", command =  self.openFolder)
        self.open_button.pack(side= 'left', anchor = 'sw')

        self.close_button = ttk.Button(self.photo_frame, text = "close", command = self.master.destroy)
        self.close_button.pack(side = "left", anchor = "sw")

        self.back_button = ttk.Button(self.photo_frame, text = "<", state = "disabled", command = self.moveBackward)
        self.back_button.pack(side = "left", anchor = "sw")

        self.forward_button = ttk.Button(self.photo_frame, text = ">", state = "disabled", command = self.moveForward)
        self.forward_button.pack(side= "left", anchor = "sw")

        self.meta_button = ttk.Button(self.photo_frame, text = "meta", state = "disabled", command = self.extractMeta)
        self.meta_button.pack(side = "left", anchor = "sw")

        

    ##############################################################################################################
    ##   Open Folder
    ##############################################################################################################
    def openFolder(self):

        try:
            self.folder = filedialog.askdirectory(title = 'open a folder')
            self.image_list = os.listdir(self.folder)   # list all the files in the folder
            self.new_image_list = [img for img in self.image_list if img.endswith(".jpg")
                                or img.endswith('.JPG') or img.endswith('.png')]
        except FileNotFoundError:
            self.pop_up = tkinter.Toplevel(self.master)
            self.pop_up.title("Alert")
            self.pop_up.resizable(False, False)
            self.pop_up.lift(self.master)
            ttk.Label(self.pop_up, text = "operation cancelled", background = "red").pack(padx = 20, pady = 20)
            ttk.Button(self.pop_up, text = "ok", command = self.pop_up.destroy).pack(padx = 20, pady = 20)

             



    ##############################################################################################################
    ##   Load image
    ##############################################################################################################

    def loadImage(self):
        pass

    ##############################################################################################################
    ##   Next Image
    ############################################################################################################## 
    
    def moveForward(self):
        pass

    ##############################################################################################################
    ##   Previous Image
    ##############################################################################################################

    def moveBackward(self):
        pass

    ##############################################################################################################
    ##   Helper
    ##############################################################################################################

    def helper(self):
        pass

    ##############################################################################################################
    ##   Extract Meta
    ##############################################################################################################

    def extractMeta(sef):
        pass



if __name__ == '__main__':
    root = tkinter.Tk()
    App(root)
    root.title("Image Viewer App")
    root.geometry('1350x750+125+50')
    root.mainloop()
