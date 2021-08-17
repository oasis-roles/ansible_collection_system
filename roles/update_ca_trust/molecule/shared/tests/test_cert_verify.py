def test_cert_verify(host):
    cert_path = '/root/localhost.localdomain.crt'
    assert host.run('openssl verify {0}'.format(cert_path)).rc == 0
