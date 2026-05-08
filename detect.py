import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/detect/train3/weights/best.pt') # select your model.pt path
    model.predict(source='input/images', # input folder
                  imgsz=640,
                  #conf=0.5,    # ← ignore weak detections
                  project='C:/Users/Seilsl/Creative Cloud Files  Seilsl@outlook.com 011A70565F4D83C70A495C57@AdobeID/ALL/CODE/Gatech/Data Driven Methods/ToTrainYolo/YOLO_Balcony_Detector/detections', # output folder
                  name='exp',
                  show_labels=True,
                  save=True,
                  # conf=0.2,
                  # visualize=True # visualize model features maps
                )
    


