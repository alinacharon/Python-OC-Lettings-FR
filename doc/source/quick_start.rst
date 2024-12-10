Quick Start Guide
=================

**To quickly get started with OC-Lettings, follow these steps:**

1. **Clone the repository**:
   ```
   git clone https://github.com/alinacharon/Python-OC-Lettings-FR.git
   cd Python-OC-Lettings-FR
   ```

2. **Create and activate a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```
   python manage.py migrate
   ```

5. **Start the development server**:
   ```
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://localhost:8000`.

You should now see the OC-Lettings application running locally.