# -*- coding: utf-8 -*-
import json

with open("files/inabi.json", "r") as fh:
    js = json.load(fh)
    for input_field in js["inputFields"]:
        print (str(input_field["name"]) + '\t' + str(input_field["value"]) + '\t' + str(input_field["label"]))
    print("-------- Signals ---------")
    for signals in js["signals"]:
        print(str(signals["name"]) + '\t' + str(signals["condition"]) + '\t' + str(signals["value"]))

