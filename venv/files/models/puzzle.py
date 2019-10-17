class Puzzle:
    def __init__(self, howmuch_elements, warranty, material, type_level):
        self.howmuch_elements = howmuch_elements
        self.warranty = warranty
        self.material = material
        self.type_level = type_level

    def __str__(self):
        return str(self.howmuch_elements)+' '\
               + str(self.warranty)+' '\
               + self.material+' '\
               + self.type_level
