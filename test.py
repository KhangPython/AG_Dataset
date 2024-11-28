import os

from Ipython.display import display, Image
Image(filename=f"runs/detect/predict3/{filename}.jpg", height=600)
base_path = '/content/run/detect'

predict_dirs = [d for d in os.listdir(base_path) if d.startswith('predict')]

if predict_dirs:
    predict_dirs = sorted(predict_dirs, key=lambda x: os.path.getctime(os.path.join(base_path, x)), reverse=True)
    latest_predict_path = os.path.join(base_path, predict_dirs[0])
    image_files = [f for f in os.listdir(latest_predict_path) if f.endswith('.jpg')]

    if image_files:
        latest_image = image_files[0]
        latest_image_path = os.path.join(latest_predict_path, latest_image)
        display(Image(filename=latest_image_path, height=600))
    else:
        print("Không tìm thấy ảnh kết quả")
else:
    print("Không có kết quả kiểm thử")