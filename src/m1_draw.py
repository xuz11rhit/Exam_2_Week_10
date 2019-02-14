###############################################################################
#   You are going to do a great job on this exam!
#   Read each question carefully.
#   Be sure to commit and push after each question
#   Be sure to right-click on src, and Mark Directory as Sources root
#   You will be asked to write 3 functions that demonstrate your
#   understanding of the concepts covered in class
#
###############################################################################
import rosegraphics as rg


def main():
    #
    #   Tests are called from here.  Do not make any changes to main
    #
    test_draw_a_picture()


def test_draw_a_picture():
    ###############################################################################
    #   This method tests draw_a_picture
    #
    ###############################################################################
    point1 = rg.Point(100, 100)
    n = 10
    test_window = rg.RoseWindow(500, 500)

    #  tests draw_a_picture with point 1, n=10, and test_window
    print('###################################################')
    print('Test 1 of draw_a_picture.')
    print('Called with point1 =', point1)
    print( 'n =', n, ' color = blue')
    print('###################################################')
    draw_a_picture(point1, n, 'blue', test_window)

    point2 = rg.Point(100, 300)
    n = 4
    #  tests draw_a_picture with point 2, n =4, test_window
    print('###################################################')
    print('Test 2 of draw_a_picture.')
    print('Called with point2 =', point2)
    print( 'n =', n, ' color = green')
    print('###################################################')
    draw_a_picture(point2, n, 'green', test_window)
    test_window.close_on_mouse_click()


###############################################################################
# def draw_a_picture(point, n, color, window):
#     """
#     See   m1_draw_problem_picture.pdf   in this project for pictures
#     that may help you better understand the following specification:
#
#     What comes in:
#       -- An rg.Point.
#       -- A positive integer n.
#       -- A fill-color
#       -- An rg.RoseWindow.
#
#     What goes out:  Nothing (i.e., None).
#     Side effects:
#       Draws an rg.Circle with the given point as the center.
#       The radius of the rg.Circle is 200 pixels
#       Draws an rg.Rectangle with the given point as the center.
#       The width of the Rectangle is 160 pixels and the height is 80 pixels
#       Draws n lines from the Center of the Rectangle to the top line
#       of the Rectangle that are equally spaced
#       The color is used as the line colors unless the number of the line
#       is prime.  If the number of the line is prime,
#       the color should be 'orange'.
#
#       -- There is a 0.5 second pause after each rg.Circle is drawn.
#       Must  ** NOT close **   the window.
#
#     Type hints:
#       :type circle: rg.Circle
#       :type n: int
#       :type window: rg.RoseWindow
#   The is_prime function is supplied.  Do NOT change is_prime
#     """
# -------------------------------------------------------------------------
#  TODO: 1. Implement and test the draw_a_picture function.
#           Tests have been written for you (above in main).
#  We suggest breaking this into multiple commits.
#     Can you show the correct circle?
#     Can you make the correct rectangle?
#     Are they in the correct location?
#     Can you draw equally spaced lines?  Are they the correct color?
#     Finally, can you make the lines whose numbers are prime orange?
############################################################################
# HINT:   render(0.5)
#         renders with a half-second pause after rendering.
############################################################################
# -------------------------------------------------------------------------
#
#
#
def draw_a_picture(point, n, color, window):

    pass


main()