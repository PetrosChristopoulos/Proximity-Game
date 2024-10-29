#
# Πριν τρέξετε τον παρακάτω κώδικα πρέπει:
# 1) Να εγκαταστήσετε το hexalattice. Aυτό μπορεί να γίνει είτε με την εντολή
#    pip install hexalattice είτε με την εντολή conda install -c conda-forge hexalattice
#    Τις εντολές αυτές τις τρέχετε ή στο command prompt (Windows) ή στο terminal (Linux - MacOS)
# 2) Στις παρακάτω γραμμές που έχουν το σχόλιο CHANGE πρέπει να αντικαταστήσετε το XΧ με τον αριθμό του παίκτη σας.
#    

from hexalattice.hexalattice import *
import random
#            CHANGE
import ProximityXX_Player
import ProximityXX_Player

X = 10
Y = 8

#              CHANGE
board = [ProximityXX_Player.Cell(0,0) for x in range(X*Y)] # Create empty board

#                CHANGE             CHANGE
player1 = ProximityXX_Player.ProximityXX(1, X, Y) #RED player -> 1
player2 = ProximityXX_Player.ProximityXX(2, X, Y) #GREEN player -> 2

player = 1


# = = = = INIT GRAPH = = = = = = = = = = = = = = =
hex_centers, hax = create_hex_grid(nx=X, ny=Y, do_plot=True)

colors = np.ones([X*Y,3])
col = ['white']*(X*Y)

hax = plot_single_lattice_custom_colors(hex_centers[:,0],
                                  hex_centers[:,1],
                                  face_color = colors,
                                  edge_color=colors,
                                  min_diam=0.9,
                                  plotting_gap=0.0,
                                  rotate_deg=0,
                                  h_ax=hax)

annot = ['0' for x in range(X*Y)]
plt_anot = []
for i in range(X*Y):
    plt_anot.append(hax.annotate(annot[i], xy=(hex_centers[i,0],hex_centers[i,1])))
    #plt_anot.append(hax.annotate(annot[i], xy=(hex_centers[i,0],hex_centers[i,1]), xycoords='board'))
plt.show(block=False)
plt.pause(0.2)

# = = = = = = = = = = = = = = = = = = = = = = = =

# = = = CREATE TILE SEQUENCES OF EQUAL SUM = = = 
tiles1 = [random.randint(1,20) for i in range(int(X*Y/2))]
tiles2 = [random.randint(1,20) for i in range(int(X*Y/2))]
dif = sum(tiles1) - sum(tiles2)

while abs(dif) > int(X*Y/2):
    tiles2 = [random.randint(1,20) for i in range(int(X*Y/2))]
    dif = sum(tiles1) - sum(tiles2)

while dif!=0:
    if dif>0:
        for j in range(dif):
            if tiles2[j] < 20:
                tiles2[j] = tiles2[j]+1
    elif dif<0:
        for j in range(abs(dif)):
            if tiles1[j] < 20:
                tiles1[j] = tiles1[j]+1
    dif = sum(tiles1) - sum(tiles2)
print('Difference is: ', dif)
# = = = = = = = = = = = = = = = = = = = = = = = = 
 
sum1 = 0
sum2 = 0
k1 = 0 # tile counter for player 1
k2 = 0 # tile counter for player 2

for i in range(X*Y):
# - - - - - - Player 1 - - - - -   
    if player == 1:
        num = tiles1[k1]
        k1 = k1 + 1
        player = 2
        sum1 = sum1+num

        # ACTUAL PLAY
        board = player1.placeTile(num,board)

        # = = = UPDATE GRAPH = = = 
        for pos, value in enumerate(board):
            plt_anot[pos].set_text(str(value.getValue()))
            if value.getOwner() == 1 and value.getValue() != 0:  # RED
                colors[pos,:] = [1., 0., 0.]
            elif value.getOwner() == 2 and value.getValue() != 0: # GREEN
                colors[pos,:] = [0., 1., 0.]
        hax = plot_single_lattice_custom_colors(hex_centers[:,0],
                                      hex_centers[:,1],
                                      face_color = colors,
                                      edge_color=colors,
                                      min_diam=0.9,
                                      plotting_gap=0.0,
                                      rotate_deg=0,
                                      h_ax=hax)
        # = = = COUNT TILES = = = = 
        RED = 0
        GREEN = 0
        for num in board:
            if num.getOwner() == 1:
                RED += num.getValue()
            else:
                GREEN += num.getValue()
        plt.title('Red: '+ str(RED) + ' Green: ' + str(GREEN))
        plt.show(block=False)
        plt.pause(0.9)    
# - - - - End of Player 1 - - - - 
    else:
# - - - - - - Player 2 - - - - - 
        num = tiles2[k2]
        k2 = k2 + 1
        player = 1
        sum2 = sum2+num

        # ACTUAL PLAY
        board = player2.placeTile(num,board)

        # = = = UPDATE GRAPH = = =
        for pos, value in enumerate(board):
            plt_anot[pos].set_text(str(value.getValue()))
            if value.getOwner() == 1 and value.getValue() != 0:  # RED
                colors[pos,:] = [1., 0., 0.]
            elif value.getOwner() == 2 and value.getValue() != 0: # GREEN
                colors[pos,:] = [0., 1., 0.]
        hax = plot_single_lattice_custom_colors(hex_centers[:,0],
                                      hex_centers[:,1],
                                      face_color = colors,
                                      edge_color=colors,
                                      min_diam=0.9,
                                      plotting_gap=0.0,
                                      rotate_deg=0,
                                      h_ax=hax)
        # = = = COUNT TILES = = = =
        RED = 0
        GREEN = 0
        for num in board:
            if num.getOwner() == 1:
                RED += num.getValue()
            else:
                GREEN += num.getValue()
        plt.title('Red: '+ str(RED) + ' Green: ' + str(GREEN))
        plt.show(block=False)
        plt.pause(0.9)    
#  - - - - - End of Player 2 - - - - - 


RED = 0
GREEN = 0
for num in board:
    if num.getOwner() == 1:
        RED += num.getValue()
    else:
        GREEN += num.getValue()
    

print('THE END')
print('Green:', GREEN)
print('Red:', RED)
print('Sum 1: ', sum1)
print('Sum 2: ', sum2)

