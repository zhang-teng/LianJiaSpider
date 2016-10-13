class mr_list(list):
    def __init__(self,iterobj=(),*args,**kw):
        super().__init__(iterobj,*args,**kw)
    def map(self,fun):
        '''caution: the map is not manipulate on the original object'''
        try:
            return mr_list(map(fun,self))
        except:
            return None
