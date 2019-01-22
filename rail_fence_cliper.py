# code: utf-8


def encode_rail_fence_cipher(string, n):
    rails = ['' for _ in range(n)]
    j = 0
    k = 1
    for s in string:
        rails[j] += s
        j += k
        if j == n-1:
            k = -1
        if j == 0:
            k = 1
    return ''.join(rails)


def decode_rail_fence_cipher(string, n):
    print(string, n)
    rails_num = [[] for _ in range(n)]
    j = 0
    k = 1
    for a in range(len(string)):
        rails_num[j].append(a)
        j += k
        if j == n-1:
            k = -1
        if j == 0:
            k = 1
    rails_n = []
    for e in rails_num:
        rails_n += e
    print(rails_n)
    out = ''.join(string[rails_n.index(e)] for e in range(len(string)))
    print(out)
    return out


encode_rail_fence_cipher("Hello, World!", 4)
print("Hoo!el,Wrdl l")

decode_rail_fence_cipher("H !e,Wdloollr", 4)
print("Hello, World!")
