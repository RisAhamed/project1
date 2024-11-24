import logging
import os
from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

import logging
import os
from datetime import datetime

# Create a log file name with the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Create a console handler and set the level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the console handler
formatter = logging.Formatter("[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)

