def rotateImage(image):
    """
    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Note:

    You have to rotate the image in-place, which means you have to modify the 
    input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    """

    # the 3 x 3 example is misleading! Try 4 x 4

    # idea: rotate in layers!
    n = len(image)
    # just found a relation between dimension and # layers.
    num_layers = (n - 1) % 2 + 1

    for i in range(num_layers):
        # store the 'edge size' of that layer
        for j in range(i, n-i-1):
            image[i][j], image[j][n - i - 1], image[n - i - 1][n - j - 1], image[n - j -
                                                                                 1][i] = image[n - j - 1][i], image[i][j], image[j][n - i - 1], image[n - i - 1][n - j - 1]

    return image
