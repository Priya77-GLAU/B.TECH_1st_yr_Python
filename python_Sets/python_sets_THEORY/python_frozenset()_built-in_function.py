#______What is Frozenset in python___________________________________________
                |
                |
                |
           just an immutable version of Python Set.
        _______________________________________________

"_________________________PTR's (Points to remember)________________________"

1.) Elements of a frozen set remains the same after creation. Due to this
    property frozen sets can be used as a key in dictionary.

    But But like sets, it is not ordered. (Elements can be set at any index).

2.) Syntax:
                frozenset([iterable])

        ::: Here parameter is optional. And Iterable can be set, dictionary, tuple, etc.

        ::: return value --> returns an immutable frozenset initialized with elements from the given iterable.
        
    
3.) Example:
                vowels = ('a', 'e', 'i', 'o', 'u') # tuple of vowels
                fSet = frozenset(vowels)
                print('The frozen set is:', fSet)
                print('The empty frozen set is:', frozenset())

                OUTPUT >>>  The frozen set is: frozenset({'i', 'a', 'u', 'e', 'o'})
                            The empty frozen set is: frozenset()
                

4.) When you use dictionary as an iterable for a frozen set.

                person = {"name": "John", "age": 23, "section": "AA"} # random dictionary
                fSet = frozenset(person)
                print('The frozen set is:', fSet)

                OUTPUT >>>  The frozen set is: frozenset({'name', 'section', 'age'}) #It only takes key of the dictionary to create the set.

5.) frozen sets can be used as key in Dictionary or as element of another set.

6.) find what are the things work with frozenset, write this:

            dir(frozenset())

           OUTPUT   >>>  ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
                        '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__',
                        '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
                        '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference',
                        'union']




                

