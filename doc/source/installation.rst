Installation
============
To install OC-Lettings, follow the steps below:

1. **Clone the repository**:

   Clone the project from the GitHub repository:
   ```bash
   git clone https://github.com/alinacharon/Python-OC-Lettings-FR.git
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**:
   Update the database:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   To start the local server:
   ```bash
   python manage.py runserver
   ```

6. **Deployment on Render**:

   OC-Lettings is deployed on the Render platform for online access. If you need to update the deployment, follow these steps: \n
   1. **Render Account**: Ensure you have an account on Render.\n
   2. **Update Service**: In your Render dashboard, navigate to your existing web service.\n
   3. **Environment Variables**: Verify that any necessary environment variables, such as `SENTRY_DSN`, are correctly set in the Render dashboard under the "Environment" section.\n
   4. **Trigger Redeploy**: If you push changes to your GitHub repository, Render will not automatically rebuild and redeploy your application. You should do it mannually.\n

7. **CI Pipeline with GitHub Actions**:

   A CI Pipeline is set up using GitHub Actions. You can find the configuration in the `.github/workflows/ci.yml` file. This pipeline includes steps for linting, testing, building, and deploying the application.

The site is currently accessible at: (https://python-oc-lettings-fr-o8k3.onrender.com).