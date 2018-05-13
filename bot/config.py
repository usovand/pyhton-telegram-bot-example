#!/usr/bin/env python3

# Api token file
TOKEN_FILE = 'token.txt'

with open(TOKEN_FILE, 'r') as f:
    TOKEN = f.read()

# Api url
API_URL = 'https://api.telegram.org/bot' + TOKEN + '/{method}'

# Local server port
PORT = 8080

# Webhook hostname
WEBHOOK_HOST = 'nixdrey.com'

# Webhook route
WEBHOOK_ROUTE = '/webhook/' + TOKEN

# Webhook url
WEBHOOK_URL = 'https://{hostname}{route}'.format(hostname=WEBHOOK_HOST, route=WEBHOOK_ROUTE)
