import time
import csv
from passlib.hash import pbkdf2_sha256 #Password-Based Key Derivation Function 2 with encrypting code sha256
import stdiomask
from os import system,name
import shutil

with open('users.csv','a') as csv_file:
	csv_writer = csv.writer(csv_file)

	default_path = "/home/parth/Desktop/profile_pictures/Default.png" #folder containing profile pictures

	def clear():
		if name == 'nt':
			_=system('cls')

		else:
			_=system('clear')


	def sign_up():
		clear()
		print("BAREBONES DBMS REGISTRATION PAGE")
		Name = input("Enter Your Full Name \n")
		ph_no = input("Enter Your Contact Number\n")
		email = input("Enter Your Email Address \n")
		with open('users.csv','r') as fr:
			csv_reader = csv.reader(fr)
			for row in csv_reader:
				if row[0]==email:
					print("Email Address Not Available. Please enter valid one")
					email = input("Enter Your Email Address\n")
					fr.seek(0)
			sex = input("Enter Your gender\n")
			add = input("Enter Your Address\n")

			path = default_path
			opt = int(input("Enter 1 for Default Profile Picture and 2 for custom path: "))
			if(opt == 2):
				path = (input("Enter Complete Path Of Image: "))
				format_img = path.split('.')[1]
				shutil.copy(path,"/home/parth/Desktop/profile_pictures/"+email+'.'+format_img)
				path = "/home/parth/Desktop/profile_pictures/"+email+'.'+format_img

			pw = stdiomask.getpass(prompt = "Enter Your Password: ", mask = '*')
			pw2 = stdiomask.getpass(prompt = "Re-Enter Your Password: ", mask = '*')
			if pw==pw2:
				pw_hashed = pbkdf2_sha256.hash(pw) #hashing with automatic random key generation and number of iterations set to 29000 by default
				csv_writer.writerow([email,pw_hashed,Name,ph_no,sex,add,path])
				csv_file.flush()
				print()
				print("Signed Up Successfully!!!")
				print()
				time.sleep(3)
				clear()
				return True;
			return False;


	def sign_in():
		clear()
		print("BAREBONES DBMS LOGIN PAGE")
		un = input("Enter Your Email Address: ")
		pw = stdiomask.getpass(prompt = "Enter Your Password: ", mask = '*')
		with open('users.csv','r') as fr:
			csv_reader = csv.reader(fr)
			for row in csv_reader:
				if un==row[0]:
					i=0
					
					while not pbkdf2_sha256.verify(pw,row[1]):
						print("Wrong Password :(.... Please Retry")
						pw = stdiomask.getpass(prompt = "Enter Your Password: ", mask = '*')			
						i=i+1
						if i==3:
							print("Wrong Password... Attempts Exhausted.. Please Restart")
							return False, ['w','p']
					print("Signed In Successfully!!!")
					return True , row
			
			return False , []

	def disp(row): #[email,pw_hashed,name,ph_no,sex,add,path]
		clear()    # storing data in file in the above order
		print("Name: "+row[2])
		print("Phone Number: "+row[3])
		print("Email Address: "+row[0])
		print("Gender: "+row[4])
		print("Address: "+row[5]+'\n')

	def sear(NS):
		with open('users.csv','r') as fr:
			csv_reader = csv.reader(fr)
			for row in csv_reader:
				if row[2].lower() == NS.lower():
					print()
					print("Name: "+row[2])
					print("Phone Number: "+row[3])
					print("Address: "+row[5])

	def main():
		clear()
		print("WELCOME TO BAREBONES DBMS HOME PAGE")
		time.sleep(2)
		row =[]
		sign_in_cond = False
		ch=0

		while ch!=5:
			print("MAIN MENU\nChoices:-")
			print("1. Sign Up/Register (For New Users)")
			print("2. Sign In (For Existing Users)")
			print("3. Searching Details For Existing Users")
			print("4. Sign Out")
			print("5. Exit")
			ch = int(input("Enter 1, 2, 3, 4 or 5 for selecting choices: "))
			print(ch)
			if(ch==1):
				print(ch)
				sign_up()
			if(ch==2):
				sign_in_cond, row = sign_in()
				if(sign_in_cond):
					disp(row)
					print()			
				if (not sign_in_cond) and row==[]:
					print("Email Address Doesnt Exist.... Either Register or Retry")
				if (not sign_in_cond) and row==['w','p']:
					print("Wrong Password.... Either Register or Retry")
			if ch==3 and sign_in_cond:
				NS = input("Enter Full Name Of Person To Be searched: ")
				sear(NS)
			if ch==3 and (not sign_in_cond):
				clear()
				print("\nSign In First To Search\n")
				time.sleep(2)
			
			if ch==4 and (not sign_in_cond):
				sign_in_cond=False
				print("Already Signed Out")
				time.sleep(2)			
				clear()

			if ch==4 and sign_in_cond:
				clear()
				sign_in_cond=False
				print("Signed Out")

			if ch==5:
				clear()
				sign_in_cond=False
				print("Signed Out")
				print("Thank You For Using Our BAREBONES DBMS")
				time.sleep(1)
				exit()

	if __name__ == '__main__':
		main()