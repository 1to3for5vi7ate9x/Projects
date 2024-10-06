from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Resume: Ankit", ln=True, align='C')

# Add a line break
pdf.ln(10)

# Set font for the body
pdf.set_font("Arial", size=12)

# Add Professional Summary
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Professional Summary", ln=True)
pdf.set_font('Arial', '', 12)
professional_summary = (
    "Detail-oriented and highly motivated IT Systems Administrator with extensive experience in managing "
    "and supporting diverse environments, including Mac, Windows, and Linux. Proficient in systems administration, "
    "endpoint management, troubleshooting, and optimizing performance in high-pressure environments. Strong track "
    "record in maintaining security best practices and improving service delivery for internal teams. Previous experience "
    "as a System Administrator at Krates with a relentless passion for learning and solving complex technical issues."
)
pdf.multi_cell(0, 10, txt=professional_summary)

# Add a line break
pdf.ln(5)

# Add Key Skills
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Key Skills", ln=True)
pdf.set_font('Arial', '', 12)
key_skills = (
    "- Mac, Windows, and Linux OS administration\n"
    "- SCCM, Jamf, and AirWatch endpoint management\n"
    "- Active Directory management (OU, Security Group maintenance)\n"
    "- IT on-boarding and configuration for new employees\n"
    "- A/V equipment support and server room maintenance\n"
    "- Strong customer service and communication skills\n"
    "- Security best practices and incident management\n"
    "- Asset procurement, delivery, and inventory management\n"
    "- Troubleshooting and problem-solving under tight deadlines\n"
    "- Automation and optimization of system processes"
)
pdf.multi_cell(0, 10, txt=key_skills)

# Add a line break
pdf.ln(5)

# Add Professional Experience
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Professional Experience", ln=True)
pdf.set_font('Arial', '', 12)
professional_experience = (
    "Krates, Pune, India\n"
    "System Administrator\n"
    "MM/YYYY - Present\n"
    "- Managed a large-scale IT infrastructure that included both Mac, Windows, and Linux-based systems.\n"
    "- Provided front-line technical support for internal users, ensuring swift and efficient resolution of issues.\n"
    "- Administered Active Directory, creating and maintaining user accounts, OUs, and Security Groups.\n"
    "- Managed SCCM and Jamf for endpoint security, software updates, and troubleshooting.\n"
    "- Worked closely with teams to implement process improvements, including system automation and optimization for enhanced user experience.\n"
    "- Played a key role in on-boarding new hires by configuring hardware and software, ensuring a smooth integration process.\n"
    "- Supported A/V setups for meetings, and provided hands-on assistance in the server/network room when needed.\n"
    "- Led initiatives to document IT policies and procedures to ensure compliance and operational efficiency."
)
pdf.multi_cell(0, 10, txt=professional_experience)

# Add a line break
pdf.ln(5)

# Add Education
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Education", ln=True)
pdf.set_font('Arial', '', 12)
education = "[Your Degree]\n[Your University], [Location]\nGraduation Date: MM/YYYY"
pdf.multi_cell(0, 10, txt=education)

# Add a line break
pdf.ln(5)

# Add Certifications
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Certifications", ln=True)
pdf.set_font('Arial', '', 12)
certifications = (
    "- [List any relevant certifications such as CompTIA Security+, Microsoft Certified: Azure Administrator, etc.]\n"
    "- [Other certifications specific to system administration or security best practices]"
)
pdf.multi_cell(0, 10, txt=certifications)

# Add a line break
pdf.ln(5)

# Add Projects
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Projects", ln=True)
pdf.set_font('Arial', '', 12)
projects = (
    "- Endpoint Management Optimization: Reduced incident response times by automating routine tasks for system "
    "monitoring, patching, and updates using Jamf and SCCM.\n"
    "- Security Best Practices Implementation: Spearheaded the rollout of a comprehensive security best practices "
    "initiative across multiple platforms, enhancing system integrity and reducing vulnerabilities."
)
pdf.multi_cell(0, 10, txt=projects)

# Add a line break
pdf.ln(5)

# Add Additional Information
pdf.set_font('Arial', 'B', 12)
pdf.cell(200, 10, txt="Additional Information", ln=True)
pdf.set_font('Arial', '', 12)
additional_info = (
    "- Willing to travel as required.\n"
    "- Comfortable working night shifts and collaborating with global teams."
)
pdf.multi_cell(0, 10, txt=additional_info)

# Save the PDF
#file_path = "/mnt/data/Ankit_IT_Systems_Administrator_Resume.pdf"
#pdf.output(file_path)

#file_path

