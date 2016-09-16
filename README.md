# Telegram bot example
## This repo was created to reproduce strange bug

### Install requirements
```
pip install -r requirements.txt
```

### Start the bot via command line
```
python run.py 123:botTokenHere
```

### Reproduce the error
Just write to the bot then bot will try to send your response with Markdown text and will fail. You will find the error in the command line. Example of the error:
```
telepot.exception.TelegramError: ('Bad Request: Wrong port number specified in the URL', 400, {'ok': False, 'description': 'Bad Request: Wrong port number specified in the URL', 'error_code': 400})
ERROR:root:on_close() called due to TelegramError: ('Bad Request: Wrong port number specified in the URL', 400, {'ok': False, 'description': 'Bad Request: Wrong port number specified in the URL', 'error_code': 400})
```
