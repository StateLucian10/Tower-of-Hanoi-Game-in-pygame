

 ###contains 3 files:
- _main.py_  - where the game is located
- _button.py_ - where I created the buttons
- _images_  - where the images in the game are located

## main.py explanation:

### Create Screen:
- First time I import the libraries that helped me to write the code.
- I created the screen using pygame.display.set_mode.
- I created some fonts for my text.
- I updated the icon and the title of the game on the display using pygame.display.set_icon and pygame.display.set_caption.

### Game Variables:

- I created the game variables that I will use in the game.
- Tower1, Tower2, Tower3 store the disks that are currently in them.
- DISK_NUMBER will store the disks number
- precedentTower will store the nome the name of the tower from which the disk was extracted. This will help if the player put the disk to a wrong place
- moves variable will store the number of the moves that the player or computer made
- active_disc will store the index of the current disk that is moved
- In objects_rect list will be store the disks rect
- In the position list will be store the position of every disk

### Create the Towers and the disks:
- I loaded all the images from the game using pygame.image.load.
- I created all buttons using the class that I defined in _buttons.py_.
- I created the Towers using the images, and after I created a rect around them that helped me to check for collision.
- I created the disks and I store them in objects_rect and the coordinates of the every disk is stored in position list.
- I added all disks in the Tower1 list because at the start all disks is in the first tower.

### Helper Functions:
- I created a function that will draw all the disks
- check_collision() will check for collision between a disk and a tower.
- draw_text() will print all texts
- the draw() function helped me to update the screen for every computer move.
- move_disc() function helped me to move the disks to different towers and update the towers lists and position of every disk.
- hanoi_move() function helped me to make all the movements of the computer in different towers and also to call the draw() function where each movement of the computer will be updated. I used time.sleep() to wait after each computer move.
- hanoi() is a recursive function that is called by itself to guide the calculator in making the necessary moves for the solution.

### Game Loop
- I created an infinite while loop to run the game until the quit button or the cross is pressed

#### Menu:
- If the menu button is pressed the game will be paused using game_paused variable
- Resume button will resume the game
- Solve button will make the computer to solve the game
- Quit will exit the game

#### Game
- If the game is not paused the game will display all the images, texts and buttons
- If the restart button is pressed will restart all variables from 0
- If the up arrow is pressed will restart all variables from 0 and will increase DISC_NUMBER.
- If the down arrow is pressed will restart all variables from 0 and will decrease DISC_NUMBER.
- If the Tower3 list contains al of the disks the game will end and will display "Great Job!!".

#### Events
- I created a for loop that handles al off the game events
- If the right mouse button is down the game will check for collision between mouse and the first smaller disk from Towers.
- If the correct disk was clicked the active_disc variable will change to current disk and also the Towers list will be updated.
- If the mouse moves the disk will follow the mouse
- If the right button is up the game will check for collision between the disk and towers. If the disk is put in a correct tower the Towers variables will be updated and the position of the disk will be changed using move_disc() function. If thed disk is put in a wrong place the disk will be moved back to his position.
- If cross is pressed the game loop will end
- pygame.display.flip() will update the game at every iteration of the game loop
