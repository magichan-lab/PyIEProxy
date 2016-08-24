#-*- config: utf-8 -*-

try:
    import winreg as reg
except ImportError:
    import _winreg as reg


class IEProxy:
    KEY_NAME = 'Software\Microsoft\Windows\CurrentVersion\Internet Settings'

    def __init__(self):
        self.network_reg = reg.OpenKey(
            reg.HKEY_CURRENT_USER, IEProxy.KEY_NAME, 0, reg.KEY_ALL_ACCESS)

    def set_proxy(self, proxy):
        reg.SetValueEx(self.network_reg, 'ProxyServer', 0, reg.REG_SZ, proxy)

    def get_proxy(self):
        return reg.QueryValueEx(self.network_reg, 'ProxyServer')[0]

    def is_enable(self):
        return reg.QueryValueEx(self.network_reg, 'ProxyEnable')[0] is 1

    def enable(self):
        reg.SetValueEx(self.network_reg, 'ProxyEnable', 0, reg.REG_DWORD, 1)

    def disable(self):
        reg.SetValueEx(self.network_reg, 'ProxyEnable', 0, reg.REG_DWORD, 0)
