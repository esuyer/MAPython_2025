import os
# Audio fix for headless environments
os.environ['SDL_AUDIODRIVER'] = 'dummy'
import pygame

pygame.init()

WIDTH=800
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Homework 9")
clock=pygame.time.Clock()

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)

font=pygame.font.SysFont("arial", 24)

print("Problem 1\n")
nums = []
for _ in range(5):
    nums.append(int(input("Give me a number: ")))

print("First plus last: ", nums[0] + nums[-1])
for n in nums:
    print(n)

print("Odd numbers only: ")
for n in nums:
    if n % 2 == 1:
        print(n)

print("\nProblem 2\n")
friends = []
f_count = int(input("How many friends do you want to invite: "))
for _ in range(f_count):
    name = input("Enter a name: ")
    friends.append(name)
print(friends)

print("\nProblem 3\n")
multi = []
h = int(input("Give me a number: "))
for i in range(h):
    multi.append("*" * (i + 1))
print(multi)

print("\nProblem 4\n")
print("Enter 4 pokemon for Jake:")
jake = [input(f"Jake's pokemon {i+1}: ") for i in range(4)]
print("\nEnter 4 pokemon for Andrew:")
andrew = [input(f"Andrew's pokemon {i+1}: ") for i in range(4)]

print("Jake's pokemon: ", jake)
print("Andrew's pokemon: ", andrew)
print("Different pokemon in Jake's list compared to Andrew's at same index: ")
for i in range(len(jake)):
    if jake[i] != andrew[i]:
        print(jake[i])

print("\nProblem 5\n")
colours = []
q = int(input("How many colours do you want to enter: "))
for i in range(q):
    r = input("Enter a colour: ")
    colours.append(r)

# Replacement for turtle using Pygame
print("\nRendering Pygame window for Problem 5 visualization...")
running = True
drawn = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    
    # Draw "stamps" for colours
    x_pos = 100
    for c_name in colours:
        try:
            # Simple color mapping for common turtle colors
            color = pygame.Color(c_name)
        except:
            color = WHITE
            
        pygame.draw.circle(screen, color, (x_pos, HEIGHT//2), 20)
        x_pos += 100
        if x_pos > WIDTH - 50:
            break

    txt = font.render("Problem 5: Colour Stamps (Pygame Replacement for Turtle)", True, WHITE)
    screen.blit(txt, (20, 20))
    
    pygame.display.flip()
    clock.tick(60)
    
    if not drawn:
        print("Visualization active in VNC view. Close the window or stop the workflow to exit.")
        drawn = True

pygame.quit()
