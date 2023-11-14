import ssl
import os
import sslkeylog

# Set Environment Key
sslkeylog.set_keylog(os.environ.get('/opt/ssl.log'))

# Export SSLKEYLOGFILE
context = ssl.create_default_context()
