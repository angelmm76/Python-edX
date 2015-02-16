# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """    
    #si new va despues que atme
    if newFrob.myName() >= atMe.myName():
        newFrob.setBefore(atMe)
        atMe.setAfter(newFrob)
        if atMe.getAfter() != None:
            newFrob.setAfter(atMe.getAfter())
            atMe.getAfter().setBefore(newFrob)
    else:
        newFrob.setAfter(atMe)
        atMe.setBefore(newFrob)
        if atMe.getBefore() != None:
            newFrob.setBefore(atMe.getBefore())
            atMe.getBefore().setAfter(newFrob)


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)
#insert(martha, fred)

print eric.getBefore().name 
print eric.name 
print eric.getAfter().name 
print eric.getAfter().getAfter().name 
print eric.getAfter().getAfter().getAfter().name
print eric.getAfter().getAfter().getAfter().getAfter().name

