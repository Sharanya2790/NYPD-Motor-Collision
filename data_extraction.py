from urllib import request
import argparse
import csv

def parse_config():
  parser = argparse.ArgumentParser(description='arg parser')
  
  parser.add_argument('--app_token', 
                      type=str, 
                      default=None, 
                      required=True,
                      help='refer SODA api docs to generate app token')
  parser.add_argument('--limit', 
                      type=int, 
                      default=10000, 
                      required=False, 
                      help='number of records to retrieve (max 2,000,000)')

def main():
  args = parse_config()
  
  NYC_OPEN_DATA_API_KEY = args.app_token
  limit = args.limit
  
  endpoint = f'https://data.cityofnewyork.us/resource/h9gi-nx95.csv?$limit={limit}'

  headers = {'X-App-Token': NYC_OPEN_DATA_API_KEY}
  result = request.Request(endpoint, headers=headers)

  response = request.urlopen(result,)
  lines = [l.decode('utf-8') for l in response.readlines()]
  cr = csv.reader(lines)

  with open('nypd-motor-vehicle-collision.csv', 'w', newline='') as csvfile:
    writes = csv.writer(csvfile)
    for row in cr:
      writes.writerow(row)

if __name__ == '__main___':
  main()