#coding: utf-8


def justify(text, width):
    # your code here
    print(text, width)
    output = ''
    stext = str.split(text)
    sline = []
    s = ' '
    while stext:
        tmp = stext.pop(0)
        print('------------'+tmp)
        sline.append(tmp)
        if s.join(sline).__len__() < width:
            print('less: ' + s.join(sline))
            continue

        if s.join(sline).__len__() == width:
            print('good: ' + s.join(sline))
            output += s.join(sline)
            output += '\n'
            sline = []
            s = ' '
            continue

        print('more: ' + s.join(sline))
        while s.join(sline).__len__() > width:
            tmp = sline.pop()
            stext.insert(0, tmp)

        print('sink: ' + s.join(sline))
        if len(sline) == 1:
            print('good: ' + sline[0])
            output += ' '*(width-len(sline[0])) + sline[0]
            output += '\n'
            sline = []
            s = ' '
            continue

        n = sline.__len__()
        r = width - ''.join(sline).__len__()
        c = r // (n-1)
        f = r % (n-1)
        gs = ''
        for j in range(n-1):
            gs += sline[j]
            if j < f:
                gs += ' ' * (c+1)
            else:
                gs += ' ' * c
        gs += sline[-1]
        print('good: ' + gs + ' |%d' % gs.__len__())
        output += gs
        output += '\n'
        sline = []
        s = ' '

    if sline:
        output += ' '.join(sline)
    if output[-1] == '\n':
        return output[0:-1]
    return output


s = justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor.', 15)

ss = s.split('\n')
for e in ss:
    print(e, len(e))
