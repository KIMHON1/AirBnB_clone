import json

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
class FileStorage:
    """a class FileStorage that serializes 
    instances to a JSON file and deserializes JSON file to instances:
    """
    
     # string - path to the JSON file
    __file_path = "file.json"
    #dictionary - empty but will store all objects by <class name>.id
    __objects = {}
    
    def all(self):
        """
        sets in __objects the obj with key <obj class name>.id
        """

       
        return self.__objects
    
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict(save_check=True)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)       
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
        
     
    def get(self, cls, id):
        """Retrieving object by class and/or id
        """
        key = cls.__name__ + '.' + id

        if key in self.__objects:
            return self.__objects[key]
        else:
            return None

    def count(self, cls=None):
        """Return count of objects in storage
        """
        return len(self.all(cls))

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    
    