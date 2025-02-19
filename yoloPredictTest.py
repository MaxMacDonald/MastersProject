from ultralytics import YOLO


# Predict with the model
# We can pass an array with paths to the videos later





# Break down video into frames (using )
# For each frame predict using yolo, find humans with confidence of 0.7 or higher (as a starting point) (do this using an array of the frames of the video)
# For each frame i, find frame i - 1. Iterate through boxes, if their positions are 5-10% different in position then assmume they are the same human and add this 
# region to an array with index n where n is the index of the human in the scene. If it doesn't exist add a new array with index n+1.

# Perform depth estimation and mesh fitting on each indexed human (lets throw this all in a dictionary for ease of use)

def are_boxes_similar(box1,box2):
    #TODO


# Function borrowed from DynoBOA
def video_to_images(vid_file, img_folder=None, return_info=False):
    if img_folder is None:
        img_folder = osp.join('/tmp', osp.basename(vid_file).replace('.', '_'))

    os.makedirs(img_folder, exist_ok=True)

    command = ['ffmpeg',
               '-i', vid_file,
               '-f', 'image2',
               '-v', 'error',
               f'{img_folder}/%06d.png']
    print(f'Running \"{" ".join(command)}\"')
    subprocess.call(command)

    print(f'Images saved to \"{img_folder}\"')

    return img_folder

vid_dir = config.InternetData_ROOT
for vid_file in glob.glob(f'{vid_dir}/*.mp4'):
    forename = osp.basename(vid_file)[:-4]
    video_to_images(vid_file, f'{vid_dir}/images/{forename}')



# Load a model
model = YOLO("yolo11n.pt")  # load an official model

# Get all frames
frames = []
for image in image_folder:
    image.path.append(frames)

results = model(frames, classes = [0])  # predict only person objects on an image

# Process results list
for result in results:
    boxesInFrame = []
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk

    # Check confidence rating of each box
    for box in boxes:
        if box.conf > 0.8:
            print("found one!")

        boxesInFrame.append(box) 

    framesWithBoxes.append(boxesInFrame)

#   Iterate through each frame, compare each box to the boxes in the previous frame
#   if they are within tolerance of each other then assign to the same human index
#   if they are not (or its the first frame) add to a new index.
human_region_index = {}
human_index = 0
for i in range(len(framesWithBoxes)):
    if i == 0:
        for box in framesWithBoxes(i):
            name = "human_" + str(human_index)
            human_region_index[name] = [box]
            human_index += 1
    else:
        currentFrame = framesWithBoxes(i)
        previous_frame = framesWithBoxes(i-1)
        for box in currentFrame:
            noneSimilar = True
            for key,value in human_region_index.items():
                if are_boxes_similar(box,value[-1]):
                    noneSimilar = False
                    value.append(box)


            if noneSimilar == True:
                name = "human_" + str(human_index)
                human_region_index[name] = [box]
                human_index += 1
            #Compare with previous frame boxes







# humans = {human_1: [frame1box,frame2box,frame3box]}
# frame1 = [box1,box2 ...] -> [frame1boxes, frame2boxes] -> {human_1: [frame1box,frame2box,frame3box]}
