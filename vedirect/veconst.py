# -*- coding: utf-8 -*-
class Veconst:
    (TYPE_UN8, TYPE_UN16, TYPE_UN32, TYPE_SN16, TYPE_STRING) = range(5)

    REG_BATTERYSAFE_MODE = 0xEDFF         # Removed since 1.13
    REG_ADAPTIVE_MODE = 0xEDFE
    REG_AUTOMATIC_EQUALISATION_MODE = 0xEDFD
    REG_BATTERY_BULK_TIME_LIMIT = 0xEDFC
    REG_BATTERY_ABSORPTION_TIME_LIMIT = 0xEDFB
    REG_BATTERY_ABSORPTION_VOLTAGE = 0xEDF7
    REG_BATTERY_FLOAT_VOLTAGE = 0xEDF6
    REG_BATTERY_EQUALISATION_VOLTAGE = 0xEDF4
    REG_BATTERY_TEMP_COMPENSATION = 0xEDF2
    REG_BATTERY_TYPE = 0xEDF1
    REG_BATTERY_MAXIMUM_CURRENT = 0xEDF0
    REG_BATTERY_VOLTAGE = 0xEDEF
    REG_BATTERY_TEMPERATURE = 0xEDEC
    REG_BATTERY_VOLTAGE_SETTING = 0xEDEA
    REG_BMS_PRESENT = 0xEDE8
    REG_TAIL_CURRENT = 0xEDE7
    REG_LOW_TEMPERATURE_CHARGE_CURRENT = 0xEDE6
    REG_AUTO_EQUALISE_STOP_ON_VOLTAGE = 0xEDE5
    REG_EQUALISATION_CURRENT_LEVEL = 0xEDE4
    REG_EQUALISATION_DURATION = 0xEDE3
    REG_RE_BULK_VOLTAGE_OFFSET = 0xED2E
    REG_BATTERY_LOW_TEMPERATURE_LEVEL = 0xEDE0
    REG_VOLTAGE_COMPENSATION = 0xEDCA

    REG_SERIAL_NUMBER = 0x010A

    # param_name : [ ID, Scale, Data Lengh, Unit, Description, Mock Data]

    (IDX_ID, IDX_SCALE, IDX_DATA_TYPE, IDX_UNIT, IDX_DESC, IDX_MOCK_DATA) = range(6)

    REG_PARAMS = {
        REG_SERIAL_NUMBER : [0x010A, -1, TYPE_STRING, "", "Serial Number", ":70A01004851313832393550483350000000000086"],

        REG_BATTERYSAFE_MODE :[0xEDFF, -1, 1, "","Batterysafe mode", ":7FFED0161"],
        REG_ADAPTIVE_MODE : [0xEDFE, -1, 1, "", "Adaptive mode", ":7FEED000162"],
        REG_AUTOMATIC_EQUALISATION_MODE : [0xEDFD, -1, 1, "", "Automatic equalisation mode", ":7FDED000064"],
        REG_BATTERY_BULK_TIME_LIMIT : [0xEDFC, 0.01, 2, "Hours", "Battery bulk time limit", ":7FCED0164"],
        REG_BATTERY_ABSORPTION_TIME_LIMIT : [0xEDFB, 0.01, 2, "Hours", "Battery absorption time limit", ":7FBED0058020C"],
        REG_BATTERY_ABSORPTION_VOLTAGE : [0xEDF7, 0.01, 2, "V", "Battery absorption voltage", ":7F7ED009C09C5"],
        REG_BATTERY_FLOAT_VOLTAGE : [0xEDF6, 0.01, 2, "V", "Battery float voltage", ":7F6ED00600902"],
        REG_BATTERY_EQUALISATION_VOLTAGE : [0xEDF4, 0.01, 2, "V", "Battery equalisation voltage", ":7F4ED00210B41"],
        REG_BATTERY_TEMP_COMPENSATION : [0xEDF2, 0.01, 2, "mV/K", "Battery temp. compensation", ":7F2ED0058F324"],
        REG_BATTERY_TYPE : [0xEDF1, -1, 1, "", "Battery type", ":7F1ED00FF71"],
        REG_BATTERY_MAXIMUM_CURRENT : [0xEDF0, 0.1, 2, "A", "Battery maximum current", ":7F0ED00F4017C"],
        REG_BATTERY_VOLTAGE : [0xEDEF, 1, 1, "V", "Battery voltage", ":7EFED00185A"],
        REG_BATTERY_TEMPERATURE : [0xEDEC, 0.01, 2, "K", "Battery temperature", ":7ECED00FFFF77"],
        REG_BATTERY_VOLTAGE_SETTING : [0xEDEA, 1, 1, "V", "Battery voltage setting", ":7EAED00185F"],
        REG_BMS_PRESENT : [0xEDE8, -1, 1, "", "BMS present", ":7E8ED000079"],
        REG_TAIL_CURRENT : [0xEDE7, 0.1, 2, "A", "Tail current", ":7E7ED00320048"],
        REG_LOW_TEMPERATURE_CHARGE_CURRENT : [0xEDE6, 0.1, 2, "A", "Low temperature charge current", ":7E6ED00FFFF7D"],
        REG_AUTO_EQUALISE_STOP_ON_VOLTAGE : [0xEDE5, -1, 1, "", "Auto equalise stop on voltage", ":7E5ED00017B"],
        REG_EQUALISATION_CURRENT_LEVEL : [0xEDE4, 1, 1, "%", "Equalisation current level", ":7E4ED000875"],
        REG_EQUALISATION_DURATION : [0xEDE3, 0.01, 2, "Hours", "Equalisation duration", ":7E3ED0064001A"],
        REG_RE_BULK_VOLTAGE_OFFSET : [0xED2E, 0.01, 2, "V", "Re-bulk voltage offset", ":72EED0014001F"],
        REG_BATTERY_LOW_TEMPERATURE_LEVEL : [0xEDE0, 0.01, 2, "°C", "Battery low temperature level", ":7E0ED00F4018C"],
        REG_VOLTAGE_COMPENSATION : [0xEDCA, 0.01, 2, "V", "Voltage compensation", ":7CAED0196"]
    }

    PARAM_MAP = {
        "BatteryFloatVoltage": ':7F6ED00',
        "BatteryAbsorptionVoltage": ":7F7ED00",
        "SystemTotal":":7DDED00",
        "UserTotal":"7DCEDDC"
    }

    VEDIRECT_MAPPING = {
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
