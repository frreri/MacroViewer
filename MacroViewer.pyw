import os
import sqlite3
import tkinter as tk
import tkinter.messagebox
from os.path import expanduser
from tkinter import simpledialog, ttk

from SetIcon import iconData

home = expanduser("~\\Documents\\MacroViewer")
try:
    os.mkdir(home)
except:
    pass

conn = sqlite3.connect(home+'\\'+'config.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE settings
        (option, value)''')
    c.execute("INSERT INTO settings VALUES ('path','default')")
    conn.commit()
except:
    pass
conn.close()

class MacroObject(object):
    def __init__(self, name, realm, account, path):
        self.account = account
        self.realm = realm
        self.name = name
        self.path = path
        self.macroName = []
        self.macroText = []

def pathfind():
    drives = ['c','d','e','f','g','h','i','j']
    paths = [':\\program files (x86)', ':\\program files', ':\\spel', ':\\games', ':\\']
    for drive in drives:
        for path in paths:
            try:
                templist = [x.lower() for x in os.listdir(drive+path)]
                #World of Warcraft is a registered trademark of Blizzard Entertainment, Inc.
                #The creator of this application is in no way affiliated with or endorsed by Blizzard Entertainment, Inc.
                for dir_name in ['world of warcraft', 'wow']:
                    if dir_name in templist:
                        if os.path.exists(drive+path+'\\'+dir_name+'\\_retail_'):
                            path = drive+path+'\\'+dir_name+'\\_retail_'
                            conn= sqlite3.connect(home+'\\'+'config.db')
                            c = conn.cursor()
                            c.execute("UPDATE settings SET value = '{}' WHERE option = 'path'".format(path))
                            conn.commit()
                            conn.close()
                            return path
            except:
                pass
    answer=''
    while answer == '':
        answer = simpledialog.askstring("MacroViewer", "       Please enter the game directory:       ", parent=master)
    if answer == None:
        return answer
    conn= sqlite3.connect(home+'\\'+'config.db')
    c = conn.cursor()
    c.execute("UPDATE settings SET value = '{}' WHERE option = 'path'".format(answer))
    conn.commit()
    conn.close()
    return answer

def setPath():
    conn= sqlite3.connect(home+'\\'+'config.db')
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE option = 'path'")
    old_path = c.fetchall()[0][0]
    new_path = simpledialog.askstring("MacroViewer", "     Please enter the game directory path:     ", initialvalue=old_path ,parent=master)
    if new_path != None:
        c.execute("UPDATE settings SET value = '{}' WHERE option = 'path'".format(new_path.lower()))
        conn.commit()
    conn.close()

macro_canvas = {}
macro_frames = {}
macro_objects = {}
account_tab_control = {}
account_realm_tab_control = {}
tabControl = {}

def findMacros():
    path_list = []
    global macro_objects
    macro_objects = []
    accounts = []
    account_tabs = {}
    global account_tab_control
    account_tab_control = {}
    account_realms = {}
    account_realm_tabs = {}
    global account_realm_tab_control
    account_realm_tab_control = {}
    account_realm_character = {}
    account_realm_character_tabs = {}
    macro_canvas_frames = {}
    global macro_canvas
    macro_canvas = {}
    macro_scrollbars = {}
    global macro_frames
    macro_frames = {}
    macro_texts = {}
    conn= sqlite3.connect(home+'\\'+'config.db')
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE option = 'path'")
    saved_path = c.fetchall()[0][0]
    conn.close()
    if saved_path == 'default':
        macro_path = pathfind()
    else:
        macro_path = saved_path
    if macro_path == None:
        return None
    for root, dirs, files in os.walk(macro_path):
        for file in files:
            if file == 'macros-cache.txt':
                path_list.append(os.path.join(root, file))
    for path in path_list:
        split_path = path.split('\\')
        file_index = len(split_path) - 1
        if split_path[file_index-2] == 'Account':
            macro_objects.append(MacroObject('Global','Global', split_path[file_index-1], path))
        else:
            macro_objects.append(MacroObject(split_path[file_index-1], split_path[file_index-2], split_path[file_index-3], path))
    global tabControl
    tabControl.update({ "tab_control" : ttk.Notebook(master)})
    tabControl["tab_control"].grid(row=0,column=0)
    for objects in macro_objects:
        data = ""
        with open(objects.path, "r", encoding='utf8') as macro:
            for line in macro.readlines():
                if line.startswith("VER"):
                    objects.macroName.append(line.split('"')[1])
                else:
                    data = data + line
            objects.macroText = data.split("END")
    for objects in macro_objects:
        if objects.account not in accounts:
            account_tabs.update({ objects.account : ttk.Frame(tabControl["tab_control"])})
            tabControl["tab_control"].add(account_tabs[objects.account], text=objects.account)
            account_tab_control.update({ objects.account : ttk.Notebook(account_tabs[objects.account])})
            account_tab_control[objects.account].pack()
            accounts.append(objects.account)
        for item in macro_objects:
            if item.account == objects.account:
                try:
                    if item.realm not in account_realms[item.account]:
                        account_realms.setdefault(item.account, []).append(item.realm)
                        account_realm_tabs.update({item.account+item.realm : ttk.Frame(account_tab_control[item.account])})
                        account_tab_control[item.account].add(account_realm_tabs[item.account+item.realm], text=item.realm)
                        if not item.realm == 'Global':
                            account_realm_tab_control.update({item.account+item.realm : ttk.Notebook(account_realm_tabs[item.account+item.realm])})
                            account_realm_tab_control[item.account+item.realm].grid(row=0,column=0)
                        else:
                            if item.account + item.name not in macro_frames:
                                macro_canvas_frames.update({item.account+item.realm+item.name :tk.Frame(account_realm_tabs[item.account+item.realm],
                                relief=tk.GROOVE,width=500,height=400,bd=1)})
                                macro_canvas_frames[item.account+item.realm+item.name].grid(row=0, column=0)
                                macro_canvas.update({item.account+item.realm+item.name : tk.Canvas(macro_canvas_frames[item.account+item.realm+item.name], highlightthickness=0)})
                                macro_frames.update({item.account+item.realm+item.name : tk.Frame(macro_canvas[item.account+item.realm+item.name])})
                                macro_scrollbars.update({item.account+item.realm+item.name : tk.Scrollbar(macro_canvas_frames[item.account+item.realm+item.name],
                                    orient="vertical",command=macro_canvas[item.account+item.realm+item.name].yview)})
                                macro_canvas[item.account+item.realm+item.name].configure(yscrollcommand=macro_scrollbars[item.account+item.realm+item.name].set)
                                macro_scrollbars[item.account+item.realm+item.name].pack(side="right",fill="y")
                                macro_canvas[item.account+item.realm+item.name].pack(side="left")
                                macro_canvas[item.account+item.realm+item.name].create_window((0,0),window=macro_frames[item.account+item.realm+item.name],anchor="nw")
                                for idx, global_macro in enumerate(item.macroName):
                                    if idx % 2 == 0:
                                        grid_col = 0
                                        grid_row = idx
                                    else:
                                        grid_col = 1
                                        grid_row = idx-1
                                    tk.Label(macro_frames[item.account+item.realm+item.name], text=global_macro, font="none 8 bold").grid(
                                        row = grid_row, column=grid_col,sticky=tk.W, padx=5)
                                    macro_texts.update({item.account+item.realm+item.name+global_macro : tk.Text(macro_frames[item.account+item.realm+item.name],
                                        height=6, width=55, relief=tk.GROOVE,bd=2,wrap="word")})
                                    if item.macroText[idx].startswith('\n'):
                                        macro_texts[item.account+item.realm+item.name+global_macro].insert(tk.INSERT, item.macroText[idx][1:])
                                    else:
                                        macro_texts[item.account+item.realm+item.name+global_macro].insert(tk.INSERT, item.macroText[idx])
                                    macro_texts[item.account+item.realm+item.name+global_macro].grid(row = grid_row+1, column=grid_col, padx=5)
                except:
                    account_realms.setdefault(item.account, []).append(item.realm)
                    account_realm_tabs.update({item.account+item.realm : ttk.Frame(account_tab_control[item.account])})
                    account_tab_control[item.account].add(account_realm_tabs[item.account+item.realm], text=item.realm)
                    if not item.realm == 'Global':
                        account_realm_tab_control.update({item.account+item.realm : ttk.Notebook(account_realm_tabs[item.account+item.realm])})
                        account_realm_tab_control[item.account+item.realm].grid(row=0,column=0)
                    else:
                        if item.account + item.name not in macro_frames:
                            macro_canvas_frames.update({item.account+item.realm+item.name :tk.Frame(account_realm_tabs[item.account+item.realm],
                            relief=tk.GROOVE,width=500,height=400,bd=1)})
                            macro_canvas_frames[item.account+item.realm+item.name].grid(row=0, column=0)
                            macro_canvas.update({item.account+item.realm+item.name : tk.Canvas(macro_canvas_frames[item.account+item.realm+item.name], highlightthickness=0)})
                            macro_frames.update({item.account+item.realm+item.name : tk.Frame(macro_canvas[item.account+item.realm+item.name])})
                            macro_scrollbars.update({item.account+item.realm+item.name : tk.Scrollbar(macro_canvas_frames[item.account+item.realm+item.name],
                                orient="vertical",command=macro_canvas[item.account+item.realm+item.name].yview)})
                            macro_canvas[item.account+item.realm+item.name].configure(yscrollcommand=macro_scrollbars[item.account+item.realm+item.name].set)
                            macro_scrollbars[item.account+item.realm+item.name].pack(side="right",fill="y")
                            macro_canvas[item.account+item.realm+item.name].pack(side="left")
                            macro_canvas[item.account+item.realm+item.name].create_window((0,0),window=macro_frames[item.account+item.realm+item.name],anchor="nw")
                            for idx, global_macro in enumerate(item.macroName):
                                if idx % 2 == 0:
                                    grid_col = 0
                                    grid_row = idx
                                else:
                                    grid_col = 1
                                    grid_row = idx-1
                                tk.Label(macro_frames[item.account+item.realm+item.name], text=global_macro, font="none 8 bold").grid(
                                    row = grid_row, column=grid_col,sticky=tk.W, padx=5)
                                macro_texts.update({item.account+item.realm+item.name+global_macro : tk.Text(macro_frames[item.account+item.realm+item.name],
                                    height=6, width=55, relief=tk.GROOVE,bd=2,wrap="word")})
                                if item.macroText[idx].startswith('\n'):
                                    macro_texts[item.account+item.realm+item.name+global_macro].insert(tk.INSERT, item.macroText[idx][1:])
                                else:
                                    macro_texts[item.account+item.realm+item.name+global_macro].insert(tk.INSERT, item.macroText[idx])
                                macro_texts[item.account+item.realm+item.name+global_macro].grid(row = grid_row+1, column=grid_col, padx=5)
            if item.account == objects.account and item.realm == objects.realm and not item.name == 'Global':
                try:
                    if item.name not in account_realm_character[item.account+item.realm]:
                        account_realm_character.setdefault(item.account+item.realm, []).append(item.name)
                        account_realm_character_tabs.update({item.account+item.realm+item.name : ttk.Frame(account_realm_tab_control[item.account+item.realm])})
                        account_realm_tab_control[item.account+item.realm].add(account_realm_character_tabs[item.account+item.realm+item.name], text=item.name)
                        if item.realm + item.name not in macro_frames:
                            macro_canvas_frames.update({item.account+item.realm+item.name :tk.Frame(account_realm_character_tabs[item.account+item.realm+item.name],
                            relief=tk.GROOVE,width=500,height=400,bd=1)})
                            macro_canvas_frames[item.account+item.realm+item.name].grid(row=0, column=0)
                            macro_canvas.update({item.account+item.realm+item.name : tk.Canvas(macro_canvas_frames[item.account+item.realm+item.name], highlightthickness=0)})
                            macro_frames.update({item.account+item.realm+item.name : tk.Frame(macro_canvas[item.account+item.realm+item.name])})
                            macro_scrollbars.update({item.account+item.realm+item.name : tk.Scrollbar(macro_canvas_frames[item.account+item.realm+item.name],
                                orient="vertical",command=macro_canvas[item.account+item.realm+item.name].yview)})
                            macro_canvas[item.account+item.realm+item.name].configure(yscrollcommand=macro_scrollbars[item.account+item.realm+item.name].set)
                            macro_scrollbars[item.account+item.realm+item.name].pack(side="right",fill="y")
                            macro_canvas[item.account+item.realm+item.name].pack(side="left")
                            macro_canvas[item.account+item.realm+item.name].create_window((0,0),window=macro_frames[item.account+item.realm+item.name],anchor="nw")
                            for idx, char_macro in enumerate(item.macroName):
                                if idx % 2 == 0:
                                    grid_col = 0
                                    grid_row = idx
                                else:
                                    grid_col = 1
                                    grid_row = idx-1
                                tk.Label(macro_frames[item.account+item.realm+item.name], text=char_macro, font="none 8 bold").grid(
                                    row = grid_row, column=grid_col,sticky=tk.W, padx=5)
                                macro_texts.update({item.account+item.realm+item.name+char_macro : tk.Text(macro_frames[item.account+item.realm+item.name],
                                    height=6, width=55, relief=tk.GROOVE,bd=2,wrap="word")})
                                if item.macroText[idx].startswith('\n'):
                                    macro_texts[item.account+item.realm+item.name+char_macro].insert(tk.INSERT, item.macroText[idx][1:])
                                else:
                                    macro_texts[item.account+item.realm+item.name+char_macro].insert(tk.INSERT, item.macroText[idx])
                                macro_texts[item.account+item.realm+item.name+char_macro].grid(row = grid_row+1, column=grid_col, padx=5)
                except:
                    account_realm_character.setdefault(item.account+item.realm, []).append(item.name)
                    account_realm_character_tabs.update({item.account+item.realm+item.name : ttk.Frame(account_realm_tab_control[item.account+item.realm])})
                    account_realm_tab_control[item.account+item.realm].add(account_realm_character_tabs[item.account+item.realm+item.name], text=item.name)
                    if item.realm + item.name not in macro_frames:
                        macro_canvas_frames.update({item.account+item.realm+item.name :tk.Frame(account_realm_character_tabs[item.account+item.realm+item.name],
                            relief=tk.GROOVE,width=500,height=400,bd=1)})
                        macro_canvas_frames[item.account+item.realm+item.name].grid(row=0, column=0)
                        macro_canvas.update({item.account+item.realm+item.name : tk.Canvas(macro_canvas_frames[item.account+item.realm+item.name], highlightthickness=0)})
                        macro_frames.update({item.account+item.realm+item.name : tk.Frame(macro_canvas[item.account+item.realm+item.name])})
                        macro_scrollbars.update({item.account+item.realm+item.name : tk.Scrollbar(macro_canvas_frames[item.account+item.realm+item.name],
                            orient="vertical",command=macro_canvas[item.account+item.realm+item.name].yview)})
                        macro_canvas[item.account+item.realm+item.name].configure(yscrollcommand=macro_scrollbars[item.account+item.realm+item.name].set)
                        macro_scrollbars[item.account+item.realm+item.name].pack(side="right",fill="y")
                        macro_canvas[item.account+item.realm+item.name].pack(side="left")
                        macro_canvas[item.account+item.realm+item.name].create_window((0,0),window=macro_frames[item.account+item.realm+item.name],anchor="nw")                      
                        for idx, char_macro in enumerate(item.macroName):
                            if idx % 2 == 0:
                                grid_col = 0
                                grid_row = idx
                            else:
                                grid_col = 1
                                grid_row = idx-1
                            tk.Label(macro_frames[item.account+item.realm+item.name], text=char_macro, font="none 8 bold").grid(
                                row = grid_row, column=grid_col,sticky=tk.W, padx=5)
                            macro_texts.update({item.account+item.realm+item.name+char_macro : tk.Text(macro_frames[item.account+item.realm+item.name],
                                height=6, width=55, relief=tk.GROOVE,bd=2,wrap="word")})
                            if item.macroText[idx].startswith('\n'):
                                macro_texts[item.account+item.realm+item.name+char_macro].insert(tk.INSERT, item.macroText[idx][1:])
                            else:
                                macro_texts[item.account+item.realm+item.name+char_macro].insert(tk.INSERT, item.macroText[idx])
                            macro_texts[item.account+item.realm+item.name+char_macro].grid(row = grid_row+1, column=grid_col, padx=5)    
    runCanv()
    resetScroll()

def runCanv():
    for key, val in macro_frames.items():
        val.bind("<Configure>", confCanvas)

def resetScroll():
    for x, z in account_realm_tab_control.items():
        z.bind('<Button-1>', tab_click)
    for n, m in account_tab_control.items():
        m.bind('<Button-1>', tab_click)
    tabControl["tab_control"].bind('<Button-1>', tab_click)

def confCanvas(event):
    for key, val in macro_canvas.items():
        val.configure(scrollregion=val.bbox("all"),width=910,height=490)

def showInfo():
    tkinter.messagebox.showinfo('About',
        """This is an application for viewing World of Warcraft macros from cached textfiles in the game folder.
        \nWorld of Warcraft is a registered trademark of Blizzard Entertainment, Inc.
        \nThe creator of this application is in no way affiliated with or endorsed by Blizzard Entertainment, Inc.
        \n\nVersion 1.1\n\nCopyright 2019 Fredrik Eriksson""")

def _on_mousewheel(event):
    for macro_item in macro_objects:
        if len(macro_item.macroText) > 8:
            try:
                macro_canvas[macro_item.account+macro_item.realm+macro_item.name].yview_scroll(int(-1*(event.delta/120)), "units")
            except:
                print('error')
                pass

def tab_click(event):
    for macro_item in macro_objects:
        if len(macro_item.macroText) > 8:
            try:
                macro_canvas[macro_item.account+macro_item.realm+macro_item.name].yview_moveto(0)
            except:
                print('error')
                pass

master = tk.Tk()
master.title('MacroViewer')
master.geometry('940x590')
master.option_add('*tearOff', False)
master.resizable(False, False)
icondata = iconData()
tempFile = "icon.ico"
with open(tempFile, "wb") as iconfile:
    iconfile.write(icondata)
master.wm_iconbitmap(tempFile)
os.remove(tempFile)
menyn = tk.Menu(master)
master.config(menu=menyn)
subMeny1 = tk.Menu(menyn)
menyn.add_cascade(label="Start", menu=subMeny1)
subMeny1.add_command(label="Load macros", command=findMacros)
subMeny1.add_command(label="Exit", command=master.destroy)
subMeny2 = tk.Menu(menyn)
menyn.add_cascade(label="Edit", menu=subMeny2)
subMeny2.add_command(label="Set path", command=setPath)
subMeny3 = tk.Menu(menyn)
menyn.add_cascade(label="Info", menu=subMeny3)
subMeny3.add_command(label="About", command=showInfo)
master.bind_all("<MouseWheel>", _on_mousewheel)
master.mainloop()
