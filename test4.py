
def about_me():
    # dictionary
    me = {
        "first": "Tyrell",
        "last": "Patton",
        "age": 39
}

    print(me)


    # read values
    print(me["first"])
    print(me["age"])

    # add new elements
    me["email"] = "patton@example"
    print(me)

    #update existing 
    me["age"] = 39

    #check if key exist, before reading
    if"preferred_color" in me:
        me["preferred_color"] 


def test_address():
    location = {
        "street": "Evergreen",
        "number": 27,
        "city": "Springfield",
        "state": "CA",
        "zip": "92101"
    }

    print("street", "number", "city")
    

about_me()
test_address()


