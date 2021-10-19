def display_hash(hashTable,m):
      
    for i in range(m):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
# Creating Hashtable as 
# a nested list.

def hashing(keyString,m):
    value = getValue(keyString)
    return (value % m)

def insert(Hashtable, m, keyString):      
    value = hashing(keyString,m)
    Hashtable[value].append(keyString)
    
def getValue(string):
    values = [ord(character) for character in string]
    totalValue = 0
    for value in values:
        totalValue = totalValue + value
    return totalValue
    
def search(string,HashTable):
    returnValue = 0;
    searchKey = hashing(string,m)    
    for j in range(len(HashTable[searchKey])):        
        if(string == HashTable[searchKey][j]):
            returnValue = 1 + j        
    return returnValue
            
#m = int(input("Digite um número M:"))
m = 503

HashTable = [[]for _ in range(m)]

input1 = open("nomes_10000.txt", "r")
inputs1 = input1.readlines()
for line in inputs1:
    if(line[-1] == "\n"):
        lineA = line[:-1]  
    else:
        lineA = line
    insert(HashTable,m,lineA)
    
input2 = open("consultas.txt", "r")
output1 = open("saida1.txt", "w")
inputs2 = input2.readlines()
for line in inputs2:    
    if(line[-1] == "\n"):
        lineA = line[:-1]  
    else:
        lineA = line
    print(lineA)
    searchValue = search(lineA,HashTable)
    output1.write(f"{lineA} #{str(searchValue)}\n")    

#display_hash(HashTable,m)
