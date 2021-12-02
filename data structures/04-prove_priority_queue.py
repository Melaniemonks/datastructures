"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        #new_node = Priority_Queue.Node(priority, value)
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            #runs until highest priority last in the queue is found
            #if self.queue[index].priority >= self.queue[high_pri_index].priority:
                #high_pri_index = index

            #correct
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        # delete node
        del self.queue[high_pri_index]
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: create a queue that can add values (10, 2, 3) and their priority (5, 1, 7) to the list based on their enqueue order
# Expected Result: the result should look like [10 (pri:5), 2 (pri:1), 3(pri:7) ]
print("Test 1")
queue = Priority_Queue()
queue.enqueue(10, 5)
queue.enqueue(2,1)
queue.enqueue(3, 7)
print(f"Queue List with priority: {queue}")
# Defect(s) Found: The initial had the code print out in the order of priority rather than values. 

print("=================")

# Test 2
# Scenario: deleting nodes with highest priority
# Expected Result: the result should look like [10 (pri:5), 2 (pri:1) ]
print("Test 2")
queue = Priority_Queue()
queue.enqueue(10,5)
queue.enqueue(2,1)
queue.enqueue(3,7)
print(f"Queue List: {queue}")
removed_value = queue.dequeue()
print(f"New list with priority: {queue}")
print(f"Deleted node: {removed_value}")
# Defect(s) Found: There was no delete function in the code.

print("=================")

# Add more Test Cases As Needed Below

# Test 2
# Scenario: deletes node from empty list
# Expected Result: The queue is empty
print("Test 3")
queue = Priority_Queue()
queue.dequeue()
#defect(s) found: None.
print("=================")