import uuid
from datetime import datetime


class BaseModel:
    
    """_summary_
     class BaseModel that defines all common attributes/methods for other classes
    """
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
  
    

    def __str__(self):
        """
         function that should print: [<class name>] (<self.id>) <self.__dict__>
         
        """
        return "[{}]({}){}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """
             updates the public instance attribute updated_at with the current datetime
        """
      
        return datetime.now()
    
    def to_dict(self):
        """
                to_dict(self): returns a dictionary containing all keys/values of __dict__ of the instance
        """
        dic = self.__dict__
        new = {}
        for (key,value) in dic.items():
            if isinstance(value, datetime):
                new[key] = value.isoformat()
            else:
                new[key] = value
        return new



                
            
                
        
      
        
