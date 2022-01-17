import argparse

parser = argparse.ArgumentParser()

# Creating flags
parser.add_argument('-I', '--input-path',
                    required=True,
                    default=None,
                    dest='input_path',
                    help='Provide path to exported "secpol.inf" file(s).',
                    type=str
                    )

parser.add_argument('-O', '--output-path',
                    required=False,
                    default=None,
                    dest='out_path',
                    help='Provide output path for Parsed_Secpol.xlsx file',
                    type=str
                    )

parser.add_argument('-C', '--common-names',
                    required=False,
                    default=None,
                    dest='brute_dict',
                    help='Provide a file with common names',
                    type=str
                    )

args = parser.parse_args()

