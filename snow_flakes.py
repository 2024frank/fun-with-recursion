#snow_flakes
import picture
from math import sqrt
def snowflake(length, depth):
    """
    Recursively draw one side of the Koch Snowflake.
    
    Parameters:
    length (float): Length of the current line segment.
    depth (int): Current recursion depth.
    """
    if depth == 0:
        return
    if depth == 1:
        # Base case: Draw a straight line of the given length
        picture.draw_forward(length)
        return
    
    # Calculate the length of each smaller segment
    sub_length = length / 3
    
    # Recursive calls for the four segments
    snowflake(sub_length, depth - 1)  # First segment
    picture.rotate(-60)                    # Turn left for the peak
    snowflake(sub_length, depth - 1)  # Second segment
    picture.rotate(120)                    # Turn right for the peak
    snowflake(sub_length, depth - 1)  # Third segment
    picture.rotate(-60)                    # Return to original direction
    snowflake(sub_length, depth - 1)  # Final segment

def draw_snowflake(length, depth):
    """
    Draw the complete Koch Snowflake.
    
    Parameters:
    length (float): Length of each side of the initial equilateral triangle.
    depth (int): Recursion depth of the snowflake.
    """
    # Draw the three sides of the snowflake
    for _ in range(3):
        snowflake(length, depth)
        picture.rotate(120)  # Rotate 120 degrees clockwise for the next side

def call_snow_flakes(size, depth):
    """
    Main function to set up the canvas and draw the snowflake.
    """
    # Calculate length and depth
   # Length of each side of the triangle
    
    # making the lenth of the triangle size depend on the canvas size
    length = int(sqrt(2*((size//2)*(size//2))) - (sqrt(2*((size//2)*(size//2))))*0.3)
    
    # Ensure a minimum canvas size
    
    
    # Create picture with calculated size
    picture.new_picture(size, size)
    
    picture.set_fill_color("purple")
    picture.draw_filled_square(0, 0, size)

    picture.set_pen_width(5)

    picture.set_outline_color("white")
    
    
    picture.set_position(size//2 -length//2, size//3)
    
    # Draw the snowflake
    draw_snowflake(length, depth)
    
    # Save the final image
    picture.save_picture("snowflake.png")

