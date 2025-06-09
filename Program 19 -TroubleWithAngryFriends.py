
j_angry = True
s_angry = False
def friends_in_trouble(j_angry,s_angry ):
    if (j_angry== True and s_angry==False) :
        return False
    elif (j_angry== False and s_angry==True) :
        return False
    else:
        return True

CheckTrouble = friends_in_trouble(j_angry,s_angry)
print(CheckTrouble)
