Deployment
==========

The deployment of the OC-Lettings application is managed through the Render platform. The CI/CD pipeline is configured to automate the build and deployment process whenever changes are pushed to the repository or a manual trigger is initiated.

### Deployment Steps

1. **Connect to Render**: Ensure your GitHub account is linked to your Render account.
2. **Create a New Web Service**: If not already created, set up a new web service in the Render dashboard.
3. **Configure Deployment Settings**:
   - Set the build command to `docker build -t alinacharon/lettings .`
   - Set the start command to `docker run alinacharon/lettings`.
4. **Set Environment Variables**: In the Render dashboard, navigate to the "Environment" section and add the necessary environment variables:
   - `SENTRY_DSN`
   - `SECRET_KEY_DJANGO`
5. **Trigger Deployment**: 
   - If you push changes to the GitHub repository, Render will automatically rebuild and redeploy the application.
   - Alternatively, you can manually trigger a deployment through the Render dashboard by selecting your service and clicking on "Deploy".

The site is currently accessible at: [https://python-oc-lettings-fr-o8k3.onrender.com](https://python-oc-lettings-fr-o8k3.onrender.com).