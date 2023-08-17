import splitfolders


input_folder = '/home/nvidia/sea_animal_data/sea_animal_original'


# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, (.8, .2).
# Train, val, test
splitfolders.ratio(input_folder, 
                   output="sea_animals_split", 
                   seed=42, 
                   ratio=(.8, .1, .1), 
                   group_prefix=None) 