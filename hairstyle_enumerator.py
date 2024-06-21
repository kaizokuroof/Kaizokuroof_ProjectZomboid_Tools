import xml.etree.ElementTree as ET

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    element_dict = {}

    for index, element in enumerate(root.findall('.//male') + root.findall('.//female')):
        name = element.find('name').text
        element_dict[name] = index + 1

    return element_dict

xml_file = 'C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\media\hairStyles\hairStyles.xml'  # replace with your file path

element_dict = parse_xml(xml_file)

for name, element_number in element_dict.items():
    print(f"{name}")