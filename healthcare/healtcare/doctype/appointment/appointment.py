# -*- coding: utf-8 -*-
# Copyright (c) 2015, Vishal Dhayagude and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Appointment(Document):
    def validate(self):
        appointment_booked = frappe.db.get_value("Appointment",
            {
                "doctor": self.doctor,
                "appointment_date": self.appointment_date,
                "appointment_time": self.appointment_time,
                "name": ["!=", self.name]
                })
        if appointment_booked:
            frappe.throw(_("Another Appointment avialble for same time "))
