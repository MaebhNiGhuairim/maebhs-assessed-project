# The Yoga Loft

## Overview
The Yoga Loft is a web application designed to simplify yoga class scheduling and booking for students of the studio. This Django-powered website provides an intuitive, user-friendly interface where yoga enthusiasts can easily browse class schedules, create personal accounts, and seamlessly reserve spots in their preferred yoga sessions. By offering real-time booking capabilities, detailed class descriptions, and a streamlined registration process, The Yoga Loft Booking Platform eliminates traditional scheduling barriers, making it convenient for students to explore and commit to their wellness journey, which in turn improves class numbers.

## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [The project's KanBan board.](https://github.com/users/MaebhNiGhuairim/projects/5)
  - I used Perplexity to brainstorm some user ideas, but I sorted through them, selected and modified the most relevant user stories for this project.
- **Wireframes:**
  - [Attach or link to accessible wireframes used in the design process, ensuring high colour contrast and alt text for visual elements.]
  - [Explain the rationale behind the layout and design choices, focusing on usability and accessibility for all users, including those using assistive technologies.]
- **Design Rationale:**
  - [Explain key design decisions, such as layout, colour scheme, typography, and how accessibility guidelines (e.g., WCAG) were integrated.]
  - [Highlight any considerations made for users with disabilities, such as screen reader support.]
- **Reasoning For Any Final Changes:**
  - [Summarise significant changes made to the design during development and the reasons behind them.]
  - [Reflect on how these changes enhance inclusivity and accessibility.]

## Key Features
### Implemented
- 🧘 Dynamic class scheduling with 4-week rolling dates
- 📅 Intelligent date picker (auto-excludes past dates)
- 🔐 Django-Allauth authentication with email verification
- ♿ Accessible modal system for booking management
- 📱 Mobile-optimized responsive layout
- **Inclusivity Notes:** 
  - [Mention how the features address the needs of diverse users, including those with SEND.]

# Deployment  

## Deployment Overview  
The application was developed using **Visual Studio Code** as the integrated development environment (IDE). **GitHub** served as the version control system, and the project was deployed to **Heroku** via the connected repository.  

---

## Pre-Deployment Checklist  
Ensure the following are configured before deployment:  

1. **Requirements File**  
   - Keep `requirements.txt` updated with all dependencies using:  
     ```bash  
     pip3 freeze --local > requirements.txt  
     ```  

2. **Procfile**  
   - Include a Procfile to configure Heroku to use Gunicorn:  
     ```bash  
     web: gunicorn [your_project_name].wsgi  
     ```  

3. **Allowed Hosts**  
   - Update `ALLOWED_HOSTS` in `settings.py`:  
     ```python  
     ALLOWED_HOSTS = ['herokuapp.com', 'localhost']  
     ```  

4. **Environment Variables**  
   - Store sensitive data (e.g., `DATABASE_URL`, `CLOUDINARY_URL`, `SECRET_KEY`) in `.env` and add it to `.gitignore`.  
   - Add these variables to Heroku’s **Config Vars** in the app settings.  

---

## Deploying to Heroku  
Follow these steps to deploy the project:  

1. **Create a Heroku App**  
   - Log in to Heroku and click **Create New App**.  
   - Choose a unique name and select your region.  

2. **Connect to GitHub**  
   - In the **Deploy** tab, link your GitHub repository.  

3. **Set Config Vars**  
   - Add environment variables in Heroku’s **Config Vars**:  
     ```plaintext  
     CLOUDINARY_URL: your_cloudinary_api_key  
     DATABASE_URL: your_postgres_url  
     SECRET_KEY: your_secret_key  
     DISABLE_COLLECTSTATIC: 1  # Remove after final deployment  
     ```  

4. **Deploy the Branch**  
   - Select the main branch and click **Deploy Branch**.  
   - After deployment, click **View** to access the live site.  

**Live Link**: [Zen Yoga Studio](https://your-yoga-app.herokuapp.com/) 
*###* 

---

## Forking and Cloning the Repository  

### Fork the Project  
1. Navigate to the GitHub repository.  
2. Click **Fork** (top-right) to create a copy in your GitHub account.  

### Clone the Project  
1. On the repository page, click **Code** and copy the HTTPS/SSH URL.  
2. In your terminal, run:  
   ```bash  
   git clone https://github.com/your-username/yoga-studio.git
   ```
3. Install dependencies:
   pip3 install -r requirements.txt


## Local Development Setup
### Environment Variables
1. Create an env.py file in the root directory:
   ```
    import os  
    os.environ["DATABASE_URL"] = "your_postgres_url"  
    os.environ["CLOUDINARY_URL"] = "your_cloudinary_api_key"  
    os.environ["SECRET_KEY"] = "your_secret_key"  
    os.environ["DEBUG"] = "True"  # For local development only
   ```

3. Add env.py to .gitignore.
   
### Database and Migrations
1. Apply migrations
    ```
    python3 manage.py migrate
    ```
2. Create a superuser:
   ```
   python3 manage.py createsuperuser
   ```
### Services Used
1. PostgreSQL Database
2. Cloudinary

### Key Notes
1. Debug Mode - this should always be disabled in production:
   ```bash  
   DEBUG = False
   ```
3. Static Files:
   
   Remove DISABLE_COLLECTSTATIC from Heroku Config Vars after final deployment
5. Use gitignore to protect sensitive data like the secret key.
   
   For more details, refer to the [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/).



## Tech Stack
**Frontend:** HTML5, CSS3, JavaScript  
**Backend:** Django 4.2, PostgreSQL  
**Tools:** Crispy Forms, Django REST Framework, WhiteNoise 

## AI Implementation and Orchestration

### Use Cases and Reflections:
(Highlight how prompts, such as reverse, question-and-answer or multi-step, were used to support learners with SEND or ALN where relevant.)

  - **Code Creation:** 
    - Reflection: Strategic use of AI allowed for rapid prototyping, with minor adjustments for alignment with project goals. 
    - Examples: Reverse prompts for alternative code solutions and question-answer prompts for resolving specific challenges.
  - **Debugging:** 
    - Reflection: Key interventions included resolving logic errors and enhancing maintainability, with a focus on simplifying complex logic to make it accessible.
  - **Performance and UX Optimization:** 
    - Reflection: Minimal manual adjustments were needed to apply AI-driven improvements, which enhanced application speed and user experience for all users.
  - **Automated Unit Testing:**
    - Reflection: Adjustments were made to improve test coverage and ensure alignment with functionality. Prompts were used to generate inclusive test cases that considered edge cases for accessibility.

- **Overall Impact:**
  - AI tools streamlined repetitive tasks, enabling focus on high-level development.
  - Efficiency gains included faster debugging, comprehensive testing, and improved code quality.
  - Challenges included contextual adjustments to AI-generated outputs, which were resolved effectively, enhancing inclusivity.

## Testing Summary
- **Manual Testing:**
  - **Devices and Browsers Tested:** [List devices and browsers, ensuring testing was conducted with assistive technologies such as screen readers or keyboard-only navigation.]
  - **Features Tested:** [Summarise features tested manually, e.g., CRUD operations, navigation.]
  - **Results:** [Summarise testing results, e.g., "All critical features worked as expected, including accessibility checks."]
- **Automated Testing:**
  - Tools Used: [Mention any testing frameworks or tools, e.g., Django TestCase.]
  - Features Covered: [Briefly list features covered by automated tests.]
  - Adjustments Made: [Describe any manual corrections to AI-generated test cases, particularly for accessibility.]

### Upcoming
- Class waitlist system
- Instructor dashboard
- Integrated payment processing
