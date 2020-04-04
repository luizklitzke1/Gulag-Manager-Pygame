jorge  = "a"
print (jorge)

def a():
    
    global jorge
    if  jorge == "a":
        
        print("A")
        
    else: 
         jorge = "b"
        
a()
print (jorge)