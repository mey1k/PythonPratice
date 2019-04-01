"""
#특정 문자열이 특정 문자열의 접두사가 된다면 false
#아니면 true
#
"""

import re

def solution(phone_book):

    answer = True

    phone_book = sorted(phone_book)

    for i in range(len(phone_book)):
        p = re.compile(phone_book[i])
        for j in range(len(phone_book)):
         result = p.findall(phone_book[j])
         if result:
             if result[0] != phone_book[j]:
                if result[0][:1] != phone_book[j][:1]:
                    break
                else:
                    answer = False
                    break
         else:
             answer = True
        if not answer:
            break



    return print(answer)


solution(["12232332", "12", "222222"])


#-2
#import re
#def solution(phoneBook):

#    for b in phoneBook:
#        p = re.compile("^"+b)
#        for b2 in phoneBook:
#            if b != b2 and p.match(b2):
#                return False
#    return True

#-3
#def solution(phoneBook):
#    phoneBook = sorted(phoneBook)

#    for p1, p2 in zip(phoneBook, phoneBook[1:]):
#        if p2.startswith(p1):
#            return False
#    return True

#-4
#phone_num={}
#def check(num):
#    if(num == 0):
#        return True
#    else:
#        if(phone_num.get(num)==None):
#            return check(int(num/10))
#        else:
#            return False


#def solution(phone_book):
#    change_book = list(map(int, phone_book))
#    change_book.sort()
#    for phonenum in change_book:
#        num = int(phonenum)
#        if( num < 10):
#            if(phone_num.get(num)==None):
#                phone_num[num] = 1 
#        else:
#            if(check(num)== True):
#                phone_num[num] = {num:1} 
#                continue
#            else:
#                return False
#    answer = True
#    return answer