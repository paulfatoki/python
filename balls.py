#list of balls to pick the yellow ball
pickyellowball=[]
balls=['black'] * 3 + ['yellow'] * 4 + ['white'] * 5
for ball in balls:
    if ball == 'yellow':
        print("you picked yellow ball!")
