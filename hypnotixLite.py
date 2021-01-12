#!/usr/bin/python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import sys
import warnings
import mpv
import threading
from os import path as fpath, linesep

warnings.filterwarnings("ignore")

        
class MyWindow(Gtk.Window):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
    
        
    def my_zoom(self, widget, event):
        if not self.sidebar.is_visible():                  
            w = self.win.get_size()[0]
            h = self.win.get_size()[1]
            direction = event.get_scroll_deltas()[2]
            if direction < 0:
                if not w > 1250:
                    self.win.resize(w + 30, (w + 30) / 1.777777778)
            elif direction > 0:
                if not w < 260:
                    self.win.resize(w - 30, (w - 30) / 1.777777778)
                    
    def msgbox(self, message):
        dialog = Gtk.Dialog(title="Message", flags=0)
        dialog.add_buttons(Gtk.STOCK_OK, Gtk.ResponseType.OK)

        dialog.set_default_size(250, 200)

        label = Gtk.Label()
        label.set_text(message)
        box = dialog.get_content_area()
        box.add(label)       
        dialog.show_all()
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("playlist imported")

        dialog.destroy()
                    
    ####### import playlist #######
    def import_playlist(self):
        dlg = Gtk.FileChooserDialog(title="Please choose a file", parent=None, action = 0)
        dlg.add_buttons("Cancel", Gtk.ResponseType.CANCEL,
                     "Open", Gtk.ResponseType.OK)
                     
        filter = Gtk.FileFilter()
        filter.set_name("Playlists")
        filter.add_pattern("*.m3u")
        dlg.add_filter(filter)
        response = dlg.run()

        if response == Gtk.ResponseType.OK:
             infile = (dlg.get_filename())
             print("FileName:", infile)
             dlg.destroy()
             self.parse_playlist(infile)
             self.msgbox("Saved as mychannels10.txt\n\nShortcut 0")
        else:
            dlg.destroy()
        
        
    def parse_playlist(self, infile):
        t = open(infile, "r").read()
        text = linesep.join([s for s in t.splitlines() if s])
        chList = []
        urlList = []
        mlist = text.splitlines()

        for line in mlist:
            if line.startswith("#EXTINF"):
                ch = line.partition('tvg-name="')[2].partition('" ')[0]
                if ch == "":
                    ch = line.partition(',')[2]
                chList.append(ch)
            if line.startswith("http"):
                urlList.append(line)
        outfile = "mychannels10.txt"
        with open(outfile, "w") as f:
            for x in range(len(chList)):
                if not "***" in chList[x]:
                    f.write(f"{chList[x].replace('Pluto ', '').replace(' Made In Germany', '')},{urlList[x]}\n")
                    
        f.close()
        self.makeList(outfile)

    def on_button_press_event(self, widget, button):
        if (button.button == 1): ## left mouse button
            return True
        else:
            return False
            
    def on_key_press_event(self, widget, event):
        if event.keyval == Gdk.KEY_q:
            Gtk.main_quit()
        if event.keyval == Gdk.KEY_i:            
            self.import_playlist()
        ### lists
        if event.keyval == Gdk.KEY_1:
            if fpath.isfile("mychannels1.txt"):
                self.makeList(self.list_1)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_2:
            if fpath.isfile("mychannels2.txt"):
                self.makeList(self.list_2)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_3:
            if fpath.isfile("mychannels3.txt"):
                self.makeList(self.list_3)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_4:
            if fpath.isfile("mychannels4.txt"):
                self.makeList(self.list_4)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_5:
            if fpath.isfile("mychannels5.txt"):
                self.makeList(self.list_5)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_6:
            if fpath.isfile("mychannels6.txt"):
                self.makeList(self.list_6)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_7:
            if fpath.isfile("mychannels7.txt"):
                self.makeList(self.list_7)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_8:
            if fpath.isfile("mychannels8.txt"):
                self.makeList(self.list_8)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_9:
            if fpath.isfile("mychannels9.txt"):
                self.makeList(self.list_9)
                self.sidebar.show()
        if event.keyval == Gdk.KEY_0:
            if fpath.isfile("mychannels9.txt"):
                self.makeList(self.list_10)
                self.sidebar.show()
            # volume up
        if event.keyval == Gdk.KEY_plus:
            if self.mpv.volume < 205:
                self.mpv.volume += 5.0
                self.volume = self.mpv.volume
            print(f"Volume: {self.mpv.volume}")
            # volume down
        if event.keyval == Gdk.KEY_minus: 
            if self.mpv.volume >= 5:
                self.mpv.volume -= 5.0
                self.volume = self.mpv.volume
            print(f"Volume: {self.mpv.volume}")
            # toggle sidebar
        if event.keyval == Gdk.KEY_s:
            self.toggleSideBar()            
        if event.keyval == Gdk.KEY_f or \
             (self.fullscreen and event.keyval == Gdk.KEY_Escape):
            self.toggle_fullscreen()
            # next
        if self.is_playing:
            if event.keyval == Gdk.KEY_Up:
                child = self.channelbox.get_child_at_index(self.id + 1)
                self.channelbox.select_child(child)
                if self.sidebar.is_visible():
                    self.toggleSideBar()
                self.id += 1
                self.play_async(self.nameList[self.id], self.urlList[self.id])
                # previous
            if event.keyval == Gdk.KEY_Down:
                child = self.channelbox.get_child_at_index(self.id - 1)
                self.channelbox.select_child(child)
                if self.sidebar.is_visible():
                    self.toggleSideBar()
                self.id -= 1
                self.play_async(self.nameList[self.id], self.urlList[self.id]) 
            
    def toggle_fullscreen(self):
        self.fullscreen = (not self.fullscreen)
        if self.fullscreen:
            # Fullscreen
            self.win.fullscreen()
            self.sidebar.hide()
        else:
            # Normal
            self.win.unfullscreen()
            #self.sidebar.show()
            
    def toggleSideBar(self):
        if self.sidebar.is_visible():
            w = self.win.get_size()[0]
            h = self.win.get_size()[1]
            self.sidebar.hide()
            self.win.resize(h * 1.77, h)
        else:
            w = self.win.get_size()[0]
            h = self.win.get_size()[1]
            self.sidebar.show()
            self.win.resize(h * 2.2 , h)
            
            
    def btn_clicked(self, wdg, i):
        self.play_async(self.nameList[i], self.urlList[i])
        child = self.channelbox.get_child_at_index(i)
        self.channelbox.select_child(child)
        if self.sidebar.is_visible():
            self.toggleSideBar()
        self.id = i
        
    def on_mpv_player_realize(self, widget):
        self.reinit_mpv()

    def reinit_mpv(self):
        if self.mpv != None:
            self.mpv.stop()

        self.mpv = mpv.MPV(volume=str(self.volume), input_cursor=False, hwdec=False, 
                                input_default_bindings=False, border=False, 
                                input_vo_keyboard=False, osc=False, ontop=True, wid=str(self.mpv_player.get_window().get_xid()))

    def reinit_mpv_movies(self):
        if self.mpv != None:
            self.mpv.stop()

        self.mpv = mpv.MPV(volume=str(self.volume), input_cursor=True, hwdec=False, 
                                input_default_bindings=False, border=False, 
                                input_vo_keyboard=False, osc=True, ontop=True, wid=str(self.mpv_player.get_window().get_xid()))
                                
    def on_mpv_player_draw(self, widget, cr):
        cr.set_source_rgb(0.0, 0.0, 0.0)
        cr.paint()
        
    def async_function(func):
        def wrapper(*args, **kwargs):
            thread = threading.Thread(target=func, args=args, kwargs=kwargs)
            thread.daemon = True
            thread.start()
            return thread
        return wrapper
        
    @async_function
    def play_async(self, channelname, channelurl):
        ext = [".mkv", ".mp4", ".mpg", ".mpeg", ".flv", ".wmv"]
        url_ext = f'.{channelurl.rpartition(".")[2]}'
        print (f"Sender: {channelname}\nurl: {channelurl}")
        if channelname != None and channelurl != None:
            if url_ext in ext:
                self.reinit_mpv_movies()
            else:
                self.reinit_mpv()
            self.mpv.play(channelurl)
            self.mpv.wait_until_playing()
            self.is_playing = True
            self.mpv.show_text(channelname, duration="3000", level=None)
            
    def makeList(self, mlist):
        for child in self.channelbox.get_children():
            self.channelbox.remove(child)

        text = open(mlist, 'r').read()
        self.urlList = []
        self.nameList = []      
        for lines in text.splitlines():
            line = lines.split(",")
            self.nameList.append(line[0])
            self.urlList.append(line[1])
  
        i = 0
        for ch in self.nameList:
            btn = Gtk.Button(label = ch)
            btn.set_name(f"btn{str(i)}")
            btn.set_can_focus(True)
            btn.connect("clicked", self.btn_clicked, i)
            self.channelbox.add(btn)
            i += 1
        self.channelbox.show_all()
        
    def main(self, argv):
        self.list_1 = "mychannels1.txt"
        self.list_2 = "mychannels2.txt"
        self.list_3 = "mychannels3.txt"
        self.list_4 = "mychannels4.txt"
        self.list_5 = "mychannels5.txt"
        self.list_6 = "mychannels6.txt"
        self.list_7 = "mychannels7.txt"
        self.list_8 = "mychannels8.txt"
        self.list_9 = "mychannels9.txt"
        self.list_10 = "mychannels10.txt"
        self.urlList = []
        self.nameList = []
        self.volume = 90
        self.is_playing = False
        self.mpv = None
        self.fullscreen = False
        self.id = 0
        builder = Gtk.Builder()
        builder.add_from_file("myglade_mpv.glade")

        screen = Gdk.Screen.get_default()        
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path('mystyle.css')

        context = Gtk.StyleContext()
        context.add_provider_for_screen(screen, css_provider,
          Gtk.STYLE_PROVIDER_PRIORITY_USER)


        self.mpv_player = builder.get_object("mpv_player")
        self.win = builder.get_object("window")
        self.win.set_events (Gdk.EventMask.ALL_EVENTS_MASK)
        self.win.connect('key_press_event', self.on_key_press_event)
        self.sidebar = builder.get_object("sidebar")
        self.channelbox = builder.get_object("channels_flowbox")
        self.win.connect("destroy", Gtk.main_quit)
        self.win.connect('button_press_event', self.on_button_press_event)
        self.win.connect('scroll-event', self.my_zoom)
        
        self.mpv_player.connect("realize", self.on_mpv_player_realize)
        self.mpv_player.connect("draw", self.on_mpv_player_draw)
        
        self.win.set_title("TV Player")
        
        if fpath.isfile("mychannels1.txt"):
            self.makeList(self.list_1)
                
        self.win.set_keep_above(True)
        self.win.set_decorated(False)
        self.win.resize(640, 300)
        self.win.move(50, 50)
        self.win.show_all()
        Gtk.main() 


if __name__ == "__main__":
    w = MyWindow()
    w.main(sys.argv)
                            
