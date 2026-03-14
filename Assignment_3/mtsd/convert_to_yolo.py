import os
import json
import random
import shutil

base_dir = "mtsd_v2_fully_annotated"
images_dir = os.path.join(base_dir, "images")
annotations_dir = os.path.join(base_dir, "annotations")

output_dir = "dataset"
output_images = os.path.join(output_dir, "images")
output_labels = os.path.join(output_dir, "labels")

CLASS_NAMES = [
    "stop",
    "yield",
    "speed_limit",
    "no_entry",
    "turn_restriction",
    "warning",
    "pedestrian",
    "parking",
    "priority",
    "directional",
    "traffic_light",
    "other"
]

def map_label_to_class(label):
    label = label.lower()

    if "stop" in label:
        return 0
    elif "yield" in label:
        return 1
    elif "maximum-speed-limit" in label or "speed-limit" in label:
        return 2
    elif "no-entry" in label or "do-not-enter" in label:
        return 3
    elif "no-left-turn" in label or "no-right-turn" in label or "turn" in label:
        return 4
    elif "warning" in label or "danger" in label:
        return 5
    elif "pedestrian" in label or "crosswalk" in label or "children" in label:
        return 6
    elif "parking" in label:
        return 7
    elif "priority" in label:
        return 8
    elif "direction" in label or "information" in label or "guide" in label or "arrow" in label:
        return 9
    elif "traffic-light" in label or "signal" in label:
        return 10
    else:
        return 11

def convert_bbox(xmin, ymin, xmax, ymax, img_w, img_h):
    x_center = ((xmin + xmax) / 2.0) / img_w
    y_center = ((ymin + ymax) / 2.0) / img_h
    width = (xmax - xmin) / img_w
    height = (ymax - ymin) / img_h
    return x_center, y_center, width, height

# Create output folders
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(output_images, split), exist_ok=True)
    os.makedirs(os.path.join(output_labels, split), exist_ok=True)

# Find actual image files you have
image_files = []
for file in os.listdir(images_dir):
    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        image_files.append(file)

image_files.sort()
random.seed(42)
random.shuffle(image_files)

n = len(image_files)
n_train = int(0.8 * n)
n_val = int(0.1 * n)
n_test = n - n_train - n_val

train_files = image_files[:n_train]
val_files = image_files[n_train:n_train + n_val]
test_files = image_files[n_train + n_val:]

splits = {
    "train": train_files,
    "val": val_files,
    "test": test_files
}

for split_name, files in splits.items():
    copied = 0
    skipped = 0

    for image_file in files:
        image_id = os.path.splitext(image_file)[0]
        annotation_path = os.path.join(annotations_dir, image_id + ".json")
        image_path = os.path.join(images_dir, image_file)

        if not os.path.exists(annotation_path):
            skipped += 1
            continue

        with open(annotation_path, "r") as f:
            data = json.load(f)

        img_width = float(data["width"])
        img_height = float(data["height"])

        label_lines = []

        for obj in data["objects"]:
            label = obj["label"]
            class_id = map_label_to_class(label)

            bbox = obj["bbox"]
            xmin = float(bbox["xmin"])
            ymin = float(bbox["ymin"])
            xmax = float(bbox["xmax"])
            ymax = float(bbox["ymax"])

            x, y, w, h = convert_bbox(xmin, ymin, xmax, ymax, img_width, img_height)
            label_lines.append(f"{class_id} {x:.6f} {y:.6f} {w:.6f} {h:.6f}")

        dest_image = os.path.join(output_images, split_name, image_file)
        dest_label = os.path.join(output_labels, split_name, image_id + ".txt")

        shutil.copy(image_path, dest_image)

        with open(dest_label, "w") as f:
            f.write("\n".join(label_lines))

        copied += 1

    print(f"{split_name}: copied {copied}, skipped {skipped}")

print("Done.")
print("Class names:")
for i, name in enumerate(CLASS_NAMES):
    print(i, name)