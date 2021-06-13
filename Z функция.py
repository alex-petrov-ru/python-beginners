def z_func(s):
    s += '$'
    l, r = 0, 0
    z = [0] * len(s)
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - l], r - i))
        while s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i +z[i]
    return z[:-1]

print(z_func("abcdabscabcdabia"))


def zfun(s):
    z = []
    if not s: return z
    i, slen = 1, len(s)
    z.append(slen)
    while i < slen:
        left, right = 0, i
        while right < slen and s[left] == s[right]:
            left += 1
            right += 1
        z.append(left)
        i += 1
    return z

print(zfun("abcdabscabcdabia"))