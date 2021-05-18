import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import imshow
from PIL import Image
import copy
import requests
from io import BytesIO

def reverse(image_path, reverse = 'horizontal', url = False):
  """
  reverse will take the path of the image and return a mirrored/reversed picture.
  It achieves this by reversing the rows of a matrix for a horizontal reverse,
  and reverse the columns of a matrix for a vertical reverse.
  The default option for reverse is horizontal, if users would like to reverse it 
  vertically, they should input vertical
  
  reverse='vertical' will return the image vertically reversed.
  reverse='vertical mirror' will return the image vertically mirrored.
  It can take both a path from the working directory or from the web. 
  To use the function from a web image link, 
  users have to put in the argument url = True

  Input: image path, (reverse='horizontal' as default)
  Output: The reversed image (horizontal as default)
  """
  if url == False:
    image = Image.open(image_path)
    mat_image = np.array(image)
    m, n, depth = mat_image.shape

  elif url == True:
    response = requests.get(image_path)
    with Image.open(BytesIO(response.content)) as image:
      mat_image = np.array(image)
      m, n, depth = mat_image.shape

  if reverse == 'horizontal':
    mat_image_reverse = copy.deepcopy(mat_image)
    mat_image_rows_reverse = copy.deepcopy(mat_image)
      
    for i in range(m):
      c = 0
      for j in range(n-1,-1,-1):
        mat_image_rows_reverse[i][c] = mat_image_reverse[i][j]
        c += 1
      
    plt.axis('off')
    plt.imsave('image_reversed.png', mat_image_rows_reverse)  
    return imshow(mat_image_rows_reverse) 
  
  elif reverse == 'vertical':
    mat_image_reverse = copy.deepcopy(mat_image)
    mat_image_column_reverse = copy.deepcopy(mat_image)

    for i in range(n):
      c = 0
      for j in range(m-1,-1,-1):
        mat_image_column_reverse[c][i] = mat_image_reverse[j][i]
        c += 1
    
    plt.axis('off')
    plt.imsave('image_reversed.png', mat_image_column_reverse)  
    return imshow(mat_image_column_reverse)
    
  elif reverse == 'vertical mirror':
    mat_image_reverse = copy.deepcopy(mat_image)

    for i in range(n):
      c = 0
      for j in range(m-1,-1,-1):
        mat_image_reverse[c][i] = mat_image[j][i]
        c += 1
      
    mat_image_reverse_mirror = copy.deepcopy(mat_image_reverse)

    for i in range(m):
      c = 0
      for j in range(n-1,-1,-1):
        mat_image_reverse_mirror[i][c] = mat_image_reverse[i][j]
        c += 1

    plt.axis('off')
    plt.imsave('image_reversed.png', mat_image_reverse_mirror)  
    return imshow(mat_image_reverse_mirror)


def rotate(image_path, deg = 90, url = False):
  """
  rotate will take the path of the image and return a rotated 90 degrees picture.
  The default option for degrees is 90, if users would like to rotate it 180 or 
  270 degrees, they should input deg = 180 or deg = 270
  
  It rotates the image by tranposing the matrix.

  It can take both a path from your os or from the web. To use the function from
  a web image link, users have to put in the argument url = True
  
  Input: image path, (deg = 90 as default)
  Output: The rotated image (90 degrees as default)
  """
  if url == False:
    image = Image.open(image_path)
    mat_image = np.array(image)
    m, n, d = mat_image.shape
  
  elif url == True:
    response = requests.get(image_path)
    with Image.open(BytesIO(response.content)) as image:
      mat_image = np.array(image)
      m, n, d = mat_image.shape  

  if deg == 90:

    mat_image = list(zip(*mat_image))
    for i in range(n):
      reversed_row = []
      for j in range(m-1, -1, -1):
        reversed_row.append(mat_image[i][j])
      mat_image[i] = reversed_row

    plt.axis('off')
    plt.imsave("rotated_image.png", mat_image)
    return imshow(mat_image)
    

  elif deg == 180:
    mat_image_column_reverse = copy.deepcopy(mat_image)

    for i in range(n):
      c = 0
      for j in range(m-1,-1,-1):
        mat_image_column_reverse[c][i] = mat_image[j][i]
        c += 1

    plt.axis('off')
    plt.imsave("rotated_image.png", mat_image)
    return imshow(mat_image_column_reverse)

  elif deg == 270:

    mat_image = list(zip(*mat_image))
    
    plt.axis('off')
    return imshow(mat_image)

def bw_filter(image_path, url=False):
  """
  bw_filter will take the path of the image and return a black-white image.
  The users can adjust the intensity to their liking. 
  The default intensity is 0.
  
  It achieves this by assigning 0 to the pixels which value is less or 
  equal than the mean of the matrix and 255 otherwise.

  Input: image path, (intensity = 0 as default)
  Output: The filtered image 
  """
  if url == False:
    with Image.open(image_path).convert('L') as image:
      mat_image = np.array(image)
      m, n = mat_image.shape
  
  elif url == True:
    response = requests.get(image_path)
    with Image.open(BytesIO(response.content)).convert('L') as image:
      mat_image = np.array(image)
      m, n = mat_image.shape  

  mat_avg = round(np.average(mat_image), 1)
  rep_val = 0
  rep_val2 = 255 

  for i in range(m):
    for j in range(n):
      if mat_image[i][j] < mat_avg:
        mat_image[i][j] = rep_val
      else:
        mat_image[i][j] = rep_val2

  plt.axis('off')
  plt.imsave("bwfiltered_image.jpg", mat_image)
  return imshow(mat_image, cmap='gray')

def inverse(image_path, url = False):
  """
  bw_filter will take the path of a RGB image and return an inversed coloured image.
  
  It achieves this by replacing the values (R,G,B) by it’s negative complement 

  It can take both a path from your os or from the web. To use the function from
  a web image link, users have to put in the argument url = True
  
  Input: image path
  Output: The inversed coloured image 
  """
  if url == False:
    with Image.open(image_path) as image:
      mat_image = np.array(image)
      m, n, d = mat_image.shape
  
  elif url == True:
    response = requests.get(image_path)
    with Image.open(BytesIO(response.content)) as image:
      mat_image = np.array(image)
      m, n, d = mat_image.shape  

  negative_mat = copy.deepcopy(mat_image)

  for x in range(m):
    for y in range(n):
      r, g, b = image.getpixel((y,x))
      r = 255-r
      g = 255-g
      b = 255-b
      negative_mat[x][y][0] = r
      negative_mat[x][y][1] = g
      negative_mat[x][y][2] = b

  plt.axis('off')
  plt.imsave("negative_image.jpg", negative_mat)
  return imshow(negative_mat)

def brighten(image_path, intensity = 50, url = False):
  """
  brigthen will take the path of a RGB image and return a brightened image.
  The users can adjust the intensity to their liking by assigining higher/lower 
  values for the intensity. The default intensity is 0.
  
  It achieves this by multiplying each value from the tuple (R,G,B) by the constant br

  It can take both a path from your os or from the web. To use the function from
  a web image link, users have to put in the argument url = True

  Input: image path, (intensity = 50 as default)
  Output: The brightened image 
  """
  if url == False:
    with Image.open(image_path) as image:
      mat_image = np.array(image, dtype=float)
      m, n, d = mat_image.shape
  
  elif url == True:
    response = requests.get(image_path)
    with Image.open(BytesIO(response.content)) as image:
      mat_image = np.array(image, dtype=float)
      m, n, d = mat_image.shape

  mat_image = copy.deepcopy(mat_image)

  for x in range(1, m-1):
    for y in range(1, n-1):
      r, g, b = image.getpixel((y,x))
      r = r + intensity
      g = g + intensity
      b = b + intensity
      mat_image[x][y][0] = r
      mat_image[x][y][1] = g
      mat_image[x][y][2] = b

  plt.axis('off')
  mat_image = np.array((mat_image - np.min(mat_image)) / (np.max(mat_image) - np.min(mat_image)))
  plt.imsave("brightened_image.jpg", mat_image)
  return imshow(mat_image)

def blur(image_path, intensity = 50, url = False):
  """
  blur will take the path of an image and return a blurred image.
  The users can adjust the intensity to their liking by assigining higher/lower 
  values for the intensity. The default intensity is 50. 
  It will return a grayscale image. 

  It achieves this by assigning each pixel a weighted average of the neighbor's pixels

  It can take both a path from your os or from the web. To use the function from
  a web image link, users have to put in the argument url = True
    
  Input: image path, (intensity = 50 as default)
  Output: The blurred image 
  """
  if url == False:
    with Image.open(image_path) as image:
      mat_image = np.array(image, dtype = float)
      m, n, depth = mat_image.shape
  
  elif url == True:
    response = requests.get(image_path)
    with Image.open(BytesIO(response.content)) as image:
      mat_image = np.array(image,dtype = int)
      m, n, depth = mat_image.shape

  a = intensity
  
  if intensity <=  50:

    for i in range(1, m-1):
      for j in range(1, n-1):
        mat_image[i][j] = a*(mat_image[i][j-1] + mat_image[i-1][j] + mat_image[i+1][j] + mat_image[i][j+1])/(4*a)
  
    plt.axis('off')
    mat_image = mat_image.astype(np.uint8)
    plt.imsave("blurred_image.jpg", mat_image)
    return imshow(mat_image,  cmap='gray')


  elif intensity>50 and intensity<=100:
    num = 0
    while num<3:
      for i in range(1, m-1):
        for j in range(1, n-1):
          mat_image[i][j] = a*(mat_image[i][j-1] + mat_image[i-1][j] + mat_image[i+1][j] + mat_image[i][j+1])/(4*a)

      num += 1

    plt.axis('off')
    mat_image = mat_image.astype(np.uint8)
    plt.imsave("blurred_image.jpg", mat_image)
    return imshow(mat_image,  cmap='gray')
  

  elif intensity > 100:
    num = 0
    while num <5:
      for i in range(1, m-1):
        for j in range(1, n-1):
          mat_image[i][j] = a*(mat_image[i][j-1] + mat_image[i-1][j] + mat_image[i+1][j] + mat_image[i][j+1])/(4*a)
      num += 1

    plt.axis('off')
    mat_image = mat_image.astype(np.unint)
    plt.imsave("blurred_image1.jpg", mat_image)
    return imshow(mat_image,  cmap='gray')

def random_crop(image_path, url = False):
  """
  random_crop will take the path of an image and return a random cropped image.
  It can take both a path from your os or from the web. To use the function from
  a web image link, users have to put in the argument url = True
  
  It achieves this by deleting a portion of the height of the image, 
  and the width of the image. It finally outputs a cropped image.

  Input: image path
  Output: A randomly cropped image 
  
  reference: https://note.nkmk.me/en/python-numpy-delete/
  """
  if url == False:
    with Image.open(image_path) as image:
      mat_image = np.array(image)
      H, W, d = mat_image.shape
  
  elif url == True:
    response = requests.get(image_path)
    with Image.open(BytesIO(response.content)) as image:
      mat_image = np.array(image)
      H, W, d = mat_image.shape  

  h_start = np.random.randint(0, H) 
  w_start = np.random.randint(0, W)
  
  mat_image = np.delete(np.delete(mat_image, slice(h_start), 0), slice(w_start), 1)
  
  #mat_image = np.delete(mat_image, slice[:w_start], 1)
  #mat_image = np.delete(mat_image, slice[:h_start], 0)
  
  plt.axis('off')
  plt.imsave("randomlycropped_image.jpg", mat_image)
  return imshow(mat_image)

