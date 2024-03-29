import os

def ask_img_to_open(images: list):
    image_to_open = 0
    while not (0 < image_to_open <= len(images)):
        try:
            print("List of image names:")
            for image_path in images:
                print(os.path.basename(image_path))

            image_to_open = int(input(f"Enter image number in range 1...{len(images)}: "))
        except ValueError:
            pass

    return image_to_open

def ask_rgb_mode():
    answer = "None"
    options = ['y', 'n']
    while not answer.lower() in options:
        answer = str(input(f"Compress as RGB? {options}: "))

    if answer.lower() == options[0]:
        return True
    return False

def ask_img_compression_percentage():
    compr_perc = 0
    while not (0 < compr_perc < 100):
        try:
            compr_perc = float(input("Enter compression percentage (0..100)%: "))
        except ValueError:
            pass
    
    return compr_perc