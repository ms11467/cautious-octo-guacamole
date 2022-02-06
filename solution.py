import hashlib


print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
print(" ")

t = "NYU Computer Networking"
m = hashlib.md5(t.encode()).hexdigest()
s = hashlib.sha256(t.encode()).hexdigest()
# print('MD5 hash generator: ', m)

'''
### welcome_assignment_answers
### Input - All eight questions given in the assignment.
### Output - The right answer for the specific question.

#def welcome_assignment_answers(question):
    #Students do not have to follow the skeleton for this assignment.
    #Another way to implement is using a "case" statements similar to C.
'''
question = input("In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?:")
if question == "mtls":
   print("Answer = mtls")
else:
   print("Try Again")
question = input("Are encoding and encryption the same? - Yes/No:")
if question == "No":
   print("Answer = No")
else:
   print("Try Again")
question = input("Is it possible to decrypt a message without a key? - Yes/No:")   
if question == "No":
   print("Answer = No")
else:
   print("Try Again")  
question = input("Is it possible to decode a message without a key? - Yes/No:")
if question == "Yes":
   print("Answer = Yes")
else:
   print("Try Again")   
question = input("Is a hashed message supposed to be un-hashed? - Yes/No:") 
if question == "No":
   print("Answer = No")
else:
   print("Try Again")   
question = input("What is the MD5 hashing value to the following message: 'NYU Computer Networking':")
if question == "md5":
   print("MD5 hasing value =", m)
else:
   print("Try Again") 
question = input("Is MD5 a secured hashing algorithm? - Yes/No:")
if question == "Yes":
   print("Answer = Yes")
else:
   print("Try Again")   
question = input("What layer from the TCP/IP model the protocol DHCP belongs to? (Numeric): ")
if question == "3":
   print("Answer = 3")
else:
   print("Try Again, Require a Numeric value")   
question = input("What layer of the TCP/IP model the protocol TCP belongs to? (Numeric): ")
if question == "4":
   print("Answer = 4")
else:
   print("Try Again, Require a Numeric value") 

'''
if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No: "
    print(welcome_assignment_answers(debug_question))
'''  
