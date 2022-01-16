SecPol.inf file Auditing tool
---

#### This script performs auditing based on CIS Benchmark against Secpol.inf file configuration.

#### Secpol.inf file contains:
Account Policies
- Password Policy
- Account Lockout Policy

Local Policies
- Security Options (Mostly done)
- User Rights Assignment (In Development)
- Audit Policy (Recommended configuring advanced audit policy instead)

#### To export Secpol.inf:

    secedit /export /CFG PATH:/secpol.inf

#### Prerequisites

- Download & Install [Python](https://www.python.org/downloads/) (tested with python ~> 3.8).
- Make sure you have [Git](https://git-scm.com/downloads) installed.
  [requirements.txt](https://github.com/akpysec/SecPol_Audit/blob/master/requirements.txt) file.
- The required libraries can be found in the



#### Installation

    git clone https://github.com/akpysec/SecPol_Audit
    python -m venv SecPol_Audit/venv
    source SecPol_Audit/venv/Scripts/activate
    pip install -r SecPol_Audit/requirements.txt
    python SecPol_Audit --help

#### Usage

    python SecPol_Audit --input-file="secpol.inf" --output-file="secpol.csv"

* For checking username against common name list, add names to
  [Common Names text file](https://github.com/akpysec/SecPol_Audit/blob/master/engine/common_names.txt).

#### License
Firewall RuleBase Audit is released under the
[GNU Public License](https://github.com/akpysec/SecPol_Audit/LICENSE)


#### Contact
Contact me via <akpysec@gmail.com>.
