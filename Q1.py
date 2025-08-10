import cv2
import numpy as np
import os

# Load the reference good image
good_img_path = input("Enter the path to the good image (reference): ").strip()
good = cv2.imread(good_img_path, cv2.IMREAD_GRAYSCALE)
if good is None:
    print("❌ Error: Could not read good image.")
    exit()

_, good_bin = cv2.threshold(good, 127, 255, cv2.THRESH_BINARY)

# Create output folder
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

while True:
    test_path = input("\nEnter image path to check (or 'q' to quit): ").strip()
    if test_path.lower() == 'q':
        break

    test = cv2.imread(test_path, cv2.IMREAD_GRAYSCALE)
    if test is None:
        print("❌ Error: Could not read image.")
        continue

    _, test_bin = cv2.threshold(test, 127, 255, cv2.THRESH_BINARY)

    # Difference mask
    diff = cv2.bitwise_xor(good_bin, test_bin)
    diff_area = np.sum(diff > 0)

    if diff_area < 50:  # small threshold to ignore noise
        print(f"✅ {os.path.basename(test_path)} → GOOD PART")
        continue

    # Find contours of defect
    contours, _ = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    test_color = cv2.cvtColor(test, cv2.COLOR_GRAY2BGR)

    defect_type = None
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        mask = np.zeros_like(good_bin)
        cv2.drawContours(mask, [cnt], -1, 255, -1)

        extra_pixels = np.sum((mask == 255) & (test_bin == 255) & (good_bin == 0))
        missing_pixels = np.sum((mask == 255) & (good_bin == 255) & (test_bin == 0))

        if extra_pixels > missing_pixels:
            defect_type = "FLASH"
            color = (0, 255, 0)
        else:
            defect_type = "CUT"
            color = (0, 0, 255)

        cv2.rectangle(test_color, (x, y), (x + w, y + h), color, 2)
        cv2.putText(test_color, defect_type, (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # Save output
    base_name = os.path.splitext(os.path.basename(test_path))[0]
    cv2.imwrite(f"{output_dir}/{base_name}_mask.png", diff)
    cv2.imwrite(f"{output_dir}/{base_name}_result.png", test_color)

    print(f"❌ {os.path.basename(test_path)} → DEFECT DETECTED → {defect_type}")
    print(f"Results saved in '{output_dir}' folder.")
