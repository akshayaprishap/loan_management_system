# Copyright (c) 2021, Akshaya Prisha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class loandetails1(Document):
	def on_submit(self):
		loan_amount= self.loan_amount
		max_loan_amount=1000000
		min_loan_amount=10000
		if(loan_amount >= min_loan_amount and loan_amount <= max_loan_amount):
			#interest=loan_amount/10
			#frappe.msgprint("Sucessfully Your loan is Applied !!")
			if(loan_amount<=500000):
				m_p=loan_amount*(5/100)
				self.interest=(loan_amount+m_p)/(5*12)
				self.interest=int(self.interest)
				self.total_months=5*12
				t_amount=loan_amount+m_p
				self.total_amount=t_amount
			else:
				m_p=loan_amount*(10/100)
				self.interest=(loan_amount+m_p)/(10*12)
				self.total_months=10*12
				t_amount=loan_amount+m_p
				self.total_amount=t_amount
				
		else:
			frappe.throw("Loan amount is not in loan range")


    #def on_submit(self):
		if frappe.db.exists("payslip",{'id':self.loan_id}):
			pass
		else:
			xy=frappe.new_doc("payslip")
			xy.customer_name=self.customer_name
			xy.id=self.loan_id
			xy.total_amount=self.total_amount
			xy.monthly_pay=self.interest
			xy.save()