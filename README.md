# HematoVision

Blood cell classification using Transfer Learning. Supports eosinophils, lymphocytes, monocytes, and neutrophils.

## How to Use

1. Place dataset in `dataset/` folder.
2. Run training:
   ```
   python src/train.py
   ```
3. Run prediction:
   ```
   python src/predict.py path_to_image.jpg
   ```

4. Optional Flask App:
   ```
   python app.py
   ```

## Dependencies

Install using:
```
pip install -r requirements.txt
```
