class myNumberList:
    def __init__(self, *args):
        self.__list = []
        if args:
            for item in args:
                self.add(item)

    def getList(self):
        return self.__list

    def add(self, value):
        if type(value) == int or type(value) == float:
            self.__list.append(value)
        else:
            print("Not a float or int value")
        # print(self.getList())

    def remove(self, value):
        while value in self.__list:
            for i in range(len(self.__list)):
                if value == self.__list[i]:
                    self.__list.pop(i)
                    break

    def head(self):
        return self.__list[0]

    def __repr__(self):
        # print('[', end='')
        # for i in range(len(self.__list)):
        #     if len(self.__list) - 1 == i:
        #         print('{}]'.format(self.__list[i]), end='')
        #     else:
        #         print('{}, '.format(self.__list[i]), end='')
        # print(self.getList(), end='')
        return str(self.getList())


class myRevOrderedNumberList(myNumberList):
    # def __init__(self, *args):
    #     myNumberList.__init__(self, *args)

    def head(self):
        return self.getList()[0]

    def getList(self):
        return sorted(myNumberList.getList(self), reverse=True)

    def __repr__(self):
        # print('[', end='')
        # temp = sorted(self.getList(), reverse=True)
        # for i in range(len(temp)):
        #     if len(temp) - 1 == i:
        #         print('{}]'.format(temp[i]), end='')
        #     else:
        #         print('{}, '.format(temp[i]), end='')
        print(self.getList(), end='')
        return ''


myL = myNumberList(2, 'f')
myL.add(15)
myL.add(20)
myL.add(1)
print(myL.head())  # 15
print(myL)  # [15,20,1]
myL.add("5")  # Only numbers can be added.
print(myL)  # [15,20,1]
myL.add(15)
print(myL)  # [15,20,1,15]
myL.remove(15)
print(myL)

myL2 = myRevOrderedNumberList()
myL2.add(15)
myL2.add(20)
myL2.add(1)
myL.add("hello")  # Only numbers can be added.
print(myL2)  # [20, 15, 1]
print(myL2.head())  # 20
print(myL2.getList())
