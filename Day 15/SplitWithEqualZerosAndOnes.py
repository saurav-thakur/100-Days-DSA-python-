def split_strings(s):

    count0 = 0
    count1 = 0
    final_count = 0

    for i in range(len(s)):
        if s[i] == '0':
            count0 +=1

        elif s[i] == '1':
            count1+=1

        if count1 == count0:
            final_count += 1

    if final_count == 0:
        return -1
    return final_count

s = "0100110101"
print(split_strings(s))
