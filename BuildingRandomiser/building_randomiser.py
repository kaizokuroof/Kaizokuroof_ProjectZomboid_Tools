import random, time, os
# - Multi Tile - #
from multi_tile_seating_indoor import multi_tile_residential_north_seating
from multi_tile_furniture_tables_high import multi_tile_residential_north_table_high
from multi_tile_furniture_bedding import furniture_bedding_4_tiles_north, furniture_bedding_4_tiles_south, furniture_bedding_4_tiles_east, furniture_bedding_4_tiles_west
from multi_tile_furniture_bedding import furniture_bedding_2_tiles_north, furniture_bedding_2_tiles_south, furniture_bedding_2_tiles_east, furniture_bedding_2_tiles_west
from multi_tile_furniture_storage_01 import multi_tile_storage_cupboards_north, multi_tile_storage_cupboards_south, multi_tile_storage_cupboards_east, multi_tile_storage_cupboards_west
#from multi_tile_roof import residential_roof_tiles
from multi_tile_rooves_with_shallow_tiles import rooves

# - Single Tile - #
from single_tile_floors import floor_interior_tile, floor_interior_wood, floor_interior_carpet
from single_tile_fixtures_counters import fixtures_counters
from single_tile_appliances_fridges import single_tile_residential_fridges
from single_tile_wall_exterior import wall_exterior_residential, walls_and_caps_exterior_residential
from single_tile_wall_interior import wall_interior_residential
from single_tile_seating_indoors import single_tile_residential_north_seating_lounge
from single_tile_storage_01 import single_tile_drawers
from single_tile_tv_stands import tv_stands_east, tv_stands_north
from single_tile_fixtures_windows import fixtures_window
from single_tile_furniture_shelving import shelving

def get_base_template(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content

def output_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def get_first_tbx_file(file_path):
    # List all files in the directory
    files = os.listdir(file_path)
    
    # Find the first file with .tbx extension
    tbx_file = next((f for f in files if f.endswith('.tbx')), None)
    
    # If a .tbx file is found, read its content and return it along with the file name
    if tbx_file:
        tbx_file_path = os.path.join(file_path, tbx_file)
        with open(tbx_file_path, 'r') as file:
            file_content = file.read()
        
        # Remove the file extension from the file name
        filename = os.path.splitext(tbx_file)[0]
        
        return file_content, filename
    else:
        print("No .tbx file found in the provided directory.")
        return None, None

def output_random_building(file_name, content):
    """
    Write content to a file inside a 'buildings' folder.

    Args:
    - file_path (str): The file name (without the directory) to write the content to.
    - content (str): The content to write to the file.
    """
    # Ensure the 'buildings' folder exists in the current working directory
    buildings_folder = 'buildings'
    if not os.path.exists(buildings_folder):
        os.makedirs(buildings_folder)
    
    # Construct the full path to the file inside the 'buildings' folder
    output_path = os.path.join(buildings_folder, file_name)
    
    # Write content to the file
    with open(output_path, 'w') as file:
        file.write(content)

def replace_tiles_from_lists(file_content, new_file_path, list_of_lists):
    for i in range(len(list_of_lists)):
        #if isinstance(list_of_lists[0], list):
        if isinstance(list_of_lists[i], list):
            # Nested list
            random_index = random.randrange(len(list_of_lists))
            #count_lists(list_of_lists)
            #print('Random Index for Nested Loop: ' + str(random_index)) 
            for n in range(len(list_of_lists[i])):
                if isinstance(list_of_lists[i][n], list):
                    # Nested Nested list
                    # We will need to generate the new random index here if we have another nested list.
                    for j in range(len(list_of_lists[i][n])):
                        #print(list_of_lists[i][n][j])
                        print('TODO: this nested loop')
                else:
                    random_tile = list_of_lists[random_index][n]
                    if list_of_lists[i][n] in file_content:
                        print('Swapping: ' + str(list_of_lists[i][n]) + ' ' + str(random_tile))
                        file_content = file_content.replace(list_of_lists[i][n], random_tile)
        else:
            # We're passing a list directly.
            random_index = random.randrange(len(list_of_lists))
            random_tile = list_of_lists[random_index]
            if list_of_lists[i] in file_content:
                print('Swapping: ' + str(list_of_lists[i]) + ' ' + str(random_tile))
                file_content = file_content.replace(list_of_lists[i], random_tile)
    return file_content
                


# TODO: 1) Add in wooden external wall tiles? 2) Add in roof caps 3) add in roof tiles

def count_lists(list_of_lists_to_count):
    for i in range(len(list_of_lists_to_count)):
        print(len(list_of_lists_to_count[i]))


for i in range(30):
    random.seed(random.randint(0,999999))
    
    #new_building = get_base_template('test.tbx')
    new_building, file_name = get_first_tbx_file('./')
    replacement_name = file_name + str(i+1) + '.tbx'
    print(replacement_name)
    
    # - Floor
    new_building = replace_tiles_from_lists(new_building, replacement_name, floor_interior_wood)
    new_building = replace_tiles_from_lists(new_building, replacement_name, floor_interior_carpet)
    new_building = replace_tiles_from_lists(new_building, replacement_name, floor_interior_tile)
    # - Seating
    new_building = replace_tiles_from_lists(new_building, replacement_name, multi_tile_residential_north_seating)
    new_building = replace_tiles_from_lists(new_building, replacement_name, multi_tile_residential_north_table_high)

    new_building = replace_tiles_from_lists(new_building, replacement_name, single_tile_residential_north_seating_lounge)
    # - Bedding 4 tile
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_4_tiles_north)
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_4_tiles_south)
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_4_tiles_east)
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_4_tiles_west)
    # - Bedding 2 tile
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_2_tiles_north)
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_2_tiles_south)
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_2_tiles_east)
    new_building = replace_tiles_from_lists(new_building, replacement_name, furniture_bedding_2_tiles_west)
    # - Storage
    new_building = replace_tiles_from_lists(new_building, replacement_name, single_tile_drawers)

    # - TV stands
    new_building = replace_tiles_from_lists(new_building, replacement_name, tv_stands_east)
    new_building = replace_tiles_from_lists(new_building, replacement_name, tv_stands_north)

    # - Cupboards
    new_building = replace_tiles_from_lists(new_building, replacement_name, multi_tile_storage_cupboards_north)
    new_building = replace_tiles_from_lists(new_building, replacement_name, multi_tile_storage_cupboards_south)
    new_building = replace_tiles_from_lists(new_building, replacement_name, multi_tile_storage_cupboards_east)
    new_building = replace_tiles_from_lists(new_building, replacement_name, multi_tile_storage_cupboards_west)
    
    # - Shelving
    new_building = replace_tiles_from_lists(new_building, replacement_name, shelving) # Check working

    # - Counters
    new_building = replace_tiles_from_lists(new_building, replacement_name, fixtures_counters)

    # - Appliances
    new_building = replace_tiles_from_lists(new_building, replacement_name, single_tile_residential_fridges)

    # - Walls
    new_building = replace_tiles_from_lists(new_building, replacement_name, wall_interior_residential)
    new_building = replace_tiles_from_lists(new_building, replacement_name, walls_and_caps_exterior_residential)
    #new_building = replace_tiles_from_lists(new_building, replacement_name, wall_exterior_residential) # This does only walls.

    # - Windows
    new_building = replace_tiles_from_lists(new_building, replacement_name, fixtures_window)
    
    # - Roof
    #new_building = replace_tiles_from_lists(new_building, replacement_name, residential_roof_tiles)
    new_building = replace_tiles_from_lists(new_building, replacement_name, rooves)

    output_random_building(replacement_name, new_building)