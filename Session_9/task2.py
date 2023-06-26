# Write a program to find out whether a student is pass or fail , if it requires total of 40%  and 
# at least 33% in each subject to pass, Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter first subject marks: "))
sub2 = int(input("Enter second subject marks: "))
sub3 = int(input("Enter third subject marks: "))

if(sub1 < 33 or sub2< 33 or sub3 < 33):
    print("you are fail because ypu have less than 33 in one of the subjects")
elif ((sub1+sub2+sub3)/3 < 40):
    print("you are fail due to total percentage less than 40")
else:
    print("Congratulations! you are pass")
