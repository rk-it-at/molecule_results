"""Role testing files using testinfra."""

def test_apache_installed(host):
    a = host.package("httpd")
    assert a.is_installed

def test_apache_cert(host):
    c = host.file("/etc/pki/tls/certs/localhost.crt")
    assert c.is_file
    assert c.user == "root"
    assert c.group == "root"
    assert c.mode == 0o644

def test_apache_port(host):
    p = host.socket("tcp://0.0.0.0:80")
    assert p.is_listening
