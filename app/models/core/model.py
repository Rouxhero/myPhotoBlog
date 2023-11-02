# -*- coding: utf-8 -*-
# oOoOo Author oOoOo
#      Rouxhero
# -------------------
from collections.abc import MutableMapping
import json
from app.resources.entry import db


class Model(MutableMapping):

    fields: dict = {}
    mId: int = 0


    def __init__(self,kwargs={}):
        self.iFields = self.fields.copy()
        if kwargs != {}:
            self.__create(**kwargs)

    def __create(self, **args) -> None:
        for k in self.fields.keys():
            if k not in args.keys() and self.fields[k][1] == "required":
                raise KeyError(f"[Model][{self.__class__.__name__}][Create Error] {k} is not defined !")
        row = db.insert(self.__class__.__name__, args)
        self.__load_row(self,row)

    @property
    def id(self):
        return self.mId

    @id.setter
    def id(self, value):
        self.mId = value
    
    def save(self) -> None:
        db.update(self.__class__.__name__, self)

    def get(self, **args):
        for k in args.keys():
            if k not in self.keys() and k != "id":
                raise KeyError(f"[Model][{self.__class__.__name__}][Get Error] {k} is not defined !")
        row = db.select(self.__class__.__name__, args,self.fields)
        if row == None:
            return None
        self.__load_row(self,row)
        return self
    
    def get_all(self):
        row = db.select(self.__class__.__name__, {},self.fields,-1)
        if row == None:
            return []
        return [self.__load_row(self.__class__(),r) for r in row]
    
    def __load_row(self,dest, row):
        for k in list(dest.fields.keys()):
            if k == "id" or k == None: 
               continue
            elif type(dest.fields[k][0]) == dict:
                dest[k] = json.loads(row[k])
            elif type(dest.fields[k][0]) == list:
                dest[k] = json.loads(row[k])
            elif type(dest.fields[k][0]) == int:
                dest[k] = int(row[k])
            else:
                dest[k] = row[k]
        dest.id = row['id']
        return dest

    def __delitem__(self, key):
        if key not in self.fields:
            raise KeyError(f"[Model][{self.__class__.__name__}][Del Error] {key} is not defined !")
        self.iFields[key] = None

    def __setitem__(self, key, value):
        if not key in self.fields:
            raise KeyError(f"[Model][{self.__class__.__name__}][Set Error] {key} is not defined !")
        if type(value) != type(self.fields[key][0]) and value != None:
            raise TypeError(f"[Model][{self.__class__.__name__}][Set Error] {key} is {type(self.fields[key][0])} not  {type(value)} !")
        self.iFields[key] = value

    def __getitem__(self, key):
        if key not in self.fields:
            raise KeyError(f"[Model][{self.__class__.__name__}][Get Error] {key} is not defined !")
        return self.iFields[key]

    def __iter__(self):
        return iter(self.iFields)

    def __len__(self):
        return len(self.iFields)