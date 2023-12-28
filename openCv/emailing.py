

import os.path
import base64
import google.auth

from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



#print('started')
  # If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.send", "https://www.googleapis.com/auth/gmail.compose", "https://www.googleapis.com/auth/gmail.modify"]
#"https://www.googleapis.com/auth/gmail.readonly", "https://www.googleapis.com/auth/gmail.send", "https://mail.google.com/","https://www.googleapis.com/auth/gmail.compose"

def authentication():    
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  
  if os.path.exists("token.json"): #This is your token file based on your client secret file.
    #print('Token exists! \n')
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
  # If there are no (valid) credentials available, let the user log in.
  # You should get a client secrets file from Google Developer Cloud that is set up for an offline app
  # Then add it to the root directory and rename it to "credentials.json" for the Oauth2 flow to work.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    # If this function is uncommented you need to request permission in the scopes to read the accounts data.
    
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    
    """
    #results = service.users().labels().list(userId="me").execute()
    #labels = results.get("labels", [])
   
    if not labels:
      print("No labels found.")
      return
    print("Labels:")
    for label in labels:
      print(label["name"])
    """
  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")
    
    
def gmail_send_message(emailAdr,emailBody, attachment,subject="Automated draft"):
  """Create and send an email message
  Print the returned  message id
  Returns: Message object, including message id
  """
  creds = Credentials.from_authorized_user_file("token.json", SCOPES)

  try:
    service = build("gmail", "v1", credentials=creds)
    
    message = MIMEMultipart()
    
    #The actual message
    message.attach(MIMEText(f'New email from: {emailAdr}\n\n{emailBody}\n\nKind Regards'))
    
    # Attach the image
    with open(attachment, "rb") as img_file:
        img_data = img_file.read()
        img_mime = MIMEImage(img_data, name=os.path.basename(attachment))
        message.attach(img_mime)
        
    #Build the text part of the message
    message["To"] = "gduser1@workspacesamples.dev" #Add your mail adress here.
    
    #This set when calling the function from main
    message["From"] = f'{emailAdr}'
    message["Subject"] = f'{subject} from: {emailAdr}'
    

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        service.users()
        .messages()                              
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  return send_message
