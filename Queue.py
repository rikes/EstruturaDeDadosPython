class Queue:
    
    #Construtor
    def __init__(self):
        self.queue = []
        self.length_queue = 0
        
    #Inseri
    def push(self,e):
        self.queue.append(e)
        self.length_queue += 1
    
    #remove inicio
    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.length_queue -= 1
        return None
    
    #Verifica se esta vazia    
    def empty(self):
        if self.length_queue == 0:
            return True
        return False
    
    #Retorna o primeiro    
    def first(self):
        if not self.empty():
            return self.queue[0]
        return None    
    
    def length(self):
        return self.length_queue

q = Queue()

q.push(5)
q.push(3)
q.push(8)
print(q.first())
q.pop()       
print(q.first()) 