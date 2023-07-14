class LibrarySystem:
	def initMenu(self):
		members={}
		books={}
		books_info={};
		while(True):
			print("-------------------------------------------")
			print("----Welcome to ITECH5403 Library System----")
			print("-------------------------------------------")
			print("Main Menu - please select an option:\n")
			print("1) Add new member \n")
			print("2) Add new book \n")
			print("3) Process borrowing \n")
			print("4) Process returning \n")
			print("5) View member status \n")
			print("6) View book status \n")
			print("7) Quit \n")
	
			selection=int(input("Main Menu - please select an option:"));
			if(selection==1):
				member_id=0
				while(True):
					print("Adding a new member: ")
					membername=input("Please enter a new member name:  \n")
					if(len(members)==0):
						member_id=1
					if(len(members)>0):
						for val in members.keys():
							member_id=val+1
					members.update({member_id:membername})
					print("Member ["+membername+"] has been created with member ID: "+str(member_id))
					for x in members.values():
						print(x)
					#print(len(members))
					opt=input("Would you like to [a]dd a new member or go-[b]ack to the previous menu? \n")
					if(opt=="b"):
						break
			elif(selection==2):
				book_id=0
				while(True):
						while(True):
							print("Adding new book: ")
							bookname=input("Please enter a new book title: \n")
							bookcopy=input("Please enter number of copies: \n")
							print("New book added: ")
							if(len(books)==0):
								book_id=1
							if(len(books)>0):
								if(bookname in books.values()):
									print("Book Name "+bookname+" Already Exists")
									break
								else:
									for val in books.keys():
										book_id=val+1
							books.update({book_id:bookname})
							print("Book ID: " +str(book_id))
							for x in books.values():
								print("Book Title:" +x)
								print("Number of copies:" +bookcopy)
							opt=input("Would you like to [a]dd a new book or go-[b]ack to the previous menu? \n")
							if(opt=="b"):
								break
						break
			elif(selection==3):
				member_id=input("Please enter a valid member ID: \n")
				for member_id in members:
					print("Valid User \n")
					for keys in members:
						print(keys)
						break
				book_id=input("Please enter a valid book ID for borrowing by member [member_id]: \n")
				for book_id in books:
					print("Book is present \n")
						
ob=LibrarySystem()
ob.initMenu()

