class Graph:
    def __init__(self , vertices , directed , *edges):
        self.n = len(vertices)
        self.vertex_name ={}
        idx = 0
        for vertex in vertices:
            self.vertex_name[idx] = vertex
            idx+=1
        self.directed = directed
        self.adj = []
        for i in range(self.n):
            l = []
            for j in range(self.n):
                if((self.vertex_name[i],self.vertex_name[j]) in edges): l.append(1)
                elif(self.directed == False and (self.vertex_name[j],self.vertex_name[i]) 
                     in edges): 
                    l.append(1)
                else : l.append(0)
            self.adj.append(l)
    def bfs(self , root = 0):
        vis = [0]*self.n
        q = [(root , 0)]
        order = []
        levels = []
        curr = 0
        while(len(q)):
            top , level = q[0]
            q.pop(0)
            order.append(top)
            vis[top] = 1
            if(level>=curr):
                levels.append([top])
                curr+=1
            else: levels[level].append(top)
            for j in range(self.n):
                if(self.adj[top][j]==1 and vis[j]==0): q.append((j , level+1))
        return [self.vertex_name[ele] for ele in order] , [[self.vertex_name[ele] for ele in k] 
                                                      for k in levels]
def main():
    g = Graph(['A' , 'B' , 'C' ,'D' , 'E' , 'F'] , False , ('A','B') , ('B','D') , ('B','E') , ('B','F'), ('A','C'))
    ans = g.bfs()
    print("Levels of traversal: " , ans[1])
    print("Traversal order: ", ans[0])
main()