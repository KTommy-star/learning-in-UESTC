'''Vertex 类的实现，其构造方法简单地初始化 id（它通常是一个字符串），以及字典connectedTo。'''
from KTommy.数据结构与算法.队列练习 import Queue


class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}

    #addNeighbor方法添加从一个顶点到另一个的连接
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    #getConnections 方法返回邻接表中的所有顶点，由 connectedTo 来表示。
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
'''Graph 类的实现，其中包含一个将顶点名映射到顶点对象的字典。
Graph 类也提供了向图中添加顶点和连接不同顶点的方法。
getVertices 方法返回图中所有顶点的名字。此外，我们还实现了__iter__方法，从而使遍历图中的所有顶点对象更加方便'''
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices=0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self, n):
        return n in self.vertList
    #创建一条从 f 指向 t 的有向边:参数分别为：起点，终点，权重
    def addEdge(self, f, t, cost=0):
         if f not in self.vertList:
            nv = self.addVertex(f)
         if t not in self.vertList:
            nv = self.addVertex(t)
         self.vertList[f].addNeighbor(self.vertList[t], cost)
    def getVertices(self):#图当中所有的顶点，作为列表返回
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())
#总之，这两个方法使我们能够根据顶点名或者顶点对象本身遍历图中的所有顶点

'''接下来是图的应用'''
#1.词梯问题:我们的目标是找到最短的单词变换序列
#将可能得单词之间的演变关系表达为图，采用“广度优先搜索BFS”，来搜寻从开始单词到结束单词之间的所有有效路径，选择其中最快到达目标单词的路径
#①建立单词关系图
#思路：首先将所有单词作为顶点加入图中，再设法建立顶点之间的边，除了最直接的比较算法，还可以改进：
#创建大量的桶，每个桶可以放若干单词，桶标记是去掉一个单词，"_"占空的单词，所有匹配标记的单词放在桶中，同一个桶之间，桶之间建立联系
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')#打开单词词库，wordfile可替换为文件路径
    # 创建词桶
    for line in wfile:
        word = line [:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]#当某个通配符模式（bucket）首次出现时，在字典 d 中创建一个新的键值对
                                  #而这里的键值对的结构是：键：bucket-->值（一个列表，包含所有匹配该模式的单词）
                                  #所以这里是创建了一个bucket键对应的值列表，并将word作为第一个单词存进去，以便后续单词加入
    # 为同一个桶中的单词添加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)#通过双重循环比较两个word，若不相等，则建立边
    return g
#②实现广度优先搜索
#BFS搜索所有从起始顶点可到达顶点的边，在到达更远的距离k+1的顶点之前，会先找到距离为k的所有顶点
#为了追踪顶点的加入过程，避免重复搜索定带你，需要增加三个属性
#distance:从起始定带你到此顶点的路径长度；前驱顶点predecessor:可反向追溯到起点；
#颜色color:尚未发现（白）、已经发现（灰）、已经完成探索（黑色）
#此外还需要用一个Queue来对已发现的顶点进行排列，决定下一个要探索的顶点（队首）
def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue=Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size()>0):
        currentVert=vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor()=='white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance()+1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')
#最后可通过回溯，来确定起始单词到任何单词顶点的最短词梯
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

    traverse(g.getVertex('sage'))

#2.骑士周游问题：
#思路：首先将合法走棋次序表示为一个图；采用DFS算法2搜寻一个长度为（行*列-1）的路径，路径上包含每个顶点恰一次
#①首先设置合法走棋位置：
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]#这是马走日8个格子
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves
#确认不走出棋盘
def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
#②构建走棋关系图
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)#单步合法走棋，把合法走棋的位置加到newPosition里面
            for e in newPositions:
                nid = posToNodeId(e[0], e[1])
                ktGraph.addEdge(nodeId, nid) #添加边以及顶点
    return ktGraph
def posToNodeId(row,col,bdSize):
    return row*bdSize+col
#③深度优先搜索DFS（骑士周游问题）：每个顶点只访问一次
def knightTour(n,path,u,limit):#n：层次；path：路径；u：当前顶点；limit：搜索总深度
    u.setColor('gray')
    path.append(u)#当前节点加入路径
    if n < limit:
        nbrList = list(u.getConnections())#对所有合法移动逐一深入
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':#选择白色未经过的顶点深入
                done = knightTour(n + 1,path,nbrList[i],limit)#层次+1，递归深入
            i = i + 1
        if not done:  # 准备回溯
            path.pop()#都无法完成总深度，回溯，尝试本层下一个顶点
            u.setColor('white')
    else:
        done = True
    return done
#③-plus：算法改进：对nbrlist灵巧构造，以特定方式排列顶点访问词素-->Warnsdorff算法
#将u的合法移动目标棋盘格排序为：具有最少合法移动目标的格子优先搜索，谁往前的路越少，就先选谁
def orderByAvail(n):
    resList = []#初始化空列表 resList，用于存储排序后的节点信息。
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0#初始化计数器 c，用于统计 v 的未访问邻居数量
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c= c + 1
            resList.append((c, v))#将 (c, v) 元组添加到 resList，其中 c 是 v 的未访问邻居数量。
    resList.sort(key = lambda x: x[0])#对 resList 按 c 的值升序排序（未访问邻居少的节点排在前面）
    return [y[1] for y in resList]#返回排序后的节点列表，仅包含 v（去掉计数器 c
#这个排序能够将未访问邻居少的节点排在前面，也就是把“路”最少的排在前面，使得整体的算法效率提高很多
#3.通用的深度优先搜索
from pythonds.graphs import Graph
#顶点vertex增加了成员discovery和finish;图graph增加了成员time用于记录算法执行的步骤数目
class DFSGraph(Graph):
    def __init__(self):
        super(). __init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')#颜色初始化--白色
            aVertex.setPred(-1)
        for aVertex in self:#对于未访问的节点（白色），创建一棵树，如果还未包括的顶点，则继续创建树，可能构成森林
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1#算法的步数
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():#对于起始顶点的蓑鲉节点一次访问
            if nextVertex.getColor() == 'white':#如果发现是白色
                nextVertex.setPred(startVertex)#则将下一个节点设置为灰色
                self.dfsvisit(nextVertex)#递归调用dfs继续向下向深搜索
        startVertex.setColor('black')#每个节点都探索完毕后，将节点设置为黑色，结束
        self.time += 1
        startVertex.setFinish(self.time)