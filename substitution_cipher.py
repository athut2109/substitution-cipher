from flask import Flask, render_template, request

app = Flask(__name__)

letters = 'abcdefghijklmnopqrstuvwxyz'
length = len(letters)

def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key
    
    for letter in text:
        letter = letter.lower()
        if letter == ' ':
            result += ' '
        else:
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= length:
                    new_index -= length
                elif new_index < 0:
                    new_index += length
                result += letters[new_index]
    if mode == 'e':
        result = result.upper()
    return result

@app.route('/', methods=['GET', 'POST'])
def home():
    error = ''
    if request.method == 'POST':
        text = request.form['text']
        mode = request.form['mode']
        try:
            key = int(request.form['key'])
            if key < 0 or key > 26:
                error = 'Key must be between 0 and 26.'
                return render_template('index.html', result='', text=text, mode=mode, key=key, error=error)
        except ValueError:
            error = 'Invalid key input.'
            return render_template('index.html', result='', text=text, mode=mode, key=0, error=error)

        result = encrypt_decrypt(text, mode, key)
        return render_template('index.html', result=result, text=text, mode=mode, key=key, error=error)
    
    return render_template('index.html', result='', error='')

if __name__ == '__main__':
    app.run(debug=True)
