books={'A Better India  A Better World':'Narayana Murthy',
	'A Passage to India' :'E.M. Foster',
	"A Revenue Stamp":"Amrita Pritam",
	"An Introduction to Dreamland":"Bhagat Singh",
	"Adventures of Tom Sawyer":"Mark Twain",
	"A Suitable Boy":"Vikram Seth",
	"A Tale of Two Cities":"Charles Darwin",
	"Aadhe Adhure":"Mohan Rakesh",
	"A Week with Gandhi":"Louis Fisher",
	"Convenient Action":"Narendra Modi",
}
i=0
reserved=[]
hm=[]
ok={}
book_name=(input("enter a book_name:"))
book_auther=(input("enter a book_auther:"))
name={book_name:book_auther}
while i<7:
	count=1
	
	if book_auther and  book_name not in name:
		book_name=(input("enter a book_name:"))
		book_auther=(input("enter a book_auther:"))
		if book_auther and  book_name in books:
			intrested=input("intrested y or n :")
			if intrested=="y":
				print("ok i understand than you fill up this form:")
				name=input("enter your name:")
				mobile_num=input("enter your mobile_num:")
				ok["name"]=name
				ok["mobile_num"]=mobile_num
				hm.append(book_name)
				hm.append(name)
				hm.append(mobile_num)
			books.pop(book_name,book_auther)
		else:
			if book_name  =="Adventures of Tom Sawyer":
				print("Adventures of Tom Sawyer")	
			if book_name  =='A Better India  A Better World':
				print('A Better India  A Better World')	
			if book_name =="Convenient Action":
				print('Convenient Action')			
		print(ok)
		print(hm)
		count+=1
	else:
		if book_auther and  book_name in books:
			intrested=input("intrested y or n :")
			if intrested=="y":
				print("ok i understand than you fill up this form:")
				name=input("enter your name:")
				mobile_num=input("enter your mobile_num:")
				reserved.append(name)
				reserved.append(mobile_num)
			books.pop(book_name,book_auther)
		else:
			print("ok thanks for coming yash library...... :)")
		print(reserved)
	i+=1

