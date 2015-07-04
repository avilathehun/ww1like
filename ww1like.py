import libtcodpy as libtcod

#Python doesn't have any hard rules about what's a constant and what isn't, so assume that anything
#in all caps like this should be treated like a constant.  If you ever assign these a new value, you
#are probably doing something wrong.
SCREEN_WIDTH = 200
SCREEN_HEIGHT = 50

#Set our custom font
libtcod.console_set_custom_font('terminal10x16_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

#Open the game window
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Let\'s all ganbare hard today!', False)

#Our global variables (python is stupid about this imo)

(playerx, playery, playerhp, playerstam, playersan, ticks) = (0, 0, 0, 0, 0, 0)

#Initialize the game.
def game_init():
    global playerx, playery, playerhp, playerstam, playersan, ticks
    playerx = SCREEN_WIDTH / 2
    playery = SCREEN_HEIGHT / 2
    playerhp = 100
    playerstam = 100
    playersan = 100
    ticks = 0
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, playerx, playery, '@', libtcod.BKGND_NONE)

#Defining a function that will handle all keypresses for us.
def handle_keys():
    global playerx, playery, ticks
    key = libtcod.console_wait_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True
    
    #Nonmovement commands.
    
    #Important note regarding movement: right means POSITIVE X, down means POSITIVE Y
    #Movement commands.
    libtcod.console_put_char(0, playerx, playery, ' ', libtcod.BKGND_NONE)
    if libtcod.console_is_key_pressed(libtcod.KEY_UP) or libtcod.console_is_key_pressed(libtcod.KEY_KP8):
        playery -= 1
    
    if libtcod.console_is_key_pressed(libtcod.KEY_DOWN) or libtcod.console_is_key_pressed(libtcod.KEY_KP2):
        playery += 1 
        
    if libtcod.console_is_key_pressed(libtcod.KEY_LEFT) or libtcod.console_is_key_pressed(libtcod.KEY_KP4):
        playerx -= 1
        
    if libtcod.console_is_key_pressed(libtcod.KEY_RIGHT) or libtcod.console_is_key_pressed(libtcod.KEY_KP6):
        playerx += 1
        
    if libtcod.console_is_key_pressed(libtcod.KEY_KP7):
        playerx -= 1
        playery -= 1
        
    if libtcod.console_is_key_pressed(libtcod.KEY_KP9):
        playerx += 1
        playery -= 1
        
    if libtcod.console_is_key_pressed(libtcod.KEY_KP1):
        playerx -= 1
        playery += 1
    
    if libtcod.console_is_key_pressed(libtcod.KEY_KP3):
        playerx += 1
        playery += 1
        
    

#Do all the things enemies do.
def enemy_action():
    print 'do shit here please'

#Actual game bullshit now
#Initialize
game_init()
while not libtcod.console_is_window_closed():
    #Game logic loop.
    #HELLO YES THIS IS GAMEPLAY
    
    #Erase the old player position.
    
    #Get key input.
    k = handle_keys()
    if k:
        #handle_keys only returns true if you press esc, so we'll quit if they press escape.
        #break causes us to exit the while loop prematurely, leading to the game closing.
        break
    libtcod.console_put_char(0, playerx, playery, '@', libtcod.white)
    #End of game loop; flush the console.
    libtcod.console_flush()
