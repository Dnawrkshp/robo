from enums.enums import MediusEnum, CipherContext
from utils import utils
from crypto.rc4 import RC4
from medius.rtpackets.serverconnectaccepttcp import ServerConnectAcceptTcpSerializer
from medius.rtpackets.serverconnectcomplete import ServerConnectCompleteSerializer
from medius.rtpackets.servercryptkeygame import ServerCryptkeyGameSerializer

class ClientConnectTcpSerializer:
    data_dict = [
        {'name': 'rtid', 'n_bytes': 1, 'cast': None},
        {'name': 'len', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
        {'name': 'unknown1', 'n_bytes': 3, 'cast': None},
        {'name': 'target_world_id', 'n_bytes': 2, 'cast': utils.bytes_to_int_little},
        {'name': 'app_id', 'n_bytes': 4, 'cast': utils.bytes_to_int_little},
        {'name': 'key', 'n_bytes': 64, 'cast': utils.bytes_to_int_little},
        {'name': 'session_key', 'n_bytes': MediusEnum.SESSIONKEY_MAXLEN, 'cast': None},
        {'name': 'access_key', 'n_bytes': MediusEnum.ACCESSKEY_MAXLEN, 'cast': None}
    ]

    def serialize(self, data: bytes):
        return utils.serialize(data, self.data_dict, __name__)

class ClientConnectTcpHandler:
    def process(self, serialized, monolith, con):

        # mls
        if 'access_key' in serialized.keys() or 'session_key' in serialized.keys():
            if con.server_name != 'mls':
                raise Exception(f'UNIMPLEMENTED ERROR: {con.server_name}!')

            # This user is reconnecting with session key
            client_manager = monolith.get_client_manager()
            if not client_manager.validate_access_key(serialized['access_key']):
                raise Exception("Invalid access key")

            if not client_manager.mls_connected(con, serialized['session_key'], serialized['target_world_id']):
                raise Exception("Invalid session key")

            username = client_manager.get_username(session_key=serialized['session_key'])
            client_manager.register_ip(username, con.addr)

            return [
                ServerConnectAcceptTcpSerializer.build(con.addr),
                ServerConnectCompleteSerializer.build()            
            ]

        # mas
        else:
            server_rc4_key = utils.generate_server_rc4_key()
            server_rc4 = RC4(server_rc4_key, context=CipherContext.RC_SERVER_SESSION)

            con.set_server_rc4(server_rc4)

            return [
                ServerCryptkeyGameSerializer.build(server_rc4_key),
                ServerConnectAcceptTcpSerializer.build(con.addr),
                ServerConnectCompleteSerializer.build()            
            ]
            