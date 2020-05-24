n=input()
lenth=len(n)
i=0
ans=""
while i<lenth:
    if n[i]=='1' :
        ans=ans+'一'
    elif n[i]=='2' :
        ans=ans+'二'
    elif n[i]=='3' :
        ans=ans+'三'
    elif n[i]=='4' :
        ans=ans+'四'
    elif n[i]=='5' :
        ans=ans+'五'
    elif n[i]=='6' :
        ans=ans+'六'
    elif n[i]=='7' :
        ans=ans+'七'
    elif n[i]=='8' :
        ans=ans+'八'
    elif n[i]=='9' :
        ans=ans+'九'
    elif n[i]=='0' :
        ans=ans+'零'
    i=i+1
print(ans)
