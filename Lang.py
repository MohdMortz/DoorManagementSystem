from common.kernel.Language import Language

language = Language()


def lget(key, *params):
    return language.get(key, *params)


def lgetDefault(key, *params):
    return language.getDefault(key, *params)


def lregister(listener):
    language.register(listener)


APPLICATION_TITLE = "application_title"
COPYRIGHT = "copyright"
WELCOME = "welcome"
DOOR_STATUS = "door_status"
PASSWORDS = "passwords"
SETTINGS = "settings"
ADVANCED_SETTINGS = "advanced_settings"
CONFIGURATIONS = "configurations"
AUTOMATIC = "automatic"
FULL_OPEN = "full_open"
PARTIAL_OPEN = "partial_open"
ONE_WAY = "one_way"
LOCK = "lock"
MANUAL = "manual"
SUMMER_AUTOMATIC = "summer_automatic"
CONSTANT = "constant"
SET_USER_PASSWORD = "set_user_password"
SET_ADVANCED_USER_PASSWORD = "set_advanced_user_password"
SET_OWNER_PASSWORD = "set_owner_password"
SET_INSTALLER_PASSWORD = "set_installer_password"
SECONDS = "seconds"
OPEN_SPEED = "open_speed"
CLOSE_SPEED = "close_speed"
OPEN_tIME = "open_time"
PARTIAL_WIDTH = "partial_width"
MAX_OPEN_POINT = "max_open_point"
REMOTE_OPEN_TIME = "remote_open_time"
INITIAL_SETUP = "initial_setup"
SENSOR_STYLE = "sensor_style"
RADAR_INSIDE = "radar_inside"
PUSH_IN_OPEN = "push_in_open"
MOTOR_DIRECTION = "motor_direction"
FACTORY_RESET = "factory_reset"
AUTO_REVERSE = "auto_reverse"
AUTO_RESET_ERRORS = "auto_reset_errors"
AUTO_RESET_ERRORS_POSTFIX = "auto_reset_errors_value_postfix"
DOOR_ON_BATTERY = "door_on_battery"
EUROPEAN = "european"
INTERNATIONAL = "international"
WITHOUT_SENSORS = "without_sensors"
NORMALLY_OPEN_NO = "normally_open_no"
FREQUENCY_100HZ = "frequency_100hz"
CURRENT_MA_DC = "current_ma_dc"
NORMAL = "normal"
INVERTED = "inverted"
NORMAL_OPERATON = "normal_operation"
STOP_IN_OPEN_POSITION = "stop_in_open_position"
LOAD_DEFAULTS = 'load_defaults'
NO_FUNCTION_NO = 'no_function_no'
FORCE_OP_NO = 'force_op_no'
FORCE_TO_CL_NO = 'force_to_cl_no'
STAY_SHUTDOWN_NO = 'stay_shutdown_no'
SIDE_SCAN_NO = 'side_scan_no'
FLIP_FLOP_NO = 'flip_flop_no'
NO_FUNCTION_NC = 'no_function_nc'
FORCE_OP_NC = 'force_op_nc'
FORCE_TO_CL_NC = 'force_to_cl_nc'
STAY_SHUTDOWN_NC = 'stay_shutdown_nc'
SIDE_SCAN_NC = 'side_scan_nc'
FLIP_FLOP_NC = 'flip_flop_nc'
INPUT_FUNCTIONS = 'input_functions'
STOP = 'stop'
ESCAPE = 'escape'
REMOTE = 'remote'
SET_BATTERY_VOLTAGE = 'set_battery_voltage'
SAVE_AS_DEFAULT = 'save_as_default'
SET_RAMPS = 'set_ramps'
OPEN_RAMPS = 'open_ramps'
CLOSE_RAMPS = 'close_ramps'
ACCELERATION_SLOPE = 'acceleration_slope'
DECELERATION_SLOPE = 'deceleration_slope'
SLOW_SPEED = 'slow_speed'
SLOW_SPEED_START_POINT = 'slow_speed_start_point'
MINIMUM_SPEED_START_POINT = 'minimum_speed_start_point'
SET_MOTOR_VALUES = 'set_motor_values'
PULLY_SIZE = 'pully_size'
GEARBOX_REDUCTION = 'gearbox_reduction'
ENCODER_PULSES = 'encoder_pulses'
ENCODER_PULSES_VALUE_POSTFIX = 'encoder_pulses_value_postfix'
MOTOR_VOLTAGE = 'motor_voltage'
GLOBAL_MINIMUM_SPEED = 'global_minimum_speed'
BEHAVIOR = 'behavior'
POSITION_CONTROL_CLOSE_ONE_WAY = 'position_control_close_one_way'
POSITION_CONTROL_OPEN_PARTIAL = 'position_control_open_partial'
AFTER_AUTO_REVERSE_IN_CLOSE_DIRECTION = 'after_auto_reverse_in_close_direction'
AFTER_AUTO_REVERSE_IN_OPEN_DIRECTION = 'after_auto_reverse_in_open_direction'
ONE_WAY_TRAFFIC = 'one_way_traffic'
HIGH_TRAFFIC_BEHAVIOUR = 'high_traffic_behaviour'
HIGH_TRAFFIC_VALUE = 'high_traffic_value'
TWO_WAY_TRAFFIC = 'two_way_traffic'
LOCK_CHECK = 'lock_check'
OPEN_BY_FORCE = 'open_by_force'
MANUFACTURER_SETTINGS = 'manufacturer_settings'
CHANGE_SERIAL = 'change_serial'
OPEN_AFTER_3_SECONDS = 'open_after_3_seconds'
OPEN_AFTER_6_SECONDS = 'open_after_6_seconds'
CLOSE = 'close'
OPEN_AND_WAIT_2X = 'open_and_wait_2x'
OPEN_AND_WAIT_3X = 'open_and_wait_3x'
OPEN = 'open'
EXIT_ONLY = 'exit_only'
ENTRY_ONLY = 'entry_only'
DOOR_DIAMETER = 'door_diameter'
NUMBER_OF_LEAVES = 'number_of_leaves'
ACTIVE_SECTIONS_DISABLED = 'active_sections_disabled'
ACTIVE_SECTIONS_NORM = 'active_sections_norm'
SENSOR_INSIDE_EXIST = 'sensor_inside_exist'
FAST_SPEED = 'fast_speed'
PUSH_AND_GO = 'push_and_go'
REVERSE_SENSITIVITY = 'reverse_sensitivity'
SHIFT_SECURITY_AREA = 'shift_security_area'
FOUR_LEAVES = 'four_leaves'
THREE_LEAVES = 'three_leaves'
OK = 'ok'
CANCEL = 'cancel'
ENTER_PASSWORD = 'enter_password'
CURRENT_ACCESS = "current_access"
USER = 'user'
ADVANCED_USER = 'advanced_user'
OWNER = 'owner'
INSTALLER = 'installer'
NO_ACCESS = 'no_access'
EXPIRES_IN_MINUTES = 'expires_in_minutes'
EXPIRES_IN = 'expires_in'
WAITING_FOR_PASSWORD = 'waiting_for_password'
PLEASE_ENTER_A_PASSWORD = 'please_enter_a_password'
INVALID_PASSWORD = 'invalid_password'
PASSWORD_ACCEPTED = 'password_accepted'
HELP = 'help'
ENTER_THE_NEW_VALUE_FOR_SETTING = 'enter_the_new_value_for_setting'
OLD_PASSWORD = 'old_password'
NEW_PASSWORD = 'new_password'
RETYPE_PASSWORD = 'retype_password'
FILL_EMPTY_FIELDS = 'fill_empty_fields'
PASSWORDS_NOT_EQUAL = 'passwords_not_equal'
ERROR = 'error'
NEW_ROLE_PASSWORD_ACCEPTED = 'new_role_password_accepted'
WEB_SERVER_URL = 'web_server_url'
MODEL = 'model'
VERSION = 'version'
PROJECT_KEY = 'project_key'
DOOR_NAME = 'door_name'
SERIAL_NO = 'serial_no'
DOOR_STATUS_CHANGED_TO = 'door_status_changed_to'
SETTING_CHANGED_TO = 'setting_changed_to'
UNGROUPED_DOORS = 'ungrouped_doors'

DOOR_ERROR_0 = 'door_error_0'
DOOR_ERROR_10 = 'door_error_10'
DOOR_ERROR_11 = 'door_error_11'
DOOR_ERROR_12 = 'door_error_12'
DOOR_ERROR_13 = 'door_error_13'
DOOR_ERROR_14 = 'door_error_14'
DOOR_ERROR_15 = 'door_error_15'
DOOR_ERROR_16 = 'door_error_16'
DOOR_ERROR_17 = 'door_error_17'
DOOR_ERROR_100 = 'door_error_100'
DOOR_ERROR_101 = 'door_error_101'
DOOR_ERROR_109 = 'door_error_109'
DOOR_ERROR_110 = 'door_error_110'
DOOR_ERROR_111 = 'door_error_111'
DOOR_ERROR_112 = 'door_error_112'
DOOR_ERROR_120 = 'door_error_120'
DOOR_ERROR_121 = 'door_error_121'
DOOR_ERROR_130 = 'door_error_130'
DOOR_ERROR_141 = 'door_error_141'
DOOR_ERROR_142 = 'door_error_142'
DOOR_ERROR_144 = 'door_error_144'
DOOR_ERROR_145 = 'door_error_145'
DOOR_ERROR_200 = 'door_error_200'
DOOR_ERROR_201 = 'door_error_201'
DOOR_ERROR_202 = 'door_error_202'
DOOR_ERROR_210 = 'door_error_210'
DOOR_ERROR_211 = 'door_error_211'
DOOR_ERROR_215 = 'door_error_215'
DOOR_ERROR_220 = 'door_error_220'
DOOR_ERROR_222 = 'door_error_222'
DOOR_ERROR_223 = 'door_error_223'
DOOR_ERROR_224 = 'door_error_224'
DOOR_ERROR_230 = 'door_error_230'
DOOR_ERROR_231 = 'door_error_231'
DOOR_ERROR_232 = 'door_error_232'
DOOR_ERROR_233 = 'door_error_233'
DOOR_ERROR_236 = 'door_error_236'
DOOR_ERROR_237 = 'door_error_237'
DOOR_ERROR_238 = 'door_error_238'
DOOR_ERROR_239 = 'door_error_239'
DOOR_ERROR_240 = 'door_error_240'
DOOR_ERROR_241 = 'door_error_241'
DOOR_ERROR_242 = 'door_error_242'
DOOR_ERROR_243 = 'door_error_243'
DOOR_ERROR_244 = 'door_error_244'
DOOR_ERROR_245 = 'door_error_245'
DOOR_ERROR_250 = 'door_error_250'
DOOR_ERROR_251 = 'door_error_251'
DOOR_ERROR_252 = 'door_error_252'
DOOR_ERROR_253 = 'door_error_253'
DOOR_ERROR_254 = 'door_error_254'

NOW = 'now'
SECONDS_AGO = "seconds_ago"
MINUTES_AGO = "minutes_ago"
HOURS_AGO = "hours_ago"
HOURS_MINUTES_AGO = "hours_minutes_ago"

SET_GROUP = "set_group"
RENAME_GROUP = "rename_group"
GROUP_NAME = "group_name"
DELETE_GROUP = "delete_group"
REMOVE_FROM_GROUP = "remove_from_group"
NEW_GROUP = "new_group"

START_COMMAND = "start_command"
SCAN = "scan"

DOOR_IS_MECHANICAL = "door_is_mechanical"