#!/usr/bin/python3

import uuid

# from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue  # skip it

                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
            models.storage.new(self)

    # [<class name>] (<self.id>) <self.__dict__>
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        # instance_dict = dict(self.__dict__)
        my_dict = self.__dict__.copy()

        my_dict["__class__"] = self.__class__.__name__
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()

        return my_dict
