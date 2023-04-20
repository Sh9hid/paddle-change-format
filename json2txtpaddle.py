import os
import json

# path to the directory containing images
image_dir = path/to/images
# path to save the annotation text file
output_file = path/to/output

# path to the annotations json file
annotations_file = /path/to/json-via-vgg

with open(annotations_file, 'r') as f:
    annotations = json.load(f)

count = 0

def add_quote(a):
    return f'"{a}"'

with open(output_file, 'w') as f:
    for ann in annotations.values():
        img_path =  ann["filename"]
        lis = []
        for box in ann["regions"]:
            x1, y1 = add_quote(str(box["shape_attributes"]["all_points_x"][0])), add_quote(str(box["shape_attributes"]["all_points_y"][0]))
            x2, y2 = add_quote(str(box["shape_attributes"]["all_points_x"][1])), add_quote(str(box["shape_attributes"]["all_points_y"][1]))
            x3, y3 = add_quote(str(box["shape_attributes"]["all_points_x"][2])), add_quote(str(box["shape_attributes"]["all_points_y"][2]))
            x4, y4 = add_quote(str(box["shape_attributes"]["all_points_x"][3])), add_quote(str(box["shape_attributes"]["all_points_y"][3]))
            transcription = box["region_attributes"]["text"]
            dic = {"points": [[x1, y1], [x2, y2], [x3, y3], [x4, y4]], "transcription": transcription}
            lis.append(dic)
        lis = json.dumps(lis, ensure_ascii=False)
        lis = lis.replace('\\', '')
        lis = lis.replace('""', '"')
        if lis == '[]':
            continue
        f.write(f'{img_path}\t{lis}\n')
        count += 1

print(f"Total number of annotations created: {count}")
