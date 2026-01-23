# fcu_state.py
from __future__ import annotations
import struct
import typing as t
from toshiba_ac.device.properties import (
    ToshibaAcAirPureIon,
    ToshibaAcFanMode,
    ToshibaAcMeritA,
    ToshibaAcMeritB,
    ToshibaAcMode,
    ToshibaAcPowerSelection,
    ToshibaAcSelfCleaning,
    ToshibaAcStatus,
    ToshibaAcSwingMode,
)

class ToshibaAcFcuState:
    NONE_VAL = 0xFF
    NONE_VAL_HALF = 0x0F
    NONE_VAL_SIGNED = -1
    ENCODING_STRUCT = struct.Struct("BBbBBBBBBbbBBBBBBBBB")

    class AcTemperature:
        @staticmethod
        def from_raw(raw: int) -> t.Optional[int]:
            raw_to_temp: t.Dict[int, t.Optional[int]] = {i: i for i in range(-128, 128)}
            raw_to_temp.update({127: None, -128: None, ToshibaAcFcuState.NONE_VAL_SIGNED: None, 126: -1})
            return raw_to_temp.get(raw, None)

        @staticmethod
        def to_raw(temperature: t.Optional[int]) -> int:
            temp_to_raw: t.Dict[t.Optional[int], int] = {i: i for i in range(-128, 128)}
            temp_to_raw.update({None: ToshibaAcFcuState.NONE_VAL_SIGNED, -1: 126})
            return temp_to_raw.get(temperature, ToshibaAcFcuState.NONE_VAL_SIGNED)

    class AcStatus:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcStatus:
            return {
                0x30: ToshibaAcStatus.ON,
                0x31: ToshibaAcStatus.OFF,
                0x02: ToshibaAcStatus.NONE,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcStatus.NONE,
            }.get(raw, ToshibaAcStatus.NONE)

        @staticmethod
        def to_raw(status: ToshibaAcStatus) -> int:
            return {
                ToshibaAcStatus.ON: 0x30,
                ToshibaAcStatus.OFF: 0x31,
                ToshibaAcStatus.NONE: ToshibaAcFcuState.NONE_VAL,
            }[status]

    class AcMode:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcMode:
            return {
                0x41: ToshibaAcMode.AUTO,
                0x42: ToshibaAcMode.COOL,
                0x43: ToshibaAcMode.HEAT,
                0x44: ToshibaAcMode.DRY,
                0x45: ToshibaAcMode.FAN,
                0x00: ToshibaAcMode.NONE,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcMode.NONE,
            }.get(raw, ToshibaAcMode.NONE)

        @staticmethod
        def to_raw(mode: ToshibaAcMode) -> int:
            return {
                ToshibaAcMode.AUTO: 0x41,
                ToshibaAcMode.COOL: 0x42,
                ToshibaAcMode.HEAT: 0x43,
                ToshibaAcMode.DRY: 0x44,
                ToshibaAcMode.FAN: 0x45,
                ToshibaAcMode.NONE: ToshibaAcFcuState.NONE_VAL,
            }[mode]

    class AcFanMode:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcFanMode:
            return {
                0x41: ToshibaAcFanMode.AUTO,
                0x31: ToshibaAcFanMode.QUIET,
                0x32: ToshibaAcFanMode.LOW,
                0x33: ToshibaAcFanMode.MEDIUM_LOW,
                0x34: ToshibaAcFanMode.MEDIUM,
                0x35: ToshibaAcFanMode.MEDIUM_HIGH,
                0x36: ToshibaAcFanMode.HIGH,
                0x00: ToshibaAcFanMode.NONE,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcFanMode.NONE,
            }.get(raw, ToshibaAcFanMode.NONE)

        @staticmethod
        def to_raw(fan_mode: ToshibaAcFanMode) -> int:
            return {
                ToshibaAcFanMode.AUTO: 0x41,
                ToshibaAcFanMode.QUIET: 0x31,
                ToshibaAcFanMode.LOW: 0x32,
                ToshibaAcFanMode.MEDIUM_LOW: 0x33,
                ToshibaAcFanMode.MEDIUM: 0x34,
                ToshibaAcFanMode.MEDIUM_HIGH: 0x35,
                ToshibaAcFanMode.HIGH: 0x36,
                ToshibaAcFanMode.NONE: ToshibaAcFcuState.NONE_VAL,
            }[fan_mode]

    class AcSwingMode:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcSwingMode:
            return {
                0x31: ToshibaAcSwingMode.OFF,
                0x41: ToshibaAcSwingMode.SWING_VERTICAL,
                0x42: ToshibaAcSwingMode.SWING_HORIZONTAL,
                0x43: ToshibaAcSwingMode.SWING_VERTICAL_AND_HORIZONTAL,
                0x50: ToshibaAcSwingMode.FIXED_1,
                0x51: ToshibaAcSwingMode.FIXED_2,
                0x52: ToshibaAcSwingMode.FIXED_3,
                0x53: ToshibaAcSwingMode.FIXED_4,
                0x54: ToshibaAcSwingMode.FIXED_5,
                0x60: ToshibaAcSwingMode.HADA_CARE,  # <--- ADDED
                0x00: ToshibaAcSwingMode.NONE,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcSwingMode.NONE,
            }.get(raw, ToshibaAcSwingMode.NONE)

        @staticmethod
        def to_raw(swing_mode: ToshibaAcSwingMode) -> int:
            return {
                ToshibaAcSwingMode.OFF: 0x31,
                ToshibaAcSwingMode.SWING_VERTICAL: 0x41,
                ToshibaAcSwingMode.SWING_HORIZONTAL: 0x42,
                ToshibaAcSwingMode.SWING_VERTICAL_AND_HORIZONTAL: 0x43,
                ToshibaAcSwingMode.FIXED_1: 0x50,
                ToshibaAcSwingMode.FIXED_2: 0x51,
                ToshibaAcSwingMode.FIXED_3: 0x52,
                ToshibaAcSwingMode.FIXED_4: 0x53,
                ToshibaAcSwingMode.FIXED_5: 0x54,
                ToshibaAcSwingMode.HADA_CARE: 0x60,  # <--- ADDED
                ToshibaAcSwingMode.NONE: ToshibaAcFcuState.NONE_VAL,
            }[swing_mode]

    class AcPowerSelection:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcPowerSelection:
            return {
                0x32: ToshibaAcPowerSelection.POWER_50,
                0x4B: ToshibaAcPowerSelection.POWER_75,
                0x64: ToshibaAcPowerSelection.POWER_100,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcPowerSelection.NONE,
            }.get(raw, ToshibaAcPowerSelection.NONE)

        @staticmethod
        def to_raw(power_selection: ToshibaAcPowerSelection) -> int:
            return {
                ToshibaAcPowerSelection.POWER_50: 0x32,
                ToshibaAcPowerSelection.POWER_75: 0x4B,
                ToshibaAcPowerSelection.POWER_100: 0x64,
                ToshibaAcPowerSelection.NONE: ToshibaAcFcuState.NONE_VAL,
            }[power_selection]

    class AcMeritB:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcMeritB:
            return {
                0x02: ToshibaAcMeritB.FIREPLACE_1,
                0x03: ToshibaAcMeritB.FIREPLACE_2,
                0x01: ToshibaAcMeritB.OFF,
                0x00: ToshibaAcMeritB.OFF,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcMeritB.NONE,
                ToshibaAcFcuState.NONE_VAL_HALF: ToshibaAcMeritB.NONE,
            }.get(raw, ToshibaAcMeritB.NONE)

        @staticmethod
        def to_raw(merit_b: ToshibaAcMeritB) -> int:
            return {
                ToshibaAcMeritB.FIREPLACE_1: 0x02,
                ToshibaAcMeritB.FIREPLACE_2: 0x03,
                ToshibaAcMeritB.OFF: 0x00,
                ToshibaAcMeritB.NONE: ToshibaAcFcuState.NONE_VAL,
            }[merit_b]

    class AcMeritA:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcMeritA:
            return {
                0x01: ToshibaAcMeritA.HIGH_POWER,
                0x02: ToshibaAcMeritA.CDU_SILENT_1,
                0x03: ToshibaAcMeritA.ECO,
                0x04: ToshibaAcMeritA.HEATING_8C,
                0x05: ToshibaAcMeritA.SLEEP_CARE,
                0x06: ToshibaAcMeritA.FLOOR,
                0x07: ToshibaAcMeritA.COMFORT,
                0x0A: ToshibaAcMeritA.CDU_SILENT_2,
                0x00: ToshibaAcMeritA.OFF,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcMeritA.NONE,
                ToshibaAcFcuState.NONE_VAL_HALF: ToshibaAcMeritA.NONE,
            }.get(raw, ToshibaAcMeritA.NONE)

        @staticmethod
        def to_raw(merit_a: ToshibaAcMeritA) -> int:
            return {
                ToshibaAcMeritA.HIGH_POWER: 0x01,
                ToshibaAcMeritA.CDU_SILENT_1: 0x02,
                ToshibaAcMeritA.ECO: 0x03,
                ToshibaAcMeritA.HEATING_8C: 0x04,
                ToshibaAcMeritA.SLEEP_CARE: 0x05,
                ToshibaAcMeritA.FLOOR: 0x06,
                ToshibaAcMeritA.COMFORT: 0x07,
                ToshibaAcMeritA.CDU_SILENT_2: 0x0A,
                ToshibaAcMeritA.OFF: 0x00,
                ToshibaAcMeritA.NONE: ToshibaAcFcuState.NONE_VAL,
            }[merit_a]

    class AcAirPureIon:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcAirPureIon:
            return {
                0x18: ToshibaAcAirPureIon.ON,
                0x10: ToshibaAcAirPureIon.OFF,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcAirPureIon.NONE,
            }.get(raw, ToshibaAcAirPureIon.NONE)

        @staticmethod
        def to_raw(air_pure_ion: ToshibaAcAirPureIon) -> int:
            return {
                ToshibaAcAirPureIon.ON: 0x18,
                ToshibaAcAirPureIon.OFF: 0x10,
                ToshibaAcAirPureIon.NONE: ToshibaAcFcuState.NONE_VAL,
            }[air_pure_ion]

    class AcSelfCleaning:
        @staticmethod
        def from_raw(raw: int) -> ToshibaAcSelfCleaning:
            return {
                0x18: ToshibaAcSelfCleaning.ON,
                0x10: ToshibaAcSelfCleaning.OFF,
                ToshibaAcFcuState.NONE_VAL: ToshibaAcSelfCleaning.NONE,
            }.get(raw, ToshibaAcSelfCleaning.NONE)

        @staticmethod
        def to_raw(self_cleaning: ToshibaAcSelfCleaning) -> int:
            return {
                ToshibaAcSelfCleaning.ON: 0x18,
                ToshibaAcSelfCleaning.OFF: 0x10,
                ToshibaAcSelfCleaning.NONE: ToshibaAcFcuState.NONE_VAL,
            }[self_cleaning]

    @classmethod
    def from_hex_state(cls, hex_state: str) -> ToshibaAcFcuState:
        state = cls()
        state.decode(hex_state)
        return state

    def __init__(self) -> None:
        self._ac_status = ToshibaAcFcuState.NONE_VAL
        self._ac_mode = ToshibaAcFcuState.NONE_VAL
        self._ac_temperature = ToshibaAcFcuState.NONE_VAL_SIGNED
        self._ac_fan_mode = ToshibaAcFcuState.NONE_VAL
        self._ac_swing_mode = ToshibaAcFcuState.NONE_VAL
        self._ac_power_selection = ToshibaAcFcuState.NONE_VAL
        self._ac_merit_b = ToshibaAcFcuState.NONE_VAL
        self._ac_merit_a = ToshibaAcFcuState.NONE_VAL
        self._ac_air_pure_ion = ToshibaAcFcuState.NONE_VAL
        self._ac_indoor_temperature = ToshibaAcFcuState.NONE_VAL_SIGNED
        self._ac_outdoor_temperature = ToshibaAcFcuState.NONE_VAL_SIGNED
        self._ac_self_cleaning = ToshibaAcFcuState.NONE_VAL
        
        # --- NEW SENSORS ---
        self._compressor_hz = 0           # cduCompHz
        self._discharge_temp = 0          # cduTdTemp
        self._suction_temp = 0            # cduTsTemp
        self._outdoor_coil_temp = 0       # cduTeTemp
        self._outdoor_fan_speed = 0       # cduFanRpm
        self._expansion_valve_pulse = 0   # cduPmvPulse
        self._indoor_coil_inlet_temp = 0  # fcuTcTemp
        self._indoor_coil_outlet_temp = 0 # fcuTcjTemp
        self._indoor_fan_speed = 0        # fcuFanRpm

    def encode(self) -> str:
        encoded = self.ENCODING_STRUCT.pack(
            self._ac_status,
            self._ac_mode,
            self._ac_temperature,
            self._ac_fan_mode,
            self._ac_swing_mode,
            self._ac_power_selection,
            self._ac_merit_b,
            self._ac_merit_a,
            self._ac_air_pure_ion,
            self._ac_indoor_temperature,
            self._ac_outdoor_temperature,
            ToshibaAcFcuState.NONE_VAL,
            ToshibaAcFcuState.NONE_VAL,
            ToshibaAcFcuState.NONE_VAL,
            ToshibaAcFcuState.NONE_VAL,
            self._ac_self_cleaning,
            ToshibaAcFcuState.NONE_VAL,
            ToshibaAcFcuState.NONE_VAL,
            ToshibaAcFcuState.NONE_VAL,
            ToshibaAcFcuState.NONE_VAL,
        ).hex()
        return (
            encoded[:12] + encoded[13] + encoded[15] + encoded[16:]
        )

    def decode(self, hex_state: str) -> None:
        extended_hex_state = (
            hex_state[:12] + "0" + hex_state[12] + "0" + hex_state[13:38]
        )
        data = self.ENCODING_STRUCT.unpack(bytes.fromhex(extended_hex_state))
        (
            self._ac_status,
            self._ac_mode,
            self._ac_temperature,
            self._ac_fan_mode,
            self._ac_swing_mode,
            self._ac_power_selection,
            self._ac_merit_b,
            self._ac_merit_a,
            self._ac_air_pure_ion,
            self._ac_indoor_temperature,
            self._ac_outdoor_temperature,
            _,
            _,
            _,
            _,
            self._ac_self_cleaning,
            *_,
        ) = data

    def update(self, hex_state: str) -> bool:
        state_update = ToshibaAcFcuState.from_hex_state(hex_state)
        changed = False
        
        # Standard Properties
        enum_states = [
            "_ac_status", "_ac_mode", "_ac_fan_mode", "_ac_swing_mode",
            "_ac_power_selection", "_ac_merit_b", "_ac_merit_a",
            "_ac_air_pure_ion", "_ac_self_cleaning",
        ]
        temperature_states = [
            "_ac_temperature", "_ac_indoor_temperature", "_ac_outdoor_temperature",
        ]

        for enum_state in enum_states:
            updated_state = getattr(state_update, enum_state)
            current_state = getattr(self, enum_state)
            if updated_state not in [ToshibaAcFcuState.NONE_VAL, ToshibaAcFcuState.NONE_VAL_HALF, current_state]:
                setattr(self, enum_state, updated_state)
                changed = True

        for temperature_state in temperature_states:
            updated_state = getattr(state_update, temperature_state)
            current_state = getattr(self, temperature_state)
            if updated_state not in [ToshibaAcFcuState.NONE_VAL_SIGNED, current_state]:
                setattr(self, temperature_state, updated_state)
                changed = True

        return changed

    def update_from_hbt(self, hb_data: t.Any) -> bool:
        changed = False

        if "iTemp" in hb_data and hb_data["iTemp"] != self._ac_indoor_temperature:
            self._ac_indoor_temperature = hb_data["iTemp"]
            changed = True

        if "oTemp" in hb_data and hb_data["oTemp"] != self._ac_outdoor_temperature:
            self._ac_outdoor_temperature = hb_data["oTemp"]
            changed = True

        # --- NEW: Capture Hidden Engineering Sensors ---
        # 1. Compressor Hz
        if "cduCompHz" in hb_data and hb_data["cduCompHz"] != self._compressor_hz:
            self._compressor_hz = hb_data["cduCompHz"]
            changed = True
        # 2. Discharge Temp
        if "cduTdTemp" in hb_data and hb_data["cduTdTemp"] != self._discharge_temp:
            self._discharge_temp = hb_data["cduTdTemp"]
            changed = True
        # 3. Suction Temp
        if "cduTsTemp" in hb_data and hb_data["cduTsTemp"] != self._suction_temp:
            self._suction_temp = hb_data["cduTsTemp"]
            changed = True
        # 4. Outdoor Coil Temp
        if "cduTeTemp" in hb_data and hb_data["cduTeTemp"] != self._outdoor_coil_temp:
            self._outdoor_coil_temp = hb_data["cduTeTemp"]
            changed = True
        # 5. Outdoor Fan Speed
        if "cduFanRpm" in hb_data and hb_data["cduFanRpm"] != self._outdoor_fan_speed:
            self._outdoor_fan_speed = hb_data["cduFanRpm"]
            changed = True
        # 6. Expansion Valve
        if "cduPmvPulse" in hb_data and hb_data["cduPmvPulse"] != self._expansion_valve_pulse:
            self._expansion_valve_pulse = hb_data["cduPmvPulse"]
            changed = True
        # 7. Indoor Coil Inlet
        if "fcuTcTemp" in hb_data and hb_data["fcuTcTemp"] != self._indoor_coil_inlet_temp:
            self._indoor_coil_inlet_temp = hb_data["fcuTcTemp"]
            changed = True
        # 8. Indoor Coil Outlet
        if "fcuTcjTemp" in hb_data and hb_data["fcuTcjTemp"] != self._indoor_coil_outlet_temp:
            self._indoor_coil_outlet_temp = hb_data["fcuTcjTemp"]
            changed = True
        # 9. Indoor Fan Speed (Raw)
        if "fcuFanRpm" in hb_data and hb_data["fcuFanRpm"] != self._indoor_fan_speed:
            self._indoor_fan_speed = hb_data["fcuFanRpm"]
            changed = True
        
        return changed

    # --- PROPERTIES ---
    @property
    def ac_status(self) -> ToshibaAcStatus:
        return ToshibaAcFcuState.AcStatus.from_raw(self._ac_status)

    @ac_status.setter
    def ac_status(self, val: ToshibaAcStatus) -> None:
        self._ac_status = ToshibaAcFcuState.AcStatus.to_raw(val)

    @property
    def ac_mode(self) -> ToshibaAcMode:
        return ToshibaAcFcuState.AcMode.from_raw(self._ac_mode)

    @ac_mode.setter
    def ac_mode(self, val: ToshibaAcMode) -> None:
        self._ac_mode = ToshibaAcFcuState.AcMode.to_raw(val)

    @property
    def ac_temperature(self) -> t.Optional[int]:
        return ToshibaAcFcuState.AcTemperature.from_raw(self._ac_temperature)

    @ac_temperature.setter
    def ac_temperature(self, val: t.Optional[int]) -> None:
        self._ac_temperature = ToshibaAcFcuState.AcTemperature.to_raw(val)

    @property
    def ac_fan_mode(self) -> ToshibaAcFanMode:
        return ToshibaAcFcuState.AcFanMode.from_raw(self._ac_fan_mode)

    @ac_fan_mode.setter
    def ac_fan_mode(self, val: ToshibaAcFanMode) -> None:
        self._ac_fan_mode = ToshibaAcFcuState.AcFanMode.to_raw(val)

    @property
    def ac_swing_mode(self) -> ToshibaAcSwingMode:
        return ToshibaAcFcuState.AcSwingMode.from_raw(self._ac_swing_mode)

    @ac_swing_mode.setter
    def ac_swing_mode(self, val: ToshibaAcSwingMode) -> None:
        self._ac_swing_mode = ToshibaAcFcuState.AcSwingMode.to_raw(val)

    @property
    def ac_power_selection(self) -> ToshibaAcPowerSelection:
        return ToshibaAcFcuState.AcPowerSelection.from_raw(self._ac_power_selection)

    @ac_power_selection.setter
    def ac_power_selection(self, val: ToshibaAcPowerSelection) -> None:
        self._ac_power_selection = ToshibaAcFcuState.AcPowerSelection.to_raw(val)

    @property
    def ac_merit_b(self) -> ToshibaAcMeritB:
        return ToshibaAcFcuState.AcMeritB.from_raw(self._ac_merit_b)

    @ac_merit_b.setter
    def ac_merit_b(self, val: ToshibaAcMeritB) -> None:
        self._ac_merit_b = ToshibaAcFcuState.AcMeritB.to_raw(val)

    @property
    def ac_merit_a(self) -> ToshibaAcMeritA:
        return ToshibaAcFcuState.AcMeritA.from_raw(self._ac_merit_a)

    @ac_merit_a.setter
    def ac_merit_a(self, val: ToshibaAcMeritA) -> None:
        self._ac_merit_a = ToshibaAcFcuState.AcMeritA.to_raw(val)

    @property
    def ac_air_pure_ion(self) -> ToshibaAcAirPureIon:
        return ToshibaAcFcuState.AcAirPureIon.from_raw(self._ac_air_pure_ion)

    @ac_air_pure_ion.setter
    def ac_air_pure_ion(self, val: ToshibaAcAirPureIon) -> None:
        self._ac_air_pure_ion = ToshibaAcFcuState.AcAirPureIon.to_raw(val)

    @property
    def ac_indoor_temperature(self) -> t.Optional[int]:
        return ToshibaAcFcuState.AcTemperature.from_raw(self._ac_indoor_temperature)

    @ac_indoor_temperature.setter
    def ac_indoor_temperature(self, val: t.Optional[int]) -> None:
        self._ac_indoor_temperature = ToshibaAcFcuState.AcTemperature.to_raw(val)

    @property
    def ac_outdoor_temperature(self) -> t.Optional[int]:
        return ToshibaAcFcuState.AcTemperature.from_raw(self._ac_outdoor_temperature)

    @ac_outdoor_temperature.setter
    def ac_outdoor_temperature(self, val: t.Optional[int]) -> None:
        self._ac_outdoor_temperature = ToshibaAcFcuState.AcTemperature.to_raw(val)

    @property
    def ac_self_cleaning(self) -> ToshibaAcSelfCleaning:
        return ToshibaAcFcuState.AcSelfCleaning.from_raw(self._ac_self_cleaning)

    @ac_self_cleaning.setter
    def ac_self_cleaning(self, val: ToshibaAcSelfCleaning) -> None:
        self._ac_self_cleaning = ToshibaAcFcuState.AcSelfCleaning.to_raw(val)

    # --- NEW PROPERTIES FOR GUI/HA ---
    @property
    def compressor_hz(self) -> int: return self._compressor_hz
    @property
    def discharge_temp(self) -> int: return self._discharge_temp
    @property
    def suction_temp(self) -> int: return self._suction_temp
    @property
    def outdoor_coil_temp(self) -> int: return self._outdoor_coil_temp
    @property
    def outdoor_fan_speed(self) -> int: return self._outdoor_fan_speed
    @property
    def expansion_valve_pulse(self) -> int: return self._expansion_valve_pulse
    @property
    def indoor_coil_inlet_temp(self) -> int: return self._indoor_coil_inlet_temp
    @property
    def indoor_coil_outlet_temp(self) -> int: return self._indoor_coil_outlet_temp
    @property
    def indoor_fan_speed(self) -> int: return self._indoor_fan_speed

    def __str__(self) -> str:
        res = f"AcStatus: {self.ac_status.name}"
        res += f", AcMode: {self.ac_mode.name}"
        res += f", AcTemperature: {self.ac_temperature}"
        res += f", AcFanMode: {self.ac_fan_mode.name}"
        res += f", AcSwingMode: {self.ac_swing_mode.name}"
        res += f", AcPowerSelection: {self.ac_power_selection.name}"
        res += f", AcFeatureMeritB: {self.ac_merit_b.name}"
        res += f", AcFeatureMeritA: {self.ac_merit_a.name}"
        res += f", AcAirPureIon: {self.ac_air_pure_ion.name}"
        res += f", AcIndoorAcTemperature: {self.ac_indoor_temperature}"
        res += f", AcOutdoorAcTemperature: {self.ac_outdoor_temperature}"
        res += f", AcSelfCleaning: {self.ac_self_cleaning.name}"
        # Print the new engineering data
        res += f", CompHz: {self.compressor_hz}"
        res += f", DischT: {self.discharge_temp}"
        res += f", SuctT: {self.suction_temp}"
        res += f", OutCoil: {self.outdoor_coil_temp}"
        res += f", OutFan: {self.outdoor_fan_speed}"
        res += f", PMV: {self.expansion_valve_pulse}"
        res += f", InCoilIn: {self.indoor_coil_inlet_temp}"
        res += f", InCoilOut: {self.indoor_coil_outlet_temp}"
        res += f", InFan: {self.indoor_fan_speed}"
        return res