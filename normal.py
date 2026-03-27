#________________________________________

# def binary_search(arr,target):
#     low=0
#     high=len(arr)-1 

#     while low<=high:
#         mid=(low+high)//2 

#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             low=mid+1 
#         elif arr[mid]>target:
#             high=high-1 
    
#     return -1 

# arr = [1, 3, 5, 7, 9, 11]
# target = 7

# result = binary_search(arr, target)

# print(result) 

#_______________________________________

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         swapped=False

#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped=True 
        

#         if not swapped:
#             break 
#     return arr 

# arr=[5,2,4,3,1]
# print(bubble_sort(arr))

# ---------------------------------

# arr=[5,2,4,3,1]
# result=sorted(arr)
# print(result)            

# --------------------------------

 
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self,value):
#         self.stack.append(value)
    
#     def pop(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.stack.pop()
    
#     def peek(self):
#         if self.is_empty():
#             return "Stack is empty"
#         return self.stack[-1]
    
#     def is_empty(self):
#         return len(self.stack)==0 

#     def size(self):
#         return len(self.stack)

# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# print(s.peek())   
# print(s.pop())    
# print(s.size())

# ------------------------------------------------

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D'],
#     'C': ['A'],
#     'D': ['B']
# }

# print(graph['A'])  

# ------------------------------------------------

# arr = [1, 2, 2, 3, 1] 

# freq={}

# for i in arr:
#     freq[i]=freq.get(i,0)+1 
# print(freq)


# def anagram(word,word1):
#     return sorted(word)==sorted(word1)

# print(anagram("silent","listen"))


# ------------------------------------------------




















        
    
    











 




