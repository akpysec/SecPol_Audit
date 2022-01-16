# From MS documentation, for User Rights checks
sid = {
    "S-1-0": "Null Authority",
    "S-1-0-0": "Nobody",
    "S-1-1": "World Authority",
    "S-1-1-0": "Everyone",
    "S-1-16-0": "Untrusted Mandatory Level",
    "S-1-16-12288": "High Mandatory Level",
    "S-1-16-16384": "System Mandatory Level",
    "S-1-16-20480": "Protected Process Mandatory Level",
    "S-1-16-28672": "Secure Process Mandatory Level",
    "S-1-16-4096": "Low Mandatory Level",
    "S-1-16-8192": "Medium Mandatory Level",
    "S-1-16-8448": "Medium Plus Mandatory Level",
    "S-1-2": "Local Authority",
    "S-1-2-0": "Local",
    "S-1-2-1": "Console Logon",
    "S-1-3": "Creator Authority",
    "S-1-3-0": "Creator Owner",
    "S-1-3-1": "Creator Group",
    "S-1-3-2": "Creator Owner Server",
    "S-1-3-3": "Creator Group Server",
    "S-1-3-4": "Owner Rights",
    "S-1-4": "Non-unique Authority",
    "S-1-5": "NT Authority",
    "S-1-5-1": "Dialup",
    "S-1-5-10": "Principal Self",
    "S-1-5-11": "Authenticated Users",
    "S-1-5-113": "Local account",
    "S-1-5-114": "Local account and member of Administrators group",
    "S-1-5-12": "Restricted Code",
    "S-1-5-13": "Terminal Server User",
    "S-1-5-14": "Remote Interactive Logon",
    "S-1-5-15": "This Organization",
    "S-1-5-17": "IIS_USRS",
    "S-1-5-18": "System (or LocalSystem)",
    "S-1-5-19": "NT Authority (LocalService)",
    "S-1-5-2": "Network",
    "S-1-5-20": "Network Service",
    "S-1-5-21domain-498": "Enterprise Read-only Domain Controllers",
    "S-1-5-21domain-500": "Administrator",
    "S-1-5-21domain-501": "Guest",
    "S-1-5-21domain-502": "KRBTGT",
    "S-1-5-21domain-512": "Domain Admins",
    "S-1-5-21domain-513": "Domain Users",
    "S-1-5-21domain-514": "Domain Guests",
    "S-1-5-21domain-515": "Domain Computers",
    "S-1-5-21domain-516": "Domain Controllers",
    "S-1-5-21domain-517": "Cert Publishers",
    "S-1-5-21domain-520": "Group Policy Creator Owners",
    "S-1-5-21domain-521": "Read-only Domain Controllers",
    "S-1-5-21-domain-522": "Cloneable Domain Controllers",
    "S-1-5-21domain-526": "Key Admins",
    "S-1-5-21domain-527": "Enterprise Key Admins",
    "S-1-5-21domain-553": "RAS and IAS Servers",
    "S-1-5-21domain-571": "Allowed RODC Password Replication Group",
    "S-1-5-21domain-572": "Denied RODC Password Replication Group",
    "S-1-5-21root domain-518": "Schema Admins",
    "S-1-5-21root domain-519": "Enterprise Admins",
    "S-1-5-3": "Batch",
    "S-1-5-32-544": "Administrators",
    "S-1-5-32-545": "Users",
    "S-1-5-32-546": "Guests",
    "S-1-5-32-547": "Power Users",
    "S-1-5-32-548": "Account Operators",
    "S-1-5-32-549": "Server Operators",
    "S-1-5-32-550": "Print Operators",
    "S-1-5-32-551": "Backup Operators",
    "S-1-5-32-552": "Replicators",
    "S-1-5-32-554": "Pre-Windows 2000 Compatible Access",
    "S-1-5-32-555": "Remote Desktop Users",
    "S-1-5-32-556": "Network Configuration Operators",
    "S-1-5-32-557": "Incoming Forest Trust Builders",
    "S-1-5-32-558": "Performance Monitor Users",
    "S-1-5-32-559": "Performance Log Users",
    "S-1-5-32-560": "Windows Authorization Access Group",
    "S-1-5-32-561": "Terminal Server License Servers",
    "S-1-5-32-562": "Distributed COM Users",
    "S-1-5-32-569": "Cryptographic Operators",
    "S-1-5-32-573": "Event Log Readers",
    "S-1-5-32-574": "Certificate Service DCOM Access",
    "S-1-5-32-575": "RDS Remote Access Servers",
    "S-1-5-32-576": "RDS Endpoint Servers",
    "S-1-5-32-577": "RDS Management Servers",
    "S-1-5-32-578": "Hyper-V Administrators",
    "S-1-5-32-579": "Access Control Assistance Operators",
    "S-1-5-32-580": "Remote Management Users",
    "S-1-5-32-582": "Storage Replica Administrators",
    "S-1-5-4": "Interactive",
    "S-1-5-5-X-Y": "Logon Session",
    "S-1-5-6": "Service",
    "S-1-5-64-10": "NTLM Authentication",
    "S-1-5-64-14": "SChannel Authentication",
    "S-1-5-64-21": "Digest Authentication",
    "S-1-5-7": "Anonymous Logon",
    "S-1-5-8": "Proxy",
    "S-1-5-80": "NT Service",
    "S-1-5-80-0": "NT Services\\All Services",
    "S-1-5-83-0": "NT Virtual Machine\\Virtual Machines",
    "S-1-5-9": "Enterprise Domain Controllers",
    "S-1-5-90-0": "Windows Manager\\Windows Manager Group",
    "S-1-5-domain-500": "Administrator",
    "S-1-5-domain-501": "Guest",
    "S-1-5-domain-502": "krbtgt",
    "S-1-5-domain-512": "Domain Admins",
    "S-1-5-domain-513": "Domain Users",
    "S-1-5-domain-514": "Domain Guests",
    "S-1-5-domain-515": "Domain Computers",
    "S-1-5-domain-516": "Domain Controllers",
    "S-1-5-domain-517": "Cert Publishers",
    "S-1-5-domain-520": "Group Policy Creator Owners",
    "S-1-5-domain-553": "RAS and IAS Servers",
    "S-1-5-root domain-518": "Schema Admins",
    "S-1-5-root domain-519": "Enterprise Admins"
}
# Enabled | Disabled - easy checks
system_access_1 = {
    "PasswordComplexity": ["Password Policy: Password must meet complexity requirements", "1"],
    "EnableAdminAccount": ["Accounts: Enable Admin Account", "1"],
    "ClearTextPassword": ["Clear Text Password", "0"],
    "LSAAnonymousNameLookup": ["LSA Anonymous Name Lookup", "0"],
    "EnableGuestAccount": ["Accounts: Enable Guest Account", "0"],
    "RequireLogonToChangePassword": ["Require Logon To Change Password", "0"],
    "ForceLogoffWhenHourExpire": ["Force Logoff When Hour Expire", "1"],
}
registry_values_1 = {
    "MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\DisablePasswordChange":
        [
            "Domain member: Disable machine account password changes",
            "0",
            "Disabled"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\FIPSAlgorithmPolicy\\Enabled":
        [
            "System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\DisableDomainCreds":
        [
            "Network access: Do not allow storage of passwords and credentials for network authentication",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\CrashOnAuditFail":
        [
            "Audit: Shut down system immediately if unable to log security audits",
            "1",
        ],
    "MACHINE\\Software\\Policies\\Microsoft\\Windows\\Safer\\CodeIdentifiers\\AuthenticodeEnabled":
        [
            "System settings: Use Certificate Rules on Windows Executables for Software Restriction Policies",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ValidateAdminCodeSignatures":
        [
            "User Account Control: Only elevate executables that are signed and validated",
            "0",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\UndockWithoutLogon":
        [
            "Devices: Allow undock without having to log on",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\PromptOnSecureDesktop":
        [
            "User Account Control: Switch to the secure desktop when prompting for elevation",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Print\\Providers\\LanMan Print Services\\Servers\\AddPrinterDrivers":
        [
            "Devices: Prevent users from installing printer drivers",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\UseMachineId":
        [
            "Network security: Allow Local System to use computer identity for NTLM",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\SCENoApplyLegacyAuditPolicy":
        [
            "Audit: Force audit policy subcategory settings (Windows Vista or later) to override audit policy category settings",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\RestrictAnonymousSAM":
        [
            "Network access: Do not allow anonymous enumeration of SAM accounts",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\RestrictAnonymous":
        [
            "Network access: Do not allow anonymous enumeration of SAM accounts and shares",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\NoLMHash":
        [
            "Network security: Do not store LAN Manager hash value on next password change",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\ProtectionMode":
        [
            "System objects: Strengthen default permissions of internal system objects (e.g. Symbolic Links)",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\ClearPageFileAtShutdown":
        [
            "Shutdown: Clear virtual memory pagefile",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Kernel\\ObCaseInsensitive":
        [
            "System objects: Require case insensitivity for non Windows subsystems",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters\\RequireSecuritySignature":
        [
            "Microsoft network client: Digitally sign communications (always)",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters\\EnableSecuritySignature":
        [
            "Microsoft network client: Digitally sign communications (if server agrees)",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanManServer\\Parameters\\RestrictNullSessAccess":
        [
            "Network access: Restrict anonymous access to Named Pipes and Shares",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanManServer\\Parameters\\RequireSecuritySignature":
        [
            "Microsoft network server: Digitally sign communications (always)",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanManServer\\Parameters\\EnableSecuritySignature":
        [
            "Microsoft network server: Digitally sign communications (if client agrees)",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanManServer\\Parameters\\EnableForcedLogOff":
        [
            "Microsoft network server: Disconnect clients when logon hours expire",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\SignSecureChannel":
        [
            "Domain member: Digitally sign secure channel data (when possible)",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\SealSecureChannel":
        [
            "Domain member: Digitally encrypt secure channel data (when possible).",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\RequireStrongKey":
        [
            "Domain member: Require strong (Windows 2000 or Later) session key",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\RequireSignOrSeal":
        [
            "Domain member: Digitally encrypt or sign secure channel data (always)",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\LimitBlankPasswordUse":
        [
            "Accounts: Limit local account use of blank passwords to console logon only",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\FilterAdministratorToken":
        [
            "User Account Control: Admin Approval Mode for the Built-in Administrator account",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableVirtualization":
        [
            "User Account Control: Virtualize file and registry write failures to per-user locations",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableUIADesktopToggle":
        [
            "User Account Control: Allow UIAccess applications to prompt for elevation without using the secure desktop",
            "0",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableSecureUIAPaths":
        [
            "User Account Control: Only elevate UIAccess applications that are installed in secure locations",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableLUA":
        [
            "User Account Control: Run all administrators in Admin Approval Mode",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\EnableInstallerDetection":
        [
            "User Account Control: Detect application installations and prompt for elevation",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\DontDisplayLastUserName":
        [
            "Interactive logon: Do not display last user name",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\ForceUnlockLogon":
        [
            "Interactive logon: Require Domain Controller Authentication to unlock workstation",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\AllocateFloppies":
        [
            "Devices: Restrict floppy access to locally logged-on user only",
            "1",
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\AllocateCDRoms":
        [
            "Devices: Restrict CD-ROM access to locally logged-on user only",
            "1",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters\\EnablePlainTextPassword":
        [
            "Microsoft network client: Send unencrypted password to third-party SMB servers",
            "0",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\DisableCAD":
        [
            "Interactive logon: Do not require CTRL+ALT+DEL",
            "0",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\FullPrivilegeAuditing":
        [
            "Audit: Audit the use of Backup and Restore privilege",
            "0",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ShutdownWithoutLogon":
        [
            "Shutdown: Allow system to be shutdown without having to log on",
            "0",
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ScForceOption":
        [
            "Interactive logon: Smart card removal behavior",
            "0",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\EveryoneIncludesAnonymous":
        [
            "Network access: Let everyone permissions apply to anonymous users",
            "0",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\AuditBaseObjects":
        [
            "Audit: Audit the access of global system objects",
            "0",
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\MSV1_0\\allownullsessionfallback":
        [
            "Network security: Allow LocalSystem NULL session fallback",
            "0",
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Setup\\RecoveryConsole\\SetCommand":
        [
            "Recovery console: Allow floppy copy and access to all drives and folders",
            "0",
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Setup\\RecoveryConsole\\SecurityLevel":
        [
            "Recovery console: Allow automatic administrative logon",
            "0",
        ]
}
# Multiple condition checks
system_access = {
    "MinimumPasswordAge": "Password Policy: Minimum password age",
    "MaximumPasswordAge": "Password Policy: Maximum password age",
    "MinimumPasswordLength": "Password Policy: Minimum password length",
    "PasswordHistorySize": "Password Policy: Enforce password history",
    "LockoutBadCount": "Lockout Policy: Account lockout threshold",
    "ResetLockoutCount": "Lockout Policy: Reset account lockout counter after",
    "LockoutDuration": "Lockout Policy: Account lockout duration",
    "NewAdministratorName": "Accounts: Rename administrator account",
    "NewGuestName": "Accounts: Rename guest account"
}
event_audit = {
    "AuditSystemEvents": ["Audit System Events", "3"],
    "AuditLogonEvents": ["Audit Logon Events", "3"],
    "AuditObjectAccess": ["Audit Object Access", "3"],
    "AuditPrivilegeUse": ["Audit Privilege Use", "3"],
    "AuditPolicyChange": ["Audit Policy Change", "3"],
    "AuditAccountManage": ["Audit Account Manage", "3"],
    "AuditProcessTracking": ["Audit Process Tracking", "3"],
    "AuditDSAccess": ["Audit DS Access", "3"],
    "AuditAccountLogon": ["Audit Account Logon", "3"]
}

registry_values = {
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\RestrictRemoteSAM":
        [
            "Network access: Restrict clients allowed to make remote calls to SAM",
            "O:BAG:BAD:(A;;RC;;;BA)",
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\Netlogon\\Parameters\\MaximumPasswordAge":
        [
            "Domain member: Maximum machine account password age",
            "30 (or less, but not 0)",
            "30 or less, excluding 0"
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LDAP\\LDAPClientIntegrity":
        [
            "Network security: LDAP client signing requirements",
            "1",
            '"Negotiate signing" at a minimum'
        ],
    "MACHINE\\System\\CurrentControlSet\\Services\\LanManServer\\Parameters\\AutoDisconnect":
        [
            "Microsoft network server: Amount of idle time required before suspending session",
            "15",
            "15 minutes or less"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\SubSystems\\optional":
        [
            "System settings: Optional subsystems",
            "",
            "Blank"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\SecurePipeServers\\Winreg\\AllowedPaths\\Machine":
        [
            "Network access: Remotely accessible registry paths",
            "Registry Paths",
            "Check Manually"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\SecurePipeServers\\Winreg\\AllowedExactPaths\\Machine":
        [
            "Network access: Remotely accessible registry paths and subpaths",
            "Specific Registry Paths",
            "Check Manually"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\MSV1_0\\NTLMMinServerSec":
        [
            "Network security: Minimum session security for NTLM SSP based (including secure RPC) servers",
            "0x20080000",
            "537395200"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\MSV1_0\\NTLMMinClientSec":
        [
            "Network security: Minimum session security for NTLM SSP based (including secure RPC) clients",
            "0x20080000",
            "537395200"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\LmCompatibilityLevel":
        [
            "Network security: LAN Manager authentication level",
            "5",
            "Send NTLMv2 response only. Refuse LM & NTLM"
        ],
    "MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\ForceGuest":
        [
            "Network access: Sharing and security model for local accounts",
            "0",
            "Classic - local users authenticate as themselves"
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\LegalNoticeText":
        [
            "Interactive logon: Message text for users attempting to log on",
            "Warning text",
            "Check manually"
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\LegalNoticeCaption":
        [
            "Interactive logon: Message title for users attempting to log on",
            "Warning text",
            "Check manually"
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\InactivityTimeoutSecs":
        [
            "Interactive logon: Machine inactivity limit",
            "0x00000384",
            "900 (or less)"
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ConsentPromptBehaviorUser":
        [
            "User Account Control: Behavior of the elevation prompt for standard users",
            "0",
            "Automatically deny elevation requests"
        ],
    "MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\\ConsentPromptBehaviorAdmin":
        [
            "User Account Control: Behavior of the elevation prompt for administrators in Admin Approval Mode",
            "4",
            "Prompt for consent"
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\ScRemoveOption":
        [
            "Interactive logon: Smart card removal behavior",
            "1",  # or "2"
            "Lock Workstation or Force Logoff"
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\PasswordExpiryWarning":
        [
            "Interactive logon: Prompt user to change password before expiration",
            "14 (or greater)",
            "14 days or more"
        ],
    "MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\CachedLogonsCount":
        [
            "Interactive logon: Number of previous logons to cache (in case domain controller is not available)",
            "4 (or less)",
            "4 logons or less"
        ],
}

privilege_rights = {
    "SeBackupPrivilege": ["Back up files and directories", "VALUE", "READABLE_VALUE"],
    "SeChangeNotifyPrivilege": ["Bypass traverse checking", "VALUE", "READABLE_VALUE"],
    "SeSystemtimePrivilege": ["Change the system time", "VALUE", "READABLE_VALUE"],
    "SeTimeZonePrivilege": ["Change the time zone", "VALUE", "READABLE_VALUE"],
    "SeCreatePagefilePrivilege": ["Create a page file", "VALUE", "READABLE_VALUE"],
    "SeCreateTokenPrivilege": ["Create a token object", "VALUE", "READABLE_VALUE"],
    "SeCreateGlobalPrivilege": ["Create global objects", "VALUE", "READABLE_VALUE"],
    "SeCreatePermanentPrivilege": ["Create permanent shared objects", "VALUE", "READABLE_VALUE"],
    "SeCreateSymbolicLinkPrivilege": ["Create symbolic links", "VALUE", "READABLE_VALUE"],
    "SeDebugPrivilege": ["Debug programs", "VALUE", "READABLE_VALUE"],
    "SeDenyNetworkLogonRight": ["Deny access to this computer from the network", "VALUE", "READABLE_VALUE"],
    "SeDenyBatchLogonRight": ["Deny log on as a batch job", "VALUE", "READABLE_VALUE"],
    "SeDenyServiceLogonRight": ["Deny log on as a service", "VALUE", "READABLE_VALUE"],
    "SeDenyInteractiveLogonRight": ["Deny log on locally", "VALUE", "READABLE_VALUE"],
    "SeDenyRemoteInteractiveLogonRight": ["Deny log on through Remote Desktop Services", "VALUE", "READABLE_VALUE"],
    "SeEnableDelegationPrivilege": ["Enable computer and user accounts to be trusted for delegation", "VALUE",
                                    "READABLE_VALUE"],
    "SeRemoteShutdownPrivilege": ["Force shutdown from a remote system", "VALUE", "READABLE_VALUE"],
    "SeAuditPrivilege": ["Generate security audits", "VALUE", "READABLE_VALUE"],
    "SeImpersonatePrivilege": ["Impersonate a client after authentication", "VALUE", "READABLE_VALUE"],
    "SeIncreaseWorkingSetPrivilege": ["Increase a process working set", "VALUE", "READABLE_VALUE"],
    "SeIncreaseBasePriorityPrivilege": ["Increase scheduling priority", "VALUE", "READABLE_VALUE"],
    "SeLoadDriverPrivilege": ["Load and unload device drivers", "VALUE", "READABLE_VALUE"],
    "SeLockMemoryPrivilege": ["Lock pages in memory", "VALUE", "READABLE_VALUE"],
    "SeBatchLogonRight": ["Log on as a batch job", "VALUE", "READABLE_VALUE"],
    "SeServiceLogonRight": ["Log on as a service", "VALUE", "READABLE_VALUE"],
    "SeSecurityPrivilege": ["Manage auditing and security log", "VALUE", "READABLE_VALUE"],
    "SeRelabelPrivilege": ["Modify an object label", "VALUE", "READABLE_VALUE"],
    "SeSystemEnvironmentPrivilege": ["Modify firmware environment values", "VALUE", "READABLE_VALUE"],
    "SeManageVolumePrivilege": ["Perform volume maintenance tasks", "VALUE", "READABLE_VALUE"],
    "SeProfileSingleProcessPrivilege": ["Profile single process", "VALUE", "READABLE_VALUE"],
    "SeSystemProfilePrivilege": ["Profile system performance", "VALUE", "READABLE_VALUE"],
    "SeUndockPrivilege": ["Remove computer from docking station", "VALUE", "READABLE_VALUE"],
    "SeAssignPrimaryTokenPrivilege": ["Replace a process level token", "VALUE", "READABLE_VALUE"],
    "SeRestorePrivilege": ["Restore files and directories", "VALUE", "READABLE_VALUE"],
    "SeShutdownPrivilege": ["Shut down the system", "VALUE", "READABLE_VALUE"],
    "SeSyncAgentPrivilege": ["Synchronize directory service data", "VALUE", "READABLE_VALUE"],
    "SeTakeOwnershipPrivilege": ["Take ownership of files or other objects", "VALUE", "READABLE_VALUE"],
    "SeDelegateSessionUserImpersonatePrivilege": ["Modify firmware environment values", "VALUE", "READABLE_VALUE"]
}

audit_reg_values = {
    '0': 'No auditing',
    '1': 'Success',
    '2': 'Failure',
    '3': 'Success, Failure',
}

enable_disable_switch = {
    '0': 'Disabled',
    '1': 'Enabled'
}
