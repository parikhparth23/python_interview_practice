def outOfOrder(org_str):
    org_str = org_str.lower()
    for i in range(0,len(org_str)-1):
        if ord(org_str[i+1]) < ord(org_str[i]):
            print(i+1)
            # print(org_str[i+1])


# org_str = "dfhka"
org_str = "aBcDea"

outOfOrder(org_str)