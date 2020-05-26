# Digant Kumar
# A program that takes a passage of English Language text as a string and that recovers and returns the hidden message
# by taking the first letter of every fifth word of the text.

def extract(text):
    word_split = text.split()
    count = 0
    hidden_message = ""
    for word in word_split:
        count += 1
        if count % 5 == 0:
            for c in word:
                hidden_message = hidden_message + c
                break
    return hidden_message
string = "Yesterday  I  saw  an  aardvark  while  walking  my  pet  tortoise,  Frank.   What a  sight  this  was! Aarvarks  are  nocturnal  " \
         "animals appearing  in  daylight  with caution.  Make sure to bring kippers when you visit."
print(extract(string))                       ##### Output - attack #####
