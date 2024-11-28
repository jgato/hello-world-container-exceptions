import time
import os
import traceback
import sys

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
        # Log the exception stack trace to stderr
        print("Caught an exception with detailed traceback:", file=sys.stderr)
        print("".join(traceback.format_exception(None, e, e.__traceback__)), file=sys.stderr)

def raise_exception():
    # Obtener el tiempo de espera de la variable de entorno, con un valor por defecto de 60 segundos
    wait_time = int(os.getenv("WAIT_TIME", 60))

    while True:
        try:
            print(f"Running... Exception will be raised in {wait_time} seconds.", file=sys.stdout)
            time.sleep(wait_time)
            cause_complex_exception()
        except Exception as e:
            # Log the exception and continue
            print(f"Continuing after catching an exception: {e}", file=sys.stderr)
            continue

if __name__ == "__main__":
    raise_exception()

