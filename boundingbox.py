import cv2
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET


sample_img_path = r'C:\Proyecto IA\dataset\Images\n02085620-Chihuahua\n02085620_199.jpg'
annotation_file_path = r'C:\Proyecto IA\dataset\Annotation\n02085620-Chihuahua\n02085620_199'

tree = ET.parse(annotation_file_path)
root = tree.getroot()


xmin = int(root.find('.//xmin').text)
ymin = int(root.find('.//ymin').text)
xmax = int(root.find('.//xmax').text)
ymax = int(root.find('.//ymax').text)


image = cv2.imread(sample_img_path)



image_with_bbox = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(image_with_bbox, cv2.COLOR_BGR2RGB))
plt.title('Imagen con Bounding Box')
plt.show()