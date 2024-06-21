import xml.etree.ElementTree as ET

LoadXML = 'C:\Program Files (x86)\Steam\steamapps\common\ProjectZomboid\media\clothing\clothing.xml'  # replace with your actual file path

tree = ET.parse(LoadXML)
root = tree.getroot()

def find_m_name_elements(parent):
    m_names = []
    for child in parent:
        if child.tag == 'm_Name':
            m_names.append(child.text)  # collect the text content of <m_Name> elements
        elif child.tag.startswith('m_'):
            m_names.extend(find_m_name_elements(child))  # recursive call for nested elements
    return m_names

all_m_names = find_m_name_elements(root)

print(all_m_names)  # Output: ['1RJTest']