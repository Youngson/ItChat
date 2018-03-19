# -*- coding: utf-8 -*-
"""
# @Time    : 18-3-20 上午9:43
# @Author  : Youngson
# @Site    : 
# @File    : signals.py
# @Software: PyCharm
# @Desc    : 
# @License : Apache Licence
# @Contact : Youngson.gu@gmail.com
"""
from blinker import Namespace

_signals = Namespace()

scan_qr_code = _signals.signal('scan-qr-code')
confirm_login = _signals.signal('confirm-login')
logged_in = _signals.signal('logged-in')
logged_out = _signals.signal('logged-out')
