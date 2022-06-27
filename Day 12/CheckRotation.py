def check_rotation(S1,S2):
    if len(S1) != len(S2):
        return False

    temp = S1+S2

    if temp.count(S2) > 1:
        return True
    return False

string1 = "AACD"
string2 = "ACDA"
print(check_rotation(string1,string2))