class Room:
    def __init__(self):
        
        #Could be anything, but we'll change it almost as soon as we instantiate it anyway.
        self.description = "A Sample Room Description"
        
        # This is an empty list, which we can fill later. 
        # Yes, that kind of portal, only since our game is pretty simple, each portal will point to another room.
        self.portals = []
        
        #Another empty list, we'll fill it when we instantiate.
        self.contents = []

class Item:
    def __init__(self):
        self.description = "Sample item description"
        self.name = "Sample Item"
        self.verbs = []

