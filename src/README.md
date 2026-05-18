## Installation and Local Usage

### Prerequisites
* Python 3.9 or higher.
* An OpenAI API Key (Optional: the application includes a "mock mode" if no key is detected).

### Steps to Run
1. **Clone the repository:**
   ```bash
   git clone [REPO URL]
   cd [FOLDER NAME]
   ```
2. **Set up a Virtual Environment (Recommended):**

Using a virtual environment is a best practice to ensure dependency isolation.

* For Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
* For Linux (Ubuntu/Debian):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the application with Streamlit:**
    ```bash
    streamlit run app.py
    ```

## Repository Structure
* `/src`: Application source code.
* `/docs`: Technical documentation and Sprint 1 reflections.
* `/management`: Scrum management evidence, including the Product Backlog and Sprint 1 board.
* `requirements.txt`: System dependencies file.
