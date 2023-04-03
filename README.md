# Industry Project 2
Industry Project 2 about object measuring in images. Acts as prestudy for Bachelor Thesis.

| Role   | Name         |
| ------------- | ------------- |
| Author   | Dominique Peytrignet         |
| 1st Supervisor| Prof. Dr. Cédric Bessire         |
| Expert | Matt Stark       |

# Abstract of Industry Project 2
The ability to let a computer understand images and videos to fulfil a specific task, is called computer vision. Computer vision applications are used in many industries such as in automotive to detect and classify road signs, in manufacturing to visually control the quality of the produced product.  

A well known problem in computer vision tasks is to accurately determine the real-world  dimensions of the object of interest in the image. Solving this problem can be very helpful in the field of medical imaging, where a diagnosis for a patient can be drawn based on the shape and volume of their Red Blood Cells (RBC) . Current methods to determine the volume the RBC require high investment costs and lots of time. A image based processing would improve this process and safe time. 

Therefore in this project, the goal was to create a script which is capable of measuring the x- and y-dimensions of objects in an image, measure the accuracy of it and identify what factors may have a negative influence on the accuracy. A further objective was, looking forward to the Bachelor Thesis, to evaluate methods on how the volume and the shape of RBCs can be estimated, based on two-dimensional images. 

To achieve these goals, first a script has been developed to measure a selection of objects (Jenga piece, coins etc.) in an image, mainly using the Python library OpenCV. To detect the objects, the image first was put into grayscale colours and blurred, after that their edges and their contours were detected. After the contours were detected a rectangle was fitted on to them. The script takes the left most object in the image as a reference, to know what the ratio between the pixels and the desired metric is. This ratio is then applied to the other objects to know their dimensions. The results show that the measured values can differ up to 10% from the real world values. Higher deviations can be caused due to parallax error, depth differences or bad lightning conditions. 

As a second step, images were provided where RBCs are flowing through a channel. The image was taken from a video sequence. The goal was to do a first measurement and determine their width and height, by applying the same methodology as with the selection of objects. As a reference length the width of the channel was taken. Because the real world values of the RBCs, in the image, couldn’t be determined, the measured value couldn’t be compared. But based on an healthy human the results are reasonable and show that it is possible to detect single RBC and measure their width and height. 

In a third step, a literature research was conducted to find out methodologies on how the volume of an object can be estimated, based on a single or multiple 2D images. Further some method were presented on how the object be visualized, containing the 3rd dimension. The result showed, that the most promising methodology, for this task, is to apply the same approach as presented by Graikos et. al. where they use a depth estimation- and segmentation-network to estimate the volume of food portions. 

As a future work, namely the Bachelor Thesis, it has to be evaluated whether this methodology can be applied to the RBC images. A difficulty would be trying to track the RBC in the video sequence, as it would be required to build the depth estimation network. As an alternative, further methodologies could be evaluated which have other solutions to estimate the volume of RBCs.

# Usage of scripts
To probarly use the [Object_Measurements](https://github.com/DominiquePeytrignet/BTHE/blob/main/PythonFiles/Object_Measurements.ipynb) script and recreate the measurement results gained with the images, please alter the width and the image-path the section "Define width of left most object in image and image-path" , according to the following table:

| Image file    | Width         |
| ------------- | ------------- |
| Test_1.jpg   | 31.34         |
| Test_1_90.jpg| 53.88         |
| Test_1_180.jpg| 74.30        |
| Test_1_270.jpg| 69.78 |
| Test_2.jpg   | 53.88         |
| Test_2_180  .jpg  | 27.30 |
| Test_3.jpg   | 31.34         |
| Test_3_180.jpg  | 27.30 |
| Test_4.jpg   | 85.46         |


In the [Alternative_shapes]https://github.com/DominiquePeytrignet/BTHE/blob/main/PythonFiles/Alternative_shapes.ipynb script the amount of edges can be altered to identidy different polygons. 

All the other scripts can be used as they are. 
