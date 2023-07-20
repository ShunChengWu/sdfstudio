import argparse
import os
import glob
import cv2
from tqdm import tqdm
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="preprocess nerfstudio dataset to sdfstudio dataset, "
                                                 "currently support colmap and polycam")
    parser.add_argument("-i","--input-dir", dest="input_dir", required=True, help="path to input data directory")
    parser.add_argument("-o","--output-dir", dest="output_dir", required=True, help="path to output data directory")
    args = parser.parse_args()
    
    image_paths = glob.glob(os.path.join(args.input_dir,"*"))
    
    for image_path in tqdm(image_paths):
        basename = os.path.basename(image_path)
        out_index = int(basename.replace('dynamic_mask_','').split('.')[0])
        save_path = os.path.join(args.output_dir,f"{out_index:06d}_foreground_mask.png")
        # print(out_index)
        # print(save_path)
        mask = cv2.imread(image_path)
        cv2.imwrite(save_path,(1-mask)*255)