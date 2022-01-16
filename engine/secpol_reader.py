from configparser import ConfigParser
from engine.mappings import *

# For Debugging purposes
from inspect import currentframe, getframeinfo

""" Variables set up """
SECTIONS = [
    "System Access",
    "Event Audit",
    "Registry Values",
    "Privilege Rights"
]

# Un-used yet..
REG_VALUE_TYPES = ["REG_SZ", "REG_DWORD"]

check_status = [
    "PASSED -",
    "FAILED -",
    "HALF -",
    "MANUAL -"
]

input_path = "C:\\Users\\andreyk\\PycharmProjects\\SecPol_Audit\\tests\\CIS.inf"
brute_dict = "C:\\Users\\andreyk\\PycharmProjects\\SecPol_Audit\\engine\\common_names.txt"


def sec_pol_reader(sec_pol_file: str):
    """ Reading sec_pol.inf file function """

    parser = ConfigParser()
    with open(sec_pol_file, encoding="utf-16") as stream:
        parser.read_string('[default]\n' + stream.read())

    return parser


def easy_check(sec_pol_object: ConfigParser):
    """ Easy checks function based on "Enabled-Disabled" values checkup sections System Access, Registry Values &
    Audit Values """
    all_checks = list()

    # System Access
    for key in sec_pol_object[SECTIONS[0]]:
        for k, v in system_access_1.items():
            if key == k.lower():
                stat = sec_pol_object.get(SECTIONS[0], k)

                if v[1] == stat:
                    all_checks.append([check_status[0], v[0], enable_disable_switch.get(stat)])
                elif v[1] != stat:
                    all_checks.append([check_status[1], v[0], enable_disable_switch.get(stat)])
                else:
                    print(
                        f"Checking Conditions weren't met, check the code for a fix:\n"
                        f"File name: {getframeinfo(currentframe()).filename}\n"
                        f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                    )

    # Audit Values
    for key in sec_pol_object[SECTIONS[1]]:
        for k, v in event_audit.items():
            if key == k.lower():
                stat = sec_pol_object.get(SECTIONS[1], k)
                if int(stat) == 3:
                    all_checks.append([check_status[0], v[0], audit_reg_values.get(stat)])
                elif int(stat) == 2:
                    all_checks.append([check_status[2], v[0], audit_reg_values.get(stat)])
                elif int(stat) == 1:
                    all_checks.append([check_status[2], v[0], audit_reg_values.get(stat)])
                elif int(stat) == 0:
                    all_checks.append([check_status[1], v[0], audit_reg_values.get(stat)])
                else:
                    print(
                        f"Checking Conditions weren't met, check the code for a fix:\n"
                        f"File name: {getframeinfo(currentframe()).filename}\n"
                        f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                    )

    # Registry Values
    for key in sec_pol_object[SECTIONS[2]]:
        for k, v in registry_values_1.items():
            if key == k.lower():
                stat = sec_pol_object.get(SECTIONS[2], k).replace('"', '').split(",")

                if v[1] == stat[1]:
                    all_checks.append([check_status[0], v[0], enable_disable_switch.get(stat[1])])
                elif v[1] != stat[1]:
                    all_checks.append([check_status[1], v[0], enable_disable_switch.get(stat[1])])
                else:
                    print(
                        f"Checking Conditions weren't met, check the code for a fix:\n"
                        f"File name: {getframeinfo(currentframe()).filename}\n"
                        f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                    )

    return all_checks


def system_access_check(sec_pol_object: ConfigParser, dictionary_supplied: str):
    """ Checking System Access not Enabled / Disabled based values """

    all_checks = list()

    for key in sec_pol_object[SECTIONS[0]]:
        for k, v in system_access.items():
            if key == k.lower():
                stat = sec_pol_object.get(SECTIONS[0], k)
                # Make it use able before make it reusable :)
                if v == "Minimum password age":
                    if int(stat) >= 1:
                        all_checks.append([check_status[0], v, stat])
                    elif int(stat) < 1:
                        all_checks.append([check_status[1], v, stat])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                if v == "Maximum password age":
                    if int(stat) <= 90:
                        all_checks.append([check_status[0], v, stat])
                    elif int(stat) > 90 or int(stat) == 0:
                        all_checks.append([check_status[1], v, stat])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                if v == "Minimum password length":
                    if int(stat) >= 8:
                        all_checks.append([check_status[0], v, stat])
                    elif int(stat) < 8:
                        all_checks.append([check_status[1], v, stat])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                if v == "Enforce password history":
                    if int(stat) >= 5:
                        all_checks.append([check_status[0], v, stat])
                    elif int(stat) < 5:
                        all_checks.append([check_status[1], v, stat])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                if v == "Account lockout threshold":
                    if int(stat) >= 1:
                        all_checks.append([check_status[0], v, stat])
                    elif int(stat) < 1:
                        all_checks.append([check_status[1], v, stat])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                if v == "Reset account lockout counter after":
                    if int(stat) >= 5:
                        all_checks.append([check_status[0], v, stat])
                    elif int(stat) < 5:
                        all_checks.append([check_status[1], v, stat])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                if v == "Account lockout duration":
                    if int(stat) >= 5 or int(stat) == 0:
                        all_checks.append([check_status[0], v, stat])
                    elif int(stat) < 5:
                        all_checks.append([check_status[0], v, stat])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                    # You can add names to list or pass some name dictionary to check against
                # in "dictionary_supplied" variable
                common_names = []  # "Admin", "admin", "Administrator", etc...
                filter_double_passed = set()
                if len(dictionary_supplied) > 0:
                    with open(dictionary_supplied, "r", encoding="utf8") as names:
                        for line in names:
                            common_names.append(line.strip("\n"))
                if v == "Accounts: Rename administrator account" or v == "Accounts: Rename guest account":
                    for common in common_names:
                        if common in stat:
                            # print(
                            #     stylize("FAILED -", BOLD_RED),
                            #     stylize(v, BOLD_ORANGE),
                            #     stylize(stat, BOLD_BLUE),
                            #     stylize(f"- Contains common name:", BOLD_YELLOW),
                            #     stylize(common, BOLD_RED)
                            # )
                            all_checks.append([check_status[1], v, stat, f"- Contains common name: {common}"])
                        elif common not in stat:
                            pass
                        else:
                            print(
                                f"Checking Conditions weren't met, check the code for a fix:\n"
                                f"File name: {getframeinfo(currentframe()).filename}\n"
                                f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                            )
    return all_checks


def registry_values_check(sec_pol_object: ConfigParser):
    """ Checking Registry Values not Enabled / Disabled based values """

    all_checks = list()

    for key in sec_pol_object[SECTIONS[2]]:
        for k, v in registry_values.items():
            if key == k.lower():
                stat = sec_pol_object.get(SECTIONS[2], k).replace('"', '').split(",")

                # Manual checks
                if v[0] == "Network access: Remotely accessible registry paths" or \
                        v[0] == "Network access: Remotely accessible registry paths and subpaths" or \
                        v[0] == "Interactive logon: Message text for users attempting to log on" or \
                        v[0] == "Interactive logon: Message title for users attempting to log on" or \
                        v[0] == "Network access: Restrict clients allowed to make remote calls to SAM" or \
                        v[0] == "System settings: Optional subsystems":

                    all_checks.append([check_status[3], v[0], stat[1]])

                elif v[0] == "Domain member: Maximum machine account password age":
                    if int(stat[1]) <= 30 and int(stat[1]) != 0:
                        all_checks.append([check_status[0], v[0], stat[1]])
                    elif int(stat[1]) > 30:
                        all_checks.append([check_status[1], v[0], stat[1]])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                elif v[0] == "Microsoft network server: Amount of idle time required before suspending session":
                    if int(stat[1]) <= 15 and int(stat[1]) != 99999:
                        all_checks.append([check_status[0], v[0], stat[1]])
                    elif int(stat[1]) > 15:
                        all_checks.append([check_status[1], v[0], stat[1]])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                elif v[0] == "Interactive logon: Machine inactivity limit":
                    if int(stat[1]) <= 900:
                        all_checks.append([check_status[0], v[0], stat[1]])
                    elif int(stat[1]) >= 901:
                        all_checks.append([check_status[1], v[0], stat[1]])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                elif v[0] == "Interactive logon: Prompt user to change password before expiration":
                    if int(stat[1]) >= 14 and int(stat[1]) != 0:
                        all_checks.append([check_status[0], v[0], stat[1]])
                    elif int(stat[1]) >= 4:
                        all_checks.append([check_status[1], v[0], stat[1]])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                elif v[0] == "Interactive logon: Number of previous logons to cache (in case domain controller is not available)":
                    if int(stat[1]) <= 2:
                        all_checks.append([check_status[0], v[0], stat[1]])
                    elif int(stat[1]) > 2:
                        all_checks.append([check_status[1], v[0], stat[1]])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

                elif v[0] == "":
                    if int(stat[1]) <= 2:
                        all_checks.append([check_status[0], v[0], stat[1]])
                    elif int(stat[1]) > 2:
                        all_checks.append([check_status[1], v[0], stat[1]])
                    else:
                        print(
                            f"Checking Conditions weren't met, check the code for a fix:\n"
                            f"File name: {getframeinfo(currentframe()).filename}\n"
                            f"Line Number: ~{getframeinfo(currentframe()).lineno}"
                        )

    return all_checks
