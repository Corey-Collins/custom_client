import sys

class CpuInfo(object):
    """ CPU's characteristics """

    def __init__(self):
        self.physical_cpu_count = None
        self.logical_cpu_count = None
        if sys.platform.startswith('linux'):
            from subprocess import check_output
            info = self.__parse_colon_divided_text(check_output(('lscpu')))
            sockets = int(info['Socket(s)'])
            cores_per_socket = int(info['Core(s) per socket'])
            self.physical_cpu_count = sockets*cores_per_socket
            self.logical_cpu_count = int(info['CPU(s)'])
        elif sys.platform == 'win32':
            from win32com.client import GetObject
            root = GetObject("winmgmts:root\cimv2")
            cpus = root.ExecQuery("Select * from Win32_Processor")
            self.physical_cpu_count = sum(
                cpu.NumberOfCores for cpu in cpus)
            self.logical_cpu_count = sum(
                cpu.NumberOfLogicalProcessors for cpu in cpus)
        elif sys.platform == 'darwin':
            from subprocess import check_output
            info = self.__parse_colon_divided_text(check_output(
                ('sysctl', 'hw.physicalcpu', 'hw.logicalcpu')))
            self.physical_cpu_count = int(info['hw.physicalcpu'])
            self.logical_cpu_count  = int(info['hw.logicalcpu'])

    @classmethod
    def __parse_colon_divided_text(self, txt):
        return dict(
            (s.strip() for s in items)
            for items in (li.split(':') for li in txt.split('\n'))
            if len(items) == 2)

    def __str__(self):
        try:
            return '\n'.join((
                "Physical CPU(s): %(physical_cpu_count)i",
                "Logical CPU(s) : %(logical_cpu_count)i",
                )) % vars(self)
        except TypeError:
            return "Unknown"

cpu_info = CpuInfo()

if __name__ == '__main__':
    print cpu_info
