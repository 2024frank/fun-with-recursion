import picture

def carpet(x, y, length, depth):
    """
    Recursively draw a Sierpinski Carpet fractal.
    
    Parameters:
    x (int): x-coordinate of the top-left corner of the square
    y (int): y-coordinate of the top-left corner of the square
    r (int): side length of the square
    depth (int): recursion depth of the fractal
    """
    if depth > 0:
        # Calculate the size of each sub-square
        sub_length = length // 3
        
        # Draw the central square
        picture.draw_filled_square(x + sub_length, y + sub_length, sub_length)
        
        # Recursively draw 8 surrounding squares
        for i in range(3):
            for j in range(3):
                # Skip the central square
                if i == 1 and j == 1:
                    continue
                
                # Calculate new x and y for each sub-square
                new_x = x + i * sub_length
                new_y = y + j * sub_length
                
                carpet(new_x, new_y, sub_length, depth - 1)

def call_carpet(size, depth):
    # Set the dimension of the canvas
   
    
    # Create the canvas
    picture.new_picture(size, size)
    
    # background
    picture.set_fill_color("coral")
    picture.set_outline_color("coral")
    picture.draw_filled_square(0, 0, size)
    
    # Set fractal colors
    picture.set_fill_color("moccasin")
    picture.set_outline_color("moccasin")
    depth = 5
    # Draw the Sierpinski Carpet
    carpet(0, 0, size, depth)

    
    # Save the fractal image
    picture.save_picture("carpet.png")

