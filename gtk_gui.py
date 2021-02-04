import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

'''
class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "YazLang")
        self.set_border_width(10)
        self.set_default_size(200, 100)

        #Title
        Title = Gtk.Box()
        self.add(Title)
        label = Gtk.Label("Welcome to YazzLang")
        Title.add(label)

        #ListBox
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 130)
        row_1.add(box_1)
        label = Gtk.Label("Check it of")
        check = Gtk.CheckButton()
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        listbox.add(row_1)

        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 100)
        row_2.add(box_2)
        label = Gtk.Label("This is check")
        switch = Gtk.Switch()
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(switch, True, True, 0)
        listbox.add(row_2)

        #Box
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)
        self.grid = Gtk.Grid()
        self.grid2 = Gtk.Grid()

        #Buttons
        #Array of buttons
        self.arraybuttons = []
        self.arraylabels = []
        for i in range(10):
            self.arraybuttons.append( Gtk.Button(label = "Button {}".format(i)) )
            self.arraylabels.append( Gtk.Label("This is button: {}".format(i)) )

        for j in range( len(self.arraybuttons) ):
            self.grid.add(self.arraybuttons[j])
            self.grid2.add(self.arraylabels[j])

        self.box.pack_start(self.grid2, True, True, 0)
        self.box.add(self.grid)
        

        #Bacon button
        self.baconbutton = Gtk.Button(label = "Press me!!")
        self.baconbutton.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.baconbutton, True, True, 0)

        #Tuna Button
        self.Tunabutton = Gtk.Button(label = "Dont Press Me!!!")
        self.Tunabutton.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.Tunabutton, True, True, 0)

    def on_button_clicked(self, widget):
        print("Hi")
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''
class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

builder = Gtk.Builder()
builder.add_from_file("simple.glade")
builder.connect_signals(Handler())

window = builder.get_object("Window")
window.show_all()


Gtk.main()