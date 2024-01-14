##############################################################################################################
##   Import Dependencies
##############################################################################################################

import os
import random
from PIL import Image, ImageTk
from PIL.ExifTags import TAGS
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
            self.forward_button.state(['!disabled'])
            self.meta_button.state(['!disabled'])
            self.loadImage()

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

    def loadImage(self, image_counter = 0):
        # Getting the complete path of the image
        self.image_counter = image_counter
        self.image = self.folder + '/' + self.new_image_list[self.image_counter]
        # Resize the image
        width, height = Image.open(self.image).size
        if width > height:
            self.image_resized = Image.open(self.image).resize((850, 550))
        else:
            self.image_resized = Image.open(self.image).resize((450, 600))
        
        self.load_image = ImageTk.PhotoImage(self.image_resized)
        # Attach the image to the image label
        self.image_label.image = self.load_image
        self.image_label.config(image = self.image_label.image)
    ##############################################################################################################
    ##   Next Image
    ############################################################################################################## 
    
    def moveForward(self):
        self.meta_button.state(['!disabled'])
        self.clearMeta()
        self.image_counter += 1
        self.loadImage(self.image_counter)
        self.back_button.state(['!disabled'])
        if self.image_counter + 1 == len(self.new_image_list):
            self.forward_button.state(['disabled'])


    ##############################################################################################################
    ##   Previous Image
    ##############################################################################################################

    def moveBackward(self):
        self.meta_button.state(['!disabled'])
        self.clearMeta()
        self.image_counter -= 1
        self.loadImage(self.image_counter)
        self.forward_button.state(['!disabled'])
        if self.image_counter == 0:
            self.back_button.state(['disabled'])


    ##############################################################################################################
    ##   Clear Meta data
    ##############################################################################################################

    def clearMeta(self):
        if self.content_frame.pack_slaves():
            for widget in self.content_frame.pack_slaves():
                widget.destroy()

    ##############################################################################################################
    ##   Extract Meta
    ##############################################################################################################

    def extractMeta(self):
        self.clearMeta()
        file = Image.open(self.image)
        data = file.getexif()
        if data:
            for key, value in data.items():
                tag_name = TAGS.get(key)  # Use TAGS dictionary to get tag name
                label_text = f"{tag_name}: {str(value)}"
                ttk.Label(self.content_frame, text = label_text).pack(anchor = "sw", pady = 3)
        else:
            ttk.Label(self.content_frame, text = "No metadata found").pack(anchor = "sw", padx = 20, pady = 3)
        self.meta_button.state(['disabled'])



if __name__ == '__main__':
    root = tkinter.Tk()
    App(root)
    root.title("Image Viewer App")
    root.geometry('1350x750+125+50')
    root.mainloop()
