# Copyright (c) 2013, Makarand Bauskar and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

test_records = frappe.get_test_records('Client Support Ticket')

class TestClientSupportTicket(unittest.TestCase):
	pass
