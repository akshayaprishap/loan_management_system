# Copyright (c) 2021, Akshaya Prisha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class payslip(Document):
	def validate(self):
		if(not self.balance):
			self.balance=self.total_amount	
		self.balance=self.balance-self.monthly_pay
		