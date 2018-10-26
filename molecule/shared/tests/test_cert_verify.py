def test_cert_verify(host):
    cert_path = '/etc/pki/ca-trust/source/anchors/localhost.localdomain.crt'
    assert host.run('openssl verify {0}'.format(cert_path)).rc == 0
