# Trabalho Laboratório 4 - Classificação e Pesquisa de Dados - Gabriel Castelo Branco Gomes e Tiago Torres Schmidt.
def hashing(keyString,m):#Função de hashing. Recebe a string, com um parâmetro M de valor da tabela.
    value = getValue(keyString)#Chama a função getValue.
    return (value % m)#Retorna o modulo de valor por m

def insert(Hashtable, m, keyString):#Função insert. Insere a String na Hashtable de tamanho M.   
    value = hashing(keyString,m)#Descobre o índice a ser usado na tabela.
    Hashtable[value].append(keyString)#Insere a string na índice.
    
def getValue(string):#Função getValue. Recebe um string com finalidade de gerar um valor.
    values = [ord(character) for character in string]#Cria um vetor com os valores de cada caractere da palavra.
    totalValue = 0
    for value in values:#Soma todos os valores dos caracteres da string.
        totalValue = totalValue + value
    return totalValue#Retorna o valor.
    
def search(string,HashTable,m):#Função search. Realiza busca através do valor de hash.
    returnValue = -1;#Retorno em caso de erro.
    searchKey = hashing(string,m)#Busca a chave da palavra.
    for j in range(len(HashTable[searchKey])):#Busca na lista encadeada da chave encontrada.
        if(string == HashTable[searchKey][j]):#Em caso de encontrar, retorna
            returnValue = 1 + j        
    return returnValue
            
def main():#Função main.
    m = 503#Primeiro valor m a ser experimentado.
    HashTable503 = [[]for _ in range(m)]

    input1 = open("nomes_10000.txt", "r")#Abre o arquivo de base.
    inputs1 = input1.readlines()
    for line in inputs1:
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line  
        insert(HashTable503,m,lineA)#Insere na tabela.
        
    input2 = open("consultas.txt", "r")#Abre os arquivos de escrita e consulta.
    output1 = open("experimento503.txt", "w")
    inputs2 = input2.readlines()
    totalSearches = 0;#Variáveis de estatística.
    totalValue = 0;
    maxValue = 0;
    for line in inputs2:#Realiza a consulta e a contagem da estatística.
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        searchValue = search(lineA,HashTable503,m)
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1  
        if(searchValue > maxValue):
            maxValue = searchValue
        output1.write(f"{lineA} #{str(searchValue)}\n")   
    averageSearch = totalValue / totalSearches#Escreve o valor na saída.
    output1.write(f"MÉDIA #{averageSearch}\n")   
    output1.write(f"MÁXIMO #{maxValue}\n")  

    m = 2503#Segue o padrão do primeiro valor M.
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
    maxValue = 0;
    for line in inputs2:    
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line
        searchValue = search(lineA,HashTable2503,m)
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1   
        if(searchValue > maxValue):
            maxValue = searchValue        
        output1.write(f"{lineA} #{str(searchValue)}\n")   
    averageSearch = totalValue / totalSearches
    output1.write(f"MÉDIA #{averageSearch}\n")  
    output1.write(f"MÁXIMO #{maxValue}\n")

    m = 5003#Segue o padrão do primeiro valor M.
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
    maxValue = 0;
    for line in inputs2:    
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line    
        searchValue = search(lineA,HashTable5003,m)
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1   
        if(searchValue > maxValue):
            maxValue = searchValue        
        output1.write(f"{lineA} #{str(searchValue)}\n")   
    averageSearch = totalValue / totalSearches
    output1.write(f"MÉDIA #{averageSearch}\n")  
    output1.write(f"MÁXIMO #{maxValue}\n")  

    m = 7507#Segue o padrão do primeiro valor M.  
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
    maxValue = 0;
    inputs2 = input2.readlines()
    for line in inputs2:    
        if(line[-1] == "\n"):
            lineA = line[:-1]  
        else:
            lineA = line   
        searchValue = search(lineA,HashTable7507,m) 
        if(searchValue > 0):
            totalValue = totalValue + searchValue    
        totalSearches = totalSearches + 1   
        if(searchValue > maxValue):
            maxValue = searchValue          
        output1.write(f"{lineA} #{str(searchValue)}\n")       
    averageSearch = totalValue / totalSearches
    output1.write(f"MÉDIA #{averageSearch}\n") 
    output1.write(f"MÁXIMO #{maxValue}\n") 

if __name__ == "__main__":
    main()


