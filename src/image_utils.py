import cv2

def draw_boxes(image, boxes, scores):

    for box, score in zip(boxes,scores):
        if score > 0.5:
            ymin, xmin, ymax, xmax = box
            (startX, startY, endX, endY) = (int(xmin * image.shape[1]), int(ymin * image.shape[0]),
                                            int(xmax * image.shape[1]), int(ymax * image.shape[0]))

            #kolor ramki w zalenosci od wyniku pewnosci

            if 0.5 <= score < 0.7:
                color = (0, 0, 255) #czerwony
            elif 0.7 <= score < 0.9:
                color = (0, 255, 255) #pomaranczowy
            elif score >= 0.9:
                color = (0, 255, 0) #zielony

            thickness = 3
            cv2.rectangle(image, (startX, startY), (endX, endY), color, thickness) #ramka

            #dodanie tekstu
            label = f"{score * 100:.2f}%"
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, label, (startX, startY - 10), font, 3.0, color, 2)

    return image



    