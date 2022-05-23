import pyvips
from PIL import Image, ImageDraw, ImageFont
import os
# vipshome = 'c:\\vips-dev-8.7\\bin'
# os.environ['PATH'] = vipshome + ';' + os.environ['PATH']

# text = "ఒక గ్రామంలో వివిధ వృత్తుల వారి మధ్య విభేదాలు వచ్చాయి."
# output_file = "./Images/backgroundimagereal.jpg"
# image = pyvips.Image.text(text, width=800, height=500, font='Arial Unicode MS', dpi=96)
# image.write_to_file(output_file)

image = pyvips.Image.new_from_file('some-image.jpg', access='sequential')
image *= [1, 2, 1]
mask = pyvips.Image.new_from_array([[-1, -1, -1],
                                    [-1, 16, -1],
                                    [-1, -1, -1]
                                   ], scale=8)
image = image.conv(mask, precision='integer')
image.write_to_file('x.jpg')