from socket import socket

from OpenSSL import SSL, crypto
from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display


display = Display()


class LookupModule(LookupBase):
    def run(self, terms, variables=None, **kwargs):
        certs = []
        for term in terms:
            display.debug(f"Fetching SSL cert for {term}")
            connection = \
                SSL.Connection(SSL.Context(SSL.TLSv1_2_METHOD), socket())
            server_certs = []

            try:
                connection.connect((term, 443))
                connection.do_handshake()
                server_certs = connection.get_peer_cert_chain()
                print(server_certs)
            except SSL.Error as e:
                raise AnsibleError(f"SSL Error: {str(e)}")

            try:
                cert = server_certs[-1]
                pem_cert = \
                    crypto.dump_certificate(crypto.FILETYPE_PEM, cert)\
                    .decode('utf-8')
                components = dict(cert.get_subject().get_components())
                cn = components.get(b'CN').decode('utf-8')
                display.vvvv(f"Found cert for CA {cn}:\n{pem_cert}")
                certs.append(pem_cert)
            except SSL.Error as e:
                raise e
        print(certs)
        return certs


if __name__ == '__main__':
    lm = LookupModule()
    import sys
    lm.run(sys.argv[1:])
