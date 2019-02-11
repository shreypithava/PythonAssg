import tkinter as tk


class Window:
    def __init__(self):
        self.__root = tk.Tk()  # the window
        self.__root.geometry('400x400')  # size of window
        self.__root.title('My Patient Program')
        self.__labels = list()  # put_label puts labels in this
        self.__labels.append(tk.Label(self.__root, text='Please load patient file'))
        self.__labels[0].grid(row=0, column=0, sticky='w')
        self.__put_label()
        self.__options()  # for menu
        self.__file = FileHandling()  # FileHandling for read write operations
        self.__data = self.__file.read()  # reads from file
        self.__newWin = None  # New patient window
        self.__modWin = None  # Modifying patient window

    def run(self):
        self.__root.mainloop()

    def __open(self):
        for i in range(len(self.__data)):
            self.__labels[i]['text'] = self.__data[i]  # puts data in text field of labels

    def __options(self):  # puts menu and all options in menu
        menu = tk.Menu(self.__root)
        filemenu = tk.Menu(menu, tearoff=0)
        helpmenu = tk.Menu(menu, tearoff=0)
        filemenu.add_command(label='Open', command=self.__open)
        filemenu.add_command(label='New', command=self.__new)
        filemenu.add_command(label='Modify', command=self.__modify)
        filemenu.add_command(label='Save', command=self.__save)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=self.__root.destroy)
        menu.add_cascade(label='File', menu=filemenu)
        menu.add_cascade(label='Help', menu=helpmenu)
        self.__root.config(menu=menu)

    def __put_label(self):  # puts labels for data
        for i in range(20):
            self.__labels.append(tk.Label(self.__root))
            self.__labels[i].grid(row=i + 1, column=0, sticky='w')

    def __new(self):  # open new Patient Window
        self.__newWin = New()

    def __save(self):  # truly saves the data
        if self.__newWin:
            if self.__newWin.save():
                self.__data.append(self.__newWin.save())
                self.__file.write(self.__data)
                self.__newWin = None
        elif self.__modWin:
            if self.__modWin.save():
                self.__data.pop(self.__modWin.save()[1])
                self.__data.append(self.__modWin.save()[0])
                self.__file.write(self.__data)
                self.__modWin = None

    def __modify(self):  # Calls Modify Patient window
        self.__modWin = Modify(self.__data)  # passes whole data


class FileHandling:
    def __init__(self, filename='data.txt'):  # filename by default is my text file
        self.__filename = filename
        self.__data = list()
        for data in open(self.__filename).readlines():
            self.__data.append(data.rstrip().split())  # removes \n and splits by space

    def read(self):
        return self.__data  # returns data read from the txt file

    def write(self, data):  # writes to file
        with open(self.__filename, 'w') as file:
            for record in data:
                for item_no in range(len(record)):
                    print(record[item_no], file=file, end='')
                    if item_no + 1 == len(record):
                        print('\n', end='', file=file)
                    else:
                        print(' ', end='', file=file)


class New:  # new patient window
    def __init__(self):
        self.__root = tk.Tk()
        self.__root.geometry('400x400')
        self.__root.title('New Patient')
        self.__content = list()
        self.__data = None
        self.__labels()

    def __labels(self):  # puts content on the window(labels and entry fields)
        self.__content.append(tk.Label(self.__root, text='First and LastName:'))
        self.__content[0].grid(row=0, column=0, sticky='e')
        self.__content.append(tk.Entry(self.__root))
        self.__content[1].grid(row=0, column=1, sticky='w')
        self.__content.append(tk.Label(self.__root, text='Address:'))
        self.__content[2].grid(row=1, column=0, sticky='e')
        self.__content.append(tk.Entry(self.__root))
        self.__content[3].grid(row=1, column=1, sticky='w')
        self.__content.append(tk.Label(self.__root, text='Birthday (mm/dd/yy)'))
        self.__content[4].grid(row=2, column=0, sticky='e')
        self.__content.append(tk.Entry(self.__root))
        self.__content[5].grid(row=2, column=1, sticky='w')
        self.__content.append(tk.Button(self.__root, text='Save', command=self.__get))
        self.__content[6].grid(row=4, column=0, sticky='se')
        self.__content.append(tk.Button(self.__root, text='Close', command=self.__root.destroy))
        self.__content[7].grid(row=4, column=1, sticky='sw')

    def __get(self):  # gets data from entry fields
        self.__data = [self.__content[1].get(), self.__content[3].get(), self.__content[5].get()]
        self.__root.destroy()

    def save(self):
        return self.__data


class Modify:  # creates modify window
    def __init__(self, data):
        self.__root = tk.Tk()
        self.__root.geometry('400x400')
        self.__root.title('Modify Patient')
        self.__data = data
        self.__modata = None  # changed data
        self.__content = list()
        self.__counter = 0
        self.__labels()

    def __labels(self):
        self.__content.append(tk.Label(self.__root, text='First and LastName:'))
        self.__content[0].grid(row=0, column=0, sticky='e')
        self.__content.append(tk.Entry(self.__root))
        self.__content[1].grid(row=0, column=1, sticky='w')
        self.__content[1].insert('0', self.__data[0][0])
        self.__content.append(tk.Label(self.__root, text='Address:'))
        self.__content[2].grid(row=1, column=0, sticky='e')
        self.__content.append(tk.Entry(self.__root))
        self.__content[3].grid(row=1, column=1, sticky='w')
        self.__content[3].insert('0', self.__data[0][1])
        self.__content.append(tk.Label(self.__root, text='Birthday (mm/dd/yy)'))
        self.__content[4].grid(row=2, column=0, sticky='e')
        self.__content.append(tk.Entry(self.__root))
        self.__content[5].grid(row=2, column=1, sticky='w')
        self.__content[5].insert('0', self.__data[0][2])
        self.__content.append(
            tk.Button(self.__root, text='Previous', command=lambda: self.__change(-1)))  # -1 for previous, see __change
        self.__content[6].grid(row=3, column=0, sticky='e')
        self.__content.append(
            tk.Button(self.__root, text='Next', command=lambda: self.__change(1)))  # 1 for next, see __change
        self.__content[7].grid(row=3, column=1, sticky='w')
        self.__content.append(tk.Button(self.__root, text='Save', command=self.__modget))
        self.__content[8].grid(row=4, column=0, sticky='se')
        self.__content.append(tk.Button(self.__root, text='Close', command=self.__root.destroy))
        self.__content[9].grid(row=4, column=1, sticky='sw')

    def __change(self, num):  # for previous and next buttons in modify patient
        if -1 < self.__counter + num < len(self.__data):
            self.__counter += num
            for i in range(3):
                self.__content[i * 2 + 1].delete('0', tk.END)
                self.__content[i * 2 + 1].insert('0', self.__data[self.__counter][i])

    def __modget(self):
        self.__modata = [self.__content[1].get(), self.__content[3].get(), self.__content[
            5].get()], self.__counter  # returns changed data of patient as list and position
        self.__root.destroy()

    def save(self):
        return self.__modata


gui = Window()  # instance of Window
gui.run()  # calls mainloop
