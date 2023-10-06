def convert(s, numRows):
    index_track = 0
    ones_fill_index = numRows - 2
    # 2d Array
    array = [['#' for x in range(numRows)] for y in range(7)]

    for i in range(7):  # 0 - 6
        # if end of the string break off from the loop
        if index_track == len(s):
            break
        # loop for 7 times
        if i % (numRows - 1) == 0:  # 0 2 4 6 <--- 3  0 3 6 <---- 4
            # for all fill columns
            for j in range(numRows):  # 0 - 2
                array[i][j] = s[index_track]
                index_track += 1
                if index_track == len(s):
                    break
        else:
            # for only 1 fill columns
            if ones_fill_index == 0:
                ones_fill_index = numRows - 2
            for j in range(numRows):  # 0 - 3
                if j == ones_fill_index:
                    array[i][j] = s[index_track]
                    index_track += 1
                    if index_track == len(s):
                        break
                    ones_fill_index -= 1
                    # reset
                else:
                    array[i][j] = "#"

    print(array)
    empty_str = ""
    for i in range(numRows):
        for row in array:
            if row[i] == "#":
                continue
            else:
                empty_str += row[i]

    print(empty_str)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 4
    convert(s, numRows)
