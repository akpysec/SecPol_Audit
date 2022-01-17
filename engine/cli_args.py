import argparse

parser = argparse.ArgumentParser()

# Creating flags
parser.add_argument('-I', '--input-file',
                    required=True,
                    default=None,
                    dest='input_path',
                    help='Provide path to exported "secpol.inf" file.',
                    type=str
                    )

parser.add_argument('-O', '--output-file',
                    required=False,
                    default=None,
                    dest='out_path',
                    help='Provide output path and file name with .CSV extension',
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

