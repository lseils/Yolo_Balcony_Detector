import warnings
warnings.filterwarnings('ignore')
import m
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('yolov8-YOLO_Balcony_Detector.yaml', task='detect')

    
    model.train(data='data.yaml',
                cache=False,
                imgsz=640,
                epochs=200,
                batch=16,
                close_mosaic=10,
                workers=8,
                device='gpu',
                lr = 0.001,
                optimizer='SGD',
                project='YOLO_Balcony_Detector/train',
                name='exp',
                )