# The Yoga Loft

## Overview
The Yoga Loft is a web application designed to simplify yoga class scheduling and booking for students of the studio. This Django-powered website provides an intuitive, user-friendly interface where yoga enthusiasts can easily browse class schedules, create personal accounts, and seamlessly reserve spots in their preferred yoga sessions. By offering real-time booking capabilities, detailed class descriptions, and a streamlined registration process, The Yoga Loft Booking Platform eliminates traditional scheduling barriers, making it convenient for students to explore and commit to their wellness journey, which in turn improves class numbers.

## Table of Contents
1. [Overview](#overview)
2. [UX Design Process](#ux-design-process)  
   - [Link to User Stories](#link-to-user-stories)  
   - [Wireframes](#wireframes)
3. [Accessibility](#accessibility)  
4. [Design Rationale](#design-rationale)  
5. [Reasoning for Final Changes](#reasoning-for-final-changes)  
6. [Key Features](#key-features)  
   - [Implemented](#implemented)  
7. [Deployment](#deployment)  
   - [Deployment Overview](#deployment-overview)  
   - [Pre-Deployment Checklist](#pre-deployment-checklist)  
   - [Deploying to Heroku](#deploying-to-heroku)  
8. [Forking and Cloning the Repository](#forking-and-cloning-the-repository)  
   - [Fork the Project](#fork-the-project)  
   - [Clone the Project](#clone-the-project)  
9. [Local Development Setup](#local-development-setup)  
   - [Environment Variables](#environment-variables)  
   - [Database and Migrations](#database-and-migrations)  
   - [Services Used](#services-used)  
10. [Tech Stack](#tech-stack)  
11. [AI Implementation and Orchestration](#ai-implementation-and-orchestration)  
    - [Use Cases and Reflections](#use-cases-and-reflections)  
12. [Testing Summary](#testing-summary)  
    - [Manual Testing](#manual-testing)  
    - [Automated Testing](#automated-testing)  
13. [Upcoming Features](#upcoming-features)  



## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [The project's KanBan board.](https://github.com/users/MaebhNiGhuairim/projects/5)
  - I used Perplexity to brainstorm some user ideas, but I sorted through them, selected and modified the most relevant user stories for this project.
- **Wireframes:**
  - [Attach or link to accessible wireframes used in the design process, ensuring high colour contrast and alt text for visual elements.]
  - Whilst my homepage wireframe looks quite similar to the end product, the about and classes section has changed. This reflects new considerations I kept in mind as the website was developing.
  - 

### Accessibility

The Yoga Loft prioritizes simplicity, usability, and inclusivity to create a seamless experience for all users, including those with disabilities. Accessibility features are integrated throughout the design:  

1. **Navigation and User Flow**  
   - The site uses a clear, logical layout with intuitive navigation links (e.g., Home, Classes, Book a Class, My Bookings).  
   - Buttons, forms, and other interactive elements are labeled meaningfully to ensure clarity and ease of use for all users, including those relying on assistive technologies.  

2. **Responsiveness and Compatibility**  
   - Fully responsive design ensures usability across all devices, from smartphones to desktops.  
   - Semantic HTML elements (e.g., `<header>`, `<nav>`, `<main>`) enhance compatibility with screen readers and assistive technologies.  

3. **WCAG Adherence**  
   - Text and background colors are carefully chosen to meet WCAG contrast standards, ensuring readability for users with visual impairments.  
   - Keyboard accessibility ensures that all interactive elements can be navigated without a mouse.  

4. **Forms and Dynamic Features**  
   - Clear labels, placeholders, and user-friendly error messages guide users through the booking process.  
   - Dynamic dropdown menus update based on user input, simplifying navigation and reducing cognitive load.  

By implementing these features, The Yoga Loft ensures inclusivity, making the website functional and accessible for users of all abilities.  

---

### Design Rationale

The Yoga Loft’s design reflects a balance between aesthetics, functionality, and inclusivity. Below are the key design decisions:  

1. **Layout**  
   - A clean, minimal layout directs users to the site’s primary functions (browsing classes, booking, and viewing bookings) without unnecessary distractions.  

2. **Colour Scheme**  
   - A calming palette reflects the studio’s ethos:  
     - **Primary Colours**: `#AD6E56` (earthy terracotta) and `#4F6757` (forest green).  
     - **Secondary Colours**: `#9C9B8E` (grey-green) and `#E0CDC1` (soft beige).  
     - **Background/Accent Colours**: `#F4F0EB` and `#f3ece7` (light tones) for contrast and content highlighting.  
   - Colors maintain sufficient contrast to meet WCAG AA standards for accessibility.  

3. **Typography**  
   - The sans-serif font "Montserrat" provides a modern, clean appearance and high readability.  
   - Font sizes are scaled for optimal legibility across all devices, with headings prominent and body text easy to read.  

4. **Accessibility Considerations**  
   - **Screen Reader Support**: Semantic HTML and ARIA roles improve accessibility for users relying on screen readers.  
   - **Visual Impairments**: High-contrast text and scalable fonts enhance usability.  
   - **Motor Impairments**: Large, easy-to-click buttons and intuitive navigation support users with limited dexterity.  

By combining accessibility principles with thoughtful design choices, The Yoga Loft delivers a welcoming, user-friendly experience for all visitors, while reflecting the calm, serene atmosphere of a yoga studio.  



- **Reasoning For Final Changes:**
  - I removed the Join button to allow for better symmetry in the navbar, and made the "Book a class" button bigger to be a stronger call to action.
  - I moved the about section to the homepage as I wanted the homepage to be the welcome to the studio.
  - I added a "My account" section to the navbar to indicate when a user was logged in.

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
