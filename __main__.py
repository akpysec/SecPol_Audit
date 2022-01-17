from engine.cli_args import args
import engine.secpol_reader as checks
import colored
from colored import stylize
import pandas as pd

""" Coloring Scheme """
BOLD_RED = colored.fg("red") + colored.attr("bold")
BOLD_BLUE = colored.fg("blue") + colored.attr("bold")
BOLD_GREEN = colored.fg("green") + colored.attr("bold")
BOLD_TURQUOISE = colored.fg("dark_turquoise") + colored.attr("bold")
BOLD_ORANGE = colored.fg("dark_orange_3a") + colored.attr("bold")
BOLD_YELLOW = colored.fg("yellow_3b") + colored.attr("bold")

one = checks.registry_values_check(
    sec_pol_object=checks.sec_pol_reader(
        sec_pol_file=args.input_path)
)

two = checks.system_access_check(
    sec_pol_object=checks.sec_pol_reader(
        sec_pol_file=args.input_path),
    dictionary_supplied=args.brute_dict
)

three = checks.easy_check(
    sec_pol_object=checks.sec_pol_reader(
        sec_pol_file=args.input_path)
)

total = one + two + three

if args.out_path:
    dataframe = pd.DataFrame(total)
    dataframe.columns = ["Status", "Name", "Configuration", "Comment"]
    dataframe.sort_values(by="Status", inplace=True)
    dataframe.to_csv(args.out_path, index=False)

for t in sorted(total):
    if len(t) == 3:
        if t[0] == checks.check_status[0]:
            print(stylize(t[0], BOLD_GREEN), t[1], stylize(t[2], BOLD_TURQUOISE))
        elif t[0] == checks.check_status[1]:
            print(stylize(t[0], BOLD_RED), t[1], stylize(t[2], BOLD_TURQUOISE))
        elif t[0] == checks.check_status[3]:
            print(stylize(t[0], BOLD_BLUE), t[1], stylize(t[2], BOLD_TURQUOISE))
        elif t[0] == checks.check_status[2]:
            print(stylize(t[0], BOLD_ORANGE), t[1], stylize(t[2], BOLD_TURQUOISE))
    elif len(t) == 4:
        if t[0] == checks.check_status[0]:
            print(stylize(t[0], BOLD_GREEN), t[1], stylize(t[2], BOLD_TURQUOISE), stylize(t[3], BOLD_ORANGE))
        elif t[0] == checks.check_status[1]:
            print(stylize(t[0], BOLD_RED), t[1], stylize(t[2], BOLD_TURQUOISE), stylize(t[3], BOLD_ORANGE))
        elif t[0] == checks.check_status[3]:
            print(stylize(t[0], BOLD_BLUE), t[1], stylize(t[2], BOLD_TURQUOISE), stylize(t[3], BOLD_ORANGE))
        elif t[0] == checks.check_status[2]:
            print(stylize(t[0], BOLD_ORANGE), t[1], stylize(t[2], BOLD_TURQUOISE), stylize(t[3], BOLD_ORANGE))
