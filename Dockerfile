FROM ultralytics/ultralytics:latest
RUN wget https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n-seg.pt -O /ultralytics/yolo11n-seg.pt
CMD ["yolo", "segment", "train", "data=/usr/src/LabWork41/datasets/data.yaml", "model=/ultralytics/yolo11n-seg.pt", "epochs=100", "imgsz=640"]