def get_value_from_dictionary(dictionary, dict_name=""):

    if not dict_name:
        print("입력된 딕셔너리:")
    else:
        print(f"{dict_name} 딕셔너리:")
    
    for key, value in dictionary.items():
        print(f"{key}: {value}")

    while True:
        user_input = input("값을 찾을 키를 입력하세요 (종료하려면 'exit' 입력): ")

        if user_input.lower() == 'exit':
            break 

        value = dictionary.get(user_input, "해당 키가 존재하지 않습니다.")
        print(f"{user_input}에 대한 값: {value}")

