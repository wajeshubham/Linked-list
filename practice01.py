exp = [
    {"january": 2200,
     "february": 2350,
     "march": 2000,
     "april": 2130,
     "may": 2000},
]

# print(f"you spent ${exp[0]['february']} in february")
# print(f"your total expense in first quarter is ${exp[0]['january']+exp[0]['february']+exp[0]['march']}")

exp[0]["april"]-=200

print(exp)

max_no=int(input("enter a number: "))

odd_lst=[]

for i in range(1,max_no+1):
    if i%2==1:
        odd_lst.append(i)

print(odd_lst)
