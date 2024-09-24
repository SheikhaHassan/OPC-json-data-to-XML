import json
import xml.etree.ElementTree as ET

#open-read json file
with open('OPC.json') as jsonFile:
    json_data = json.load(jsonFile)

#function to convert json dictionary into xml
def json_to_xml(element, dictionary):
    #loop iterates through each key-value pair in the input dictionary
    for key, value in dictionary.items():
        #Checks if the current value is dictionary
        if isinstance(value, dict):
            #creates a new XML sub-element with the current key and attaches it to the parent XML element.
            sub_element = ET.SubElement(element, key)
            #Calls the function recursively to process the nested dictionary.
        #Checks if the current value is a list.
        elif isinstance(value, list):
            #Iterates through each item in the list.
            for item in value:
                #Creates a new XML sub-element with the current key for each item in the list
                list_element = ET.SubElement(element, key)
                #Calls the dict_to_xml function recursively to process each item in the list.
                json_to_xml(list_element, item)
        else:
            element.set(key, str(value))

# Create the root element
root = ET.Element("root")

# Convert the JSON data to XML
json_to_xml(root, json_data)

# Create an ElementTree object
tree = ET.ElementTree(root)

# Save the XML to a file
tree.write("output.xml", encoding="utf-8", xml_declaration=True)

print("Conversion complete. XML file saved as 'output.xml'")
