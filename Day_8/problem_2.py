def minus_string(string0, string1):
    string_out = str()
    for char in string0:
        if not char in string1: string_out += char
    return string_out

def plus_string(string0, string1):
    string_out = string0
    for char in string1:
        if not char in string0: string_out += char
    return string_out

def include(string0, string1):
    if all(char in string1 for char in string0): 
        return True
    return False

def get_key_by_value(dct, value):
    key_list = list(dct.keys())
    value_list = list(dct.values())
    index = value_list.index(value)
    return key_list[index]

def decrypt(sample):
    finsih_patterns = dict()
    while len(finsih_patterns) < 10:
        for segment in sample:
            segment = "".join(sorted(segment))
            if segment in finsih_patterns.values(): pass
            else:
                if segment in finsih_patterns.values(): pass
                elif len(segment) == 2: finsih_patterns[1] = segment
                elif len(segment) == 3: finsih_patterns[7] = segment
                elif len(segment) == 4: finsih_patterns[4] = segment
                elif len(segment) == 7: finsih_patterns[8] = segment

                if not all(keys in finsih_patterns for keys in(1, 7, 4, 8)): pass
                elif len(segment) == 5:
                    if include(finsih_patterns[1], segment): finsih_patterns[3] = segment
                    elif include(minus_string(finsih_patterns[4], finsih_patterns[1]), segment): finsih_patterns[5] = segment
                    else: finsih_patterns[2] = segment
                elif len(segment) == 6:
                    if not include(finsih_patterns[1], segment): finsih_patterns[6] = segment
                    elif include(finsih_patterns[4], segment): finsih_patterns[9] = segment
                    else: finsih_patterns[0] = segment
    return finsih_patterns

def crack_code(inp):
    output_sum = int()
    for display in inp:
        decode_sample, output = display.split(" | ")
        output = output.split(" ")
        decode_sample = decode_sample.split(" ")
        decoded = decrypt(decode_sample)
        segment_sum = str()
        for segment in output:
            segment_sum += str(get_key_by_value(decoded, "".join(sorted(segment))))
        output_sum += int(segment_sum)
    return output_sum
file_input = open(r"C:\Users\emild\OneDrive\Dokument\GitHub\Advent-of-Code-2021\Day_8\input.txt", "r+").read().split("\n")
print(crack_code(file_input))