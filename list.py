number= [-3,-2,-1,0,1,2,3]
positivelist = [x for x in number if x >0 ]
print(positivelist)



n=3
square=[x**2  for x in range(1,n+1)]
print(square)


word="language"
vowels=[ch for ch in word if ch in "aeiou" ]
print(vowels)

word="ABCD"
ordinals=[ord(ch) for ch in word ]
print(ordinals )