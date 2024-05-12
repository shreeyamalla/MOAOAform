from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        company_name = request.form['company_name']
        office_address = request.form['office_address']
        company_objectives = request.form['company_objectives']
        liability_members = request.form['liability_members']
        share_capital = request.form['share_capital']
        association_clause = request.form['association_clause']
        subscription_clause = request.form['subscription_clause']
        witness_clause = request.form['witness_clause']
        today_date = request.form['today_date']
        return render_template('result.html', company_name=company_name, office_address=office_address, company_objectives=company_objectives, liability_members=liability_members, share_capital=share_capital, association_clause=association_clause, subscription_clause=subscription_clause, witness_clause=witness_clause, today_date=today_date)


if __name__ == '__main__':
    app.run(debug=True)
