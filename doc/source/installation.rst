Installation
============
To install OC-Lettings, follow the steps below:

1. **Clone the repository**:

   Clone the project from the GitHub repository:
   ```
   git clone https://github.com/alinacharon/Python-OC-Lettings-FR.git
   ```

2. **Create a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Configure the database**:
   Update the database:
   ```
   python manage.py migrate
   ```

5. **Start the development server**:
   To start the local server:
   ```
   python manage.py runserver
   ```

**Quick Start Guide**

After setting up the project, you can access the application by navigating to `http://localhost:8000` in your web browser. You can log in using the admin credentials provided in the documentation.

**Deployment and Application Management**

OC-Lettings is deployed on the Render platform for online access. If you need to update the deployment, follow these steps: 
1. **Render Account**: Ensure you have an account on Render.
2. **Update Service**: In your Render dashboard, navigate to your existing web service.
3. **Environment Variables**: Verify that any necessary environment variables, such as `SENTRY_DSN`, are correctly set in the Render dashboard under the "Environment" section.
4. **Trigger Redeploy**: If you push changes to your GitHub repository, Render will not automatically rebuild and redeploy your application. You should do it manually.

The site is currently accessible at: [https://python-oc-lettings-fr-o8k3.onrender.com](https://python-oc-lettings-fr-o8k3.onrender.com).