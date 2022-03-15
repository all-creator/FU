def calc_part_key(key_publ_m, key_prim, key_publ_s):
    key_part_m = key_publ_m ** key_prim % key_publ_s
    return key_part_m


def calc_full_key(key_part_s, key_prim, key_publ_s):
    key_full = key_part_s ** key_prim % key_publ_s
    return key_full


def coding(st, key):
    s = list(st)
    for i in range(len(s)):
        j = ord(s[i])
        j += key
        j = chr(j)
        s[i] = j
    return ''.join(s)


def decoding(st, key):
    s = list(st)
    for i in range(len(s)):
        j = ord(s[i])
        j -= key
        j = chr(j)
        s[i] = j
    return ''.join(s)
