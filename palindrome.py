
##this function reverses the number
def get_reverse(number):
	number_str=str(number)
	number_rvs_str_lst=[]
	index=len(number_str)
	for i in range(0,index):
		number_rvs_str_lst.append(number_str[index-1-i])
	number_rvs_str="".join(number_rvs_str_lst)
	number_rvs=int(number_rvs_str)
	return number_rvs
##this function checks whether a number is palindrom or not
def check_palindrom(number):
	number_rvs=get_reverse(number)
	if number==number_rvs:
		return 1
	else:
		return 0

#this function adds a number with its reverse one
def create_palindrom(number):
	number_rvs=get_reverse(number)
	number_sum=number+number_rvs
	return number_sum

##main function starts from here
print("Enter the number")
number=input()
number=int(number)
flag=0
itr_nmbr=1000
count=0
flag=check_palindrom(number)
if flag==1:
	print "the number is already palindrom"
else:
	while count!=itr_nmbr:
		if count==0:
			temp=create_palindrom(number)
		else:
			temp=create_palindrom(temp)
		flag=check_palindrom(temp)
		count=count+1
		if flag==1:
			print "the palindrom number of %d is %d" %(number,temp)
			break
if count>=itr_nmbr:
	print "the number has no palindrom"













