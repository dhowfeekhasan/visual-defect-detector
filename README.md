
# Defect Detector
A simple Python script for automated visual quality control that uses OpenCV to compare test images against a "golden reference" image. It automatically detects and classifies common manufacturing defects such as FLASH (excess material) and CUT (missing material), highlighting them on the image for review.

Working:

1. Focus on the Shape (cv2.threshold) 🎨
First, we simplify the image into a pure black-and-white shadow to focus only on the object's exact shape. This process, known as Binarization, is done using the OpenCV function cv2.threshold.

2. Spot the Difference (cv2.bitwise_xor) 🔍
Next, we digitally compare the two shapes to see where they don't match. This Image Differencing is done with cv2.bitwise_xor, which marks any pixel that is different between the two images, creating a "difference map."

3. Outline Each Flaw (cv2.findContours) ✏️
Instead of seeing the differences as one big blob, we need to find the outline of each individual flaw. The function cv2.findContours does this for us, acting like a digital pencil that traces around each separate white shape on our difference map.

4. Decide: Extra or Missing? (Classification Logic) ⚖️
Finally, for each outlined flaw, the script analyzes the area to decide if it's extra material or a missing piece. This decision, a simple form of Classification, is the custom "brain" of our script that labels the flaw as Flash or Cut.

**Flowchart**

<img width="290" height="641" alt="image" src="https://github.com/user-attachments/assets/fd013d78-663b-4763-bb38-9a255f8ebe63" />

 **Sample Images:**
 
 Good Image
 
<img width="203" height="191" alt="image" src="https://github.com/user-attachments/assets/88f1a5bc-4cf7-40f3-8bdf-1c28136ae0c7" />




Defective Images

1.Flashes

 <img width="315" height="150" alt="image" src="https://github.com/user-attachments/assets/5375cf01-1e55-4971-92d1-73b6ff499943" />


2.Cuts

<img width="414" height="196" alt="image" src="https://github.com/user-attachments/assets/f06ca66a-008f-4fce-b4eb-50d71b09fe09" />


**Output Terminal Snapshots**

<img width="891" height="418" alt="image" src="https://github.com/user-attachments/assets/fd8d8fa5-9a73-456b-82df-c8a1ba3c3e0a" /> 

Output Images : 
https://github.com/dhowfeekhasan/visual-defect-detector/tree/main/output


 
