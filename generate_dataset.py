import pandas as pd
import random
import faker

# Initialize Faker to generate random data
fake = faker.Faker()

# List of 100 job roles
job_roles = [
    "Software Engineer", "Data Scientist", "Data Analyst", "Machine Learning Engineer", "Full Stack Developer",
    "Backend Developer", "Frontend Developer", "Product Manager", "UX/UI Designer", "Web Developer", 
    "Cloud Engineer", "DevOps Engineer", "Mobile App Developer", "QA Engineer", "HR Manager", "Business Analyst",
    "Marketing Manager", "Graphic Designer", "Sales Manager", "Project Manager", "Systems Administrator",
    "IT Support Specialist", "Network Engineer", "Database Administrator", "Artificial Intelligence Engineer",
    "Cybersecurity Analyst", "SEO Specialist", "Content Writer", "Digital Marketing Specialist", "E-commerce Manager",
    "Financial Analyst", "Accountant", "Social Media Manager", "SEO Manager", "Web Designer", "Research Scientist",
    "Blockchain Developer", "Cloud Architect", "Game Developer", "Embedded Systems Engineer", "Cloud Support Engineer",
    "Video Game Tester", "Cloud Consultant", "Salesforce Developer", "Machine Learning Researcher", "Technical Writer",
    "Marketing Analyst", "Data Engineer", "IT Project Manager", "Product Designer", "Brand Manager", "Technical Support Engineer",
    "Public Relations Specialist", "IT Consultant", "Supply Chain Manager", "Video Editor", "Business Intelligence Analyst",
    "Virtual Assistant", "HR Coordinator", "Customer Service Representative", "Research Analyst", "Creative Director",
    "Account Manager", "Event Coordinator", "Legal Assistant", "Security Consultant", "Web Content Manager", "Database Developer",
    "Financial Planner", "Medical Researcher", "Cloud Data Architect", "Marketing Executive", "Account Executive",
    "HR Specialist", "IT Specialist", "Network Administrator", "Java Developer", "React Developer", "Salesforce Administrator",
    "Data Visualization Specialist", "Mobile App Designer", "Artificial Intelligence Researcher", "Technical Product Manager",
    "Network Architect", "Cloud Operations Engineer", "SAP Consultant", "Security Engineer", "Game Tester", "Marketing Coordinator",
    "Operations Manager", "Compliance Analyst", "Legal Consultant", "Financial Controller", "Tax Specialist", "Advertising Executive",
    "Media Planner", "Systems Engineer", "Cloud Software Engineer", "Product Marketing Manager", "Content Marketing Specialist"
]

# Function to generate random resume text based on job role
def generate_resume_text(job_role):
    resume_text = fake.text(max_nb_chars=600)
    
    # Add job role specific text to the resume
    if job_role == "Software Engineer":
        resume_text += "\n\nProficient in Java, Python, C++, and experience in developing scalable web applications."
    elif job_role == "Data Scientist":
        resume_text += "\n\nExperience with machine learning algorithms, data visualization, and data wrangling."
    elif job_role == "Data Analyst":
        resume_text += "\n\nProficient in SQL, Python, and data cleaning techniques for analyzing large datasets."
    elif job_role == "Machine Learning Engineer":
        resume_text += "\n\nExperience in designing, implementing, and deploying machine learning models."
    elif job_role == "Full Stack Developer":
        resume_text += "\n\nProficient in both front-end (HTML, CSS, JavaScript) and back-end technologies (Node.js, Python)."
    elif job_role == "Backend Developer":
        resume_text += "\n\nStrong knowledge of server-side languages like Python, Ruby, and PHP for developing scalable applications."
    elif job_role == "Frontend Developer":
        resume_text += "\n\nSkilled in HTML5, CSS3, JavaScript, React, and Vue.js for creating interactive websites."
    elif job_role == "Product Manager":
        resume_text += "\n\nExperienced in managing product lifecycles, from concept to market launch."
    elif job_role == "UX/UI Designer":
        resume_text += "\n\nExpert in wireframing, prototyping, and conducting usability testing for user-friendly interfaces."
    elif job_role == "Web Developer":
        resume_text += "\n\nExperienced in HTML, CSS, JavaScript, and modern frameworks like React and Angular."
    elif job_role == "Cloud Engineer":
        resume_text += "\n\nProficient in cloud platforms like AWS, Google Cloud, and Azure for deploying and maintaining cloud services."
    elif job_role == "DevOps Engineer":
        resume_text += "\n\nSkilled in continuous integration/continuous deployment (CI/CD) practices, Jenkins, and Docker."
    elif job_role == "Mobile App Developer":
        resume_text += "\n\nExperienced in developing mobile applications for Android and iOS using Kotlin and Swift."
    elif job_role == "QA Engineer":
        resume_text += "\n\nExperienced in manual and automated testing for identifying software defects and ensuring quality."
    elif job_role == "HR Manager":
        resume_text += "\n\nExperienced in talent acquisition, employee relations, and implementing HR policies."
    elif job_role == "Business Analyst":
        resume_text += "\n\nSkilled in gathering business requirements and conducting data analysis to improve operational efficiency."
    elif job_role == "Marketing Manager":
        resume_text += "\n\nExperienced in developing marketing strategies, leading campaigns, and analyzing consumer behavior."
    elif job_role == "Graphic Designer":
        resume_text += "\n\nProficient in Adobe Creative Suite, creating visually appealing designs for various media platforms."
    elif job_role == "Sales Manager":
        resume_text += "\n\nExperienced in leading sales teams, managing key accounts, and achieving revenue targets."
    elif job_role == "Project Manager":
        resume_text += "\n\nSkilled in managing cross-functional teams and overseeing project execution from start to finish."
    elif job_role == "Systems Administrator":
        resume_text += "\n\nExperienced in managing network infrastructure, performing backups, and troubleshooting server issues."
    elif job_role == "IT Support Specialist":
        resume_text += "\n\nProficient in troubleshooting hardware and software issues, providing technical support to end users."
    elif job_role == "Network Engineer":
        resume_text += "\n\nExperienced in designing, implementing, and maintaining network infrastructure for enterprise systems."
    elif job_role == "Database Administrator":
        resume_text += "\n\nProficient in database management, including backup, recovery, and performance tuning for SQL databases."
    elif job_role == "Artificial Intelligence Engineer":
        resume_text += "\n\nExperienced in developing AI-based applications, including chatbots, image recognition systems, and recommendation engines."
    elif job_role == "Cybersecurity Analyst":
        resume_text += "\n\nSkilled in implementing security measures to protect networks, systems, and data from cyber threats."
    elif job_role == "SEO Specialist":
        resume_text += "\n\nProficient in search engine optimization techniques to improve website rankings and drive organic traffic."
    elif job_role == "Content Writer":
        resume_text += "\n\nExperienced in writing engaging blog posts, articles, and web content on various topics."
    elif job_role == "Digital Marketing Specialist":
        resume_text += "\n\nSkilled in digital marketing strategies, including SEO, PPC, email marketing, and social media campaigns."
    elif job_role == "E-commerce Manager":
        resume_text += "\n\nExperienced in managing online stores, optimizing product listings, and developing marketing strategies for e-commerce growth."
    elif job_role == "Financial Analyst":
        resume_text += "\n\nProficient in analyzing financial data, preparing reports, and providing insights for investment decisions."
    elif job_role == "Accountant":
        resume_text += "\n\nSkilled in bookkeeping, preparing financial statements, and managing tax filings for small to medium-sized businesses."
    elif job_role == "Social Media Manager":
        resume_text += "\n\nExperienced in creating and executing social media campaigns to engage with audiences and drive brand awareness."
    elif job_role == "SEO Manager":
        resume_text += "\n\nProficient in managing SEO campaigns, conducting keyword research, and optimizing website content for search engines."
    elif job_role == "Web Designer":
        resume_text += "\n\nSkilled in designing visually appealing websites with a focus on usability and user experience."
    elif job_role == "Research Scientist":
        resume_text += "\n\nExperienced in conducting scientific experiments and publishing research findings in peer-reviewed journals."
    elif job_role == "Blockchain Developer":
        resume_text += "\n\nProficient in developing blockchain applications, smart contracts, and cryptocurrency platforms."
    elif job_role == "Cloud Architect":
        resume_text += "\n\nSkilled in designing scalable and secure cloud infrastructures using AWS, Azure, or Google Cloud."
    elif job_role == "Game Developer":
        resume_text += "\n\nExperienced in developing video games using Unity and Unreal Engine with a focus on gameplay mechanics."
    elif job_role == "Embedded Systems Engineer":
        resume_text += "\n\nProficient in developing embedded systems, including programming microcontrollers and working with hardware interfaces."
    elif job_role == "Cloud Support Engineer":
        resume_text += "\n\nSkilled in troubleshooting cloud infrastructure issues and providing technical support to clients."
    elif job_role == "Video Game Tester":
        resume_text += "\n\nExperienced in testing video games to identify bugs and ensure functionality across different platforms."
    elif job_role == "Cloud Consultant":
        resume_text += "\n\nExperienced in providing expert guidance on cloud migration, architecture, and security best practices."
    elif job_role == "Salesforce Developer":
        resume_text += "\n\nSkilled in developing custom Salesforce applications, integrating with third-party systems, and optimizing workflows."
    elif job_role == "Machine Learning Researcher":
        resume_text += "\n\nProficient in conducting research and developing new machine learning algorithms for innovative applications."
    elif job_role == "Technical Writer":
        resume_text += "\n\nExperienced in creating clear and concise technical documentation for software products and systems."
    elif job_role == "Marketing Analyst":
        resume_text += "\n\nSkilled in analyzing market trends, customer behavior, and competitive landscapes to inform business strategy."
    elif job_role == "Data Engineer":
        resume_text += "\n\nProficient in building and maintaining data pipelines, performing ETL processes, and ensuring data quality."
    elif job_role == "IT Project Manager":
        resume_text += "\n\nExperienced in managing IT projects, ensuring timely delivery, and overseeing all phases of project lifecycle."
    elif job_role == "Product Designer":
        resume_text += "\n\nProficient in designing product concepts, conducting user research, and creating prototypes for new product ideas."
    elif job_role == "Brand Manager":
        resume_text += "\n\nSkilled in developing and maintaining brand identities, as well as managing brand campaigns across multiple channels."
    elif job_role == "Technical Support Engineer":
        resume_text += "\n\nProficient in providing technical support for hardware and software issues, including remote troubleshooting."
    elif job_role == "Public Relations Specialist":
        resume_text += "\n\nExperienced in managing media relations, developing PR campaigns, and handling crisis communications."
    elif job_role == "IT Consultant":
        resume_text += "\n\nSkilled in advising organizations on IT infrastructure, software solutions, and digital transformation."
    elif job_role == "Supply Chain Manager":
        resume_text += "\n\nExperienced in managing supply chains, optimizing logistics, and ensuring timely delivery of products."
    elif job_role == "Video Editor":
        resume_text += "\n\nSkilled in editing video footage, adding special effects, and creating engaging content for social media and commercials."
    elif job_role == "Business Intelligence Analyst":
        resume_text += "\n\nExperienced in using BI tools to analyze data and create actionable insights for business decision-making."
    elif job_role == "Virtual Assistant":
        resume_text += "\n\nProficient in managing administrative tasks, scheduling appointments, and providing support to executives."
    elif job_role == "HR Coordinator":
        resume_text += "\n\nSkilled in supporting HR functions such as recruitment, onboarding, and maintaining employee records."
    elif job_role == "Customer Service Representative":
        resume_text += "\n\nExperienced in assisting customers with inquiries, troubleshooting issues, and providing excellent service."
    elif job_role == "Research Analyst":
        resume_text += "\n\nSkilled in conducting research, analyzing data, and preparing detailed reports to support decision-making."
    elif job_role == "Creative Director":
        resume_text += "\n\nExperienced in leading creative teams, conceptualizing visual campaigns, and overseeing content production."
    elif job_role == "Account Manager":
        resume_text += "\n\nSkilled in managing client relationships, developing strategies to meet client needs, and ensuring customer satisfaction."
    elif job_role == "Event Coordinator":
        resume_text += "\n\nProficient in planning and executing events, including managing logistics, vendors, and budgets."
    elif job_role == "Legal Assistant":
        resume_text += "\n\nExperienced in supporting legal teams by researching case law, preparing documents, and managing schedules."
    elif job_role == "Security Consultant":
        resume_text += "\n\nSkilled in assessing security risks, developing strategies to protect assets, and ensuring compliance with regulations."
    elif job_role == "Web Content Manager":
        resume_text += "\n\nExperienced in creating, curating, and managing content for websites and digital platforms."
    elif job_role == "Database Developer":
        resume_text += "\n\nProficient in developing and maintaining databases, writing SQL queries, and optimizing database performance."
    elif job_role == "Financial Planner":
        resume_text += "\n\nSkilled in advising clients on financial planning, including investments, retirement, and estate planning."
    elif job_role == "Medical Researcher":
        resume_text += "\n\nExperienced in conducting clinical research, analyzing data, and publishing findings in scientific journals."
    elif job_role == "Cloud Data Architect":
        resume_text += "\n\nProficient in designing cloud-based data architectures, optimizing data storage, and ensuring data integrity."
    elif job_role == "Marketing Executive":
        resume_text += "\n\nExperienced in executing marketing campaigns, analyzing performance, and driving customer acquisition."
    elif job_role == "Account Executive":
        resume_text += "\n\nSkilled in managing client accounts, identifying opportunities for upselling, and maintaining customer relationships."
    elif job_role == "HR Specialist":
        resume_text += "\n\nProficient in recruiting, employee engagement, and developing HR policies and training programs."
    elif job_role == "IT Specialist":
        resume_text += "\n\nExperienced in managing IT infrastructure, supporting end-users, and maintaining security protocols."
    elif job_role == "Network Administrator":
        resume_text += "\n\nSkilled in configuring, maintaining, and troubleshooting network hardware and software systems."
    elif job_role == "Java Developer":
        resume_text += "\n\nProficient in Java programming and developing scalable, enterprise-level applications."
    elif job_role == "React Developer":
        resume_text += "\n\nExperienced in developing modern web applications using React, Redux, and related technologies."
    elif job_role == "Salesforce Administrator":
        resume_text += "\n\nProficient in managing Salesforce instances, customizing workflows, and optimizing CRM performance."
    elif job_role == "Data Visualization Specialist":
        resume_text += "\n\nExperienced in creating interactive dashboards, reports, and visualizations using tools like Tableau and Power BI."
    elif job_role == "Mobile App Designer":
        resume_text += "\n\nSkilled in designing user-friendly mobile applications and wireframes for Android and iOS platforms."
    elif job_role == "Artificial Intelligence Researcher":
        resume_text += "\n\nExperienced in developing AI algorithms, conducting experiments, and publishing research in top journals."
    elif job_role == "Technical Product Manager":
        resume_text += "\n\nSkilled in defining product roadmaps, coordinating cross-functional teams, and ensuring product delivery."
    elif job_role == "Network Architect":
        resume_text += "\n\nExperienced in designing and implementing large-scale network infrastructures, ensuring scalability and security."
    elif job_role == "Cloud Operations Engineer":
        resume_text += "\n\nSkilled in managing cloud resources, automating workflows, and optimizing cloud infrastructure for efficiency."
    elif job_role == "SAP Consultant":
        resume_text += "\n\nExperienced in implementing and customizing SAP systems to meet business needs across various industries."
    elif job_role == "Security Engineer":
        resume_text += "\n\nSkilled in securing systems, networks, and applications from potential threats and vulnerabilities."
    elif job_role == "Game Tester":
        resume_text += "\n\nExperienced in testing video games, identifying bugs, and ensuring quality control during development."
    elif job_role == "Marketing Coordinator":
        resume_text += "\n\nSkilled in coordinating marketing campaigns, tracking metrics, and supporting marketing team activities."
    elif job_role == "Operations Manager":
        resume_text += "\n\nExperienced in managing day-to-day operations, improving business processes, and ensuring efficiency."
    elif job_role == "Compliance Analyst":
        resume_text += "\n\nProficient in monitoring and ensuring compliance with legal, financial, and regulatory standards."
    elif job_role == "Legal Consultant":
        resume_text += "\n\nSkilled in providing legal advice, reviewing contracts, and ensuring regulatory compliance across industries."
    elif job_role == "Financial Controller":
        resume_text += "\n\nExperienced in managing financial operations, budgeting, and ensuring the financial health of the organization."
    elif job_role == "Tax Specialist":
        resume_text += "\n\nSkilled in providing tax planning services, preparing tax returns, and advising clients on tax-related matters."
    elif job_role == "Advertising Executive":
        resume_text += "\n\nExperienced in developing and executing advertising campaigns to promote products and services."
    elif job_role == "Media Planner":
        resume_text += "\n\nSkilled in planning and buying media placements across TV, radio, print, and digital channels."
    elif job_role == "Systems Engineer":
        resume_text += "\n\nExperienced in designing and implementing complex systems, troubleshooting issues, and optimizing performance."
    elif job_role == "Cloud Software Engineer":
        resume_text += "\n\nSkilled in developing cloud-based software applications and ensuring seamless integration with cloud platforms."
    elif job_role == "Product Marketing Manager":
        resume_text += "\n\nExperienced in defining product positioning, messaging, and go-to-market strategies for new products."
    elif job_role == "Content Marketing Specialist":
        resume_text += "\n\nProficient in developing content strategies, creating engaging content, and analyzing content performance."
    
    return resume_text
# Number of records to generate (5000 or 10000)
num_records = 10000  # You can set this to 5000 or 10000

# Generate dataset
data = []
for i in range(num_records):
    filename = f"resume{i+1}.pdf"  # Simulated filename
    label = random.choice(job_roles)  # Randomly assign a job role
    resume_text = generate_resume_text(label)  # Generate corresponding resume text
    data.append([filename, label, resume_text])

# Create DataFrame
df = pd.DataFrame(data, columns=['filename', 'label', 'resume_text'])

# Save the dataset to CSV
df.to_csv('resume_labels.csv', index=False)

print(f"Dataset generated with {num_records} records and saved as 'resume_labels.csv'.")
