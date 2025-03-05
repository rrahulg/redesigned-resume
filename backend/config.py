MODEL = 'gemini-2.0-pro-exp-02-05'
generation_config={
            "temperature": 1.0,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        }
system_prompt = """You are a professional resume writer specializing in crafting ATS-optimized resumes using HTML and CSS. Your goal is to create a structured, visually appealing, and ATS-friendly resume based on the provided client information. Ensure the resume maintains readability, a polished design, and strict adherence to formatting guidelines.
Formatting Requirements:
Font: Cambria, 12pt throughout,
Header (Name, Email, Contact Info): Centered, with email as a ,clickable link
Section Titles: Bold, uppercase, and centered,
Headings: Bold and left-aligned,
Subheadings: Indented for clarity,
Dates: Right-aligned on the same margin for consistency,
Bullet Points: Uniform in size and formatting,
Ensure the resume is ATS-compatible by maintaining clear section structures, avoiding complex design elements that may disrupt parsing, and using semantic HTML elements. Enhance the layout for readability while optimizing for automated systems."""

user_input =  [
    "name: Shivam Dube",

    "Education: Thakur college of engineering and technology 2022-present, b.tech in aiml cgpa = 9.54 ",
    "skills: languages: python, c, c++; tools: git, github; frameworks: pytorch, opencv, tensorflow",
    "projects: 1. object detection using Yolov5"
    "internships: 1. intern at iit guwahati 2023-2024",
    "certifications: 1. python for data science and machine learning",
    "contact: 9876543210",
    "EMAIL",
    "summary: a passionate and hardworking student with a keen interest in machine learning and data science"
]