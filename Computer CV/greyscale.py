import cv2

image = cv2.imread("for project.jpg")
greyconvert = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
resized_image = cv2.resize(greyconvert, (224, 224))


cv2.imshow('Processed Image', resized_image)
key = cv2.waitKey(0)
if key ==ord('s'):
    cv2.imwrite('greyscale_resized_for project.jpg', resized_image)
    print("Image saved as greyscale_resized_for project.jpg")
else:
    print("Image not saved.")


cv2.destroyAllWindows()

print(f"Processed Image Dimensions: {resized_image.shape}")
 