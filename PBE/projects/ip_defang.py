def defang_ip(address):
    ip_defanged = ""
    split_address = address.split(".")
    sep = "[.]"
    ip_defanged = sep.join(split_address)
    return ip_defanged

ip_address = defang_ip("192.168.1.1")
print(ip_address)