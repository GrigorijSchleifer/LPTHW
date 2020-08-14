sequence = [90, 101, 100, 32, 65, 46, 32, 83, 104, 97, 119]
name = ''

def decode_name(sequence):
    for i in sequence:
        print(chr(i), end='')

decode_name(sequence)
