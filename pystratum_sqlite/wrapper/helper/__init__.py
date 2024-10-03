def strtr(strng, replace):
    buf, i = [], 0
    while i < len(strng):
        for s, r in replace.items():
            if strng[i:len(s) + i] == s:
                buf.append(r)
                i += len(s)
                break
        else:
            buf.append(strng[i])
            i += 1
    return ''.join(buf)
