import os, tempfile, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cmdline.config import Config


def test_config():

    # Convert text into tmp file
    tmp_file = tempfile.NamedTemporaryFile(suffix=".cfg", delete=False)
    with open(tmp_file.name, "w") as f:
        f.write("""
                [GLOBAL]
                export_cmd=bcp
                servers_connections=[{"db1": {"port": 3306, "user": "xx", "password": "xx"},
                                      "db2": {"port": 3306, "user": "xx", "password": "xx"}}]
        """)


    c = Config(tmp_file.name)

    assert c.export_cmd == "bcp"
    assert c.servers_connections == [
        {'db1': {'port': 3306, 'user': 'xx', 'password': 'xx'},
        'db2': {'port': 3306, 'user': 'xx', 'password': 'xx'}
        }]
