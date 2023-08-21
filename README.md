
# LEXER - C++ Compiler

LEXER is a Flask-based web application that performs lexical analysis, syntax analysis for the C++ programming language, and expression tree generation. It helps programmers analyze and understand their C++ code by generating tokens, validating syntax, and visualizing the structure of the code through an expression tree.


## Demo
You can try out LEXER by visiting the live demo at https://lexer-87uy.onrender.com/.

## Features


- ***Lexical analysis***: Generates tokens from C++ code.
- ***Syntax analysis***: Checks if the code follows the correct syntax.
- ***Expression tree generation***: Creates an expression tree to visualize the code structure.
- ***User-friendly interface***: A simple and intuitive web interface for interacting with the compiler.

## Installation (For Devs)

To run LEXER locally, follow these steps:

1. Clone the GitHub repository:
```bash
  git clone https://github.com/sallar-ba/Lexer.git
```

2. Navigate to the project directory:
```bash
  cd Lexer
```
3. Create a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:
- For Windows:

    ```bash
    venv\Scripts\activate
    ```
- For Unix or Linux:

    ```bash
    source venv/bin/activate
    ```


5. Install the required dependencies:
```bash
pip install -r requirements.txt
```

6. Start the Flask development server:
```bash
flask run
```

7. Access LEXER by visiting http://localhost:5000 in your web browser.




## Usage


1. Open LEXER in your web browser.

2. Paste your C++ code into the provided text area.

3. Click the "Analyze" button to perform lexical and syntax analysis.

4. View the generated tokens and the syntax analysis result in the respective sections.

5. Click the "Generate Tree" button to create an expression tree based on the analyzed code.

6. Explore the expression tree visualization to understand the code structure.

7. Repeat the process with different C++ code snippets as needed.




## Authors

- [@sallar-ba](https://github.com/sallar-ba)

- [@HuzaifaIlyas02](https://github.com/HuzaifaIlyas02)

- [@ali39121](https://github.com/ali39121)
## Contributing

Contributions are welcome! If you find a bug or want to suggest an enhancement, please open an issue on the GitHub repository. You can also fork the repository, make your changes, and submit a pull request.


## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/)
.
