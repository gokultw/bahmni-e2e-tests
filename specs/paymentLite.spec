# Payment Lite
* create Login Users for paymentlite
## Doctor and medicines should be billed in paymentlite

tags: clinic, payment-lite, smoke, regression

* Login to Bahmni location "Bahmni Clinic" as a "receptionist"
* Receptionist creates the patient and starts an OPD
* Logout and Login to Bahmni location "Bahmni Clinic" as a "doctor"
* Open clinical tab
* Doctor advises medicines "consultation/medications/paracetamol,consultation/medications/Morphine,consultation/medications/Diazepam,consultation/medications/Ceftriaxone" and tests "consultation/orders/Platelets"
* Goto Bahmni main home
* put doctor first name "d3FirstName" middle name "d3MiddleName" lastname "d3LastName"
* Goto paymentlite
* Login to Payment lite as "FrontDesk"
* Create a doctor in Payment Lite with consultation fee "15000"
* Create drug with price "100"
Drug should flow from Bahmni
* Raise an invoice for patient
* Collect the payment from the patient
* Verify the payment is complete
* Logout of Payment Lite
START BAH-2151
Steps are added as workaround to avoid auto login to application. Bug - BAH-2151
* Goto paymentlite
* Logout of Payment Lite if logged in
END BAH-2151
* Login to Payment lite as "Doctor"
* Run report and validate
* Logout of Payment Lite
* Goto Clinical application
* visit is closed at the front desk
