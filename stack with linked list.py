class queuelist:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,items):
        self.items.append(items)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            