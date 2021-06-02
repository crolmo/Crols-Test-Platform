#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/5/13 17:46
# @Author : Crolmo
# @Site : 
# @File : cpu_status.py
# @Software: PyCharm

import psutil


def get_cpu_usages(seconds):
    cpu_usages = psutil.cpu_percent(interval=seconds, percpu=True)
    return cpu_usages


class CpuStatus:

    """
    1.return all cpu usages
    2.return everyone cpu core usage
    """

    def __init__(self,seconds=1):
        self.seconds = seconds
        self._all_cpu_usages = get_cpu_usages(self.seconds)

    def get_cpu_core_usage(self,core_id):
        if isinstance(core_id, int):
            return self._all_cpu_usages[core_id]
        else:
            raise KeyError("core id must be int")

    def get_sum_cpu_usage(self):
        usage = psutil.cpu_percent(interval=self.seconds)
        return usage

    def get_pid_cpu_usage(self):
        usage = ""
        return usage

    def get_cpu_count(self):
        logical_cpu = psutil.cpu_count()
        physical_cpu = psutil.cpu_count(logical=False)
        cpu_count = {
            "logical cpu": logical_cpu,
            "physical cpu": physical_cpu
        }
        return cpu_count


