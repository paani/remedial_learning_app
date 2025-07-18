import streamlit as st
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="D.P. Public School - Remedial Sessions Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, vibrant design
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    /* Global Styles */
    .main > div {
        padding-top: 0rem;
    }
    
    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
        color: white;
        text-align: center;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="50%" cy="50%" r="50%"><stop offset="0%" style="stop-color:%23ffffff;stop-opacity:0.1"/><stop offset="100%" style="stop-color:%23ffffff;stop-opacity:0"/></radialGradient></defs><circle cx="200" cy="200" r="100" fill="url(%23a)"/><circle cx="800" cy="300" r="150" fill="url(%23a)"/><circle cx="400" cy="700" r="80" fill="url(%23a)"/></svg>');
        animation: float 20s ease-in-out infinite;
        pointer-events: none;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1rem;
        position: relative;
        z-index: 2;
        text-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        margin-bottom: 1rem;
        opacity: 0.9;
        position: relative;
        z-index: 2;
    }
    
    .hero-description {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.8;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        position: relative;
        z-index: 2;
        line-height: 1.6;
    }
    
    /* Stats Section */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
        padding: 2rem;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stat-item {
        text-align: center;
        color: white;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        transition: transform 0.3s ease;
    }
    
    .stat-item:hover {
        transform: translateY(-10px);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        color: #ffffff;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .stat-label {
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Features Section */
    .features-section {
        background: white;
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 700;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .section-subtitle {
        font-size: 1.2rem;
        color: #666;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        transition: all 0.3s ease;
        border-left: 4px solid #667eea;
        position: relative;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .feature-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .feature-description {
        color: #666;
        line-height: 1.6;
    }
    
    /* Testimonials Section */
    .testimonials-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        color: white;
    }
    
    .testimonial-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .testimonial-text {
        font-size: 1.1rem;
        line-height: 1.7;
        margin-bottom: 1.5rem;
        font-style: italic;
    }
    
    .testimonial-author {
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    
    .testimonial-role {
        opacity: 0.8;
        font-size: 0.9rem;
    }
    
    /* CTA Section */
    .cta-section {
        background: #1a1a1a;
        padding: 4rem 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        text-align: center;
        color: white;
    }
    
    .cta-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .cta-description {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        color: #ccc;
        line-height: 1.6;
    }
    
    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
    }
    
    /* Navigation */
    .nav-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        padding: 1rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .nav-title {
        font-size: 1.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .section-title {
            font-size: 2rem;
        }
        
        .cta-title {
            font-size: 2rem;
        }
        
        .stats-container {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in-up {
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'page_loaded' not in st.session_state:
    st.session_state.page_loaded = True

# Navigation
st.markdown("""
<div class="nav-container">
    <div class="nav-title">🎓 D.P. Public School</div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section fade-in-up">
    <h1 class="hero-title">Transform Your Child's Learning Journey</h1>
    <p class="hero-subtitle">Remedial Sessions Platform</p>
    <p class="hero-description">
        Bridging the gap between classroom and home with our innovative parent-teacher 
        collaborative platform. Personalized learning, real-time progress tracking, 
        and seamless communication for every child's success.
    </p>
</div>
""", unsafe_allow_html=True)

# Hero Buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🚀 Launch Platform", key="launch"):
        st.success("🎉 Ready to launch! This would redirect to your main application.")
        st.balloons()
    
    if st.button("📚 Learn More", key="learn"):
        st.info("📖 Exploring our features below! Scroll down to discover more.")

# Stats Section
st.markdown("""
<div class="stats-container">
    <div class="stat-item">
        <div class="stat-number">150+</div>
        <div class="stat-label">Students Supported</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">75+</div>
        <div class="stat-label">Teachers Connected</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">300+</div>
        <div class="stat-label">Parents Engaged</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">98%</div>
        <div class="stat-label">Satisfaction Rate</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("""
<div class="features-section">
    <div class="section-header">
        <h2 class="section-title">Powerful Features for Modern Education</h2>
        <p class="section-subtitle">Discover how our platform revolutionizes the way teachers and parents collaborate to support student success</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Features Grid
features = [
    {
        "icon": "🎯",
        "title": "Personalized Assessment",
        "description": "Advanced competency tracking across all subjects with detailed analytics and progress visualization for targeted learning interventions."
    },
    {
        "icon": "📖",
        "title": "Smart Learning Materials",
        "description": "AI-powered content recommendations and customized worksheets tailored to each student's learning style and pace."
    },
    {
        "icon": "📊",
        "title": "Real-time Analytics",
        "description": "Comprehensive dashboard with live progress tracking, completion rates, and predictive insights for proactive support."
    },
    {
        "icon": "💬",
        "title": "Seamless Communication",
        "description": "Integrated messaging system with instant notifications, file sharing, and video conferencing capabilities."
    },
    {
        "icon": "🏆",
        "title": "Achievement Tracking",
        "description": "Gamified learning experience with badges, certificates, and milestone celebrations to keep students motivated."
    },
    {
        "icon": "🔒",
        "title": "Enterprise Security",
        "description": "Bank-level security with end-to-end encryption, secure authentication, and GDPR-compliant data protection."
    }
]

# Display features in a 2-column layout
col1, col2 = st.columns(2)

for i, feature in enumerate(features):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{feature['icon']}</div>
            <h3 class="feature-title">{feature['title']}</h3>
            <p class="feature-description">{feature['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Testimonials Section
st.markdown("""
<div class="testimonials-section">
    <div class="section-header">
        <h2 class="section-title">What Our Community Says</h2>
        <p class="section-subtitle">Real stories from teachers and parents who have transformed their educational experience</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Testimonials
testimonials = [
    {
        "text": "This platform has completely revolutionized how I connect with my students' families. The real-time progress tracking and instant communication have made my teaching more effective and rewarding than ever before.",
        "author": "Mrs. Priya Sharma",
        "role": "Grade 3 Teacher"
    },
    {
        "text": "As a parent, I love being able to see exactly what my daughter is working on and how she's progressing. The detailed feedback from her teacher helps me provide the right support at home. It's truly a game-changer!",
        "author": "Mr. Rajesh Kumar",
        "role": "Parent of Grade 1 Student"
    }
]

col1, col2 = st.columns(2)

for i, testimonial in enumerate(testimonials):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
        <div class="testimonial-card">
            <p class="testimonial-text">"{testimonial['text']}"</p>
            <p class="testimonial-author">— {testimonial['author']}</p>
            <p class="testimonial-role">{testimonial['role']}</p>
        </div>
        """, unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-section">
    <h2 class="cta-title">Ready to Transform Education?</h2>
    <p class="cta-description">
        Join the D.P. Public School community in creating a collaborative educational 
        environment where every child can thrive, learn, and reach their full potential 
        through innovative technology and dedicated support.
    </p>
</div>
""", unsafe_allow_html=True)

# CTA Buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("🌟 Start Your Journey", key="start"):
        st.success("✨ Welcome aboard! Let's begin your educational transformation journey.")
        st.balloons()

with col3:
    if st.button("📅 Schedule Demo", key="demo"):
        st.info("📅 Demo scheduled! We'll contact you soon to arrange a personalized demonstration.")

# Interactive Elements
st.markdown("---")

# Add an interactive demo section
st.markdown("""
<div class="section-header">
    <h2 class="section-title">Interactive Demo</h2>
    <p class="section-subtitle">Experience our platform features</p>
</div>
""", unsafe_allow_html=True)

# Demo tabs
tab1, tab2, tab3 = st.tabs(["📊 Analytics Dashboard", "📚 Learning Materials", "💬 Communication Hub"])

with tab1:
    st.markdown("### Student Progress Overview")
    
    # Sample data for demo
    import pandas as pd
    import numpy as np
    
    # Create sample progress data
    subjects = ['Mathematics', 'Science', 'English', 'Social Studies', 'Hindi']
    progress_data = {
        'Subject': subjects,
        'Completion (%)': [85, 78, 92, 67, 73],
        'Grade': ['A', 'B+', 'A+', 'B', 'B+']
    }
    
    df = pd.DataFrame(progress_data)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.dataframe(df, use_container_width=True)
    
    with col2:
        st.bar_chart(df.set_index('Subject')['Completion (%)'])

with tab2:
    st.markdown("### Personalized Learning Content")
    
    # Sample learning materials
    materials = [
        {"title": "Mathematics - Fractions", "type": "Interactive Quiz", "difficulty": "Medium"},
        {"title": "Science - Solar System", "type": "Video Tutorial", "difficulty": "Easy"},
        {"title": "English - Grammar Rules", "type": "Worksheet", "difficulty": "Hard"},
        {"title": "Social Studies - Indian History", "type": "Reading Material", "difficulty": "Medium"}
    ]
    
    for material in materials:
        with st.expander(f"{material['title']} - {material['type']}"):
            st.write(f"**Difficulty:** {material['difficulty']}")
            st.write("This is a sample learning material tailored to the student's current level and learning pace.")
            st.button(f"Start {material['type']}", key=f"start_{material['title']}")

with tab3:
    st.markdown("### Communication Center")
    
    # Sample messages
    with st.expander("📧 Recent Messages"):
        st.write("**From: Mrs. Priya Sharma (Teacher)**")
        st.write("Great improvement in mathematics! Keep up the good work.")
        st.write("*2 hours ago*")
        
        st.write("**From: Parent**")
        st.write("Thank you for the feedback. We'll continue practicing at home.")
        st.write("*1 hour ago*")
    
    # Message composer
    st.markdown("### Send New Message")
    recipient = st.selectbox("To:", ["Teacher", "Parent", "Student"])
    message = st.text_area("Message:", placeholder="Type your message here...")
    
    if st.button("Send Message"):
        if message:
            st.success(f"Message sent to {recipient}!")
        else:
            st.error("Please enter a message before sending.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; background: rgba(255, 255, 255, 0.1); 
           border-radius: 15px; margin-top: 2rem; color: white;">
    <h3>🎓 D.P. Public School</h3>
    <p>Empowering every child's educational journey through innovative technology and collaborative learning.</p>
    <p style="margin-top: 1rem; opacity: 0.8;">
        📧 info@dpschool.edu | 📞 +91 98765 43210 | 📍 Education District, City
    </p>
    <p style="margin-top: 1rem; opacity: 0.6;">
        © 2024 D.P. Public School. All rights reserved. Built with ❤️ for education.
    </p>
</div>
""", unsafe_allow_html=True)

# Add some interactive elements at the bottom
st.markdown("---")

# Feedback section
st.markdown("### 💭 Quick Feedback")
col1, col2 = st.columns(2)

with col1:
    rating = st.slider("Rate this landing page:", 1, 5, 5)
    if rating >= 4:
        st.success(f"Thank you for the {rating}-star rating! 🌟")
    else:
        st.info("We appreciate your feedback and will work to improve!")

with col2:
    feedback = st.text_area("Any suggestions?", placeholder="Share your thoughts...")
    if st.button("Submit Feedback"):
        if feedback:
            st.success("Thank you for your valuable feedback!")
        else:
            st.info("Feel free to share your thoughts anytime!")

# Easter egg - Add a fun fact generator
if st.button("🎲 Fun Education Fact"):
    facts = [
        "The human brain can process information as fast as 120 meters per second! 🧠",
        "Finland has no standardized testing until age 16, yet has one of the best education systems! 🇫🇮",
        "The word 'school' comes from the Greek word 'schole' meaning 'leisure'! 📚",
        "A group of flamingos is called a 'flamboyance'! 🦩",
        "Honey never spoils - archaeologists have found 3000-year-old honey that's still edible! 🍯"
    ]
    
    import random
    fact = random.choice(facts)
    st.info(f"💡 Did you know? {fact}")

# Add current time and welcome message
current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
st.markdown(f"""
<div style="text-align: center; margin-top: 2rem; opacity: 0.7; color: white;">
    <p>Current time: {current_time}</p>
    <p>Welcome to the future of education! 🚀</p>
</div>
""", unsafe_allow_html=True)
