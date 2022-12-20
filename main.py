# Pandas Technical Assessment Response
# Author: Uriel Knopf
import pandas as pd
import xml.etree.ElementTree as ET


def read_file(file_location):
    try:
        dataframe = pd.read_csv(file_location, sep='|')
        return dataframe
    except Exception as e:
        print("An error occurred while loading file data. Error: ", e)


def multiply_column(dataframe, column_name):
    try:
        dataframe[column_name] = dataframe[column_name]*2
        return dataframe
    except Exception as e:
        print("An error occurred while multiplying int values. Error: ", e)


def fill_data(dataframe, column_name):
    try:
        dataframe[column_name].replace(' ', 'new data', inplace=True)
    except Exception as e:
        print("An error occurred while filling missing data. Error: ", e)


def create_xml(dataframe, column_names):
    try:
        root = ET.Element("xml")
        for row in dataframe.values.tolist():
            participant_id = ET.SubElement(root, "ParticipantId", value=row[0])
            ET.SubElement(participant_id, "itemdata", name=column_names[1], value=row[1])
            ET.SubElement(participant_id, "itemdata", name=column_names[2], value=row[2])
            ET.SubElement(participant_id, "itemdata", name=column_names[3], value=str(row[3]))
            ET.SubElement(participant_id, "itemdata", name=column_names[4], value=str(row[4]))
            ET.SubElement(participant_id, "itemdata", name=column_names[5], value=row[5])
            ET.SubElement(participant_id, "itemdata", name=column_names[6], value=str(row[6]))
            ET.SubElement(participant_id, "itemdata", name=column_names[7], value=row[7])

        tree = ET.ElementTree(root)
        tree.write("xml_output.xml")
    except Exception as e:
        print("An error occurred while creating XML file. Error: ", e)


if __name__ == '__main__':
    file = 'sample_file.txt'
    df = read_file(file)
    print(df)

    columns = df.columns.values
    df = multiply_column(df, columns[6])

    fill_data(df, columns[7])

    create_xml(df, columns)

