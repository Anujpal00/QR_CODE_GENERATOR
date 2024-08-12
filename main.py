import qrcode

# Taking upi id as a input
upi_id =  input("Enter you upi id : ")

#upi://pay?pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment url
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
fam_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#Create Qr codes foe each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
fam_pay_qr = qrcode.make(google_pay_url)


#Save the Qr code to image file
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
fam_pay_qr.save('google_pay_qr.png')

#Display th Qr Codes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
fam_pay_qr.show()