import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

processed_img = None
img = None
gray = None

TARGET_SIZE = (1000, 600)

def upload_image():
    global img, gray, processed_img
    file_path = filedialog.askopenfilename()

    if not file_path:
        return

    img = cv2.imread(file_path)

    # Resize immediately
    img = cv2.resize(img, TARGET_SIZE)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed_img = img

    display_image(img)

def display_image(cv_img):
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(cv_img)
    imgtk = ImageTk.PhotoImage(image=im_pil)
    lbl.config(image=imgtk)
    lbl.image = imgtk

def sobel_edge():
    global processed_img
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.convertScaleAbs(sobel)
    processed_img = cv2.resize(cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR), TARGET_SIZE)
    display_image(processed_img)

def canny_edge():
    global processed_img
    edges = cv2.Canny(gray, 100, 200)
    processed_img = cv2.resize(cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR), TARGET_SIZE)
    display_image(processed_img)

def laplacian_edge():
    global processed_img
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)
    processed_img = cv2.resize(cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR), TARGET_SIZE)
    display_image(processed_img)

def gaussian_smoothing():
    global processed_img
    blur = cv2.GaussianBlur(img, (7, 7), 0)
    processed_img = cv2.resize(blur, TARGET_SIZE)
    display_image(processed_img)

def median_filtering():
    global processed_img
    median = cv2.medianBlur(img, 5)
    processed_img = cv2.resize(median, TARGET_SIZE)
    display_image(processed_img)

def save_image():
    global processed_img
    if processed_img is None:
        print("No processed image to save.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )

    if file_path:
        cv2.imwrite(file_path, processed_img)
        print("Image saved:", file_path)


root = tk.Tk()
root.title("Image Processing App")
root.geometry("900x700")

btn_upload = tk.Button(root, text="Upload Image", command=upload_image)
btn_upload.pack()

btn_display = tk.Button(root, text="Display Original Image", command=lambda: display_image(img))
btn_display.pack(pady=10)

btn_canny = tk.Button(root, text="Canny Edge Detection", command=canny_edge)
btn_canny.pack()

btn_sobel = tk.Button(root, text="Sobel Edge Detection", command=sobel_edge)
btn_sobel.pack()

btn_laplacian = tk.Button(root, text="Laplacian Edge Detection", command=laplacian_edge)
btn_laplacian.pack()

btn_gaussian = tk.Button(root, text="Gaussian Smoothing", command=gaussian_smoothing)
btn_gaussian.pack()

btn_median = tk.Button(root, text="Median Filtering", command=median_filtering)
btn_median.pack()

btn_save = tk.Button(root, text="Save Image", command=save_image)
btn_save.pack(pady=10)

lbl = tk.Label(root)
lbl.pack()

root.mainloop()
