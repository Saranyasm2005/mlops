from ultralytics import YOLO

# Load model
model = YOLO("best.pt")

# Predict on image
results = model.predict(
    source="test.mp4",
    conf=0.5,
    save=True
)

print("Prediction completed!")