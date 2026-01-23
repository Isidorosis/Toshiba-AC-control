# properties.py
from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto

@dataclass
class ToshibaAcDeviceEnergyConsumption:
    energy_wh: float
    since: datetime

class ToshibaAcStatus(Enum):
    ON = auto()
    OFF = auto()
    NONE = None

class ToshibaAcMode(Enum):
    AUTO = auto()
    COOL = auto()
    HEAT = auto()
    DRY = auto()
    FAN = auto()
    NONE = None

class ToshibaAcFanMode(Enum):
    AUTO = auto()
    QUIET = auto()
    LOW = auto()
    MEDIUM_LOW = auto()
    MEDIUM = auto()
    MEDIUM_HIGH = auto()
    HIGH = auto()
    NONE = None

class ToshibaAcSwingMode(Enum):
    OFF = auto()
    SWING_VERTICAL = auto()
    SWING_HORIZONTAL = auto()
    SWING_VERTICAL_AND_HORIZONTAL = auto()
    FIXED_1 = auto()
    FIXED_2 = auto()
    FIXED_3 = auto()
    FIXED_4 = auto()
    FIXED_5 = auto()
    HADA_CARE = auto()  # <--- NEW FEATURE ADDED
    NONE = None

class ToshibaAcPowerSelection(Enum):
    POWER_50 = auto()
    POWER_75 = auto()
    POWER_100 = auto()
    NONE = None

class ToshibaAcMeritB(Enum):
    FIREPLACE_1 = auto()
    FIREPLACE_2 = auto()
    OFF = auto()
    NONE = None

class ToshibaAcMeritA(Enum):
    HIGH_POWER = auto()
    CDU_SILENT_1 = auto()
    ECO = auto()
    HEATING_8C = auto()
    SLEEP_CARE = auto()
    FLOOR = auto()
    COMFORT = auto()
    CDU_SILENT_2 = auto()
    OFF = auto()
    NONE = None

class ToshibaAcAirPureIon(Enum):
    OFF = auto()
    ON = auto()
    NONE = None

class ToshibaAcSelfCleaning(Enum):
    ON = auto()
    OFF = auto()
    NONE = None