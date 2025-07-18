import streamlit as st
import base64
from datetime import datetime

# Configure page
st.set_page_config(
    page_title="D.P. Public School - Remedial Sessions Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 0;
        text-align: center;
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .main-header h1 {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.3rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #667eea;
        transition: transform 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .feature-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    .feature-description {
        color: #666;
        line-height: 1.6;
        text-align: center;
    }
    
    .cta-section {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 3rem 2rem;
        text-align: center;
        border-radius: 15px;
        margin: 3rem 0;
        color: white;
    }
    
    .cta-section h2 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .cta-section p {
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .stats-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: bold;
        color: #667eea;
        display: block;
    }
    
    .stat-label {
        font-size: 1.1rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    .testimonial-card {
        background: #fff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-top: 3px solid #667eea;
    }
    
    .testimonial-text {
        font-style: italic;
        color: #555;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    
    .testimonial-author {
        font-weight: bold;
        color: #333;
        text-align: right;
    }
    
    .school-info {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
    }
    
    .school-info h3 {
        color: #333;
        margin-bottom: 1rem;
    }
    
    .school-info p {
        color: #666;
        line-height: 1.6;
    }
    
    .demo-section {
        background: #f8f9fa;
        padding: 3rem 2rem;
        border-radius: 15px;
        margin: 3rem 0;
        text-align: center;
    }
    
    .demo-section h2 {
        color: #333;
        margin-bottom: 2rem;
    }
    
    .role-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem;
        box-shadow: 0 3px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .role-card:hover {
        transform: translateY(-3px);
    }
    
    .role-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .role-title {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 1rem;
    }
    
    .role-features {
        text-align: left;
        color: #666;
    }
    
    .role-features li {
        margin: 0.5rem 0;
        padding-left: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Main Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 D.P. Public School</h1>
        <p>Remedial Sessions Platform - Bridging Learning Gaps Together</p>
        <p><strong>Empowering Every Child's Educational Journey</strong></p>
    </div>
    """, unsafe_allow_html=True)

    # School Information Section
    st.markdown("""
    <div class="school-info">
        <h3>📚 About Our Platform</h3>
        <p>Our innovative Parent-Teacher Collaborative Platform is designed specifically for D.P. Public School 
        to create a seamless bridge between classroom learning and home support. We believe that every child 
        deserves personalized attention and support to overcome learning challenges and achieve their full potential.</p>
    </div>
    """, unsafe_allow_html=True)

    # Key Features Section
    st.markdown("## ✨ Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎯</div>
            <div class="feature-title">Personalized Assessment</div>
            <div class="feature-description">
                Teachers can assess student competencies across multiple subjects and track progress over time with detailed analytics.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <div class="feature-title">Customized Learning Materials</div>
            <div class="feature-description">
                Upload and share targeted learning materials, worksheets, and activities designed for each student's specific needs.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Real-time Progress Tracking</div>
            <div class="feature-description">
                Monitor daily progress, completion rates, and provide instant feedback to keep students motivated and on track.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Second row of features
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💬</div>
            <div class="feature-title">Seamless Communication</div>
            <div class="feature-description">
                Built-in messaging system enables continuous dialogue between teachers and parents about student progress.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🏆</div>
            <div class="feature-title">Achievement Tracking</div>
            <div class="feature-description">
                Celebrate milestones and achievements with detailed progress reports and competency development tracking.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col6:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔒</div>
            <div class="feature-title">Secure & Private</div>
            <div class="feature-description">
                Your data is protected with secure authentication and privacy controls designed specifically for educational use.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Stats Section
    st.markdown("## 📈 Platform Impact")
    
    st.markdown("""
    <div class="stats-container">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
            <div class="stat-item">
                <span class="stat-number">100+</span>
                <div class="stat-label">Students Supported</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">50+</span>
                <div class="stat-label">Teachers Connected</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">200+</span>
                <div class="stat-label">Parents Engaged</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">95%</span>
                <div class="stat-label">Satisfaction Rate</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Demo Section
    st.markdown("""
    <div class="demo-section">
        <h2>🚀 Explore Our Platform</h2>
        <p>Experience the power of collaborative learning with our user-friendly interface</p>
    </div>
    """, unsafe_allow_html=True)

    # Role-based features
    col_teacher, col_parent = st.columns(2)
    
    with col_teacher:
        st.markdown("""
        <div class="role-card">
            <div class="role-icon">👩‍🏫</div>
            <div class="role-title">For Teachers</div>
            <div class="role-features">
                <ul>
                    <li>✅ Assess student competencies across all subjects</li>
                    <li>✅ Upload customized learning materials</li>
                    <li>✅ Track daily progress and completion rates</li>
                    <li>✅ Provide instant feedback and support</li>
                    <li>✅ Generate detailed progress reports</li>
                    <li>✅ Communicate directly with parents</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_parent:
        st.markdown("""
        <div class="role-card">
            <div class="role-icon">👨‍👩‍👧‍👦</div>
            <div class="role-title">For Parents</div>
            <div class="role-features">
                <ul>
                    <li>✅ View your child's competency assessments</li>
                    <li>✅ Access all learning materials and activities</li>
                    <li>✅ Track daily progress and achievements</li>
                    <li>✅ Add comments and observations</li>
                    <li>✅ Receive teacher feedback instantly</li>
                    <li>✅ Stay connected with your child's education</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Grade-specific features
    st.markdown("## 📝 Grade-Specific Support")
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🌟 Specialized Grade 1 Support</div>
        <div class="feature-description">
            <strong>Comprehensive foundational skills assessment including:</strong><br>
            • <strong>English:</strong> Sound discrimination, letter recognition, phonemic blending, writing basics<br>
            • <strong>Mathematics:</strong> Number recognition, counting, shape awareness, measurement concepts<br>
            • <strong>Hindi:</strong> स्वर-व्यंजन recognition, pronunciation, reading, and writing fundamentals<br>
            <em>With age-appropriate activities and progress tracking designed for early learners</em>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Testimonials
    st.markdown("## 💬 What Our Community Says")
    
    col_test1, col_test2 = st.columns(2)
    
    with col_test1:
        st.markdown("""
        <div class="testimonial-card">
            <div class="testimonial-text">
                "This platform has revolutionized how I connect with my students' families. 
                The daily progress tracking helps me provide targeted support where it's needed most."
            </div>
            <div class="testimonial-author">- Mrs. Sharma, Grade 3 Teacher</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_test2:
        st.markdown("""
        <div class="testimonial-card">
            <div class="testimonial-text">
                "I love being able to see exactly what my daughter is working on and how she's progressing. 
                The teacher's feedback helps me support her learning at home."
            </div>
            <div class="testimonial-author">- Mr. Kumar, Parent of Grade 1 Student</div>
        </div>
        """, unsafe_allow_html=True)

    # Call to Action
    st.markdown("""
    <div class="cta-section">
        <h2>Ready to Transform Your Child's Learning Experience?</h2>
        <p>Join the D.P. Public School community in creating a collaborative educational environment 
        where every child can thrive and reach their full potential.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Action buttons
    col_cta1, col_cta2, col_cta3 = st.columns(3)
    
    with col_cta1:
        if st.button("🚀 Launch Platform", type="primary", use_container_width=True):
            st.info("Click here to redirect to your main application: `streamlit run app4_copy.py`")
    
    with col_cta2:
        if st.button("📞 Contact School", use_container_width=True):
            st.info("Contact D.P. Public School for more information about accessing the platform.")
    
    with col_cta3:
        if st.button("📖 Learn More", use_container_width=True):
            st.info("Scroll down to explore more features and benefits of our platform.")

    # Additional Information
    st.markdown("---")
    
    st.markdown("## 🔧 Technical Features")
    
    col_tech1, col_tech2 = st.columns(2)
    
    with col_tech1:
        st.markdown("""
        **🛡️ Security & Privacy**
        - Secure user authentication
        - Role-based access control
        - Data encryption and protection
        - GDPR compliant data handling
        """)
        
        st.markdown("""
        **📱 Accessibility**
        - Mobile-responsive design
        - Cross-platform compatibility
        - Intuitive user interface
        - Multi-language support (Hindi/English)
        """)
    
    with col_tech2:
        st.markdown("""
        **⚡ Performance**
        - Fast file upload and download
        - Real-time progress updates
        - Efficient data management
        - Reliable cloud hosting
        """)
        
        st.markdown("""
        **🔄 Integration**
        - Seamless teacher-parent communication
        - Automated progress tracking
        - Customizable assessment tools
        - Comprehensive reporting system
        """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 10px; margin-top: 2rem;">
        <h4>🏫 D.P. Public School - Remedial Sessions Platform</h4>
        <p>Building bridges between classroom and home for every child's success</p>
        <p><small>Developed with ❤️ for our school community | © 2024 D.P. Public School</small></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()