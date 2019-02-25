class Calculator:
    def evaluate(self, string):
        mylist = []
        ss = string.split(' ')
        ss.reverse()
        while ss:
            e = ss.pop()
            if e in ['/', '*']:
                a = int(mylist.pop())
                b = ss.pop()
                if e == '/':
                    mylist.append(int(a) / int(b))
                else:
                    mylist.append(int(a) * int(b))
            else:
                mylist.append(e)
        print(mylist)
        mylist.reverse()

        while mylist:
            e = mylist.pop()
            if e in ['+', '-']:
                a = int(ss.pop())
                b = mylist.pop()
                if e == '+':
                    ss.append(int(a) + int(b))
                else:
                    ss.append(int(a) - int(b))
            else:
                ss.append(e)
        print(ss)
        return ss[0]
        return 0


cal = Calculator()


cal.evaluate("2 / 2 + 3 * 4 - 6")
