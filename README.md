# Dialog generator tool
This tool is intended to create dialog data

# Quickstart
Environment: python 3.8.0 (tested on ubuntu/wsl) 
You can install the Python dependencies with
```
pip3 install -r requirements.txt
```

Setup face detection
```
cd dialog_system/FaceRecognition/process/module/face_detection
make
```

## Weight reparation
Speech to text: copy **2 weights** at **server23:/AIHCM/ASR/total_weight/dialog_generator_tool**  to **STT/asr_model/base**
FaceRecognize: copy **weights folder** at **server23:/AIHCM/ASR/total_weight/dialog_generator_tool/FaceRecognize**  to **FaceRecognition/weights**

## Inference

```
python inference.py -p 'video_path' -c True
```
-p: video path (str) (need save at "video" folder)
-c: cross check by Computer Vision (bool)
- The result folder (ASR_result and CV_result) will be created at the folder that contain input_video
- The dialog_file is located at ASR_result folder as txt file
