"""
pass
"""

def solution(min1, min2_10, min11, s):
    total_min = 0
    if s<min1:
        return total_min
    while s > 0:
        if total_min == 0 :
            print("Call Starting.")
            
            total_min+=1
            s-=min1
            print(f"Coins remaining after {total_min} min: {s}")
            print(f"you have been calling for: {total_min} min.")
            print("-"*20)
        
        # print(f"Coins remaining: {s}")
        # print(f"you have been calling for: {total_min} min.")
        # print('x')
        
        
        elif (total_min<10) and (total_min>=1) and ((s-min2_10)>=0):
            print(f"Funds avalible: {s}")
            total_min+=1
            s-=min2_10
            print(f"you have been calling for: {total_min} min.")
            print(f"Coins remaining: {s}")
            print("-"*20)

            
        elif total_min>=10 and (s-min11)>=0:
            print(f"Funds avalible: {s}")
            total_min+=1
            s-=min11
            print(f"you have been calling for: {total_min} min.")
            print(f"Coins remaining: {s}")
            print("-"*20)
        else:
            break           
    return total_min




min1= 10
min2_10= 1
min11= 2
s= 22
expected_result = 11
print(solution(min1, min2_10, min11, s))