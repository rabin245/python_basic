# def func1(a, b):
#     if (a and b) is True or (a and b) is False :
#         return True
#     return False

# print(func1(True, False))

# x = 'applez'
# a = x[0]
# b = x[-1]
# # x = x.replace(b, a)

# # x = x.replace(a, b)
# # x=x.replace('h', 'z')
# # y = x.find('hell')
# print(x[-1], x[0])
# print(a,b)
# print(x[1:-2])

# a = [i for i in range(5)]
# b = [i*2 for i in range(5)]
# c = list(zip(a,b))
# print(c)


# s = 'aeiouaeiou'
# k = 3
# sum =0
# tsum=0
# for char in s:
#     if char in 'aeiou':
#         sum+=1


# print(sum)

# l = [1,20,3,1,3,5,2,7,3,10]

# maxnum = max(l)
# print(maxnum)
# print(l.index(maxnum))
    
# st = 'styring'
# t = st[0:5:1]
# print(t)

# def findSubstring(s, k):
#     # Write your code here
#     sub_list=[]
#     vowel_count = []
#     for i in range(len(s)):
#         temp = s[i:i+k:1]
#         if len(temp)==k:
#             sub_list.append(temp)
    
#     for substring in sub_list:
#         count = 0
#         for char in substring:
#             if char in 'aeiou':
#                 count+=1
                
#         if count == k:
#             return substring
#         vowel_count.append(count)
    
#     max_vowels = max(vowel_count)
#     if max_vowels==0:
#         return 'Not found!'
#     vowel_substring = sub_list[vowel_count.index(max_vowels)]
#     return vowel_substring
    
s = 'some'
t = s[2:2+4]
print(t)