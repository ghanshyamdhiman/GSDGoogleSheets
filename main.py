from __future__ import print_function
import pandas as pd
import json
import numpy as np
import os.path
import matplotlib.pyplot as plt

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient._auth import credentials_from_file
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1FdNFV-RDrieoQJWDlodhcUXqOo-RWYt0rFFXhHspToc'
SAMPLE_RANGE_NAME = 'GSD!A1:B10'


def main():
    creds = credentials_from_file('credentials.json')

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        df = pd.DataFrame(values)

        df.to_excel("test.xlsx", sheet_name="stocks")

        print(type(values))

        json_data = json.dumps(values)

        print(json_data)

        if not values:
            print('No data found.')
            return

        print('Stock, Price')
        label1 = ["one"]
        price1 = [1]

        doit = False

        for row in values:
            if doit:
                print('%s, %s' % (row[0], row[1]))
                print(type(row[0]))
                label1.append(row[0])
                data = float(row[1])
                price1.append(int(data))

            doit = True


    except HttpError as err:
        print(err)

    left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    plt.bar(left, price1, tick_label=label1,
            width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.xlabel('x - axis')
    # naming the y-axis
    plt.ylabel('y - axis')
    # plot title
    plt.title('My bar chart!')

    # function to show the plot
    plt.show()


if __name__ == '__main__':
    main()
