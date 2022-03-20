from __future__ import print_function

import json
import os.path

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

        print(type(values))

        json_data = json.dumps(values)

        print(json_data)

        if not values:
            print('No data found.')
            return

        print('Stock, Price')
        for row in values:
            print('%s, %s' % (row[0], row[1]))

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()