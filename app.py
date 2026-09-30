from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    
    # Executed only when the user clicks the "Calculate" button

    if request.method == 'POST':
        # Get values sent from the HTML form
        val1 = request.form.get('input1')
        val2 = request.form.get('input2')
        operation = request.form.get('operation')

        try:
            # Convert values to numbers
            input1 = float(val1)
            input2 = float(val2)

            # Basic Python Calculator Logic
            if operation == '+':
                result = input1 + input2

            elif operation == '-':
                # Subtracting input2 from input1
                result = input1 - input2

            elif operation == '*':
                result = input1 * input2

            elif operation == '/':
                if input2 != 0:
                    result = input1 / input2
                else:
                    result = "Error: Cannot divide by 0"

            elif operation == '%':
                result = input1 % input2

            elif operation == '**':
                result = input1 ** input2

            else:
                result = "Invalid Operation"

        except ValueError:
            result = "Please enter valid numbers"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
