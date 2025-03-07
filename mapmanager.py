import pickle
from direct.showbase.ShowBase import ShowBase

class Mapmanager():
    def __init__(self, base):
        self.base = base
        self.model = 'Cube.obj'  # Модель кубика
        self.texture = 'bedrockpng.png'  # Текстура кубика
        self.land = self.base.render.attachNewNode("Land")  # Створення вузла для "землі"
        self.colors = [(0.5, 0.3, 0.0, 1),
                        (0.2, 0.2, 0.3, 1),
                        (0.5, 0.5, 0.2, 1),
                        (0.0, 0.6, 0.0, 1)]
    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)


    def addBlock(self, position, model=None, texture=None):
        # Завантаження моделі та текстури
        model_to_use = model if model else self.default_model
        texture_to_use = texture if texture else self.default_texture
        pos = position
        self.block = self.base.loader.loadModel(model_to_use)
        self.block.setTexture(self.base.loader.loadTexture(texture_to_use))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        self.color = self.getColor(position[2])
        self.block.setColor(self.color)
        self.block.setScale(0.5)
        self.block.setTag("at", str(pos))
    def findBlocks(self, pos):
        return self.land.findAllMatches('=at=' + str(pos))

    def setBlockType(self, model, texture):
        # Метод для зміни типу блоку
        self.model = model
        self.texture = texture

    def getColor(self, height):
        # Вибір кольору в залежності від висоти
        return self.colors[height % len(self.colors)]

    
    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()
    
    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty(position)
        pos = x, y, z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()
            
    def buildBlock(self, pos):
        x, y, z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
            self.addBlock(new) 
        # Додаємо блок до "землі"

    def startNew(self):
        # Скидання або оновлення "землі"
        self.land.removeNode()
        self.land = self.base.render.attachNewNode("Land")

    def clear(self):
         self.land.removeNode()
         self.startNew()
     
    def loadLand(self. filename) : 
        self.clear() 
        with open(filename) as file: 
            У = 0 
            for line in file: 
            x = 0 
            line = line.split(' ')
             for z in line:
                 for z0 in range(int(z) + 2):
                    block = self.addBlock((x, y, z0 * 2))
                x += 2
            y += 2
    

    def isEmpty(self, pos):
        blocks = self.findBlocks(pos)
        if blocks:
            print("зайнято")  # delete
            return False
        else:
            print("вільно")  # delete
            return True

    def findHighestEmpty(self, pos):
        x, y, z = pos
        z = 1
        while not self.isEmpty((x, y, z)):
            z += 1
        return (x, y, z)

    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat', 'wb') as fout:
            pickle.dump(len(blocks), fout)
            for block in blocks:
                x, y, z = block.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, fout)

    def loadMap(self):
        self.clear()
        with open('my_map.dat', 'rb') as fin:
            length = pickle.load(fin)
            for i in range(length):
                pos = pickle.load(fin)
                self.addBlock(pos)
