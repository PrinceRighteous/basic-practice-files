import pygame

class skeleton_sprite(pygame.sprite.Sprite):
    def __init__(self, s_list ,x, y, Moving):
        super().__init__()
        self.Moving = Moving
        self.sprite_list = s_list
        self.current_sprite = 0
        self.image = self.sprite_list[self.current_sprite]

        #rectangle:
        self.rect = self.image.get_rect(center = (x,y))


    def update(self):
        #RIGHT MOVEMENT MAY NEED TO MAKE SEPARATE CLASS and add pygame.display.update()
        self.current_sprite = 2
        self.current_sprite += 1
        self.image = self.sprite_list[self.current_sprite]
        if self.current_sprite >= 4:
            self.current_sprite = 2
            self.image = self.sprite_list[self.current_sprite]
        if self.Moving == False:
            self.current_sprite = 1
            self.image = self.sprite_list[self.current_sprite]





#sprite class group & objects:
x_pos, y_pos = 600, 550
sprite_group = pygame.sprite.Group()
skele = skeleton_sprite(SKELETON_IMAGES_TRANSFORMED, x_pos, y_pos, moving)
sprite_group.add(skele)






key_pressed = pygame.key.get_pressed()


sprite_group.update()
moving = True
sprite_group.draw(OUR_SCREEN) #can only use this function from group sprite variable because it's an attribute of pygame.sprite.Sprite class