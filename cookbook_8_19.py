# class Connection:
#     def __init__(self):
#         self.state = 'CLOSED'
#     def read(self):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not Open')
#         print('reading')
#     def write(self, data):
#         if self.state != 'OPEN':
#             raise RuntimeError('Not Open')
#         print('writing')
#     def open(self):
#         if self.state == 'OPEN':
#             print('Already open')
#         self.state = 'OPEN'
#     def close(self):
#         if self.state == 'CLOSED':
#             raise RuntimeError('Already closed')
class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)

    def new_state(self, new_state):
        self._state = new_state
        pass

    # delegate to the state class
    def read(self):
        return self._state.read(self)

    def open(self):
        return self._state.open(self)

    def close(self):
        return self._state.close(self)

    def write(self, data):
        return self._state.write(self, data)


# connection state base class
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()

    @staticmethod
    def write(conn, data):
        raise NotImplementedError()

    @staticmethod
    def open(conn):
        raise NotImplementedError()

    @staticmethod
    def close():
        raise NotImplementedError()


class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not Open')

    @staticmethod
    def write(conn, data):
        raise RuntimeError('Not Open')

    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)

    @staticmethod
    def close():
        raise RuntimeError('Not Open')


class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading...')

    @staticmethod
    def write(conn, data):
        print('writing...')

    @staticmethod
    def open(conn):
        raise RuntimeError('Already Open!')

    @staticmethod
    def close():
        raise RuntimeError('Already closed!')

c = Connection()

c._state
c.read()
c.open()