class Hero():
    def changeMode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True
            
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5)% 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5)% 360)
    def forward(self):
        angle =(self.hero.getH()+0) % 360
        self.move_to(angle)
    def up(self):
        self.hero.setZ(self.hero.getZ()+1)
    def down(self):
        self.hero.setZ(self.hero.getZ()-1)
    def back(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
    
    
    

    
    
        
        
    def __init__(self, pos, land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3) 
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.mode = True
    def just_move(self)
        
        self.cameraBind()
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True
    def cameraUp(self):
        base.mouseInterfaceNode(-pos[0], -pos[1], -pos(2)-3)
        self.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
        
    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.builbBlock(pos)
        
        def pac(self):
            angle = self.hero.getH() % 360
            pos = self.look_at(angle)
            if self.mode:
                self.land.addpac(pos)
            else:
                self.land.buildBlock(pos)
        def destroy(self):
            angle = self.hero.getH() % 360
            pos = self.look_at(angle)
            if self.mode:
                self.land.delBlock(pos)
            else:
                self.land.delBlockFrom(pos)
        
     
        
        self.accept_events()
        
    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('n', self.turn_left)
        base.accept('n'+'-repeat', self.turn_left)
        base.accept('m', self.turn_right)
        base.accept('m'+'-repeat', self.turn_right)
        base.accept('s', self.back)
        base.accept('s'+'-repeat', self.back)
        base.accept('w', self.forward)
        base.accept('w'+'-repeat', self.forward)
        base.accept('a', self.left)
        base.accept('a'+'-repeat', self.left)
        base.accept('d', self.right)
        base.accept('d'+'-repeat', self.right)
        base.accept('e', self.up)
        base.accept('e'+'-repeat', self.up)
        base.accept('r', self.down)
        base.accept('r'+'-repeat', self.down)
        base.accept('z', self.changeMode)        
        base.accept('v', self.destroy)
        base.accept('k', self.land.saveMap)
        base.accept('k', self.land.loadMap)
        
        
        
        

        
    def turn_left(self):
        self.hero.setH((self.hero.getH() +5) % 360)
    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()
    
    
    def just_move(self, angle):
        from_x = round(self.Hero.getX())
        from_y = round(self.Hero.getY())
        from_z = round(self.Hero.getZ())
        
        
        dx, dy = self.hero.check_dir(self, angle)
        return from_x + dx,from_y + dy, from_z
        


    def try_move(self, angle):
        pass
    def move_to(self, angle):
        pass
    def look_at(self, angle):
        pass
    def check_dir(self, angle):
        pass
    
    def check_dir(self, angle): 
        if angle >= 0 and angle <= 20: 
            return 0, -1 
        elif angle >20 and angle <= 65: 
            return +1, -1 
        elif angle >= 65 and angle <= 110: 
            return +1, 0
        elif angle >=110 and angle <= 155:
            return +1, +1
        elif angle >=155 and angle <= 200:
            return 0, +1
        elif angle >=200 and angle <= 245:
            return -1, +1
        elif angle >=245 and angle <= 290:
            return -1, 0
        elif angle >=290 and angle <= 335:
            return -1, -1
        elif angle >=335 and angle <= 0:
            return 0, -1
        
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def forward (self):
            angle = (self.hero.getH() + 0) % 360
            self.move_to(angle)
    def back (self):
            angle = (self.hero.getH() + 180) % 360
            self.move_to(angle)
    def left (self):
            angle = (self.hero.getH() + 90) % 360
            self.move_to(angle)
    def right (self):
            angle = (self.hero.getH() + 270) % 360
            self.move_to(angle)
    
    
    
        
 