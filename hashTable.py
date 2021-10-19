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
    
def search(string,HashTable,m):
    returnValue = -1;
    searchKey = hashing(string,m)    
    for j in range(len(HashTable[searchKey])):        
        if(string == HashTable[searchKey][j]):
            returnValue = 1 + j        
    return returnValue
            
def main():
    m = 503
    HashTable503 = [[]for _ in range(m)]

    input1 = open("nomes_10000.txt", "r")
    inputs1 = input1.readlines()
    for line in inputs1:
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        insert(HashTable503,m,lineA)
        
    input2 = open("consultas.txt", "r")
    output1 = open("experimento503.txt", "w")
    inputs2 = input2.readlines()
    totalSearches = 0;
    totalValue = 0;
    for line in inputs2:    
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        searchValue = search(lineA,HashTable503,m)
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1     
        output1.write(f"{lineA} #{str(searchValue)}\n")       
    averageSearch = totalValue / totalSearches
    output1.write(f"MÉDIA #{averageSearch}\n")   
    output1.write(f"TOTAL DE CONSULTAS #{totalValue}\n")  

    m = 2503
    HashTable2503 = [[]for _ in range(m)]

    input1 = open("nomes_10000.txt", "r")
    inputs1 = input1.readlines()
    for line in inputs1:
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        insert(HashTable2503,m,lineA)
        
    input2 = open("consultas.txt", "r")
    output1 = open("experimento2503.txt", "w")
    inputs2 = input2.readlines()
    totalSearches = 0;
    totalValue = 0;
    for line in inputs2:    
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1   
        searchValue = search(lineA,HashTable2503,m)
        output1.write(f"{lineA} #{str(searchValue)}\n")   
    averageSearch = totalValue / totalSearches
    output1.write(f"MÉDIA #{averageSearch}\n")  
    output1.write(f"TOTAL DE CONSULTAS #{totalValue}\n")  

    m = 5003
    HashTable5003 = [[]for _ in range(m)]

    input1 = open("nomes_10000.txt", "r")
    inputs1 = input1.readlines()
    for line in inputs1:
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        insert(HashTable5003,m,lineA)
        
    input2 = open("consultas.txt", "r")
    output1 = open("experimento5003.txt", "w")
    inputs2 = input2.readlines()
    totalSearches = 0;
    totalValue = 0;
    for line in inputs2:    
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line    
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1   
        searchValue = search(lineA,HashTable5003,m)
        output1.write(f"{lineA} #{str(searchValue)}\n")   
    averageSearch = totalValue / totalSearches
    output1.write(f"MÉDIA #{averageSearch}\n")  
    output1.write(f"TOTAL DE CONSULTAS #{totalValue}\n")  

    m = 7507    
    HashTable7507 = [[]for _ in range(m)]

    input1 = open("nomes_10000.txt", "r")
    inputs1 = input1.readlines()
    for line in inputs1:
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        insert(HashTable7507,m,lineA)
        
    input2 = open("consultas.txt", "r")
    output1 = open("experimento7507.txt", "w")
    totalSearches = 0;
    totalValue = 0;
    inputs2 = input2.readlines()
    for line in inputs2:    
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line    
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1   
        searchValue = search(lineA,HashTable7507,m)
        output1.write(f"{lineA} #{str(searchValue)}\n")       
    averageSearch = totalValue / totalSearches
    output1.write(f"MÉDIA #{averageSearch}\n") 
    output1.write(f"TOTAL DE CONSULTAS #{totalValue}\n")  


if __name__ == "__main__":
    main()


