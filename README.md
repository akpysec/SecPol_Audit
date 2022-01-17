# SecPol.inf file Auditing tool

#### This script performs auditing based on CIS Benchmark against Secpol.inf file configuration.

#

#### Secpol.inf file contains:
Account Policies
- Password Policy
- Account Lockout Policy

Local Policies
- Security Options (Mostly done)
- User Rights Assignment (In Development)
- Audit Policy (Recommended configuring advanced audit policy instead)

#

#### To export Secpol.inf:

    secedit /export /CFG PATH:/secpol.inf

#

#### Prerequisites:

- Download & Install [Python](https://www.python.org/downloads/) (tested with python ~> 3.8).
- Use [Git](https://git-scm.com/downloads) or download this tool otherwise & update installation syntax to match your OS.
- The required libraries can be found in the [requirements.txt](https://github.com/akpysec/SecPol_Audit/blob/master/requirements.txt) file.
- Install [pip](https://pip.pypa.io/en/stable/installation/).

#

#### Installation:

    git clone https://github.com/akpysec/SecPol_Audit
    python -m venv SecPol_Audit/venv
    source SecPol_Audit/venv/Scripts/activate
    pip install -r SecPol_Audit/requirements.txt
    python SecPol_Audit --help

#

#### Usage:

    python SecPol_Audit --input-path="tests/" --output-path="tests/" --common-names="engine/common_names.txt"

* For checking username against common name list, add names to
  [Common Names](https://github.com/akpysec/SecPol_Audit/blob/master/engine/common_names.txt) text file or specify your own file with similar format convention.

#

#### License:
Secpol Audit is released under the
[GNU Public License](https://github.com/akpysec/SecPol_Audit/blob/master/LICENSE)

#

#### Contact:
Contact me via <akpysec@gmail.com>.
