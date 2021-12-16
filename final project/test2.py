

class Queue:
    def __init__(self):
        self.queue = list()


    def add_to_queue(self, value):
        """Enqueue"""
    # Insert method to add element
        if value not in self.queue:
            self.queue.insert(0,value)
            return True
        return False

    def remove_from_queue(self):
        """Dequeue"""
        if len(self.queue)>0:
                return self.queue.pop()
        return ("No elements in Queue!")

    def size(self):
       return len(self.queue)


#TEST
#Scenario: enqueue 5 values and dequeue 2 of the

print("------------TEST 1--------------")
queue = Queue()
queue.add_to_queue("Monday")
queue.add_to_queue("Tuesday")
queue.add_to_queue("Wednesday")
queue.add_to_queue("Thursday")

print(queue.size())

print("----------TEST 2----------------")
removed = queue.remove_from_queue()
print(removed)
removed = queue.remove_from_queue()
print(removed)
