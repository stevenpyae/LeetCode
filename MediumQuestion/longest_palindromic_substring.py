def verify_palindrome(s):
    palin_flag = False
    # length of the string
    # find out whether even or odd 'abba'

    if len(s) >= 2:
        back_index = len(s) - 1
        for front_index in range(0, int(len(s) / 2)):
            if s[front_index] == s[back_index]:
                print(s[back_index])
                print(s[front_index])
                palin_flag = True
                back_index -= 1

            else:
                palin_flag = False
                return palin_flag

    return palin_flag


def longest_palindrome(s):
    # get the length of the string first
    # check if the whole string is palindrome
    # if not, shorten it side by side
    if len(s) < 2:
        return s

    if len(s) == 2 and (s[0] != s[1]):
        return s[0]

    temp = None

    for i in range(0, len(s)):
        print(i)
        for j in range(len(s)-1, 0, -1):
            if s[i]==s[j]:
                if temp is not None and (j-i+1 < len(temp)):
                    continue
                if verify_palindrome(s[i: j + 1]):
                    if temp is None or len(s[i:j + 1]) > len(temp):
                        temp = s[i:j+1]
                    else:
                        continue

    return temp

if __name__ == "__main__":
    s = "babad"
    print(verify_palindrome(s))
    print(longest_palindrome(s))