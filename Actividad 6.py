import cv2
import matplotlib.pyplot as plt

# Iniciar la cámara
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Presiona ESPACIO para capturar imagen, ESC para salir.")

while True:
    ret, frame = cam.read()
    if not ret:
        print("No se pudo acceder a la cámara.")
        break

    cv2.imshow("Presiona ESPACIO para capturar", frame)
    key = cv2.waitKey(1)
    if key == 27:  
        print("Cancelado por el usuario.")
        cam.release()
        cv2.destroyAllWindows()
        exit()
    elif key == 32:  
        img = frame.copy()
        break

cam.release()
cv2.destroyAllWindows()

# Mostrar imagen original
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Imagen Original")
plt.axis('off')
plt.show()

# Escala de grises
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img, cmap='gray')
plt.title("Escala de Grises")
plt.axis('off')
plt.show()

# Desenfoque y Canny
blurred_img = cv2.GaussianBlur(img, (15,15), 0)
edges_img = cv2.Canny(gray_img, 100, 200)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title("Original")
axes[0].axis('off')
axes[1].imshow(cv2.cvtColor(blurred_img, cv2.COLOR_BGR2RGB))
axes[1].set_title("Desenfoque")
axes[1].axis('off')
axes[2].imshow(edges_img, cmap='gray')
axes[2].set_title("Bordes (Canny)")
axes[2].axis('off')
plt.show()

# Umbral simple y adaptativo
_, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
adaptive_thresh_img = cv2.adaptiveThreshold(gray_img, 255,
                                            cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 11, 2)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(gray_img, cmap='gray')
axes[0].set_title("Escala de Grises")
axes[0].axis('off')
axes[1].imshow(binary_img, cmap='gray')
axes[1].set_title("Umbral Simple")
axes[1].axis('off')
axes[2].imshow(adaptive_thresh_img, cmap='gray')
axes[2].set_title("Umbral Adaptativo")
axes[2].axis('off')
plt.show()

# Contornos
contours, _ = cv2.findContours(edges_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 3)
plt.imshow(cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB))
plt.title("Contornos")
plt.axis('off')
plt.show()

# Detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Detección de Rostros")
plt.axis('off')
plt.show()
