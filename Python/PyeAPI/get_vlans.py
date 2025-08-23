#!/usr/bin/env python3

import pyeapi
import yaml

# connect = pyeapi.connect_to("leaf1")
# # raw_cmd_result = connect.enable("show vlan")
# raw_cmd_result = connect.enable("show vlan", encoding="text")
# print(raw_cmd_result)

file = open("vlans.yml", "r")

pyeapi.load_config("eapi.conf")
file_vlans_dict = yaml.safe_load(file)

for switch in file_vlans_dict["switches"]:
    connect = pyeapi.connect_to(switch)
    raw_cmd_result = connect.enable("show vlan")
    cmd_vlans_dict = raw_cmd_result[0]["result"]["vlans"]
    # print(cmd_vlans_dict)
    print(f"For switch {switch}")
    for vlan in cmd_vlans_dict:
        vlan_id = vlan
        vlan_name = cmd_vlans_dict[vlan]["name"]
        print(cmd_vlans_dict[vlan]["name"])
        print(f"VLAN ID of {vlan_id} with name {vlan_name}")
