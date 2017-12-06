# Programa para MergeSort en una lista doblemente ligada
 
# Un nodo de la lista doblemente ligada
class Node:
     
    # Constructor para crear un nuevo nodo
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None
 
class DoublyLinkedList:
 
     # Constructor para una Lista Doblemente Ligada vacía
    def __init__(self):
        self.head = None
 
    # Función para combinar dos listas ligadas
    def merge(self, first, second):
         
        # Si la primera lista ligada está vacía
        if first is None:
            return second 
         
        # Si la segunda lista ligada está vacía
        if second is None:
            return first
 
        # Elige el menor valor
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None  
            return first
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
 
    # Función para hacer merge sort
    def mergeSort(self, tempHead):
        if tempHead is None: 
            return tempHead
        if tempHead.next is None:
            return tempHead
         
        second = self.split(tempHead)
         
        # Recurrir a las mitades izquierda y derecha
        tempHead = self.mergeSort(tempHead)
        second = self.mergeSort(second)
 
        # Merge a las dos mitades ordenadas
        return self.merge(tempHead, second)

    # Separa la lista doblemente ligada (DLL) en dos DLLs
    # de la mitad del tamaño
    def split(self, tempHead):
        fast = slow =  tempHead
        while(True):
            if fast.next is None:
                break
            if fast.next.next is None:
                break
            fast = fast.next.next
            slow = slow.next
             
        temp = slow.next
        slow.next = None
        return temp
         
             
    # Dada una referencia a la cabeza de una lista y un
    # entero, inserta un nuevo nodo en el frente de la lista
    def push(self, new_data):
  
        # 1. Asignar nodo
        # 2. Pone los datos en él
        new_node = Node(new_data)
  
        # 3. Hacer el siguiente del nodo nuevo como cabeza y
        # anterior como Ninguno (ya era ninguno)
        new_node.next = self.head
  
        # 4. cambiar prev del nodo principal a new_node
        if self.head is not None:
            self.head.prev = new_node
  
        # 5. mover la cabeza para apuntar al nuevo nodo
        self.head = new_node
 
 
    def printList(self, node):
        temp = node
        print ("Traversal hacia delante usando el siguiente puntero")
        while(node is not None):
            print (node.data),
            temp = node
            node = node.next
        print ("\nTraversal hacia atrás usando el puntero anterior")
        while(temp):
            print (temp.data),
            temp = temp.prev
 
# Programa de controlador para probar las funciones anteriores

dll = DoublyLinkedList()

import random

# Aquí agregué una iteración para demostrar el funcionamiento. 750 es un número
# cualquiera de datos que serán ordenado
#for x in range(0, 750):
#    dll.push(random.randint(0,100))

#Prueba de ordenamiento alfabético
dll.push("cab")
dll.push("abc")
dll.push("bca")

import time
start = time.time()
dll.head = dll.mergeSort(dll.head)
end = time.time()
print ("Lista Ligada después de ordenar")
dll.printList(dll.head)
print ("Tiempo de ejecucion de Mergesort (segundos): ")
print (end - start)

# (http://www.geeksforgeeks.org) This code is contributed by Nikhil Kumar Singh(nickzuck_007)
