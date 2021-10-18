def display_hash(hashTable,m):
      
    for i in range(m):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
# Creating Hashtable as 
# a nested list.

def Hashing(keyString,m):
    value = getValue(keyString)
    return (value % m)

def insert(Hashtable, m, keyString):      
    value = Hashing(keyString,m)
    Hashtable[value].append(keyString)
    
def getValue(string):
    values = [ord(character) for character in string]
    totalValue = 0
    for value in values:
        totalValue = totalValue + value
    return totalValue

m = int(input("Digite um número M:"))

HashTable = [[]for _ in range(m)]

insert(HashTable, m, 'Allahabad')
insert(HashTable, m, 'Mumbai')
insert(HashTable, m, 'Mathura')
insert(HashTable, m, 'Delhi')
insert(HashTable, m, 'Punjab')
insert(HashTable, m, 'Noida')

display_hash(HashTable,m)
