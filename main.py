from flask import (Flask, render_template, request, make_response)
from models.user import User
from models.invoice import Invoice
import bootstrap



app = Flask('app')
@app.route('/')
def index():
    bootstrap.initialize()
    user = User.select().where(
    User.email=="john@doe.com"
    ).get()
    invoice = Invoice.select().where(
      Invoice.user_email == user.email
    ).get()
    total = invoice.design_fee + invoice.hosting_fee + invoice.developer_fee + invoice.domain_fee
    return render_template("invoice.html", user=user, invoice=invoice, total=total)
    



if __name__== '__main__':
  app.run(host='0.0.0.0',port = 8080) 