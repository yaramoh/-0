#Simple marks programe

subj1=int(input("enter your mark: "))
subj2=int(input("enter your mark: "))
subj3=int(input("enter your mark: "))
subj4=int(input("enter your mark: "))
subj5=int(input("enter your mark: "))

Totalresult= subj1+subj2+subj3+subj4+subj5
Average=Totalresult/5
percentage=(Totalresult/500)*100
print("your total marks is "+str(Totalresult))
print("your average is "+str(Average))
print("your percentage is "+str(percentage))
