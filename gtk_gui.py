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
        for i in range(10):
            self.arraybuttons.append( Gtk.Button(label = "Button {}".format(i)) )

        for j in range( len(self.arraybuttons) ):
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
        
        '''
        self.set_border_width(10)
        self.set_default_size(400, 200)
        textbox = Gtk.Box(spacing = 10)
        label = Gtk.Label(label = "This is my project")
        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label(label="This is a normal label")
        vbox_left.pack_start(label, True, True, 0)

        self.button = Gtk.Button(label = "Click Here")
        self.button2 = Gtk.Button(label = "Click There")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(hbox)
        self.add(self.button)

'''
    def on_button_clicked(self, widget):
        print("Hi")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()