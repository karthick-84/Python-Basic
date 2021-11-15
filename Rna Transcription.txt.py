# define a function
# for transcription
def transcript(x) :
    
  # convert string into list
  l = list(x)  
  
  for i in range(len(x)):
  
      if(l[i]=='G'):
          l[i]='C'
  
      elif(l[i]=='C'):
          l[i]='G'
  
      elif (l[i] == 'T'):
          l[i] = 'A'
  
      elif (l[i] == 'A'):
          l[i] = 'U'
  
      else:
          print('Invalid Input')                      
            
  print("Translated DNA : ",end="")      
  for char in l:
      print(char,end="")
  
# Driver code
if __name__ == "__main__":
    
  x = "GCTAA"
  # function calling
  transcript(x)