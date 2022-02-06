These scripts can generate grids of random dots with different colours, black and white noise, any pixel draws and patterns like a chess board.

I put some of these designs also on objects like t-shirt, hats, mugs, puzzles, pillows, buttons, etc. You can find them here: https://www.redbubble.com/people/Mmark94/shop?asc=u

Black and white noise
black_and_white_noise.py

You can set the dimension of your grid.
In the example there are grids of 10x10, 100x100 and 1000x1000
![grid1](media/Grid_10.png)

![grid2](media/Grid_100.png)

![grid3](media/Grid_1000.png)


You can set a different probability for each colour.
In the example I set probability 100:1, 10:1, 1:1, 1:10 and 1:100
![grid1](media/Grid_p_500_100_1.png)

![grid1](media/Grid_p_500_10_1.png)

![grid1](media/Grid_p_500_1_1.png)

![grid1](media/Grid_p_500_1_10.png)

![grid1](media/Grid_p_500_1_100.png)

You can also set a gradient of probability for each colour.
black_and_white_noise_probabilities.py

![grid1](media/grid_100_gradient0.1_w1_b500.png)

![grid1](media/grid_100_gradient-0.0001_w1_b1.png)

![grid1](media/grid_500_gradient0.0002_w1_b25.png)

![grid1](media/grid_1000_gradient0.0001_w1_b25.png)

![grid1](media/grid_1000_gradient-1e-06_w1_b1.png)


You can set how much connectivity there is in the black and white noise.
For example, high connectivity means that the probability of a square being one colour is greater if the previous square is the same colour (positive feedback).
Low connectivity means that the probability of a square being one colour is greater if the previous square is a different colour (negative feedback).
black_and_white_noise_probabilities.py

high connectivity
![gridp](media/Grid_100_p5.png)

low connectivity
![gridp](media/Grid_100_p9.png)

with different grid dimensions
![gridp](media/Grid_100_p16.png)

![gridp](media/Grid_100_p18.png)

![gridp](media/Grid_100_p22.png)

![gridp](media/Grid_100_p20.png)

You can choose as many colours as you like.

![grid2](media/Grid_c_30.png)

![grid2](media/Grid_c_100_1.png)

![grid2](media/Grid_c_1000.png)

![grid2](media/grid_100_yellow.png)

You can change the layout of the blocks; they can also have a frame.

![grid2](media/Grid_l_10.png)

![grid2](media/Grid_l_50.png)

You can also save a grid or draw it using 0 and 1 or as many colours as you want.
draw_with_grid.py

![grid2](media/smile2.png)

![grid2](media/draw1.png)

You can also generate a pattern.
In the example, I generated a chessboard pattern.
chess_board.py

![grid2](media/chess_board.png)

![grid2](media/chess_board2.png)

![grid2](media/chess_board3.png)

You can generate many other patterns. You can also create random patterns.
Pattern_generator.py

![grid_patterns](media/pattern-2.png)

![grid_patterns](media/pattern-4.png)

![grid_patterns](media/pattern-5.png)

![grid_patterns](media/pattern-10.png)

![grid_patterns](media/pattern-13.png)

![grid_patterns](media/pattern-14.png)

![grid_patterns](media/pattern-15.png)

![grid_patterns](media/pattern-17.png)

![grid_patterns](media/pattern-18.png)

![grid_patterns](media/pattern-19.png)

You can also use trigonometric functions (cos(x), sin(x)) to generate a pattern.

![grid_patterns](media/pattern-cos.png)

![grid_patterns](media/pattern-cos3_cube.png)