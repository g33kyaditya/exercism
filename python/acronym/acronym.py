def abbreviate(something):
    something = something.replace('-', ' ')
    stuff = something.split()
    jargon = ''
    for s in stuff:
        flag = False
        for char in s:
            if char.isupper():
                jargon += char
                flag = True
        if not flag:
            jargon += s[0]
    if jargon[1:3] == jargon[-2:]:
        jargon = jargon[:3]
    return jargon.upper()
