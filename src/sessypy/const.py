from enum import Enum

API_VERSION_1 = "api/v1"
API_VERSION_2 = "api/v2"

class SessyApiCommand(str, Enum):
    CT_DETAILS = f"{API_VERSION_1}/ct/details"
    METER_GRID_TARGET = f"{API_VERSION_1}/meter/grid_target"
    
    NETWORK_SCAN = f"{API_VERSION_1}/network/scan"
    NETWORK_STATUS = f"{API_VERSION_1}/network/status"
    OTA_CHECK = f"{API_VERSION_1}/ota/check"
    OTA_START = f"{API_VERSION_1}/ota/start"
    OTA_STATUS = f"{API_VERSION_1}/ota/status"
    
    POWER_SETPOINT = f"{API_VERSION_1}/power/setpoint"
    POWER_STATUS = f"{API_VERSION_1}/power/status"
    POWER_STRATEGY = f"{API_VERSION_1}/power/active_strategy"

    P1_DETAILS = f"{API_VERSION_2}/p1/details"
    P1_STATUS = f"{API_VERSION_1}/p1/status"
    
    SYSTEM_SETTINGS = f"{API_VERSION_1}/system/settings"
    SYSTEM_INFO = f"{API_VERSION_1}/system/info"
    SYSTEM_RESTART = f"{API_VERSION_1}/system/restart"
    WIFI_STA_CREDENTIALS = f"{API_VERSION_1}/wifi_sta/credentials"


class SessyPowerStrategy(str, Enum):
    API = "POWER_STRATEGY_API"
    NOM = "POWER_STRATEGY_NOM"
    ROI = "POWER_STRATEGY_ROI"
    IDLE = "POWER_STRATEGY_IDLE"

class SessySystemState(str, Enum):
    RUNNING_SAFE = "SYSTEM_STATE_RUNNING_SAFE"
    STANDBY = "SYSTEM_STATE_STANDBY"
    WAITING_FOR_SAFE = "SYSTEM_STATE_WAITING_FOR_SAFE_SITUATION"
    WAITING_SAFE = "SYSTEM_STATE_WAITING_IN_SAFE_SITUATION"
    WAITING_PERIPHERALS = "SYSTEM_STATE_WAIT_FOR_PERIPHERALS"
    ERROR = "SYSTEM_STATE_ERROR"
    INITIALIZING = "SYSTEM_STATE_INIT", 
    OVERRIDE_OVER_FREQUENCY = "SYSTEM_STATE_OVERRIDE_OVERFREQUENCY", 
    OVERRIDE_UNDER_FREQUENCY = "SYSTEM_STATE_OVERRIDE_UNDERFREQUENCY", 
    DISCONNECT = "SYSTEM_STATE_DISCONNECT", 
    RECONNECT = "SYSTEM_STATE_RECONNECT",
    BATTERY_FULL = "SYSTEM_STATE_BATTERY_FULL"
    BATTERY_EMPTY = "SYSTEM_STATE_BATTERY_EMPTY"

class SessyP1State(str, Enum):
    NOT_CONNECTED = "P1_NOT_CONNECTED"
    DATA_VALIDITY_ERROR = "P1_DATAVALIDITY_ERR"
    VERSION_ERROR = "P1_VERSION_ERR"
    PARSE_ERROR = "P1_PARSE_ERR"
    OK = "P1_OK"

class SessyOtaTarget(str, Enum):
    SELF = "OTA_TARGET_SELF"
    SERIAL = "OTA_TARGET_SERIAL"
    ALL = "OTA_TARGET_ALL"  # available as of version 1.5.1

class SessyOtaState(str, Enum):
    FAILED = "OTA_UPDATE_FAILED"
    DISABLED = "OTA_DISABLED"
    INACTIVE = "OTA_INACTIVE"
    CHECKING = "OTA_CHECKING"
    CHECK_FAILED = "OTA_CHECK_FAILED"
    UP_TO_DATE = "OTA_UP_TO_DATE"
    AVAILABLE = "OTA_NEW_VERSION_AVAILABLE"
    UPDATING = "OTA_UPDATING"
    PENDING_VERIFY = "OTA_PENDING_VERIFY"
    DONE = "OTA_DONE"
    UNKNOWN = "unknown"
