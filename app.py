# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import secrets
from utils.ranking import generate_pairs, rank_items

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Needed for session management

MAX_ITEMS = 15
MIN_ITEMS = 3 # Adjusted from 5 to 3 for easier testing, you can set it back to 5.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        items_input = request.form.get('items')
        if not items_input:
            return render_template('index.html', error="Please enter some items.")

        items_list = [item.strip() for item in items_input.split('\n') if item.strip()]
        
        # Remove duplicates while preserving order for initial input
        unique_items = []
        seen = set()
        for item in items_list:
            if item not in seen:
                unique_items.append(item)
                seen.add(item)
        
        if len(unique_items) < MIN_ITEMS or len(unique_items) > MAX_ITEMS:
            return render_template('index.html', error=f"Please enter between {MIN_ITEMS} and {MAX_ITEMS} unique items.", current_items_text="\n".join(unique_items))

        session['items'] = unique_items
        session['pairs'] = generate_pairs(unique_items)
        session['current_pair_index'] = 0
        session['preferences'] = {item: {'wins': 0, 'losses': 0} for item in unique_items}
        
        if not session['pairs']:
            return render_template('index.html', error="Not enough items to form pairs for comparison.", current_items_text="\n".join(unique_items))
            
        return redirect(url_for('compare'))

    # Clear session on GET request to '/' if user is restarting
    # Or keep data if they are just navigating back
    # For simplicity, a "Restart" button on results page will explicitly clear
    current_items_text = ""
    if 'items' in session:
        current_items_text = "\n".join(session.get('items', []))

    return render_template('index.html', current_items_text=current_items_text)

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if 'pairs' not in session or not session['pairs']:
        return redirect(url_for('index'))

    current_pair_index = session.get('current_pair_index', 0)
    pairs = session.get('pairs', [])

    if current_pair_index >= len(pairs):
        return redirect(url_for('result'))

    if request.method == 'POST':
        winner = request.form.get('winner')
        item1, item2 = pairs[current_pair_index]

        if winner not in [item1, item2]:
            # Should not happen with proper form
            return "Invalid choice.", 400

        preferences = session.get('preferences', {})
        
        loser = item2 if winner == item1 else item1

        preferences[winner]['wins'] = preferences[winner].get('wins', 0) + 1
        preferences[loser]['losses'] = preferences[loser].get('losses', 0) + 1
        
        session['preferences'] = preferences
        session['current_pair_index'] = current_pair_index + 1
        
        # Check if it was the last comparison
        if session['current_pair_index'] >= len(pairs):
            return redirect(url_for('result'))
        return redirect(url_for('compare')) # Redirect to GET to show next pair

    # GET request
    if current_pair_index < len(pairs):
        item1, item2 = pairs[current_pair_index]
        progress = int(((current_pair_index) / len(pairs)) * 100)
        return render_template('compare.html', item1=item1, item2=item2, current_pair_num=current_pair_index + 1, total_pairs=len(pairs), progress=progress)
    else:
        return redirect(url_for('result'))

@app.route('/result')
def result():
    if 'preferences' not in session:
        return redirect(url_for('index'))

    preferences = session.get('preferences', {})
    ranked_list = rank_items(preferences)
    
    # For display purposes, include win/loss counts
    results_with_details = []
    for item_name in ranked_list:
        details = preferences.get(item_name, {'wins': 0, 'losses': 0})
        results_with_details.append({
            'name': item_name,
            'wins': details['wins'],
            'losses': details['losses']
        })

    return render_template('result.html', ranked_items=results_with_details)

@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)