import face_recognition
import numpy as np

def get_face_embedding(image_path: str) -> list:
    """Extract face encoding from an image."""
    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if not encodings:
        raise ValueError("No face detected")
    return encodings[0].tolist()

def compare_faces(embedding1: list, embedding2: list) -> bool:
    """Check if two faces match."""
    distance = np.linalg.norm(np.array(embedding1) - np.array(embedding2))
    return distance < 0.6  # Threshold for match