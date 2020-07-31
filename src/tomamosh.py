from tomato.tomato import glitchify
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk as ttk

modes = ("void", "random", "bloom", "reverse",
         "invert", "pulse", "jiggle", "overlap")
truths = ("True", "False")


def render():
    if audio_var.get() == "False":
        audio = 0
    else:
        audio = 1

    if frame_var.get() == "False":
        frame = 0
    else:
        frame = 1

    glitchify(filein, mode_var.get(), audio, frame,
              int(count_entry.get()), int(posit_entry.get()))


def create_options_selector():
    new_btn = ttk.Button(root, text="different file", command=select_file)
    new_btn.grid(row=0, column=1)
    ttk.Separator(root, orient=HORIZONTAL).grid(
        row=1, column=0, columnspan=4, sticky="ew")
    mode_title = ttk.Label(root, text="Mode:").grid(row=2, column=0)
    mode_menu = ttk.Combobox(root, textvariable=mode_var)
    mode_menu['values'] = modes
    mode_menu.grid(row=2, column=1)

    ttk.Separator(root, orient=HORIZONTAL).grid(
        row=3, column=0, columnspan=4, sticky="ew")

    audio_title = ttk.Label(root, text="Activate audio:").grid(row=4, column=0)
    audio_menu = ttk.Combobox(root, textvariable=audio_var)
    audio_menu['values'] = truths

    ttk.Separator(root, orient=HORIZONTAL).grid(
        row=5, column=0, columnspan=4, sticky="ew")
    audio_menu.grid(row=4, column=1)

    ttk.Label(root, text="Quantity:").grid(row=6, column=0)
    ttk.Label(root, text="Positional frame:").grid(row=8, column=0)
    ttk.Label(root, text="Ignore first frame:").grid(row=10, column=0)

    ttk.Separator(root, orient=HORIZONTAL).grid(
        row=7, column=0, columnspan=4, sticky="ew")
    ttk.Separator(root, orient=HORIZONTAL).grid(
        row=9, column=0, columnspan=4, sticky="ew")
    ttk.Separator(root, orient=HORIZONTAL).grid(
        row=16, column=0, columnspan=4, sticky="ew")

    global count_entry
    global posit_entry
    global frame_entry

    count_entry = ttk.Entry(root)
    posit_entry = ttk.Entry(root)
    frame_menu = ttk.Combobox(root, textvariable=frame_var)
    frame_menu['values'] = truths

    count_entry.grid(row=6, column=1)
    posit_entry.grid(row=8, column=1)
    frame_menu.grid(row=10, column=1)

    count_entry.insert(10, "1")
    posit_entry.insert(10, "1")

    rend_btn = ttk.Button(root, text="Render!", command=render)
    rend_btn.grid(row=17, column=0, sticky="ew", columnspan=4)
    root.geometry()


def select_file():
    global filein
    filein = fd.askopenfilename()
    for widget in root.winfo_children():
        widget.destroy()
    if ".avi" in filein:
        up_btn.destroy()
        filepath = ttk.Label(root, text="file: " +
                             filein).grid(row=0, column=0)
        root.geometry()
        create_options_selector()
    else:
        root.destroy()


root = Tk()
root.title('Tomamosh - a tomato frontend')
s = ttk.Style()
if sys.platform == "linux":
    s.theme_use('clam')
elif sys.platform == "darwin":
    s.theme_use('aqua')
else:
    s.theme_use('default')
mode_var = StringVar(root)
audio_var = StringVar(root)
frame_var = StringVar(root)
mode_var.set("void")
audio_var.set("True")
frame_var.set("True")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
up_btn = ttk.Button(root, text="Select AVI file", command=select_file)
up_btn.grid(row=0, column=0)
root.mainloop()
