
#from direct.showbase.ShowBase import ShowBase

class Mapmanager():
    def __init__(self, base):
        self.base = base
        self.model = 'cubik.obj.obj'  # Модель кубика
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

    def addBlock(self, position):
        # Завантаження моделі та текстури
        pos = position
        self.block = self.base.loader.loadModel(self.model)  # Використовуємо self.base.loader
        self.block.setTexture(self.base.loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        self.color = self.getColor(position[2])
        self.block.setColor(self.color)
        self.block.setTag("at", str(pos))
    def findBlocks(self, pos):
        return self.land.findAllMatches('=at=' + str(pos))
    
    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()
    
    def delBlockFrom(self, posotion):
        x, y, z = self.findHighestEmpty(pos)
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
     
    def loadLand(self, filename):
        # Clear existing land and load new one
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')  # Split line into individual elements
                for z in line:
                    for z0 in range(int(z) + 2):
                        block = self.addBlock((x, y, z0*2))  # Add a block at (x, y, z0)
                    x += 2
                y += 2
    def getColor(self, z):
        # Ensure the z value is within bounds of the colors array
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len (self.colors) -1]  # Return the last color if out of bounds