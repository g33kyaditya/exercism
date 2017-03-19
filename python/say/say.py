store = {}
store[0] = 'zero'
store[1] = 'one'
store[2] = 'two'
store[3] = 'three'
store[4] = 'four'
store[5] = 'five'
store[6] = 'six'
store[7] = 'seven'
store[8] = 'eight'
store[9] = 'nine'
store[10] = 'ten'
store[11] = 'eleven'
store[12] = 'twelve'
store[13] = 'thirteen'
store[14] = 'fourteen'
store[15] = 'fifteen'
store[16] = 'sixteen'
store[17] = 'seventeen'
store[18] = 'eighteen'
store[19] = 'nineteen'
store[20] = 'twenty'
store[30] = 'thirty'
store[40] = 'forty'
store[50] = 'fifty'
store[60] = 'sixty'
store[70] = 'seventy'
store[80] = 'eighty'
store[90] = 'ninety'
store[100] = 'hundred'
store[1000] = 'thousand'
store[1000000] = 'million'
store[1000000000] = 'billion'
store[1000000000000] = 'trillion'

def say(number):
    pass

def process(sequence):
    if int(sequence) in store.keys():
        if int(sequence) < 100:
            return store[int(sequence)]
        else:
            return 'one' + store[int(sequence)]
    if sequence == '000':
        return ''
'''
    top = ''
    if size == 1:
        top = 'hundred'
    elif size == 2:
        top = 'thousand'
    elif size == '3':
        top = 'million'
    elif size == '4':
        top = 'billion'
    elif size == '5':
        top = 'trillion'
'''
    if len(sequence) == 1:
        if store[int(sequence)] != 'zero'
            return store[int(sequence)] + top
        return ''
    elif len(sequence) == 2:
        num = int(sequence)/10
        num = num*10
        return store[int(num)] + '-' + store[int(sequence[1])]
    elif sequence == 3:
        start = store[int(sequence[0])] + 'hundred and'
        return start + process(sequence[1:])

