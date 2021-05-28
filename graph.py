class Graph:
    def __init__(self,routes):
        self.routes=routes
        self.graph_dict={} 
        for key,route in routes:
            if key in self.graph_dict:
                if route not in self.graph_dict[key]:
                    self.graph_dict[key].append(route)
            else:
                self.graph_dict[key]=[route]
        print(self.graph_dict) 

    def get_path(self,start,end,path=[]):
        path=path+[start] 

        if start==end:
            return [path] 

        if start not in self.graph_dict:
            return [] 

        paths=[]

        for key in self.graph_dict[start]:
            if key not in path:
                new_path=self.get_path(key,end,path)
                for p in new_path:
                    paths.append(p)

        return paths 

    def get_path(self,start,end,path=[]):
        path=path+[start] 

        if start not in self.graph_dict:
            return [] 

        if start==end:
            return path


        

if __name__=='__main__':
    routes=[
        ('Mombai','Paris'),
        ('Mombai','Dubai'),
        ('Mombai','Paris'),
        ('Paris','Dubai'),
        ('Paris','New York'),
        ('Dubai','New York'),
        ('New York','Toronto'),
        
        
    ]
    graph=Graph(routes) 
    print(graph.get_path('Toronto','Mombai'))