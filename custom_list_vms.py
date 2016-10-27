#!/usr/bin/python
# developer: Praveen.Nagegowda@infinite.com
import sys
import XenAPI
from prettytable import PrettyTable

# grab dict of UUID:VM Name
vms_dict={}

def main(session):
    # Find a non-template VM object
    vms = session.xenapi.VM.get_all()
    print "Server has %d VM objects including templates." % (len(vms))
    # print vms
    
    for vm in vms:
        record = session.xenapi.VM.get_record(vm)
        if not(record["is_a_template"]) and not(record["is_control_domain"]):
            name = record["name_label"]
            # vms_dict(name)=record["uuid"]
            # print "Found VM uuid", record["uuid"], "called: ", name
            uuid_vm_name=(record["uuid"],name )
            vms_dict[uuid_vm_name[0]]=uuid_vm_name[1]

    # print vms_dict
    print "Given below is list of non-template vm objects:"
    vm_table = PrettyTable(['UUID', 'VM Name'])
    for key, val in vms_dict.items():
        vm_table.add_row([key, val])
    print vm_table
    
if __name__ == "__main__":
    if len(sys.argv) <> 4:
        print "Usage:"
        print sys.argv[0], " <url> <username> <password>"
        sys.exit(1)
    url = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]
    # First acquire a valid session by logging in:
    session = XenAPI.Session(url)
    session.xenapi.login_with_password(username, password, "1.0", "custom_list_vms.py")
    main(session)
