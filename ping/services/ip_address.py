import ipaddress


class IPAddressService:
    @staticmethod
    def get_ip_list(network):
        try:
            net = ipaddress.ip_network(network, strict=False)
            return [str(ip) for ip in net.hosts()]
        except ValueError:
            raise ValueError("Invalid IP or subnet mask")
