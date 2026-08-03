from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "replace-with-a-secure-key"

@app.route('/', methods=['GET', 'POST'])
def index():
    toss_count = session.get('toss_count', 0)
    heads_count = session.get('heads_count', 0)
    tails_count = session.get('tails_count', 0)
    last_result = session.get('last_result')
    result = last_result

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'reset':
            session['toss_count'] = 0
            session['heads_count'] = 0
            session['tails_count'] = 0
            session['last_result'] = None
            return redirect(url_for('index'))

        result = random.choice(['Heads', 'Tails'])
        toss_count += 1
        if result == 'Heads':
            heads_count += 1
        else:
            tails_count += 1

        session['toss_count'] = toss_count
        session['heads_count'] = heads_count
        session['tails_count'] = tails_count
        session['last_result'] = result

    if toss_count == 0:
        leader = 'No tosses yet'
    elif heads_count > tails_count:
        leader = 'Heads is winning'
    elif tails_count > heads_count:
        leader = 'Tails is winning'
    else:
        leader = 'It\'s a tie'

    return render_template(
        'index.html',
        result=result,
        toss_count=toss_count,
        heads_count=heads_count,
        tails_count=tails_count,
        leader=leader,
    )

if __name__ == '__main__':
    app.run(debug=True)
