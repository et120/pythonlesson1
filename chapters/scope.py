name = "Dave" #global scope
count = 1

# def greeting(name):
#     color = "blue" #local scope
#     print(color)
#     print(name)
    
def another():
    color = "blue"
    global count #access global scope variable to REASSIGN
    count += 1
    print(count)
    
    def greeting(name):
        nonlocal color #access variable to REASSIGN
        color = "red"
        print(color)
        print(name)
        
    greeting("Dave")
    
another()