import sys
from engine.starter import start

if __name__ == '__main__':
    try:
        start(
            output_filename="Parsed_SecPol.xlsx"
        )
    except KeyboardInterrupt as KI:
        print(f'{KI} - Error occurred')
        sys.exit(0)
    except Exception as GE:
        print(f"{GE} - Global Exception occurred")
        sys.exit(0)
