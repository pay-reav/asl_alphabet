from ultralytics import solutions

inf = solutions.Inference(
    model = r"C:\Users\reave\OneDrive\Desktop\Graduate School\Clinic\Python\YOLO\Iteration_3_995_Large_No\model_3_995_Large_No\train\weights\best.pt", 
)

inf.inference()

# Make sure to run the file using command `streamlit run path/to/file.py`