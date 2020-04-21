from tkinter import * 
from tkinter import ttk, scrolledtext, Menu, filedialog

save_commands = ['Save', 'save', 's', 'S']
open_commands = ['Open', 'open', 'o', 'O']
clear_commands = ['Clear', 'clear', 'cl', 'Cl', 'New', 'new', 'n', 'N']

black_commands = ['Black', 'black', 'b']
white_commands = ['White', 'white', 'w']
sky_commands = ['Sky', 'sky', 'sk']

def save_file(event):
	try:
		files = filedialog.asksaveasfile(mode = 'w')
		data = write.get('1.0', END)
		files.write(data)
	except AttributeError:
		pass

def open_file(event):
	try:
		global new_item
		files = filedialog.askopenfile(mode = 'r')
		data = files.read()
		write.delete('1.0', END)
		write.insert('1.0', data)
	except (UnicodeDecodeError, AttributeError):
		pass

def new_file(event):
	global new_item
	write.delete('1.0', END)

def black(event):
	app.config(bg = 'black')
	write.config(bg = 'black', fg = 'white', highlightbackground = 'black', insertbackground = 'white')
	comm_line.config(bg = 'black', fg = 'white', highlightbackground = 'black', insertbackground = 'white')
	gen_button.config(bg = 'black', fg = 'white', highlightbackground = 'black')

def white(event):
	app.config(bg = 'white')
	write.config(bg = 'white', fg = 'black', highlightbackground = 'white', insertbackground = 'black')
	comm_line.config(bg = 'white', fg = 'black', highlightbackground = 'white', insertbackground = 'black')
	gen_button.config(bg = 'white', fg = 'black', highlightbackground = 'white')

def sky(event):
	app.config(bg = '#2a2d4a')
	write.config(bg = '#2a2d4a', fg = 'white', highlightbackground = '#2a2d4a', insertbackground = 'white')
	comm_line.config(bg = '#2a2d4a', fg = 'white', highlightbackground = '#2a2d4a', insertbackground = 'white')
	gen_button.config(bg = '#2a2d4a', fg = 'white', highlightbackground = '#2a2d4a')

def global_func():
	comm = comm_line.get()
	if comm in save_commands:
		save_file()
	elif comm  in open_commands:
		open_file()
	elif comm in clear_commands:
		new_file()
	elif comm in black_commands:
		black()
	elif comm in white_commands:
		white()
	elif comm in sky_commands:
		sky()
	elif int(comm) > 9 and int(comm) < 18:
		write.config(font = ('Sans', int(comm)))

app = Tk()
app.title('Light Write')
app.config(bg = 'white')
app.minsize(width = '660', height = '500')
app.maxsize(height = '800')

app.bind('<Control-s>', save_file)
app.bind('<Control-o>', open_file)
app.bind('<Control-n>', new_file)
app.bind('<Control-b>', black)
app.bind('<Control-k>', sky)
app.bind('<Control-w>', white)

write = Text(app, bg = 'white', bd = 1)
write.pack(expand = True, fill = BOTH)
write.focus()

comm_line = Entry(app, bg = 'white', bd = 1)
comm_line.config(width = 70)
comm_line.pack(side = LEFT, fill = BOTH, expand = True)

gen_button = Button(app, text = 'Do', bg = 'white', bd = 1, command = global_func)
gen_button.pack(fill = BOTH, expand = True, side = RIGHT)

app.mainloop()
