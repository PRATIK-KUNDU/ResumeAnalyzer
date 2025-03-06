from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import fitz  # PyMuPDF
import re  # Regular expression for email extraction
from docx import Document  # For handling DOCX files

app = Flask(__name__)

# Set the maximum content length to 100MB
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB

# Create uploads directory if it doesn't exist
os.makedirs("uploads", exist_ok=True)


def parse_pdf_resume(file_path):
    """Parse a PDF resume and extract text."""
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text


def parse_docx_resume(file_path):
    """Parse a DOCX resume and extract text."""
    text = ""
    doc = Document(file_path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def extract_email(text):
    """Extract email from text using regex."""
    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_regex, text)
    return match.group(0) if match else None


def score_resume(text, role):
    """Score the resume based on keywords for the job role."""
    keywords = {
        'Software Developer':
        ['Python', 'Java', 'C++', 'JavaScript', 'React', 'SQL'],
        'Data Scientist': [
            'Python', 'R', 'Machine Learning', 'Deep Learning', 'Pandas',
            'NumPy'
        ],
        'Project Manager':
        ['Agile', 'Scrum', 'Leadership', 'Project Management', 'Budgeting'],
        'Product Manager': [
            'Product Development', 'Market Research', 'Agile', 'Leadership',
            'Strategy'
        ],
        'Graphic Designer':
        ['Photoshop', 'Illustrator', 'Creative Suite', 'UI/UX', 'Design'],
        'Marketing Manager':
        ['SEO', 'Social Media', 'Branding', 'Content Marketing', 'Strategy'],
        'HR Manager': [
            'Recruitment', 'Employee Relations', 'HR Policies', 'Onboarding',
            'Payroll'
        ],
        'Financial Analyst':
        ['Excel', 'Finance', 'Data Analysis', 'Forecasting', 'Investment'],
        'Business Analyst': [
            'SQL', 'Requirements Gathering', 'Business Intelligence',
            'Project Management'
        ],
        'Cybersecurity Analyst': [
            'Network Security', 'Firewalls', 'Penetration Testing',
            'Data Protection'
        ],
        'DevOps Engineer': ['Docker', 'Kubernetes', 'CI/CD', 'Linux', 'Cloud'],
        'Software Architect': [
            'System Design', 'Architecture', 'Cloud', 'Software Engineering',
            'Scalability'
        ],
        'Web Developer':
        ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js', 'Web Development'],
        'Database Administrator':
        ['SQL', 'Database', 'Backup', 'Recovery', 'Performance Tuning'],
        'Network Engineer':
        ['TCP/IP', 'Network Design', 'Firewall', 'Routing', 'Switching'],
        'Full Stack Developer':
        ['JavaScript', 'Node.js', 'React', 'MongoDB', 'Express'],
        'Data Engineer':
        ['Big Data', 'Hadoop', 'ETL', 'Data Warehousing', 'Apache Kafka'],
        'Quality Assurance':
        ['Testing', 'Automation', 'Bug Tracking', 'Selenium', 'QA'],
        'Sales Manager': [
            'Sales Strategy', 'Customer Acquisition', 'Lead Generation',
            'Negotiation'
        ],
        'UI/UX Designer':
        ['Wireframing', 'Prototyping', 'User Research', 'Figma', 'Adobe XD'],
        'Content Writer': [
            'Copywriting', 'SEO', 'Blogging', 'Content Strategy', 'Editing'
        ],
        'Legal Counsel': [
            'Contract Law', 'Corporate Law', 'Litigation', 'Compliance',
            'Advisory'
        ],
        'Civil Engineer': [
            'AutoCAD', 'Construction', 'Structural Analysis',
            'Project Management'
        ],
        'Electrical Engineer': [
            'Circuit Design', 'Power Systems', 'Electronics',
            'Project Engineering'
        ],
        'Mechanical Engineer': [
            'CAD', '3D Modeling', 'Manufacturing', 'Thermodynamics',
            'Mechanical Design'
        ],
        'Marketing Executive': [
            'Branding', 'Social Media', 'Market Analysis', 'SEO', 'Advertising'
        ],
        'Software Tester': [
            'Test Plans', 'Manual Testing', 'Automation Testing',
            'Bug Tracking', 'Regression'
        ],
        'Operations Manager': [
            'Logistics', 'Supply Chain', 'Process Improvement', 'Budgeting'
        ],
        'Accountant': [
            'Bookkeeping', 'Financial Reporting', 'Tax', 'Audit',
            'Accounting Software'
        ],
        'Construction Manager': [
            'Project Planning', 'Scheduling', 'Construction Site',
            'Blueprints', 'Safety'
        ],
        'Nurse': [
            'Patient Care', 'Medical Knowledge', 'Hospital Operations',
            'Clinical Skills'
        ],
        'Teacher': [
            'Curriculum Development', 'Classroom Management',
            'Student Engagement', 'Educational Technology'
        ],
        'Scientist': [
            'Research', 'Data Analysis', 'Experimentation', 'Lab Techniques',
            'Scientific Writing'
        ],
        'Research Analyst': [
            'Market Research', 'Data Analysis', 'Reporting', 'Survey Design',
            'Statistical Tools'
        ],
        'Logistics Coordinator': [
            'Inventory', 'Supply Chain', 'Shipping', 'Scheduling', 'Operations'
        ],
        'Sales Engineer': [
            'Technical Sales', 'Customer Solutions', 'Product Knowledge',
            'Engineering'
        ],
        'Health Informatics': [
            'EHR', 'Patient Records', 'Healthcare IT', 'Data Analysis',
            'Medical Coding'
        ],
        'Data Analyst': [
            'Excel', 'Power BI', 'SQL', 'Tableau', 'Data Visualization'
        ],
        'Biomedical Engineer': [
            'Biomedical', 'Medical Devices', 'Lab Testing', 'Biocompatibility'
        ],
        'Environmental Engineer': [
            'Environmental Studies', 'Pollution Control', 'Sustainability',
            'EIA'
        ],
        'Clinical Researcher': [
            'Clinical Trials', 'Data Collection', 'IRB', 'Patient Management'
        ],
        'Pharmacist': [
            'Pharmacy', 'Drug Dispensing', 'Medical Knowledge',
            'Patient Counseling'
        ],
        'Radiologist': [
            'Medical Imaging', 'Radiology', 'CT Scans', 'MRI', 'Diagnostic'
        ],
        'Agronomist': [
            'Agriculture', 'Soil Science', 'Plant Breeding', 'Farm Management'
        ],
        'Veterinarian': [
            'Animal Care', 'Surgery', 'Diagnostics', 'Animal Health'
        ],
        'Geologist': [
            'Geology', 'Field Research', 'Mineral Analysis', 'Mapping'
        ],
        'Urban Planner': [
            'Zoning', 'Urban Development', 'Land Use', 'GIS',
            'Environmental Planning'
        ],
        'Architect': [
            'Design', 'CAD', 'Blueprints', 'Building Codes', 'Construction'
        ],
        'Chef': ['Cooking', 'Menu Planning', 'Culinary Skills', 'Food Safety'],
        'Dietitian':
        ['Nutrition', 'Meal Planning', 'Diet Counseling', 'Patient Education'],
        'Translator': [
            'Translation', 'Language Proficiency', 'Editing',
            'Cultural Awareness'
        ],
        'Librarian': [
            'Cataloguing', 'Library Systems', 'Research Assistance',
            'Collection Development'
        ],
        'Museum Curator': [
            'Artifact Management', 'Exhibitions', 'Research', 'Preservation'
        ],
        'Interpreter': [
            'Language Skills', 'Oral Communication', 'Translation',
            'Cultural Sensitivity'
        ],
        'Tour Guide': [
            'Customer Service', 'Knowledge of Sites', 'Public Speaking',
            'History'
        ],
        'Event Planner': [
            'Event Coordination', 'Vendor Management', 'Budgeting', 'Logistics'
        ],
        'Social Worker': [
            'Case Management', 'Counseling', 'Social Services',
            'Community Outreach'
        ],
        'Fashion Designer': [
            'Design', 'Pattern Making', 'Fabric Knowledge', 'Fashion Trends'
        ],
        'Mechanic': [
            'Repair', 'Diagnostics', 'Vehicle Maintenance', 'Technical Skills'
        ],
        'Plumber': [
            'Piping', 'Fixture Installation', 'System Maintenance',
            'Water Systems'
        ],
        'Electrician': [
            'Wiring', 'Electrical Codes', 'Troubleshooting', 'Installation'
        ],
        'Carpenter': [
            'Woodworking', 'Blueprints', 'Cabinet Making', 'Construction'
        ],
        'Real Estate Agent': [
            'Property Listings', 'Sales', 'Negotiation', 'Market Knowledge'
        ],
        'Pilot': [
            'Flight Operations', 'Navigation', 'Safety', 'Communication'
        ],
        'Flight Attendant': [
            'Customer Service', 'Safety', 'First Aid', 'Communication'
        ],
        'Train Conductor': [
            'Operations', 'Passenger Service', 'Safety', 'Scheduling'
        ],
        'Air Traffic Controller': [
            'Aviation Knowledge', 'Radar', 'Communication', 'Safety'
        ],
        'Customs Officer':
        ['Border Security', 'Documentation', 'Customer Service', 'Compliance'],
        'Detective': [
            'Investigations', 'Surveillance', 'Interrogation',
            'Evidence Handling'
        ],
        'Firefighter': ['Fire Suppression', 'Rescue', 'Safety', 'First Aid'],
        'Paramedic': [
            'Medical Response', 'First Aid', 'Trauma Care', 'Patient Transport'
        ],
        'Police Officer': [
            'Law Enforcement', 'Patrolling', 'Public Safety',
            'Evidence Collection'
        ]
    }

    score = 0
    matched_keywords = []

    for keyword in keywords.get(role, []):
        if keyword.lower() in text.lower():
            score += 20  # Each keyword contributes 10 points
            matched_keywords.append(keyword)

    return score, matched_keywords


@app.route('/')
def home():
    """Render the home page."""
    roles = sorted([
        'Software Developer', 'Data Scientist', 'Project Manager',
        'Product Manager', 'Graphic Designer', 'Marketing Manager',
        'HR Manager', 'Financial Analyst', 'Business Analyst',
        'Cybersecurity Analyst', 'DevOps Engineer', 'Software Architect',
        'Web Developer', 'Database Administrator', 'Network Engineer',
        'Full Stack Developer', 'Data Engineer', 'Quality Assurance',
        'Sales Manager', 'UI/UX Designer', 'Content Writer', 'Legal Counsel',
        'Civil Engineer', 'Electrical Engineer', 'Mechanical Engineer',
        'Marketing Executive', 'Software Tester', 'Operations Manager',
        'Accountant', 'Construction Manager', 'Nurse', 'Teacher', 'Scientist',
        'Research Analyst', 'Logistics Coordinator', 'Sales Engineer',
        'Health Informatics', 'Data Analyst', 'Biomedical Engineer',
        'Environmental Engineer', 'Clinical Researcher', 'Pharmacist',
        'Radiologist', 'Agronomist', 'Veterinarian', 'Geologist',
        'Urban Planner', 'Architect', 'Chef', 'Dietitian', 'Translator',
        'Librarian', 'Museum Curator', 'Interpreter', 'Tour Guide',
        'Event Planner', 'Social Worker', 'Fashion Designer', 'Mechanic',
        'Plumber', 'Electrician', 'Carpenter', 'Real Estate Agent', 'Pilot',
        'Flight Attendant', 'Train Conductor', 'Air Traffic Controller',
        'Customs Officer', 'Detective', 'Firefighter', 'Paramedic',
        'Police Officer'
    ])

    return render_template('index.html', roles=roles)


@app.route('/bulk_upload', methods=['POST'])
def bulk_upload():
    """Handle bulk resume uploads."""
    if 'resume_files' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400

    resumes_data = []
    resume_files = request.files.getlist('resume_files')

    for resume_file in resume_files:
        file_path = os.path.join("uploads", resume_file.filename)
        resume_file.save(file_path)

        # Parse the resume based on its file type
        if resume_file.filename.endswith('.pdf'):
            resume_text = parse_pdf_resume(file_path)
        elif resume_file.filename.endswith('.docx'):
            resume_text = parse_docx_resume(file_path)
        else:
            return jsonify({'error': 'Unsupported file type'}), 400

        email = extract_email(resume_text)

        # Get the job role from the form data
        role = request.form.get('role')
        score, matched_keywords = score_resume(resume_text, role)

        # Add the CV file link
        cv_link = f"/uploads/{resume_file.filename}"

        resumes_data.append({
            'filename': resume_file.filename,
            'email': email,
            'score': score,
            'matched_keywords': matched_keywords,
            'cv_link': cv_link  # Include the link to the CV file
        })

    # Sort results in descending order based on the score
    sorted_resumes = sorted(resumes_data,
                            key=lambda x: x['score'],
                            reverse=True)

    return jsonify(sorted_resumes), 200


# Route to serve the uploaded CV file
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
