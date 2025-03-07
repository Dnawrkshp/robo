from enum import Enum

class Symbols:
	DEFAULT = b'\x08'
	BLUE = b'\x09'
	GREEN = b'\x0A'
	PINK = b'\x0B'
	WHITE = b'\x0C'
	GRAY = b'\x0D'
	BLACK = b'\x0E'

	CROSS = 0x10
	CIRCLE = 0x11
	TRIANGLE = 0x12
	SQUARE = 0x13
	L1 = 0x14
	R1 = 0x15
	L2 = 0x16
	R2 = 0x17
	ANALOG_LEFT = 0x18
	ANALOG_RIGHT = 0x19
	SELECT = 0x1A


class Symbols_Unicode:
    DEFAULT = '3038'
    BLUE = '3039'
    GREEN = '3041'
    PINK = '3042'
    WHITE = '3043'
    GRAY = '3044'
    BLACK = '3045'

    SELECT_BUTTON = '3141'
    CROSS = '3130'

COLOR_MAP_1 = {
    '1': Symbols_Unicode.DEFAULT,
    '2': Symbols_Unicode.BLUE,
    '3': Symbols_Unicode.GREEN,
    '4': Symbols_Unicode.PINK,
    '5': Symbols_Unicode.WHITE,
    '6': Symbols_Unicode.GRAY,
    '7': Symbols_Unicode.BLACK
}
CLANTAG_ALLOWED_CHARACTERS = {
    '3631': 'A', '3632': 'B', '3633': 'C', '3634': 'D',
    '3635': 'E', '3636': 'F', '3637': 'G', '3638': 'H',
    '3639': 'I', '3641': 'J', '3642': 'K', '3643': 'L',
    '3644': 'M', '3645': 'N', '3646': 'O', '3730': 'P',
    '3731': 'Q', '3732': 'R', '3733': 'S', '3734': 'T',
    '3735': 'U', '3736': 'V', '3737': 'W', '3738': 'X',
    '3739': 'Y', '3741': 'Z',
    '3330': '0', '3339': '9', '3338': '8', '3337': '7',
    '3336': '6', '3335': '5', '3334': '4', '3333': '3',
    '3332': '2', '3331': '1',
    '3431': 'a', '3432': 'b', '3433': 'c', '3434': 'd',
    '3435': 'e', '3436': 'f', '3437': 'g', '3438': 'h',
    '3439': 'i', '3441': 'j', '3442': 'k', '3443': 'l',
    '3444': 'm', '3445': 'n', '3446': 'o', '3530': 'p',
    '3531': 'q', '3532': 'r', '3533': 's', '3534': 't',
    '3535': 'u', '3536': 'v', '3537': 'w', '3538': 'x',
    '3539': 'y', '3541': 'z',
    '3230': ' ', '3231': '!', '3430': '@', '3233': '#',
    '3234': '$', '3235': '%', '3545': '^', '3236': '&',
    '3241': '*', '3238': '(', '3239': ')', '3546': '_',
    '3242': '+', '3742': '{', '3744': '}', '3232': '"',
    '3341': ':', '3346': '?', '3343': '<', '3345': '>',
    '3244': '-', '3344': '=', '3246': '/', '3542': '[',
    '3544': ']', '3342': ';', '3237': "'", '3245': '.',
    '3243': ',',
    '3030': 'empty',
    # Symbols_Unicode.DEFAULT: 'default color',
    Symbols_Unicode.BLUE: 'blue',
    Symbols_Unicode.GREEN: 'green',
    Symbols_Unicode.PINK: 'pink',
    Symbols_Unicode.WHITE: 'white',
    Symbols_Unicode.GRAY: 'gray',
    Symbols_Unicode.BLACK: 'black',
}



class GeneralEnum(Enum):
    @classmethod
    def get(self, value):
        for id in list(self):
            if value == id.value:
                return id

class MediusApplicationType:
    MEDIUS_APP_TYPE_GAME = 0
    LOBBY_CHAT_CHANNEL = 1

class MediusGameHostType:
    HOST_CLIENT_SERVER = 0,
    HOST_INTEGRATED_SERVER = 1
    HOST_PEER_TO_PEER = 2
    HOST_LAN_PLAY = 3 
    HOST_CLIENT_SERVER_AUX_UDP = 4

class MediusWorldStatus:
    WORLD_INACTIVE = 0
    WORLD_STAGING = 1
    WORLD_ACTIVE = 2
    WORLD_CLOSED = 3
    WORLD_PENDING_CREATION = 4
    WORLD_PENDING_CONNECT_TO_GAME = 5

class MediusChatMessageType:
    BROADCAST = 0
    WHISPER = 1
    BROADCAST_ACROSS_ENTIRE_UNIVERSE = 2
    CLAN_CHAT_TYPE = 3
    BUDDY_CHAT_TYPE = 4

class NetAddressType:
    NET_ADDRESS_NONE = 0
    NET_ADDRESS_TYPE_EXTERNAL = 1
    NET_ADDRESS_TYPE_INTERNAL = 2
    NET_ADDRESS_NAT_SERVICE = 3
    NET_ADDRESS_TYPE_BINARY_EXTERNAL = 4
    NET_ADDRESS_TYPE_BINARY_INTERNAL = 5
    NET_ADDRESS_TYPE_BINARY_EXTERNAL_VPORT = 6
    NET_ADDRESS_TYPE_BINARY_INTERNAL_VPORT = 7
    NET_ADDRESS_TYPE_BINARY_NAT_SERVICES = 8
    
class NetConnectionType:
    NET_CONNECTION_NONE = 0
    NET_CONNECTION_TYPE_CLIENT_SERVER_TCP = 1
    NET_CONNECTION_TYPE_PEER_TO_PEER_UDP = 2
    NET_CONNECTION_TYPE_CLIENT_SERVER_TCP_AUX_UDP = 3
    NET_CONNECTION_TYPE_CLIENT_LISTENER_TCP = 4


class WorldSecurityLevelType:
    WORLD_SECURITY_NONE = 0
    WORLD_SECURITY_PLAYER_PASSWORD = 1
    WORLD_SECURITY_CLOSED = 2
    WORLD_SECURITY_SPECTATOR_PASSWORD = 3

class MediusPlayerStatus:
    MEDIUS_PLAYER_DISCONNECTED = 0
    MEDIUS_PLAYER_IN_AUTH_WORLD = 1
    MEDIUS_PLAYER_IN_CHAT_WORLD = 2
    MEDIUS_PLAYER_IN_GAME_WORLD = 3
    MEDIUS_PLAYER_IN_OTHER_UNIVERSE = 4

class MediusEnum:
    BASIC_IP = 16
    BASIC_PORT = 2
    ACCOUNTNAME_MAXLEN = 32
    WORLDNAME_MAXLEN = 64
    WORLDPASSWORD_MAXLEN = 32
    WORLDSTATS_MAXLEN = 256
    SERVERIP_MAXLEN = 20
    IP_MAXLEN = 20
    SERVERPORT_MAXLEN = 8
    SERVERVERSION_MAXLEN = 16
    ACCOUNTID_MAXLEN = 32
    PASSWORD_MAXLEN = 32
    PLAYERNAME_MAXLEN = 32
    ACCOUNTSTATS_MAXLEN = 256
    GAMENAME_MAXLEN = 64
    LOBBYNAME_MAXLEN = 64
    GAMEPASSWORD_MAXLEN = 32
    LOBBYPASSWORD_MAXLEN = 32
    GAMESTATS_MAXLEN = 256
    WINNINGTEAM_MAXLEN = 64
    APPNAME_MAXLEN = 32
    CHATMESSAGE_MAXLEN = 64
    BINARYMESSAGE_MAXLEN = 400
    POLICY_MAXLEN = 256
    NEWS_MAXLEN = 256
    ERRORMSG_MAXLEN = 256
    MAX_WORLDS_PER_SERVER = 1000
    ANNOUNCEMENT_MAXLEN = 1000
    ACCOUNTLIST_MAXLEN = 256
    SESSIONKEY_MAXLEN = 17
    MESSAGEID_MAXLEN = 21
    ICONLOCATION_MAXLEN = 64
    MEDIUS_BASE_WORLDID = 1
    ACCESSKEY_MAXLEN = 17
    VERSIONSTRING_MAXLEN = 56
    LOCATIONNAME_MAXLEN = 64
    USERNAME_MAXLEN = 32
    ESC_ACCOUNTSTATS_MAXLEN = (256 * 3) + 1
    DNASSIGNATURE_MAXLEN = 32
    BILLINGTOKEN_MAXLEN = 20
    TITLENAME_MAXLEN = 64
    UNIVERSENAME_MAXLEN = 128
    UNIVERSEDNS_MAXLEN = 128
    UNIVERSEDESCRIPTION_MAXLEN = 256
    UNIVERSE_BSP_MAXLEN = 8
    UNIVERSE_BSP_NAME_MAXLEN = 128
    UNIVERSE_EXTENDED_INFO_MAXLEN = 128
    UNIVERSE_SVO_URL_MAXLEN = 128
    FULLPOLICY_MAXLEN = 10000
    LADDERSTATS_MAXLEN = 15
    LADDERSTATSWIDE_MAXLEN = 400
    BANDATETIME_MAXLEN = 32
    DEBUGMESSAGE_MAXLEN = 200
    ID_ARRAY_MAXLEN = 50
    MEDIUS_MESSAGE_MAXLEN = 512
    CLANNAME_MAXLEN = 32
    CLANSTATS_MAXLEN = 256
    ESC_CLANSTATS_MAXLEN = (256 * 3) + 1
    CLANWELCOMEMSG_MAXLEN = 200
    CLANINVITEMSG_MAXLEN = 200
    CLANINVITERESPONSEMSG_MAXLEN = 200
    CLANCHALLENGEMSG_MAXLEN = 200
    CLANMSG_MAXLEN = 200
    MEDIUS_TOKEN_MAXSIZE = 8
    MEDIUS_BITFIELD_ELEMENT_SIZE = 8
    MEDIUS_GENERIC_CHAT_FILTER_BITFIELD_LEN = 128
    MEDIUS_GENERIC_CHAT_FILTER_BYTES_LEN = (128 + 7) / 8
    MEDIUS_WORLD_STATUS = 4

class CallbackStatus():
    BEGIN_SESSION_FAILED = -1000
    ACCOUNT_ALREADY_EXISTS = -999
    ACCOUNT_NOT_FOUND = -998
    ACCOUNT_LOGGED_IN = -997
    END_SESSION_FAILED = -996
    LOGIN_FAILED = -995
    REGISTRATION_FAILED = -994
    INCORRECT_LOGIN_STEP = -993
    ALREADY_LEADER_OF_CLAN = -992
    WORLD_MANAGER_ERROR = -991
    NOT_CLAN_LEADER = -990
    PLAYER_NOT_PRIVILEGED = -989
    DATABASE_ERROR = -988
    DME_ERROR = -987
    EXCEEDS_MAX_WORLDS = -986
    REQUEST_DENIED = -985
    SET_GAME_FILTER_FAILED = -984
    CLEAR_GAME_LIST_FILTER_FAILED = -983
    GET_GAME_LIST_FILTER_FAILED = -982
    NUM_FILTERS_AT_MAX = -981
    FILTER_NOT_FOUND = -980
    INVALID_REQUEST_MESSAGE = -979
    INVALID_PASSWORD = -978
    GAME_NOT_FOUND = -977
    CHANNEL_NOT_FOUND = -976
    GAME_NAME_EXISTS = -975
    CHANNEL_NAME_EXISTS = -974
    GAME_NAME_NOT_FOUND = -973
    PLAYER_BANNED = -972
    CLAN_NOT_FOUND = -971
    CLAN_NAME_IN_USE = -970
    SESSION_KEY_INVALID = -969
    TEXT_STRING_INVALID = -968
    FILTER_FAILED = -967
    FAILURE = -966
    FILE_INTERNAL_ACCESS_ERROR = -965
    FILE_NO_PERMISSIONS = -964
    FILE_DOES_NOT_EXIST = -963
    FILE_ALREADY_EXISTS = -962
    FILE_INVALID_FILENAME = -961
    FILE_QUOTA_EXCEEDED = -960
    CACHE_FAILURE = -959
    DATA_ALREADY_EXISTS = -958
    DATA_DOES_NOT_EXIST = -957
    MAX_EXCEEDED = -956
    KEY_ERROR = -955
    INCOMPATIBLE_APP_ID = -954
    ACCOUNT_BANNED = -953
    MACHINE_BANNED = -952
    LEADER_CANNOT_LEAVE_CLAN = -951
    FEATURE_NOT_ENABLED = -950
    DNAS_SIGNATURE_LOGGED_IN = -949
    WORLD_IS_FULL = -948
    NOT_CLAN_MEMBER = -947
    SERVER_BUSY = -946
    NUM_GAME_WORLDS_PER_LOBBY_EXCEEDED = -945
    ACCOUNT_NOT_UC_COMPLIANT = -944
    PASSWORD_NOT_UC_COMPLIANT = -943
    GATEWAY_ERROR = -942
    TRANSACTION_CANCELLED = -941
    SESSION_FAILURE = -940
    TOKEN_ALREADY_TAKEN = -939
    TOKEN_DOES_NOT_EXIST = -938
    SUBSCRIPTION_ABORTED = -937
    SUBSCRIPTION_INVALID = -936
    NOT_A_MEMBER = -935
    SUCCESS = 0
    NO_RESULT = 1
    REQUEST_ACCEPTED = 2
    WORLD_CREATED_SIZE_REDUCED = 3
    PASS = 4

class MediusIdEnum():
    DMEServerVersion = b'\x00\x00'
    DMEPing = b'\x00\x01'
    DMETypePacketFragment = b'\x00\x02'
    DMEClientConnects = b'\x00\x10'
    DMERequestServers = b'\x00\x13'
    DMEServerResponse = b'\x00\x14'
    DMEUpdateClientStatus = b'\x00\x16'
    DMELANFindPacket = b'\x00\x19'
    DMELANFindResultsPacket = b'\x00\x1A'
    DMELANTextMessage = b'\x00\x21'
    DMELANRawMessage = b'\x00\x22'
    MediusServerAuthenticationRequest = b'\x03\x01'
    MediusServerAuthenticationResponse = b'\x03\x02'
    MediusServerSessionBeginRequest = b'\x03\x03'
    MediusServerSessionBeginResponse = b'\x03\x04'
    MediusServerSessionEndRequest = b'\x03\x05'
    MediusServerSessionEndResponse = b'\x03\x06'
    MediusServerCreateGameRequest = b'\x03\x07'
    MediusServerCreateGameResponse = b'\x03\x08'
    MediusServerJoinGameRequest = b'\x03\x09'
    MediusServerJoinGameResponse = b'\x03\x0A'
    MediusServerEndGameRequest = b'\x03\x0B'
    MediusServerEndGameResponse = b'\x03\x0C'
    MediusServerWorldStatusRequest = b'\x03\x0D'
    MediusServerWorldStatusResponse = b'\x03\x0E'
    MediusServerCreateGameOnMeRequest = b'\x03\x1F'
    MediusServerCreateGameOnMeResponse = b'\x03\x10'
    MediusServerEndGameOnMeRequest = b'\x03\x11'
    MediusServerEndGameOnMeResponse = b'\x03\x12'
    MediusServerMoveGameWorldOnMeRequest = b'\x03\x14'
    MediusServerMoveGameWorldOnMeResponse = b'\x03\x15'
    MediusServerSetAttributesRequest = b'\x03\x16'
    MediusServerSetAttributesResponse = b'\x03\x17'
    MediusServerCreateGameWithAttributesRequest = b'\x03\x18'
    MediusServerCreateGameWithAttributesResponse = b'\x03\x19'
    MediusServerConnectGamesRequest = b'\x03\x1A'
    MediusServerConnectGamesResponse = b'\x03\x1B'
    MediusServerDisconnectPlayerRequest = b'\x03\x1E'
    WorldReport0 = b'\x01\x00'
    PlayerReport = b'\x01\x01'
    EndGameReport = b'\x01\x02'
    SessionBegin = b'\x01\x03'
    SessionBeginResponse = b'\x01\x04'
    SessionEnd = b'\x01\x05'
    SessionEndResponse = b'\x01\x06'
    AccountLogin = b'\x01\x07'
    AccountLoginResponse = b'\x01\x08'
    AccountRegistration = b'\x01\x09'
    AccountRegistrationResponse = b'\x01\x0A'
    AccountGetProfile = b'\x01\x0B'
    AccountGetProfileResponse = b'\x01\x0C'
    AccountUpdateProfile = b'\x01\x0D'
    AccountUpdateProfileResponse = b'\x01\x0E'
    AccountUpdatePassword = b'\x01\x0F'
    AccountUpdateStats = b'\x01\x11'
    AccountUpdateStatsResponse = b'\x01\x12'
    AccountDelete = b'\x01\x13'
    AccountDeleteResponse = b'\x01\x14'
    AccountLogout = b'\x01\x15'
    AccountLogoutResponse = b'\x01\x16'
    AccountGetId = b'\x01\x17'
    AccountGetIdResponse = b'\x01\x18'
    AnonymousLogin = b'\x01\x19'
    AnonymousLoginResponse = b'\x01\x1A'
    GetMyIP = b'\x01\x1B'
    GetMyIPResponse = b'\x01\x1C'
    CreateGameRequest0 = b'\x01\x1D'
    CreateGameResponse = b'\x01\x1E'
    CreateGameOnSelf = b'\x01\x1F'
    CreateGameOnSelfResponse = b'\x01\x20'
    CreateChannelRequest0 = b'\x01\x21'
    CreateChannelResponse = b'\x01\x22'
    JoinGameRequest0 = b'\x01\x23'
    JoinGameResponse = b'\x01\x24'
    JoinChannel = b'\x01\x25'
    JoinChannelResponse = b'\x01\x26'
    JoinChannelFwd = b'\x01\x27'
    JoinChannelFwdResponse = b'\x01\x28'
    GameList = b'\x01\x29'
    GameListResponse = b'\x01\x2A'
    ChannelList = b'\x01\x2B'
    ChannelListResponse = b'\x01\x2C'
    LobbyWorldPlayerList = b'\x01\x2D'
    LobbyWorldPlayerListResponse = b'\x01\x2E'
    GameWorldPlayerList = b'\x01\x2F'
    GameWorldPlayerListResponse = b'\x01\x30'
    PlayerInfo = b'\x01\x31'
    PlayerInfoResponse = b'\x01\x32'
    GameInfo0 = b'\x01\x33'
    GameInfoResponse0 = b'\x01\x34'
    ChannelInfo = b'\x01\x35'
    ChannelInfoResponse = b'\x01\x36'
    FindWorldByName = b'\x01\x37'
    FindWorldByNameResponse = b'\x01\x38'
    FindPlayer = b'\x01\x39'
    FindPlayerResponse = b'\x01\x3A'
    ChatMessage = b'\x01\x3B'
    ChatFwdMessage = b'\x01\x3C'
    GetBuddyList = b'\x01\x3D'
    GetBuddyListResponse = b'\x01\x3E'
    AddToBuddyList = b'\x01\x3F'
    AddToBuddyListResponse = b'\x01\x40'
    RemoveFromBuddyList = b'\x01\x41'
    RemoveFromBuddyListResponse = b'\x01\x42'
    AddToBuddyListConfirmationRequest0 = b'\x01\x43'
    AddToBuddyListConfirmationResponse = b'\x01\x44'
    AddToBuddyListFwdConfirmationRequest0 = b'\x01\x45'
    AddToBuddyListFwdConfirmationResponse0 = b'\x01\x46'
    Policy = b'\x01\x47'
    PolicyResponse = b'\x01\x48'
    UpdateUserState = b'\x01\x49'
    ErrorMessage = b'\x01\x4A'
    GetAnnouncements = b'\x01\x4B'
    GetAllAnnouncements = b'\x01\x4C'
    GetAnnouncementsResponse = b'\x01\x4D'
    SetGameListFilter0 = b'\x01\x4E'
    SetGameListFilterResponse0 = b'\x01\x4F'
    ClearGameListFilter0 = b'\x01\x50'
    ClearGameListFilterResponse = b'\x01\x51'
    GetGameListFilter = b'\x01\x52'
    GetGameListFilterResponse0 = b'\x01\x53'
    CreateClan = b'\x01\x54'
    CreateClanResponse = b'\x01\x55'
    DisbandClan = b'\x01\x56'
    DisbandClanResponse = b'\x01\x57'
    GetClanByID = b'\x01\x58'
    GetClanByIDResponse = b'\x01\x59'
    GetClanByName = b'\x01\x5A'
    GetClanByNameResponse = b'\x01\x5B'
    TransferClanLeadership = b'\x01\x5C'
    TransferClanLeadershipResponse = b'\x01\x5D'
    AddPlayerToClan = b'\x01\x5E'
    AddPlayerToClanResponse = b'\x01\x5F'
    RemovePlayerFromClan = b'\x01\x60'
    RemovePlayerFromClanResponse = b'\x01\x61'
    InvitePlayerToClan = b'\x01\x62'
    InvitePlayerToClanResponse = b'\x01\x63'
    CheckMyClanInvitations = b'\x01\x64'
    CheckMyClanInvitationsResponse = b'\x01\x65'
    RespondToClanInvitation = b'\x01\x66'
    RespondToClanInvitationResponse = b'\x01\x67'
    RevokeClanInvitation = b'\x01\x68'
    RevokeClanInvitationResponse = b'\x01\x69'
    RequestClanTeamChallenge = b'\x01\x6A'
    RequestClanTeamChallengeResponse = b'\x01\x6B'
    GetMyClanMessages = b'\x01\x6C'
    GetMyClanMessagesResponse = b'\x01\x6D'
    SendClanMessage = b'\x01\x6E'
    SendClanMessageResponse = b'\x01\x6F'
    ModifyClanMessage = b'\x01\x70'
    ModifyClanMessageResponse = b'\x01\x71'
    DeleteClanMessage = b'\x01\x72'
    DeleteClanMessageResponse = b'\x01\x73'
    RespondToClanTeamChallenge = b'\x01\x74'
    RespondToClanTeamChallengeResponse = b'\x01\x75'
    RevokeClanTeamChallenge = b'\x01\x76'
    RevokeClanTeamChallengeResponse = b'\x01\x77'
    GetClanTeamChallengeHistory = b'\x01\x78'
    GetClanTeamChallengeHistoryResponse = b'\x01\x79'
    GetClanInvitationsSent = b'\x01\x7A'
    GetClanInvitationsSentResponse = b'\x01\x7B'
    GetMyClans = b'\x01\x7C'
    GetMyClansResponse = b'\x01\x7D'
    GetAllClanMessages = b'\x01\x7E'
    GetAllClanMessagesResponse = b'\x01\x7F'
    ConfirmClanTeamChallenge = b'\x01\x80'
    ConfirmClanTeamChallengeResponse = b'\x01\x81'
    GetClanTeamChallenges = b'\x01\x82'
    GetClanTeamChallengesResponse = b'\x01\x83'
    UpdateClanStats = b'\x01\x84'
    UpdateClanStatsResponse = b'\x01\x85'
    VersionServer = b'\x01\x86'
    VersionServerResponse = b'\x01\x87'
    GetWorldSecurityLevel = b'\x01\x88'
    GetWorldSecurityLevelResponse = b'\x01\x89'
    BanPlayer = b'\x01\x8A'
    BanPlayerResponse = b'\x01\x8B'
    GetLocations = b'\x01\x8C'
    GetLocationsResponse = b'\x01\x8D'
    PickLocation = b'\x01\x8E'
    PickLocationResponse = b'\x01\x8F'
    GetClanMemberList = b'\x01\x90'
    GetClanMemberListResponse = b'\x01\x91'
    LadderPosition = b'\x01\x92'
    LadderPositionResponse = b'\x01\x93'
    LadderList = b'\x01\x94'
    LadderListResponse = b'\x01\x95'
    ChatToggle = b'\x01\x96'
    ChatToggleResponse = b'\x01\x97'
    TextFilter = b'\x01\x98'
    TextFilterResponse = b'\x01\x99'
    ServerReassignGameMediusWorldID = b'\x01\x9A'
    GetTotalGames = b'\x01\x9B'
    GetTotalGamesResponse = b'\x01\x9C'
    GetTotalChannels = b'\x01\x9D'
    GetTotalChannelsResponse = b'\x01\x9E'
    GetLobbyPlayerNames = b'\x01\x9F'
    GetLobbyPlayerNamesResponse = b'\x01\xA0'
    GetTotalUsers = b'\x01\xA1'
    GetTotalUsersResponse = b'\x01\xA2'
    SetLocalizationParams = b'\x01\xA3'
    SetLocalizationParamsResponse = b'\x01\xA4'
    FileCreate = b'\x01\xA5'
    FileCreateResponse = b'\x01\xA6'
    FileUpload = b'\x01\xA7'
    FileUploadResponse = b'\x01\xA8'
    FileUploadServerReq = b'\x01\xA9'
    FileClose = b'\x01\xAA'
    FileCloseResponse = b'\x01\xAB'
    FileDownload = b'\x01\xAC'
    FileDownloadResponse = b'\x01\xAD'
    FileDownloadStream = b'\x01\xAE'
    FileDownloadStreamResponse = b'\x01\xAF'
    FileDelete = b'\x01\xB0'
    FileDeleteResponse = b'\x01\xB1'
    FileListFiles = b'\x01\xB2'
    FileListFilesResponse = b'\x01\xB3'
    FileUpdateAttributes = b'\x01\xB4'
    FileUpdateAttributesResponse = b'\x01\xB5'
    FileGetAttributes = b'\x01\xB6'
    FileGetAttributesResponse = b'\x01\xB7'
    FileUpdateMetaData = b'\x01\xB8'
    FileUpdateMetaDataResponse = b'\x01\xB9'
    FileGetMetaData = b'\x01\xBA'
    FileGetMetaDataResponse = b'\x01\xBB'
    FileSearchByMetaData = b'\x01\xBC'
    FileSearchByMetaDataResponse = b'\x01\xBD'
    FileCancelOperation = b'\x01\xBE'
    FileCancelOperationResponse = b'\x01\xBF'
    GetIgnoreList = b'\x01\xC0'
    GetIgnoreListResponse = b'\x01\xC1'
    AddToIgnoreList = b'\x01\xC2'
    AddToIgnoreListResponse = b'\x01\xC3'
    RemoveFromIgnoreList = b'\x01\xC4'
    RemoveFromIgnoreListResponse = b'\x01\xC5'
    SetMessageAsRead = b'\x01\xC6'
    SetMessageAsReadResponse = b'\x01\xC7'
    GetUniverseInformation = b'\x01\xC8'
    UniverseNewsResponse = b'\x01\xC9'
    UniverseStatusListResponse = b'\x01\xCA'
    MachineSignaturePost = b'\x01\xCB'
    LadderPositionFast = b'\x01\xCC'
    LadderPositionFastResponse = b'\x01\xCD'
    UpdateLadderStats = b'\x01\xCE'
    UpdateLadderStatsResponse = b'\x01\xCF'
    GetLadderStats = b'\x01\xD0'
    GetLadderStatsResponse = b'\x01\xD1'
    GetBuddyList_ExtraInfo = b'\x01\xD6'
    GetBuddyList_ExtraInfoResponse = b'\x01\xD7'
    GetTotalRankings = b'\x01\xD8'
    GetTotalRankingsResponse = b'\x01\xD9'
    GetClanMemberList_ExtraInfo = b'\x01\xDA'
    GetClanMemberList_ExtraInfoResponse = b'\x01\xDB'
    GetLobbyPlayerNames_ExtraInfo = b'\x01\xDC'
    GetLobbyPlayerNames_ExtraInfoResponse = b'\x01\xDD'
    BillingLogin = b'\x01\xDE'
    BillingLoginResponse = b'\x01\xDF'
    BillingListRequest = b'\x01\xE0'
    BillingListResponse = b'\x01\xE1'
    BillingDetailRequest = b'\x01\xE2'
    BillingDetailResponse = b'\x01\xE3'
    PurchaseProductRequest = b'\x01\xE4'
    PurchaseProductResponse = b'\x01\xE5'
    BillingInfo = b'\x01\xE6'
    BillingInfoResponse = b'\x01\xE7'
    BillingTunnelRequest = b'\x01\xE8'
    BillingTunnelResponse = b'\x01\xE9'
    GameList_ExtraInfo0 = b'\x01\xEA'
    GameList_ExtraInfoResponse0 = b'\x01\xEB'
    ChannelList_ExtraInfo0 = b'\x01\xEC'
    ChannelList_ExtraInfoResponse = b'\x01\xED'
    InvitePlayerToClan_ByName = b'\x01\xEE'
    LadderList_ExtraInfo0 = b'\x01\xEF'
    LadderList_ExtraInfoResponse = b'\x01\xF0'
    LadderPosition_ExtraInfo = b'\x01\xF1'
    LadderPosition_ExtraInfoResponse = b'\x01\xF2'
    JoinGame = b'\x01\xF3'
    CreateGame1 = b'\x01\xF4'
    UtilAddLobbyWorld = b'\x01\xF5'
    UtilAddLobbyWorldResponse = b'\x01\xF6'
    UtilAddGameWorld = b'\x01\xF7'
    UtilAddGameWorldResponse = b'\x01\xF8'
    UtilUpdateLobbyWorld = b'\x01\xF9'
    UtilUpdateLobbyWorldResponse = b'\x01\xFA'
    UtilUpdateGameWorld = b'\x01\xFB'
    UtilUpdateGameWorldResponse = b'\x01\xFC'
    CreateChannel1 = b'\x04\x00'
    UtilGetServerVersion = b'\x04\x01'
    UtilGetServerVersionResponse = b'\x04\x02'
    GetUniverse_ExtraInfo = b'\x04\x03'
    UniverseStatusList_ExtraInfoResponse = b'\x04\x04'
    AddToBuddyListConfirmation = b'\x04\x05'
    AddToBuddyListFwdConfirmation = b'\x04\x06'
    AddToBuddyListFwdConfirmationResponse = b'\x04\x07'
    GetBuddyInvitations = b'\x04\x08'
    GetBuddyInvitationsResponse = b'\x04\x09'
    DnasSignaturePost = b'\x04\x0A'
    UpdateLadderStatsWide = b'\x04\x0B'
    UpdateLadderStatsWideResponse = b'\x04\x0C'
    GetLadderStatsWide = b'\x04\x0D'
    GetLadderStatsWideResponse = b'\x04\x0E'
    LadderList_ExtraInfo = b'\x04\x0F'
    UtilEventMsgHandler = b'\x04\x10'
    UniverseVariableInformationResponse = b'\x04\x11'
    SetLobbyWorldFilter = b'\x04\x12'
    SetLobbyWorldFilterResponse = b'\x04\x13'
    CreateChannel = b'\x04\x14'
    ChannelList_ExtraInfo1 = b'\x04\x15'
    BinaryMessage = b'\x04\x16'
    BinaryFwdMessage = b'\x04\x17'
    PostDebugInfo = b'\x04\x18'
    PostDebugInfoResponse = b'\x04\x19'
    UpdateClanLadderStatsWide_Delta = b'\x04\x1A'
    UpdateClanLadderStatsWide_DeltaResponse = b'\x04\x1B'
    GetLadderStatsWide_wIDArray = b'\x04\x1C'
    GetLadderStatsWide_wIDArray_Response = b'\x04\x1D'
    UniverseVariableSvoURLResponse = b'\x04\x1E'
    ChannelList_ExtraInfo = b'\x04\x1F'
    GenericChatMessage = b'\x04\x23'
    GenericChatFwdMessage = b'\x04\x24'
    GenericChatSetFilterRequest = b'\x04\x25'
    GenericChatSetFilterResponse = b'\x04\x26'
    ExtendedSessionBeginRequest = b'\x04\x27'
    TokenRequest = b'\x04\x28'
    VoteToBanPlayerRequest = b'\x04\x2C'
    GetServerTimeRequest = b'\x04\x2A'
    GetServerTimeResponse = b'\x04\x2B'
    SetAutoChatHistoryRequest = b'\x04\x2D'
    SetAutoChatHistoryResponse = b'\x04\x2E'
    CreateGame = b'\x04\x2F'
    SetGameListFilter = b'\x04\x33'
    ClearGameListFilter = b'\x04\x31'
    WorldReport = b'\x04\x30'
    GameInfo = b'\x04\x35'
    GameInfoResponse = b'\x04\x36'
    GameList_ExtraInfo = b'\x04\x37'
    GameList_ExtraInfoResponse = b'\x04\x38'
    AccountUpdateStats_OpenAccess = b'\x04\x39'
    AccountUpdateStats_OpenAccessResponse = b'\x04\x3A'
    AddPlayerToClan_ByClanOfficer = b'\x04\x3B'
    AddPlayerToClan_ByClanOfficerResponse = b'\x04\x3C'


class RtIdEnum():
    CLIENT_CONNECT_TCP = 0x00
    CLIENT_DISCONNECT = 0x01
    CLIENT_APP_BROADCAST = 0x02
    CLIENT_APP_SINGLE = 0x03
    CLIENT_APP_LIST = 0x04
    CLIENT_ECHO = 0x05
    SERVER_CONNECT_REJECT = 0x06
    SERVER_CONNECT_ACCEPT_TCP = 0x07
    SERVER_CONNECT_NOTIFY = 0x08
    SERVER_DISCONNECT_NOTIFY = 0x09
    SERVER_APP = 0x0a
    CLIENT_APP_TOSERVER = 0x0b
    UDP_APP = 0x0c
    CLIENT_SET_RECV_FLAG = 0x0d
    CLIENT_SET_AGG_TIME = 0x0e
    CLIENT_FLUSH_ALL = 0x0f
    CLIENT_FLUSH_SINGLE = 0x10
    SERVER_FORCED_DISCONNECT = 0x11
    CLIENT_CRYPTKEY_PUBLIC = 0x12
    SERVER_CRYPTKEY_PEER = 0x13
    SERVER_CRYPTKEY_GAME = 0x14
    CLIENT_CONNECT_TCP_AUX_UDP = 0x15
    CLIENT_CONNECT_AUX_UDP = 0x16
    CLIENT_CONNECT_READY_AUX_UDP = 0x17
    SERVER_INFO_AUX_UDP = 0x18
    SERVER_CONNECT_ACCEPT_AUX_UDP = 0x19
    SERVER_CONNECT_COMPLETE = 0x1a
    CLIENT_CRYPTKEY_PEER = 0x1b
    SERVER_SYSTEM_MESSAGE = 0x1c
    SERVER_CHEAT_QUERY = 0x1d
    SERVER_MEMORY_POKE = 0x1e
    SERVER_ECHO = 0x1f
    CLIENT_DISCONNECT_WITH_REASON = 0x20
    CLIENT_CONNECT_READY_TCP = 0x21
    SERVER_CONNECT_REQUIRE = 0x22
    CLIENT_CONNECT_READY_REQUIRE = 0x23
    CLIENT_HELLO = 0x24
    SERVER_HELLO = 0x25
    SERVER_STARTUP_INFO_NOTIFY = 0x26
    CLIENT_PEER_QUERY = 0x27
    SERVER_PEER_QUERY_NOTIFY = 0x28
    CLIENT_PEER_QUERY_LIST = 0x29
    SERVER_PEER_QUERY_LIST_NOTIFY = 0x2a
    CLIENT_WALLCLOCK_QUERY = 0x2b
    SERVER_WALLCLOCK_QUERY_NOTIFY = 0x2c
    CLIENT_TIMEBASE_QUERY = 0x2d
    SERVER_TIMEBASE_QUERY_NOTIFY = 0x2e
    CLIENT_TOKEN_MESSAGE = 0x2f
    SERVER_TOKEN_MESSAGE = 0x30
    CLIENT_SYSTEM_MESSAGE = 0x31
    CLIENT_APP_BROADCAST_QOS = 0x32
    CLIENT_APP_SINGLE_QOS = 0x33
    CLIENT_APP_LIST_QOS = 0x34
    CLIENT_MAX_MSGLEN = 0x35
    SERVER_MAX_MSGLEN = 0x36

class CipherContext:
    ID_00 = 0x00
    RC_SERVER_SESSION = 0x01
    ID_02 = 0x02
    RC_CLIENT_SESSION = 0x03
    ID_04 = 0x04
    ID_05 = 0x05
    ID_06 = 0x06
    RSA_AUTH = 0x07
