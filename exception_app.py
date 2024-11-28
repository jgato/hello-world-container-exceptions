import time
import os
import traceback
import sys
import json
from datetime import datetime

def log_json(message, level="INFO", exception=None):
    """Genera logs en formato JSON."""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "message": message,
        "app": "exception-app",
    }

    if exception:
        log_entry["exception"] = "".join(traceback.format_exception(None, exception, exception.__traceback__))

    # Log to stdout for Vector compatibility
    print(json.dumps(log_entry), file=sys.stdout)
    sys.stdout.flush()

def cause_complex_exception():
    """Genera una excepción con múltiples líneas de error simulando un stack trace complejo."""
    try:
        def level_one():
            level_two()

        def level_two():
            level_three()

        def level_three():
            raise Exception("Custom exception at level three")

        level_one()
    except Exception as e:
        #log_json("An exception occurred", level="ERROR", exception=e)
        # by the moment exception as it is, instead of json prepared for vector
        print("".join(traceback.format_exception(None, e, e.__traceback__)), file=sys.stderr, end="")

def raise_exception():
    # Obtener el tiempo de espera de la variable de entorno, con un valor por defecto de 60 segundos
    wait_time = int(os.getenv("WAIT_TIME", 10))

    while True:
        log_json(f"Running... Exception will be raised in {wait_time} seconds.")
        time.sleep(wait_time)
        cause_complex_exception()

if __name__ == "__main__":
    raise_exception()

