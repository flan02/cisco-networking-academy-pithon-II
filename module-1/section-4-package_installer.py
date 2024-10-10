# pip --version
# pip show pip
# pip help
# pip help install
# pip list
# pip show package_name

# pip install -U package_name

# pip install pygame==package_version
# pip install pygame==1.9.2

# pip uninstall package_name

# pip search package_name # ! DEPRECATED
# TODO: Find your desired package on the website 
""" https://pypi.org/search/ """

# ? Install depency first before run the code below.
""" 
import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
  for event in pygame.event.get():
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False
"""