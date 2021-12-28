import requests

# for test usd 2020-12-25


def check_input(check_input_data: str):
    """check user input data"""
    data: list = check_input_data.split()  # splitting user input
    if len(data) > 1:  # check how much data enter
        data[1] = data[1].replace('-', '')  # formatting the date for api
    else:
        data.append('')  # if you entered only currency, add the date ''
    return data


def get_rate(currency: str):
    """get the currency rate"""
    result: str = ''
    for i in data_response_api:  # looking for the currency in the data_response_api
        if i.get('cc') == currency:
            result = i.get('rate')
            break
        else:
            result = f'Invalid currency name: {currency}'  # if there is no currency
    return result


if __name__ == '__main__':
    input_data_user: str = str(input()).upper()  # user input date
    date_for_api: list = check_input(input_data_user)
    # url_api get rate for date
    url_api: str = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date_for_api[1]}&json'
    data_response_api: list = requests.get(url_api).json()

    try:
        if data_response_api == [] or data_response_api[0].get('message') == 'Wrong parameters format':
            print(f'-------------- \nInvalid date {date_for_api[1]}\n', end='==============')
        else:
            print(f'-------------- \n{date_for_api[0]}\n\n{get_rate(date_for_api[0])}\n', end='==============')
    except Exception:
        print(f'-------------- \nSystem Error\n', end='==============')
