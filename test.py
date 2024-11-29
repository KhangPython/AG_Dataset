import os
import sys
import subprocess

# Ensure IPython is installed
subprocess.check_call([sys.executable, "-m", "pip", "install", "IPython"])
from IPython.display import Image, display

def run_yolo(hinh_thu, model):
    os.system(f'yolo task=detect mode=predict model={model} conf=0.25 source={hinh_thu} save=True')

    # Base path where YOLO saves predictions
    base_path = '/content/runs/detect'

    # Get all prediction directories
    predict_dirs = [d for d in os.listdir(base_path) if d.startswith('predict')]

    if predict_dirs:
        # Sort directories by creation time
        predict_dirs = sorted(predict_dirs, key=lambda x: os.path.getctime(os.path.join(base_path, x)), reverse=True)
        latest_predict_path = os.path.join(base_path, predict_dirs[0])

        # Get all image files in the latest prediction folder
        image_files = [f for f in os.listdir(latest_predict_path) if f.endswith('.jpg')]

        if image_files:
            # Display the latest prediction image
            latest_image = image_files[0]
            latest_image_path = os.path.join(latest_predict_path, latest_image)
            display(Image(filename=latest_image_path, height=600))
        else:
            print("Không tìm thấy ảnh kết quả")
    else:
        print("Không có kết quả kiểm thử")

def yolo_classify(hinh_thu, model):
    os.system(f'yolo task=classify mode=predict model={model} conf=0.25 source={hinh_thu} save=True')

    # Base path where YOLO saves predictions
    base_path = '/content/runs/classify'

    # Get all prediction directories
    predict_dirs = [d for d in os.listdir(base_path) if d.startswith('predict')]

    if predict_dirs:
        # Sort directories by creation time
        predict_dirs = sorted(predict_dirs, key=lambda x: os.path.getctime(os.path.join(base_path, x)), reverse=True)
        latest_predict_path = os.path.join(base_path, predict_dirs[0])

        # Get all image files in the latest prediction folder
        image_files = [f for f in os.listdir(latest_predict_path) if f.endswith('.jpg')]

        if image_files:
            # Display the latest prediction image
            latest_image = image_files[0]
            latest_image_path = os.path.join(latest_predict_path, latest_image)
            display(Image(filename=latest_image_path, height=600))
        else:
            print("Không tìm thấy ảnh kết quả")
    else:
        print("Không có kết quả kiểm thử")
