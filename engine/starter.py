import os
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


def start(output_filename: str):
    writer = pd.ExcelWriter(args.out_path + output_filename, engine='xlsxwriter')

    path_to_files = []

    if len(args.input_path) >= 2:
        path_to_files.append(args.input_path)

        # Iterate over .csv files in a path
        files = [x for x in os.listdir(path=path_to_files[0]) if x.lower().endswith(".inf")]
        if len(files) > 0:
            for file in files:

                one = checks.registry_values_check(
                    sec_pol_object=checks.sec_pol_reader(
                        sec_pol_file=path_to_files[0] + file)
                )

                two = checks.system_access_check(
                    sec_pol_object=checks.sec_pol_reader(
                        sec_pol_file=path_to_files[0] + file),
                    dictionary_supplied=args.brute_dict
                )

                three = checks.easy_check(
                    sec_pol_object=checks.sec_pol_reader(
                        sec_pol_file=path_to_files[0] + file)
                )

                total = one + two + three

                if args.out_path:
                    dataframe = pd.DataFrame(total)
                    if len(dataframe.columns) == 3:
                        dataframe.columns = ["Status", "Name", "Configuration"]
                        dataframe.sort_values(by="Status", inplace=True)
                        dataframe.to_excel(writer, sheet_name=file, startrow=0, index=False)
                    elif len(dataframe.columns) == 4:
                        dataframe.columns = ["Status", "Name", "Configuration", "Comments"]
                        dataframe.sort_values(by="Status", inplace=True)
                        dataframe.to_excel(writer, sheet_name=file, startrow=0, index=False)
                    else:
                        print("Column count miss match")

                print("-" * 150 + "\n")
                print(f"Checking file: {path_to_files[0] + file}")
                print("-" * 150 + "\n")

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
        elif len(files) == 0:
            print(f"\nNo files with extension .inf were found in the specified path:\n\n- {args.input_path}\n\n"
                  f"Specify different path & try again.\n")

    writer.save()
