import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "The Window")
        self.set_default_size(100, 50)
        #Box
        self.box = Gtk.Box(spacing=10)
        self.add(self.box)
        self.grid = Gtk.Grid()

        #Buttons
        #Array of buttons
        self.arraybuttons = []
        self.arraylabels = []
        for i in range(10):
            self.arraybuttons.append( Gtk.Button(label = "Button {}".format(i)) )
            self.arraylabels.append( Gtk.Label("This is button: {}".format(i)) )

        for j in range( len(self.arraybuttons) ):
            self.arraybuttons[j].add(self.arraylabels[j])
            self.grid.add(self.arraybuttons[j])

        self.box.pack_start(self.grid, True, True, 0)
        

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