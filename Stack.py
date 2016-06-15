class Stack:
    
    #Construtor
    def __init__(self):
        self.stack = []
        self.length_stack = 0
    
    #Inserir na pilha    
    def push(self, e):
        self.stack.append(e)
        self.length_stack += 1
    
    #Remover
    def pop(self):
        self.stack.pop(self.length_stack - 1)
        self.length_stack -= 1
    
    #Retorna o topo
    def top(self):
        if not self.empty():
            return self.stack[-1]
        return None
    
    #Verifica se esta vazia
    def empty(self):
        if self.length_stack == 0:
            return True
        return False
    
    #Tamanho
    def length(self):
        return self.length_stack

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop();
print(s.top())
