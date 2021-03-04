dict = {'V': '12800', 'VS': '12800', 'VM': '1280', 'DM': '120',
                     'VPV': '3350', 'PPV': '130', 'I': '15000', 'IL': '1500',
                     'LOAD': 'ON', 'T': '25', 'P': '130', 'CE': '13500',
                     'SOC': '876', 'TTG': '45', 'Alarm': 'OFF', 'Relay': 'OFF',
                     'AR': '1', 'H1': '55000', 'H2': '15000', 'H3': '13000',
                     'H4': '230', 'H5': '12', 'H6': '234000', 'H7': '11000',
                     'H8': '14800', 'H9': '7200', 'H10': '45', 'H11': '5',
                     'H12': '0', 'H13': '0', 'H14': '0', 'H15': '11500',
                     'H16': '14800', 'H17': '34', 'H18': '45', 'H19': '456',
                     'H20': '45', 'H21': '300', 'H22': '45', 'H23': '350',
                     'ERR': '0', 'CS': '5', 'BMV': '702', 'FW': '1.19',
                     'PID': '0x204', 'SER#': 'HQ141112345', 'HSDS': '0'}

# From Smartsolar MPPT 100|50
dict =     {'PID': '0xA057', 'FW': '154', 'SER#': 'HQ18295PH3P', 'V': '22680', 
                'I': '23400', 'VPV': '61970', 'PPV': '541', 'CS': '3', 'MPPT': '2',
                'OR': '0x00000000', 'ERR': '0', 'LOAD': 'ON', 'H19': '18405',
                'H20': '221', 'H21': '961', 'H22': '507', 'H23': '958', 'HSDS': '248'}

vedirect_mapping = {
    'V':{"name":"Battery Voltage", "unit":"V", "process":0.001},
    'V2':{"name":"Battery2 Voltage", "unit":"V", "process":0.001},
    'V3':{"name":"Battery3 Voltage", "unit":"V", "process":0.001},
    'VS':{"name":"Starter Battery Voltage", "unit":"V", "process":0.001},
    'VM':{"name":"Mid-point Voltage", "unit":"V", "process":0.001},
    'DM':{"name":"Mid-point Deviation", "unit":"‰", "process":-1},
    'VPV':{"name":"Solar Panel Voltage", "unit":"V", "process":0.001},
    'PPV':{"name":"Solar Panel Power", "unit":"W", "process":-1},

    'I':{"name":"Battery Current", "unit":"A", "process":0.001},
    'I2':{"name":"Battery2 Current", "unit":"A", "process":0.001},
    'I3':{"name":"Battery3 Current", "unit":"A", "process":0.001},
    'IL':{"name":"Load Current", "unit":"A", "process":0.001},
    'LOAD':{"name":"Load State", "unit":"", "process":-1},

    'T':{"name":"Battery Temperature", "unit":"°C", "process":-1},
    'P':{"name":"Instantaneous Power", "unit":"W", "process":-1},

    'H19':{"name":"Yield Total", "unit":"kWh", "process":0.01},
    'H20':{"name":"Yield today", "unit":"kWh", "process":0.01},
    'H21':{"name":"Maximum power today", "unit":"W", "process":1},
    'H22':{"name":"Yield yesterday", "unit":"kWh", "process":0.01},
    'H23':{"name":"Maximum power yesterday", "unit":"W", "process":1},

    'PID':{"name":"Product ID", "unit":"", "process":-10},
    'FW':{"name":"Firmware Version", "unit":"", "process":0.01},
    'SER#':{"name":"Serial Number", "unit":"", "process":-1},
    'HSDS':{"name":"Day Sequence Number", "unit":"Day", "process":-1},
    'CS':{"name":"State of Operation", "unit":"", "process":-11},
    'MPPT':{"name":"MPPT Status", "unit":"", "process":-12},

}

PID_MAPPING={
"0x203":"BMV-700",
"0x204":"BMV-702",
"0x205":"BMV-700H",
"0x0300":"BlueSolar MPPT 70|15",
"0xA040":"BlueSolar MPPT 75|50",
"0xA041":"BlueSolar MPPT 150|35",
"0xA042":"BlueSolar MPPT 75|15",
"0xA043":"BlueSolar MPPT 100|15",
"0xA044":"BlueSolar MPPT 100|30",
"0xA045":"BlueSolar MPPT 100|50",
"0xA046":"BlueSolar MPPT 150|70",
"0xA047":"BlueSolar MPPT 150|100",
"0xA049":"BlueSolar MPPT 100|50 rev2",
"0xA04A":"BlueSolar MPPT 100|30 rev2",
"0xA04B":"BlueSolar MPPT 150|35 rev2",
"0xA04C":"BlueSolar MPPT 75|10",
"0xA04D":"BlueSolar MPPT 150|45",
"0xA04E":"BlueSolar MPPT 150|60",
"0xA04F":"BlueSolar MPPT 150|85",
"0xA050":"SmartSolar MPPT 250|100",
"0xA051":"SmartSolar MPPT 150|100",
"0xA052":"SmartSolar MPPT 150|85",
"0xA053":"SmartSolar MPPT 75|15",
"0xA054":"SmartSolar MPPT 75|10",
"0xA055":"SmartSolar MPPT 100|15",
"0xA056":"SmartSolar MPPT 100|30",
"0xA057":"SmartSolar MPPT 100|50",
"0xA058":"SmartSolar MPPT 150|35",
"0xA059":"SmartSolar MPPT 150|100 rev2",
"0xA05A":"SmartSolar MPPT 150|85 rev2",
"0xA05B":"SmartSolar MPPT 250|70",
"0xA05C":"SmartSolar MPPT 250|85",
"0xA05D":"SmartSolar MPPT 250|60",
"0xA05E":"SmartSolar MPPT 250|45",
"0xA05F":"SmartSolar MPPT 100|20",
"0xA060":"SmartSolar MPPT 100|20 48V",
"0xA061":"SmartSolar MPPT 150|45",
"0xA062":"SmartSolar MPPT 150|60",
"0xA063":"SmartSolar MPPT 150|70",
"0xA064":"SmartSolar MPPT 250|85 rev2",
"0xA065":"SmartSolar MPPT 250|100 rev2",
"0xA066":"BlueSolar MPPT 100|20",
"0xA067":"BlueSolar MPPT 100|20 48V",
"0xA068":"SmartSolar MPPT 250|60 rev2",
"0xA069":"SmartSolar MPPT 250|70 rev2",
"0xA06A":"SmartSolar MPPT 150|45 rev2",
"0xA06B":"SmartSolar MPPT 150|60 rev2",
"0xA06C":"SmartSolar MPPT 150|70 rev2",
"0xA06D":"SmartSolar MPPT 150|85 rev3",
"0xA06E":"SmartSolar MPPT 150|100 rev3",
"0xA06F":"BlueSolar MPPT 150|45 rev2",
"0xA070":"BlueSolar MPPT 150|60 rev2",
"0xA071":"BlueSolar MPPT 150|70 rev2"
}

CS_MAPPING = {
"0":"Off",
"1":"Low Power",
"2":"Fault",
"3":"Bulk",
"4":"Absorption",
"5":"Float",
"6":"Storage",
"7":"Equalize (manual)",
"9":"Inverting",
"11":"Power supply",
"245":"Starting-up",
"246":"Repeated absorption",
"247":"Auto equalize / Recondition",
"248":"BatterySafe",
"249":"External Control"
}

MPPT_MAPPING={
"0":"Off",
"1":"Voltage or current limited",
"2":"MPP Tracker active"
}

tar_dict = []

# print(dict)

def mv2v(m):
    return "{:.02f}".format(float(m)/1000.0)

def human_dump(d):
    for i in d:
        print(i[0],":",i[1],i[2])

for k in dict:
    if k in vedirect_mapping.keys():
        v = dict[k]
        if vedirect_mapping[k]["process"] > 0:
            v = "{:.02f}".format(float(v)*vedirect_mapping[k]["process"])
        elif vedirect_mapping[k]["process"] == -10:
            v = PID_MAPPING[v]
        elif vedirect_mapping[k]["process"] == -11:
            v = CS_MAPPING[v]
        elif vedirect_mapping[k]["process"] == -12:
            v = MPPT_MAPPING[v]
        attr = [vedirect_mapping[k]["name"], v, vedirect_mapping[k]["unit"],dict[k]]
        # print (vedirect_mapping[k]["name"],dict[k])
    else:
        attr = [k,dict[k],"",dict[k], dict[k]]
    tar_dict.append(attr)
# print(tar_dict
print(dict)
human_dump(tar_dict)
        # print (k,dict[k])
