import sys
from engine.starter import start
from engine.cli_args import args

if __name__ == '__main__':
    try:
        if args.out_file:
            start(
                output_filename=args.out_file
            )
        elif args.out_file is None:
            start(
                output_filename="Parsed_SecPol.xlsx"
            )

    except KeyboardInterrupt as KI:
        print(f'{KI} - Error occurred')
        sys.exit(0)
    except Exception as GE:
        print(f"{GE} - Global Exception occurred")
        sys.exit(0)
