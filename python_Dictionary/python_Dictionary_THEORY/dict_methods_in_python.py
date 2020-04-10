#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! PYTHON DICTIONARY METHODS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


	
	

#1.) clear()    =>  Removes all the elements from the dictionary
car ={  "brand": "Ford",
        "model": "Mustang",
        "year": 1964}
car.clear()
print(car)



#2.) copy() =>  Returns a copy of the dictionary
car ={  "brand": "Ford",
        "model": "Mustang",
        "year": 1964}
x = car.copy()
print(x)




#3.) fromkeys() => Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

#________orr________________
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)




#4.) get()  => Returns the value of the specified key

car = {  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.get("model")
print(x)



#5.) items()    =>  Returns a list containing a tuple for each key value pair

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.items()
print(x)



#6.) keys() =>  Returns a list containing the dictionary's keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.keys()
print(x)

#When an item is added in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.keys()
car["color"] = "white"
print(x)




#7.) pop()  =>  Removes the element with the specified key
                #Note: The value of the removed item is the return value of the pop() method.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.pop("model")
print(x)
print(car)




#8.) popitem()  =>  Removes the last inserted key-value pair
                    #The popitem() method removes the item that was last inserted into the dictionary.
                    #In versions before 3.7, the popitem() method removes a random item.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.popitem()
print(car)
print(x) #The removed item is the return value of the popitem() method, as a tuple, see example below.





#9.) setdefault()   =>	Returns the value of the specified key.
#                       If the key does not exist: insert the key, with the specified value

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.setdefault("model", "Bronco")
print(x)

#Another example
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.setdefault("color", "white")
print(x)





#10.) update()  =>  Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
car.update({"color": "White"})
print(car)




#11.) values()  =>  Returns a list of all the values in the dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
x = car.values()
print(x)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!











