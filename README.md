# Plant-missing-seedling-location
Identify the position of the plants in the mobile shooting video, and according to the set spacing parameters, count the shortage of seedlings in a single row of plants in the video, and locate the missing seedlings.
This positioning is based on yolov5.
Add distance detection to detect the distance of field plants in a single row. If the distance is greater than the normal distance, it proves that there is a lack of seedlings, and the marked distance is abnormal.

# pip install -r requirements.txt

# base ----------------------------------------
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow
PyYAML>=5.3.1
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0

# logging -------------------------------------
tensorboard>=2.4.1
# wandb

# plotting ------------------------------------
seaborn>=0.11.0
pandas

# export --------------------------------------
coremltools>=4.1
onnx>=1.9.0
scikit-learn==0.19.2  for coreml quantization

# extras --------------------------------------
Cython  for pycocotools https://github.com/cocodataset/cocoapi/issues/172
pycocotools>=2.0  COCO mAP
albumentations>=1.0.3
thop  FLOPs computation
