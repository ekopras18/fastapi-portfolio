def convert_id_to_string(data_list):
    converted_data_list = []
    for item in data_list:
        converted_item = item.copy()
        converted_item.id = str(item.id)
        converted_data_list.append(converted_item)
    return converted_data_list