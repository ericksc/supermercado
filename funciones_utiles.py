import random
from datetime import datetime
def crear_id():

    offset = random.randint(0, 1000)
    return int(datetime.now().timestamp() * 1e6) + offset