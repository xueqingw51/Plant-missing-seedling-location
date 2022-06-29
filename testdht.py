"""
日期：23日
"""
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, PIL, OpenCV, numpy, multiple

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.