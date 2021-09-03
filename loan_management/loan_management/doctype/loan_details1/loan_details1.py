# Copyright (c) 2021, Akshaya Prisha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class loandetails1(Document):
	def validate(self):
		if(self.loan_id != ' '):
			if(self.loan_type=="Housing loan"):
				loan_amount= self.loan_amount
				interest_percent=self.interest_percent
				max_loan_amount=1000000
				min_loan_amount=10000
				interest=self.interest
				if(loan_amount >= min_loan_amount and loan_amount <= max_loan_amount):
			#interest=loan_amount/10
			#frappe.msgprint("Sucessfully Your loan is Applied !!")
					if(loan_amount<=500000):
						self.total_months=60
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/60
						self.interest=mp
						
					else:
						self.total_months=120
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/120
						self.interest=mp
				
			if(self.loan_type=="Personal loan"):
				loan_amount= self.loan_amount
				interest_percent=self.interest_percent
				max_loan_amount=1000000
				min_loan_amount=10000
				interest=self.interest
				if(loan_amount >= min_loan_amount and loan_amount <= max_loan_amount):
			#interest=loan_amount/10
			#frappe.msgprint("Sucessfully Your loan is Applied !!")
					if(loan_amount<=500000):
						self.total_months=60
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/60
						self.interest=mp
						
					else:
						self.total_months=120
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/120
						self.interest=mp


			if(self.loan_type=="Jewel loan"):
				loan_amount= self.loan_amount
				interest_percent=self.interest_percent
				max_loan_amount=1000000
				min_loan_amount=10000
				interest=self.interest
				if(loan_amount >= min_loan_amount and loan_amount <= max_loan_amount):
			#interest=loan_amount/10
			#frappe.msgprint("Sucessfully Your loan is Applied !!")
					if(loan_amount<=500000):
						self.total_months=60
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/60
						self.interest=mp
						
					else:
						self.total_months=120
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/120
						self.interest=mp

			if(self.loan_type=="Buisness loan"):
				loan_amount= self.loan_amount
				interest_percent=self.interest_percent
				max_loan_amount=1000000
				min_loan_amount=10000
				interest=self.interest
				if(loan_amount >= min_loan_amount and loan_amount <= max_loan_amount):
			#interest=loan_amount/10
			#frappe.msgprint("Sucessfully Your loan is Applied !!")
					if(loan_amount<=500000):
						self.total_months=60
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/60
						self.interest=mp
						
					else:
						self.total_months=120
						t_amount=loan_amount+(loan_amount*(interest_percent/100))
						self.total_amount=t_amount
						mp=self.total_amount/120
						self.interest=mp


		    
	def on_sumbit(self):
		if frappe.db.exists("payslip",{'id':self.loan_id}):
			pass
		else:
			#frappe.msgprint("hhj")
			xy=frappe.new_doc("payslip")
			xy.customer_name=self.customer_name
			xy.loan_type=self.type_of_loan
			xy.id=self.loan_id
			xy.total_amount=self.total_amount
			xy.monthly_pay=self.interest
			xy.save()