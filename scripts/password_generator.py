import random

def main():
	#Lists all the characters to make the password
	letters = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
	letters2 = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
	numbers = "1,2,3,4,5,6,7,8,9,0".split(",")
	sChar = "!,@,#,$,%,^,*,(,)<,>,-,+,?".split(",")

	#Adds all the lists together
	everything = letters + letters2 + numbers + sChar
        
	#Asks the user how many characters they want the password to be
	nums = int(input("How long would you like the password to be? Enter a number: "))

	#Gathers a random character from everything added together and generates those characters based on how many characters the user wanted
	for i in range(nums):
		print (random.choice(everything), end='')
	print("")

	#Run again?
	multirun = input("Do you want to generate another password? Enter yes or no: ")
	if multirun.lower() == "yes":
		print("")
		#Recursion is good.
		main()

#Executes the main function
main()
