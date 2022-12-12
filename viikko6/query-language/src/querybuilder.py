from matchers import All, And, HasAtLeast, HasFewerThan, PlaysIn, Or


class QueryBuilder:
    def __init__(self):
        self.query = All()
        
    def build(self):
        result = self.query
        self.query = All()
        return result
    
    def hasAtLeast(self, value, attr):
        self.query = And(self.query, HasAtLeast(value, attr))
        return self
    
    def hasFewerThan(self, value, attr):
        self.query = And(self.query, HasFewerThan(value, attr))
        return self
    
    def playsIn(self, team):
        self.query = And(self.query, PlaysIn(team))
        return self
    
    def oneOf(self, query1, query2):
        self.query = Or(query1, query2)
        return self