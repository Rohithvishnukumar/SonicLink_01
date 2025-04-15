
# from flask import Flask, render_template, request, jsonify
# from assistant_engine import handle_command

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     query = data.get("query")
#     print(f"Received command: {query}")
#     response = handle_command(query)
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(debug=True)















# from flask import Flask, request, jsonify, render_template
# from assistant_engine import handle_command

# app = Flask(__name__)

# # Route for the main web page
# @app.route("/")
# def index():
#     return render_template("index.html")

# # API endpoint to process voice commands
# @app.route("/process", methods=["POST"])
# def process():
#     data = request.json
#     query = data.get("query")
#     result = handle_command(query)
#     return jsonify(result)

# if __name__ == "__main__":
#     app.run(debug=True)























# from flask import Flask, render_template, request, jsonify
# from assistant_engine import handle_command  # Make sure this is the Gemini-powered version!

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     try:
#         data = request.get_json()
#         query = data.get('query', '')
        
#         if not query:
#             return jsonify({'response': "I didn't catch that. Can you repeat?"})

#         print(f"[User Query] {query}")
#         response = handle_command(query)

#         return jsonify({'response': response})

#     except Exception as e:
#         print("Error processing request:", e)
#         return jsonify({'response': "Oops, something went wrong."})

# if __name__ == '__main__':
#     app.run(debug=True)









# from flask import Flask, render_template, request, jsonify
# from assistant_engine import handle_command

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.json
#     query = data.get("query")
#     print(f"Received command: {query}")
#     response = handle_command(query)
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(debug=True)















# from flask import Flask, request, jsonify, render_template
# from assistant_engine import handle_command

# app = Flask(__name__)

# # Route for the main web page
# @app.route("/")
# def index():
#     return render_template("index.html")

# # API endpoint to process voice commands
# @app.route("/process", methods=["POST"])
# def process():
#     data = request.json
#     query = data.get("query")
#     result = handle_command(query)
#     return jsonify(result)

# if __name__ == "__main__":
#     app.run(debug=True)























from flask import Flask, render_template, request, jsonify
from assistant_engine import handle_command  # Make sure this is the Gemini-powered version!

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        if not query:
            return jsonify({'response': "I didn't catch that. Can you repeat?"})

        print(f"[User Query] {query}")
        response = handle_command(query)

        return jsonify({'response': response})

    except Exception as e:
        print("Error processing request:", e)
        return jsonify({'response': "Oops, something went wrong."})

if __name__ == '__main__':
    app.run(debug=True)


