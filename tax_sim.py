from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def input():
    return render_template('input.html')

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route("/requests")
# def requests():
#     return render_template('requests.html')

@app.route("/calc", methods=["post"])
def calc():
    sales = float(request.form.get('sales'))
    income = float(request.form.get('income'))
    insurance = float(request.form.get('insurance'))
    withholding_tax = float(request.form.get('withholding_tax'))
    hometown_tax = float(request.form.get('hometown_tax'))

    if income < 550000:
        income_subtraction = income
    elif 550000 <= income <= 1625000:
        income_subtraction = 550000   
    elif 1625000 < income <= 1800000:
        income_subtraction = income * 0.4  - 100000
    elif 1800000 < income <= 3600000:
        income_subtraction = income * 0.3 + 80000 
    elif 3600000 < income <= 6600000:
        income_subtraction = income * 0.2 + 440000
    elif 6600000 < income <= 8500000:
        income_subtraction = income * 0.1 + 1100000
    else:
        income_subtraction = 1950000
    
    hometown_tax_sub = hometown_tax - 2000
    income_modified = income - income_subtraction
    income_total = sales + income_modified
    subtraction =  insurance + 480000 + hometown_tax_sub
    income_for_tax = income_total - subtraction

    if income_for_tax <= 1949000:
         income_rate = 0.05
         income_rate_subtraction = 0
         income_deduction = income_for_tax * 0.05
    elif 1950000 < income_for_tax <= 3299000:
        income_rate = 0.1
        income_rate_subtraction = 97500
        income_deduction = income_for_tax * 0.1 - 97500
    elif 3299000 < income_for_tax <= 6949000:
        income_rate = 0.2
        income_rate_subtraction = 427500
        income_deduction = income_for_tax * 0.2 - 427500
    elif 6949000 < income_for_tax <= 8999000:
        income_rate = 0.23
        income_rate_subtraction = 636000
        income_deduction = income_for_tax * 0.23 - 636000
    elif 8999000 < income_for_tax <= 17999000:
        income_rate = 0.33
        income_rate_subtraction = 1536000
        income_deduction = income_for_tax * 0.33 - 1536000
    elif 17999000 < income_for_tax <= 39999000:
        income_rate = 0.4
        income_rate_subtraction = 2796000
        income_deduction = income_for_tax * 0.4 - 2796000
    else:
        income_rate = 0.5
        income_rate_subtraction = 4796000
        income_deduction = income_for_tax * 0.5 - 4796000

    tax_eq = income_deduction * 1.021
    tax = tax_eq - withholding_tax

    return render_template(
            'output.html'
            , sales = int(sales)
            , income = int(income)
            , income_total = int(income_total)
            , income_subtraction = int(income_subtraction)
            , income_for_tax = int(income_for_tax)
            , income_modified = int(income_modified)
            , hometown_tax_sub = int(hometown_tax_sub)
            , subtraction = int(subtraction)
            , insurance = int(insurance)
            , income_rate = income_rate
            , income_rate_subtraction = int(income_rate_subtraction)
            , income_deduction = int(income_deduction)
            , withholding_tax = int(withholding_tax)
            , tax_eq = int(tax_eq)
            , tax = int(tax)
        )

if __name__ == '__main__':
    app.run(debug=True)
