# code: utf-8


def next_bigger(n):
    # parse every digit in n into char list
    n_list = [e for e in str(n)]
    print(n_list)

    # from end to head, find possible tail
    for j in range(len(n_list)-1, -1, -1):
        if not n_list[j] == max(n_list[j:]):
            fix_part = n_list[:j]
            tail_part = n_list[j:]
            print(fix_part, tail_part)
            break
        # if no tail found, means no next_bigger
        if j == 0:
            return -1

    old_tail_head = tail_part[0]
    sorted_tail_part = sorted(tail_part)
    new_tail_head = sorted([e for e in tail_part if e > old_tail_head])[0]
    sorted_tail_part.remove(new_tail_head)
    new_n_list = fix_part + [new_tail_head] + sorted_tail_part
    return int(''.join(new_n_list))

    return n


num = 1234567890  # 1234567908
num = 59884848459853  # 59884848483559
next_bigger(num)
