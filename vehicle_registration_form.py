# Vehicle Registration Form
# This module handles vehicle registration for the transport department system

class VehicleRegistrationForm:
    def __init__(self):
        self.vehicle_number = ""
        self.vehicle_type = ""
        self.owner_name = ""
        self.registration_date = ""
    
    def register_vehicle(self, vehicle_number, vehicle_type, owner_name, registration_date):
        """Register a new vehicle in the system"""
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.owner_name = owner_name
        self.registration_date = registration_date
        return True
    
    def validate_form(self):
        """Validate the vehicle registration form"""
        if not self.vehicle_number or not self.vehicle_type:
            return False
        return True
