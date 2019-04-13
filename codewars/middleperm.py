from itertools import permutations 
def middle_permutation(string):
    perms = [''.join(i) for i in permutations(string)]
    if len(perms) % 2 == 0:
        return perms[int(len(perms)/2)-1]
    else:
        return perms[int(len(perms)/2)]



print (middle_permutation("abc")) #"bac"
print (middle_permutation("abcd")) #"bdca"
print (middle_permutation("abcdx")) #"cbxda"
print (middle_permutation("abcdxg")) #"cxgdba"
print (middle_permutation("abcdxgz")) #"dczxgba"