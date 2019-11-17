def convertStrToInt(org_str):
    result = 0
    for digit in org_str:
        result *= 10
        print("result is: " ,result)
        for d in "0123456789":
            result += digit > d

    print(result)


org_str = "123456"
convertStrToInt(org_str)