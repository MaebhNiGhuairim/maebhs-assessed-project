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
13. [Validation](#validation)
     
14. [Upcoming Features](#upcoming-features)  



## UX Design Process
- **Link to User Stories in GitHub Projects:**
  - [The project's KanBan board.](https://github.com/users/MaebhNiGhuairim/projects/5)
  - I used Perplexity to brainstorm some user ideas, but I sorted through them, selected and modified the most relevant user stories for this project.
  - As is visible in my KanBan, some "nice to haves" were not accomplished. They would be the focus in the next iteration.
  - Whilst I did not have an integrated Class Schedule which showed classes and their descriptions, I got around this by providing a page which explains the classes offered, and shows the schedule. So it may not fulfil the acceptance criteria, but the functionality is still present in the project. I have left the "Class Descriptions" in progress - it can be improved next iteration.
- **Wireframes:**

   ![Homepage wireframe](/assets/home_wireframe.png)
   ![About wireframe](/assets/about_wireframe.png)

  - Whilst my homepage wireframe looks quite similar to the end product, the about and classes section has changed. This reflects new considerations I kept in mind as the website was developing.

### Accessibility

The Yoga Loft prioritizes simplicity, usability, and inclusivity to create a seamless experience for all users, including those with disabilities. Accessibility features are integrated throughout the design:  

1. **Navigation and User Flow**  
   - The site uses a clear, logical layout with intuitive navigation links (e.g., Home, Classes, Book a Class, My Bookings).  
   - Buttons, forms, and other interactive elements are labeled meaningfully to ensure clarity and ease of use for all users, including those relying on assistive technologies.  

2. **Responsiveness and Compatibility**  
   - Fully responsive design ensures usability across all devices, from smartphones to desktops.  
   - Semantic HTML elements (e.g., `<header>`, `<nav>`, `<main>`) enhance compatibility with screen readers and assistive technologies.
   - Hover effects are click effects on mobile

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
   - ![colour palette](/assets/yoga_studio_palette.png)
     
3. **Imagery**
   - I chose light and airy images to invoke the calm experience of being in the studio.
   - I had to darken the hero images and card images in some instances to allow text to be read over the images.

5. **Typography**  
   - The sans-serif font "Montserrat" provides a modern, clean appearance and high readability.  
   - Font sizes are scaled for optimal legibility across all devices, with headings prominent and body text easy to read.  

6. **Accessibility Considerations**  
   - **Screen Reader Support**: Semantic HTML and ARIA roles improve accessibility for users relying on screen readers.  
   - **Visual Impairments**: High-contrast text and scalable fonts enhance usability.  
   - **Motor Impairments**: Large, easy-to-click buttons and intuitive navigation support users with limited dexterity.  

7. **Responsiveness**
   - **Works well across all screen types**: I used bootstrap mainly to create a responsive site. I used Google Inspect to view my site across a multitude of devices. I was able to ensure it scaled well.
  
   - **Homepage**
     ![Homepage Image 2](/assets/homepage_desktop.png)
     ![Homepage Image 2](/assets/homepage_mobile.png)![Homepage Image 2](/assets/homepage_tablet.png)






   - **Classes**
     ![Homepage Image 2](/assets/classes_desktop.png)
     ![Homepage Image 2](/assets/classes_mobile.png)![Homepage Image 2](/assets/classes_tablet.png)

     

   - My navbar actually has 2 separate logos, each one appearance depending on the size of the screen. This ensures the logo is centered no matter the size of the screen



By combining accessibility principles with thoughtful design choices, The Yoga Loft delivers a welcoming, user-friendly experience for all visitors, while reflecting the calm, serene atmosphere of a yoga studio.  



- **Reasoning For Final Changes:**
  - I removed the Join button to allow for better symmetry in the navbar, and made the "Book a class" button bigger to be a stronger call to action.
  - I moved the about section to the homepage as I wanted the homepage to be the welcome to the studio.
  - I added a "My account" section to the navbar to indicate when a user was logged in.

## Key Features

### Navbar
The navigation bar provides easy access to the Classes page, the About section, the Contact form, My Account section and the Book a Class button. This ensures smooth user navigation throughout the application. The logo is central to the navbar, and is visible above the dropdown menu when screens are smaller. A user knows they are logged in when they can see My Account in the navbar.

### Classes Page
The Classes page is designed the welcome the user to be curious about the classes provided. It has four cards, with the names of each class over an image from the class. When you hover over the image (or click on mobile), the description of the class is revealed. Below that is the class schedule. 

### About Section
The About section provides information about the yoga studio, including its mission and reasons why a user should join. it reiterates the call to action at the bottom - book now!

### Contact Form
The Contact form allows users to get in touch with the yoga studio by submitting inquiries, feedback, or requests through a simple form interface. It provides a success message when a messsage is sent. That message is held in the messages model, and is accessable to the admin in the django admin page. 

### Book a Class
This is the main call to action on the website. If you are not logged in, the button prompts you to sign in, before being redirected to the book a class page. There you can first select the class, then the day/time and then the date. The valid dates are prepopulated so users don't accidentally book an invalid date. If you try to book a class you have already book, you will get an error message. When you successfully book a class, you are redirected to "My bookings" and you see a success message.

### Sign Up/Sign In/Logout - All Created with AllAuth
User authentication is handled by Django AllAuth, allowing users to sign up, log in, and log out securely. This feature ensures that users can manage their accounts with ease. It was minimally styled by me

### View My Account
This page allows users to log out or view their bookings.

### View My Bookings
Users can view their current and past bookings in their profile, helping them keep track of upcoming sessions.

### Edit & Delete Bookings
Users have the ability to modify or cancel their bookings directly from their profile, providing flexibility in managing their class schedule. They are warned before deleting bookings. When they edit bookings, the date of their current booking is not available to them in the drop down. If they try to book a class they have already booked, they get a message saying they've already booked a class on that day. This prevents duplicate bookings.

### Shape dividers
I used shape dividers to improve the flow of the website. I would've used it more across the site if I had more time.




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
<br>
**Backend:** Django 4.2, PostgreSQL, Python
<br>
**Tools:** Crispy Forms, Django REST Framework, WhiteNoise, Bootstrap
<br>
**External Tools:**
- [Shape Dividers](https://www.shapedivider.app/) for better flow
- Balsamiq for wireframes
- Favicon.io for favicon
- Font Awesome for icons across the site
- GitHub - Version control and repo storage
- Google Fonts



## AI Implementation and Orchestration

### Use Cases and Reflections:

- **Code Creation:**  
  - **Reflection:** AI tools were instrumental in accelerating development by generating initial drafts for core features, such as the basic homepage and basic CSS. Minor adjustments ensured the outputs aligned with project requirements and best practices.  
  - **Examples:** Prompts were used to create basic templates for each webpage, after which I could inspect and check the code, and make whichever changes were necessary.  

- **Debugging:**  
  - **Reflection:** AI-assisted debugging resolved issues in form validation and database queries. By simplifying complex logic and refining error-handling mechanisms, the codebase became more maintainable and user-friendly.  
  - **Examples:** Logical errors in the date-picker and dynamic menu updates were quickly identified and addressed using targeted prompts.  

- **Performance and UX Optimisation:**  
  - **Reflection:** AI-driven suggestions enhanced the website's responsiveness and accessibility. Minimal manual adjustments were required to implement optimisations, resulting in faster load times and a smoother user experience.  
  - **Examples:** Adjustments were made to improve the performance of the dropdown system and ensure seamless navigation for keyboard and screen reader users.  

- **Automated Unit Testing:**  
  - **Reflection:** 
    Implementing automated unit testing using AI tools has significantly improved the efficiency and coverage of our testing process. The AI-generated test cases have helped identify edge cases and potential issues that might have been overlooked during manual testing. However, it was necessary to manually review and adjust some of the AI-generated tests to ensure they accurately reflected the application's functionality and requirements. Overall, the integration of AI in our testing workflow has enhanced the robustness and reliability of our application.

  - **Examples:** 
    Here are some examples of AI-generated unit tests that were implemented and adjusted for our application:

    - **Bookings App:**
      - Tests for creating, updating, and deleting bookings.
      - Tests to ensure that duplicate bookings are not allowed.

    - **Contact App:**
      - Tests for submitting the contact form.
      - Tests to ensure that all required fields are validated.

- **READMe documentation:**
   - **Reflection:** I was able to give ChatGPT my main points for each section, and it was able to write what was needed, which freed me to focus on testing. It also helped with writing everything in Markdown.
   - **Examples** I told AI how I used it in order to create this project, and it was able to write this section for me (except this part!)

### Overall Impact:
- AI tools significantly reduced time spent on repetitive tasks, enabling more focus on refining user experience and accessibility.
- Efficiency gains included streamlined debugging, comprehensive test coverage, and improved code maintainability.
- AI improved my understanding of building a website, as I asked it to explain its reasoning often.
- However, AI is not infallible. Often times, they do not scan the right files, or place the wrong urls in, as an example. It's important to know that you must rely on your own ability to code first

## Testing Summary

- **Manual Testing:**
  - **Devices and Browsers Tested:** 
    - Devices: Desktop (Windows, macOS), Mobile (iOS, Android)
    - Browsers: Chrome, Firefox, Safari, Edge
  - **Features Tested:** 
    - CRUD operations for bookings
    - Navigation across different pages
    - Form submissions and validations
    - Accessibility checks (ARIA roles, keyboard navigation, screen reader compatibility)
  - **Results:**
      - *Duplicate Bookings*
      - This was a major bug in my code for a very long time. I couldn't quite get the logic to work. Once I had the Make A Booking working, it would stop the Edit a Booking functionality, and vice versa. I used AI to debug my logic and in doing so, I was able to stop duplicate bookings. I then used unit testing to ensure dupkicate bookings could not occur. 
    - All critical features now work as expected, including accessibility checks.
    - No major issues found during manual testing.
    ![Contact Tests](/assets/tests_contact.png)
    ![Home Tests](/assets/tests_home.png)
    ![Booking Tests](/assets/tests_bookings.png)
    ![General Tests](/assets/tests_general.png)
  
- **Automated Testing:**
  - **Tools Used:** 
    - Django TestCase
  - **Features Covered:** 
    - Model validations
    - View responses and redirects
    - Form submissions and error handling
    - URL routing and access control
  - **Adjustments Made:** 
    - Manual corrections to AI-generated test cases to ensure proper coverage and accuracy, particularly for accessibility.

All tests passed successfully, ensuring the robustness and reliability of the application.
 
## Validation

As part of ensuring the quality, accessibility, and performance of this project, I conducted several validation checks on the codebase using industry-standard tools. Below are the results and tools used:

### 1. HTML Validation
- **Tool**: [W3C Markup Validation Service](https://validator.w3.org/)
- The HTML for this project was validated using the W3C Markup Validation Service to ensure proper syntax and structure.
- **Result**: The HTML passed validation successfully.
- ![HTML Validation Results](/assets/html_validation.png)

### 2. CSS Validation
- **Tool**: [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- The CSS was validated using the W3C CSS Validation Service to check for errors and adherence to standards.
- **Result**: The CSS passed validation without any issues.
- ![CSS Validation Results](/assets/css_validation.png)

### 3. JavaScript Validation
- **Tool**: [JSHint](https://jshint.com/)
- The JavaScript code was validated using JSHint to ensure clean and error-free scripting.
- **Result**: No major issues were found in the JavaScript. I had a number of ES6 warnings. These warnings can be ignored because they relate to ES6 features (const, arrow functions, template literals, etc.), which are fully supported by modern browsers. As this project targets modern environments, ES6 is safe and improves code readability and maintainability.
- ![JavaScript Validation Results](/assets/javascript_validator.png)

### 4. Contrast and Accessibility
- **Tool**: [WAVE Contrast Checker](https://wave.webaim.org/)
- The site’s accessibility and contrast ratios were checked using the WAVE tool to ensure compliance with WCAG standards.
- **Result**: Whilst my results were mostly good, I did have some contrast errors that related to my book a class button, and the text at the bottom of my homepage. If I gave myself a little more time, I would've made the text at the bottom of the homepage larger, and darkened the book a class button.
- ![WAVE Contrast Checker Results](/assets/contrast_checker.png)

### 5. Performance and Accessibility Audit
- **Tool**: [Google Lighthouse](https://developers.google.com/web/tools/lighthouse)
- The project underwent a Lighthouse audit for performance, accessibility, and best practices.
- **Result**:
  - **Desktop**: Achieved excellent results across all metrics. My accessibiility could've been improved with changing the colour of the book a class button.
  - **Mobile**: Scored **89** for performance due to image formatting issues.
  - If I had more time, I would reformat the images, and delete unusued css to optimize performance further.
- ![Lighthouse Desktop Results](/assets/desktop_lighthouse.png)
- ![Lighthouse Mobile Results](/assets/mobile_lighthouse.png)

### 6. Python Validation
 - **Tool:** [CI Python Linter](https://pep8ci.herokuapp.com/)
 - I checked the setting.py, and the models and urls across my project. This helped me formulate them according to Python best practices.
 - ![Bookings/Urls/py passed](/assets/bookings_urls_python_validator.png)
 - ![Settings passed](/assets/settings_python_validator.png)

### Future Features
- Class waitlist system
- Instructor dashboard
- Integrated payment processing


## Credits

- **Code Institute Learning Materials**: The learning materials from Code Institute provided the foundational knowledge for this project.
- **AI Assistance**: Tools like CodePilot and ChatGPT were used to help generate templates, styling, and assist with testing.
- **Stock Images**: Images used in the project were sourced from [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/).
- **Django**: Django was used as the web framework for building the project.
- **Bootstrap** Bootstrap was used for cards, forms, navbars and responsibility, amongst other features

---

## Thanks

- **The Code Institute Team**: A huge thank you to Dillon, Mark, John, Roo, and the entire team at Code Institute for their guidance and support throughout the development of this project.
- **Personal Support**: Thanks to Amanda, Ger, Joanna, and Maja for their massive support, and to the entire Code Institute cohort for fostering a collaborative learning environment.

