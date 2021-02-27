import requests
import zillow

#variables

address = '6931 Country Ln.'
postal_code = '53719'




auth_file = r'C:\Users\Gino\Documents\Downloads\Zillowcode.txt'
api_key= open(auth_file,'r').read()

api = zillow.ValuationApi()

data = api.GetSearchResults(
        api_key,
        address,
        postal_code
)

print(data)