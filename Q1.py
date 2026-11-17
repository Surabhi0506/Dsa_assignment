class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None

class priority_queue:
    def __init__(self):
        self.front = None

    def isempty(self):
        return self.front is None

    def enqueue(self, pid, name, priority):
        new_node = Node(pid, name, priority)

        if self.isempty() or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

        print("Patient Added Successfully")

    def display_next(self):
        if self.isempty():
            print("No patients waiting")
        else:
            print("Next Patient to be Treated:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.name)
            print("Priority:", self.front.priority)

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            temp = self.front
            print("Treated Patient:", temp.name)
            self.front = self.front.next
            temp = None

    def display_all(self):
        if self.isempty():
            print("No patients waiting")
        else:
            print("Waiting Patients:")
            temp = self.front

            while temp:
                print("Patient ID:", temp.pid)
                print("Patient Name:", temp.name)
                print("Priority:", temp.priority)

                if temp.priority == 1:
                    print("Category: Critical")
                elif temp.priority == 2:
                    print("Category: Serious")
                else:
                    print("Category: Normal")

                print("-------------------")
                temp = temp.next


pq = priority_queue()

pq.enqueue(101, "Rahul", 3)
pq.enqueue(102, "Priya", 1)
pq.enqueue(103, "Amit", 2)
pq.enqueue(104, "Sneha", 1)

pq.display_all()

pq.display_next()

pq.dequeue()

pq.display_all()