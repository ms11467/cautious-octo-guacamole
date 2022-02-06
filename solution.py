import hashlib

print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
print(" ")

t = "NYU Computer Networking"
m = hashlib.md5(t.encode()).hexdigest()
s = hashlib.sha256(t.encode()).hexdigest()
# print('MD5 hash generator: ', m)

def welcome_assignment_answers(question):
  if question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?:":
   print(question)
   answer = "mtls"
  elif question == "Are encoding and encryption the same? - Yes/No:":
   print(question)
   answer = "No"
  elif question == "Is it possible to decrypt a message without a key? - Yes/No:":
   print(question)
   answer = "No"
  elif question == "Is it possible to decode a message without a key? - Yes/No:":
   print(question)
   answer = "Yes"
  elif question == "Is a hashed message supposed to be un-hashed? - Yes/No:":
   print(question)
   answer = "No"
  elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking':":
   print(question)
   answer = (m)
  elif question == "Is MD5 a secured hashing algorithm? - Yes/No:":
   print(question)
   answer = "Yes"
  elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? (Numeric):":
   print(question)
   answer = "3"
  elif question == "What layer of the TCP/IP model the protocol TCP belongs to? (Numeric):":
   print(question)
   answer = "4"
  return answer
  
if __name__ == "__main__":
   debug_question = "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?:"
   print(welcome_assignment_answers(debug_question))
   debug_question = "Are encoding and encryption the same? - Yes/No:"
   print(welcome_assignment_answers(debug_question))
   debug_question = "Is it possible to decrypt a message without a key? - Yes/No:"
   print(welcome_assignment_answers(debug_question))
   debug_question = "Is it possible to decode a message without a key? - Yes/No:"
   print(welcome_assignment_answers(debug_question))
   debug_question = "Is a hashed message supposed to be un-hashed? - Yes/No:"
   print(welcome_assignment_answers(debug_question))
   debug_question = "What is the MD5 hashing value to the following message: 'NYU Computer Networking':"
   print("MD Hashing =", welcome_assignment_answers(debug_question))
   debug_question = "Is MD5 a secured hashing algorithm? - Yes/No:"
   print(welcome_assignment_answers(debug_question))
   debug_question = "What layer from the TCP/IP model the protocol DHCP belongs to? (Numeric):"
   print(int(welcome_assignment_answers(debug_question)))
   debug_question = "What layer of the TCP/IP model the protocol TCP belongs to? (Numeric):"
   print(int(welcome_assignment_answers(debug_question)))
