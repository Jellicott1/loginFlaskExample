# Python Flask Login Example

This is a demo project for setting up a minimal python server running flask to manage logging in to a website.

To get this working on your computer you will need the following:

- Python installed
- Pip package manager (usually comes with python)
- (optional) setup a python venv in your project folder with `python -m venv env`

## Setup Steps

1. Create a folder for the project and download/copy all of the files in this repository into the foler. Alternatively, if you have git installed you can clone the repository following GitHub's project cloning instructions.
1. Install flask AND flask_cors using pip (you can use requirements.txt` instead).

```bash
pip install flask
pip install flask_cors
```

OR

```bash
pip install requirements.txt
```

3. run the python server from the command line.

```bash
python server.py
```

4. Open the `index.html` file using either VSCode live server or by opening the file from your documents.
1. Try to login.

## Editting the code

To update the code to suit your purposes, the important parts are as follows:

In `server.py`:

```python
# Validate credentials
    if data['username'] == "test" and data['password'] == "1234":
        return jsonify({"status": "success", "message": "Welcome!"}), 200
    else:
        return jsonify({"status": "invalid", "message": "Incorrect credentials"}), 401
```

You can change `"test"` and `"1234"` to whatever you want the username and password to be. Alternatively you can replace this logic entirely if you want to check for a list of possible usernames and password. You will just have to make sure you return:

```python
return jsonify({ status: "success", message: "Welcome!" }), 200
```

If valid login details are found, and:

```python
return jsonify({ status: "invalid", message: "Incorrect credentials" }), 401
```

if invalid if they are invalid.
