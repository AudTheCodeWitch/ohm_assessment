import logging
import environment
environment.set('development')
from app_main import app

# Bootstrap(app)
# ------------------------------------------------------------------------------------------------
###############         Server Start       ####################################
# ------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.logger.setLevel(logging.DEBUG)
    app.run(host='127.0.0.1', port=6543, static_files={'': 'public'}, debug=True)
