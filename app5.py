import streamlit as st
import sqlite3
import hashlib
import os
from datetime import datetime, timedelta
import base64
import json
import uuid

# Configure page
st.set_page_config(
    page_title="Parent-Teacher Collaborative Platform",
    page_icon="📚",
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Database setup
DB_NAME = os.path.join(os.path.dirname(__file__), "remedial_platform.db")

def init_database():
    """Initialize SQLite database with all required tables"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            user_type TEXT NOT NULL,
            full_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            grade TEXT NOT NULL,
            teacher TEXT NOT NULL,
            parent TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (teacher) REFERENCES users(username),
            FOREIGN KEY (parent) REFERENCES users(username)
        )
    ''')
    
    # Assessments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assessments (
            assessment_id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,
            teacher TEXT NOT NULL,
            competencies TEXT NOT NULL,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (teacher) REFERENCES users(username)
        )
    ''')
    
    # Materials table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materials (
            material_id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,
            teacher TEXT NOT NULL,
            competency TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            file_data BLOB NOT NULL,
            filename TEXT NOT NULL,
            duration_days INTEGER NOT NULL,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (teacher) REFERENCES users(username)
        )
    ''')
    
    # Progress table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            progress_id TEXT PRIMARY KEY,
            student_id TEXT NOT NULL,
            material_id TEXT NOT NULL,
            parent TEXT NOT NULL,
            completed BOOLEAN DEFAULT FALSE,
            completed_at TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (material_id) REFERENCES materials(material_id),
            FOREIGN KEY (parent) REFERENCES users(username)
        )
    ''')
    
    # Feedback table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            feedback_id TEXT PRIMARY KEY,
            progress_id TEXT NOT NULL,
            teacher TEXT NOT NULL,
            student_id TEXT NOT NULL,
            feedback TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (progress_id) REFERENCES progress(progress_id),
            FOREIGN KEY (teacher) REFERENCES users(username),
            FOREIGN KEY (student_id) REFERENCES students(student_id)
        )
    ''')
    
    # Daily progress tracking table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_progress (
            daily_progress_id TEXT PRIMARY KEY,
            material_id TEXT NOT NULL,
            student_id TEXT NOT NULL,
            parent TEXT NOT NULL,
            day_number INTEGER NOT NULL,
            completed BOOLEAN DEFAULT FALSE,
            parent_comments TEXT,
            completed_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (material_id) REFERENCES materials(material_id),
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (parent) REFERENCES users(username)
        )
    ''')

    # Teacher feedback on daily progress
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_feedback (
            daily_feedback_id TEXT PRIMARY KEY,
            daily_progress_id TEXT NOT NULL,
            teacher TEXT NOT NULL,
            feedback TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (daily_progress_id) REFERENCES daily_progress(daily_progress_id),
            FOREIGN KEY (teacher) REFERENCES users(username)
        )
    ''')

    # Add sessions table for persistent login
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            user_type TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            expires_at TIMESTAMP NOT NULL,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    ''')
    
    conn.commit()
    conn.close()

# Helper functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, password, user_type, full_name):
    """Create a new user in the database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO users (username, password, user_type, full_name)
            VALUES (?, ?, ?, ?)
        ''', (username, hash_password(password), user_type, full_name))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

# Modified authentication function
def authenticate_user_with_session(username, password):
    """Authenticate user and create session"""
    is_authenticated, user_type = authenticate_user(username, password)
    
    if is_authenticated:
        session_id = create_session(username, user_type)
        st.session_state.session_id = session_id
        
        # Update URL to include session (optional)
        st.query_params['session_id'] = session_id
        
        return True, user_type
    
    return False, None

def get_user_info(username):
    """Get user information"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT full_name, user_type FROM users WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()
    conn.close()
    
    return result

def get_user_students(username, user_type):
    """Get students associated with a user"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if user_type == 'teacher':
        cursor.execute('''
            SELECT student_id FROM students WHERE teacher = ?
        ''', (username,))
    elif user_type == 'parent':
        cursor.execute('''
            SELECT student_id FROM students WHERE parent = ?
        ''', (username,))
    
    results = cursor.fetchall()
    conn.close()
    
    return [row[0] for row in results]

def add_student(student_id, name, grade, teacher, parent):
    """Add a new student to the database"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO students (student_id, name, grade, teacher, parent)
            VALUES (?, ?, ?, ?, ?)
        ''', (student_id, name, grade, teacher, parent))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False

def get_student_info(student_id):
    """Get student information"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT name, grade, teacher, parent FROM students WHERE student_id = ?
    ''', (student_id,))
    result = cursor.fetchone()
    conn.close()
    
    return result

def save_assessment(assessment_id, student_id, teacher, competencies, notes):
    """Save competency assessment"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO assessments (assessment_id, student_id, teacher, competencies, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (assessment_id, student_id, teacher, json.dumps(competencies), notes))
    
    conn.commit()
    conn.close()

def get_latest_assessment(student_id):
    """Get the latest assessment for a student"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT competencies, notes, created_at FROM assessments 
        WHERE student_id = ? 
        ORDER BY created_at DESC 
        LIMIT 1
    ''', (student_id,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {
            'competencies': json.loads(result[0]),
            'notes': result[1],
            'date': result[2]
        }
    return None

def save_material(material_id, student_id, teacher, competency, title, description, file_data, filename, duration_days):
    """Save learning material with duration"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO materials (material_id, student_id, teacher, competency, title, description, file_data, filename, duration_days)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (material_id, student_id, teacher, competency, title, description, file_data, filename, duration_days))
    
    conn.commit()
    conn.close()

def get_student_materials(student_id):
    """Get all materials for a student"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT material_id, competency, title, description, file_data, filename, duration_days, uploaded_at
        FROM materials WHERE student_id = ?
        ORDER BY uploaded_at DESC
    ''', (student_id,))
    results = cursor.fetchall()
    conn.close()
    
    return [{
        'material_id': row[0],
        'competency': row[1],
        'title': row[2],
        'description': row[3],
        'file_data': row[4],
        'filename': row[5],
        'duration_days': row[6],
        'uploaded_at': row[7]
    } for row in results]

def save_progress(progress_id, student_id, material_id, parent, completed=False):
    """Save or update progress"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if completed:
        cursor.execute('''
            INSERT OR REPLACE INTO progress (progress_id, student_id, material_id, parent, completed, completed_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (progress_id, student_id, material_id, parent, completed, datetime.now()))
    else:
        cursor.execute('''
            INSERT OR REPLACE INTO progress (progress_id, student_id, material_id, parent, completed)
            VALUES (?, ?, ?, ?, ?)
        ''', (progress_id, student_id, material_id, parent, completed))
    
    conn.commit()
    conn.close()

def get_progress(student_id, material_id):
    """Get progress for a specific material"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT completed, completed_at FROM progress 
        WHERE student_id = ? AND material_id = ?
    ''', (student_id, material_id))
    result = cursor.fetchone()
    conn.close()
    
    return result

def get_student_progress(student_id):
    """Get all progress for a student"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.progress_id, p.material_id, p.completed, p.completed_at, m.title, m.competency
        FROM progress p
        JOIN materials m ON p.material_id = m.material_id
        WHERE p.student_id = ?
        ORDER BY p.completed_at DESC
    ''', (student_id,))
    results = cursor.fetchall()
    conn.close()
    
    return [{
        'progress_id': row[0],
        'material_id': row[1],
        'completed': row[2],
        'completed_at': row[3],
        'title': row[4],
        'competency': row[5]
    } for row in results]

def save_feedback(feedback_id, progress_id, teacher, student_id, feedback):
    """Save teacher feedback"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO feedback (feedback_id, progress_id, teacher, student_id, feedback)
        VALUES (?, ?, ?, ?, ?)
    ''', (feedback_id, progress_id, teacher, student_id, feedback))
    
    conn.commit()
    conn.close()

def get_feedback(progress_id):
    """Get feedback for a progress item"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT feedback, created_at FROM feedback 
        WHERE progress_id = ?
        ORDER BY created_at DESC
    ''', (progress_id,))
    results = cursor.fetchall()
    conn.close()
    
    return [{
        'feedback': row[0],
        'date': row[1]
    } for row in results]

def get_completed_activities(student_id):
    """Get completed activities for feedback"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT p.progress_id, m.title, m.competency, p.completed_at
        FROM progress p
        JOIN materials m ON p.material_id = m.material_id
        WHERE p.student_id = ? AND p.completed = 1
        ORDER BY p.completed_at DESC
    ''', (student_id,))
    results = cursor.fetchall()
    conn.close()
    
    return [{
        'progress_id': row[0],
        'title': row[1],
        'competency': row[2],
        'completed_at': row[3]
    } for row in results]

def create_download_link(file_data, filename):
    """Create download link for files"""
    try:
        b64 = base64.b64encode(file_data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}" target="_blank">📄 Download {filename}</a>'
        return href
    except Exception as e:
        return f"Error creating download link: {str(e)}"

def validate_file_type(file):
    """Validate uploaded file type"""
    if file is not None:
        file_extension = file.name.split('.')[-1].lower()
        if file_extension == 'pdf':
            return True
        else:
            st.error("Please upload only PDF files.")
            return False
    return False

def save_daily_progress(daily_progress_id, material_id, student_id, parent, day_number, completed=False, parent_comments=None):
    """Save daily progress for a material"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if completed:
        cursor.execute('''
            INSERT OR REPLACE INTO daily_progress (daily_progress_id, material_id, student_id, parent, day_number, completed, parent_comments, completed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (daily_progress_id, material_id, student_id, parent, day_number, completed, parent_comments, datetime.now()))
    else:
        cursor.execute('''
            INSERT OR REPLACE INTO daily_progress (daily_progress_id, material_id, student_id, parent, day_number, completed, parent_comments)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (daily_progress_id, material_id, student_id, parent, day_number, completed, parent_comments))
    
    conn.commit()
    conn.close()

def get_daily_progress(material_id, student_id):
    """Get daily progress for a material"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT daily_progress_id, day_number, completed, parent_comments, completed_at
        FROM daily_progress 
        WHERE material_id = ? AND student_id = ?
        ORDER BY day_number
    ''', (material_id, student_id))
    results = cursor.fetchall()
    conn.close()
    
    return [{
        'daily_progress_id': row[0],
        'day_number': row[1],
        'completed': row[2],
        'parent_comments': row[3],
        'completed_at': row[4]
    } for row in results]

def save_daily_feedback(daily_feedback_id, daily_progress_id, teacher, feedback):
    """Save teacher feedback on daily progress"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO daily_feedback (daily_feedback_id, daily_progress_id, teacher, feedback)
        VALUES (?, ?, ?, ?)
    ''', (daily_feedback_id, daily_progress_id, teacher, feedback))
    
    conn.commit()
    conn.close()

def get_daily_feedback(daily_progress_id):
    """Get teacher feedback for daily progress"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT feedback, created_at FROM daily_feedback 
        WHERE daily_progress_id = ?
        ORDER BY created_at DESC
    ''', (daily_progress_id,))
    results = cursor.fetchall()
    conn.close()
    
    return [{
        'feedback': row[0],
        'date': row[1]
    } for row in results]

def get_student_daily_progress_summary(student_id):
    """Get summary of daily progress for teacher review"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT dp.daily_progress_id, dp.material_id, dp.day_number, dp.completed, 
               dp.parent_comments, dp.completed_at, m.title, m.competency
        FROM daily_progress dp
        JOIN materials m ON dp.material_id = m.material_id
        WHERE dp.student_id = ?
        ORDER BY m.uploaded_at DESC, dp.day_number
    ''', (student_id,))
    results = cursor.fetchall()
    conn.close()
    
    return [{
        'daily_progress_id': row[0],
        'material_id': row[1],
        'day_number': row[2],
        'completed': row[3],
        'parent_comments': row[4],
        'completed_at': row[5],
        'title': row[6],
        'competency': row[7]
    } for row in results]

# Add mobile detection and fallback
def is_mobile():
    """Detect if user is on mobile device"""
    try:
        # Check user agent via JavaScript (Note: this method is deprecated)
        user_agent = st.query_params.get('mobile', False)  # Updated API
        return user_agent
    except:
        return False

# Mobile-safe markdown rendering
def safe_markdown(text):
    """Render markdown safely for mobile browsers"""
    if text is None:
        return ""
    
    # Remove problematic patterns that cause regex errors
    text = str(text)  # Ensure it's a string
    # Remove lookbehind pattern that causes mobile issues
    text = re.sub(r'[^\w\s\-\.,!?():\[\]{}"\'/]', '', text)  # Remove special chars
    return text

# Add these new functions for session management
def create_session(username, user_type, days=7):
    """Create a persistent session"""
    session_id = str(uuid.uuid4())
    expires_at = datetime.now() + timedelta(days=days)
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Clean up old sessions first
    cursor.execute('DELETE FROM sessions WHERE expires_at < ?', (datetime.now(),))
    
    # Create new session
    cursor.execute('''
        INSERT INTO sessions (session_id, username, user_type, expires_at)
        VALUES (?, ?, ?, ?)
    ''', (session_id, username, user_type, expires_at))
    
    conn.commit()
    conn.close()
    
    return session_id

def validate_session(session_id):
    """Validate and return session info"""
    if not session_id:
        return None
    
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT username, user_type FROM sessions 
        WHERE session_id = ? AND expires_at > ?
    ''', (session_id, datetime.now()))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return {'username': result[0], 'user_type': result[1]}
    return None

def delete_session(session_id):
    """Delete a session (logout)"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM sessions WHERE session_id = ?', (session_id,))
    
    conn.commit()
    conn.close()

# Modified session initialization
def init_session():
    """Initialize session with persistence"""
    # Check URL parameters for session ID
    query_params = st.query_params
    session_id = query_params.get('session_id')
    
    if not session_id:
        # Check if stored in session state
        session_id = st.session_state.get('session_id')
    
    if session_id:
        session_info = validate_session(session_id)
        if session_info:
            st.session_state.logged_in = True
            st.session_state.user_type = session_info['user_type']
            st.session_state.current_user = session_info['username']
            st.session_state.session_id = session_id
            return True
    
    # Initialize as logged out
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.current_user = None
    st.session_state.session_id = None
    return False
# Modified logout function
def logout_user():
    """Logout user and clean up session"""
    if st.session_state.get('session_id'):
        delete_session(st.session_state.session_id)
    
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.current_user = None
    st.session_state.session_id = None
    
    # Clear URL parameters
    st.query_params.clear()

def backup_database():
    """Create database backup"""
    if os.path.exists(DB_NAME):
        backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.db"
        import shutil
        shutil.copy2(DB_NAME, backup_name)

# Initialize database
init_database()

# Main application
def main():
    st.title("📚 D. P. Public School's Remedial Sessions Platform")
    
    # Initialize persistent session
    init_session()
    
    # Sidebar for navigation
    with st.sidebar:
        if st.session_state.logged_in:
            user_info = get_user_info(st.session_state.current_user)
            if user_info:
                st.write(f"Welcome, {user_info[0]}")
                st.write(f"Role: {user_info[1].title()}")
            
            if st.button("Logout"):
                logout_user()
                st.rerun()
        else:
            st.write("Please login to continue")
    
    # Authentication
    if not st.session_state.logged_in:
        auth_tab1, auth_tab2 = st.tabs(["Login", "Register"])
        
        with auth_tab1:
            st.subheader("Login")
            user_type = st.selectbox("Select User Type", ["teacher", "parent"])
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.button("Login"):
                is_authenticated, db_user_type = authenticate_user_with_session(username, password)
                if is_authenticated:
                    if db_user_type == user_type:
                        st.session_state.logged_in = True
                        st.session_state.user_type = user_type
                        st.session_state.current_user = username
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Invalid user type!")
                else:
                    st.error("Invalid username or password!")
        
        with auth_tab2:
            st.subheader("Register")
            reg_user_type = st.selectbox("Register as", ["teacher", "parent"])
            reg_full_name = st.text_input("Full Name")
            reg_username = st.text_input("Choose Username")
            reg_password = st.text_input("Choose Password", type="password")
            reg_confirm_password = st.text_input("Confirm Password", type="password")
            
            if st.button("Register"):
                if not all([reg_full_name, reg_username, reg_password, reg_confirm_password]):
                    st.error("Please fill all fields!")
                elif reg_password != reg_confirm_password:
                    st.error("Passwords don't match!")
                elif create_user(reg_username, reg_password, reg_user_type, reg_full_name):
                    st.success("Registration successful! Please login.")
                else:
                    st.error("Username already exists!")
    
    # Main application after login
    else:
        if st.session_state.user_type == 'teacher':
            teacher_dashboard()
        elif st.session_state.user_type == 'parent':
            parent_dashboard()

def teacher_dashboard():
    st.header("Teacher Dashboard")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Manage Students", 
        "Assess Competencies", 
        "Upload Materials", 
        "Track Progress", 
        "Daily Progress & Feedback"
    ])
    
    with tab1:
        st.subheader("Add Student")
        col1, col2 = st.columns(2)
        
        with col1:
            student_name = st.text_input("Student Name")
            student_grade = st.selectbox("Grade", ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
            student_id = st.text_input("Student ID")
        
        with col2:
            parent_username = st.text_input("Parent Username")
            
        if st.button("Add Student"):
            if all([student_name, student_grade, student_id, parent_username]):
                # Check if parent exists
                parent_info = get_user_info(parent_username)
                if parent_info and parent_info[1] == 'parent':
                    if add_student(student_id, student_name, student_grade, st.session_state.current_user, parent_username):
                        st.success(f"Student {student_name} added successfully!")
                    else:
                        st.error("Student ID already exists!")
                else:
                    st.error("Parent username not found or invalid!")
            else:
                st.error("Please fill all fields!")
        
        # Display students
        st.subheader("My Students")
        teacher_students = get_user_students(st.session_state.current_user, 'teacher')
        if teacher_students:
            for sid in teacher_students:
                student_info = get_student_info(sid)
                if student_info:
                    st.write(f"**{student_info[0]}** (ID: {sid}) - Grade {student_info[1]} - Parent: {student_info[3]}")
        else:
            st.info("No students added yet.")
    
    with tab2:
        st.subheader("Assess Student Competencies")
        teacher_students = get_user_students(st.session_state.current_user, 'teacher')
        
        if teacher_students:
            selected_student = st.selectbox("Select Student", teacher_students, 
                                          format_func=lambda x: f"{get_student_info(x)[0]} ({x})")
            
            # Replace this in both teacher_dashboard() tab2 and tab3
            if selected_student:
                student_info = get_student_info(selected_student)
                student_grade = student_info[1]  # Get the grade
    
            # Define grade-specific competencies
            if student_grade == "1":
                competency_areas = [
                # English
                "English - Listening & Auditory - Sound discrimination",
                "English - Speaking & Oral - Clear articulation", 
                "English - Visual Literacy - Letter recognition (a-z, A-Z)",
                "English - Pre-Reading/Reading - Phonemic blending",
                "English - Pre-Writing - Pencil grip/control",
                "English - Pre-Writing - Letter formation",
                # Math
                "Math - Numeracy Readiness - Number recognition (1-20)",
                "Math - Numeracy Readiness - Counting objects accurately",
                "Math - Spatial/Shape Awareness - Shape recognition", 
                "Math - Measurement Concepts - Size & quantity comparison",
                # Hindi
                "Hindi - Listening - Recognize Hindi sounds (स्वर, व्यंजन)",
                "Hindi - Speaking - Clear pronunciation",
                "Hindi - Speaking - Simple sentence formation",
                "Hindi - Speaking - Poem recitation",
                "Hindi - Reading - Letter/matra recognition",
                "Hindi - Reading - Reading small words",
                "Hindi - Writing - Letter formation",
                "Hindi - Writing - Copy simple words"
            ]
            else:
            # Keep existing competencies for other grades
                competency_areas = [
                "Reading Comprehension", "Mathematical Problem Solving", "Scientific Inquiry",
                "Writing Skills", "Critical Thinking", "Communication", "Creativity",
                "Time Management", "Research Skills", "Digital Literacy"
            ]
            
            st.subheader("Competency Assessment")
            competency_scores = {}
            
            for area in competency_areas:
                score = st.slider(f"{area}", 0, 100, 50, key=f"comp_{area}")
                competency_scores[area] = score
            
            notes = st.text_area("Additional Notes")
            
            if st.button("Save Assessment"):
                assessment_id = f"{selected_student}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                save_assessment(assessment_id, selected_student, st.session_state.current_user, competency_scores, notes)
                st.success("Assessment saved successfully!")
        else:
            st.info("No students to assess. Please add students first.")
    
    with tab3:
        st.subheader("Upload Learning Materials")
        teacher_students = get_user_students(st.session_state.current_user, 'teacher')
        
        if teacher_students:
            selected_student = st.selectbox("Select Student", teacher_students, 
                                          format_func=lambda x: f"{get_student_info(x)[0]} ({x})",
                                          key="upload_student")
            
            if selected_student:
                student_info = get_student_info(selected_student)
                student_grade = student_info[1]  # Get the grade
    
            # Define grade-specific competencies
            if student_grade == "1":
                competency_areas = [
                # English
                "English - Listening & Auditory - Sound discrimination",
                "English - Speaking & Oral - Clear articulation", 
                "English - Visual Literacy - Letter recognition (a-z, A-Z)",
                "English - Pre-Reading/Reading - Phonemic blending",
                "English - Pre-Writing - Pencil grip/control",
                "English - Pre-Writing - Letter formation",
                # Math
                "Math - Numeracy Readiness - Number recognition (1-20)",
                "Math - Numeracy Readiness - Counting objects accurately",
                "Math - Spatial/Shape Awareness - Shape recognition", 
                "Math - Measurement Concepts - Size & quantity comparison",
                # Hindi
                "Hindi - Listening - Recognize Hindi sounds (स्वर, व्यंजन)",
                "Hindi - Speaking - Clear pronunciation",
                "Hindi - Speaking - Simple sentence formation",
                "Hindi - Speaking - Poem recitation",
                "Hindi - Reading - Letter/matra recognition",
                "Hindi - Reading - Reading small words",
                "Hindi - Writing - Letter formation",
                "Hindi - Writing - Copy simple words"
            ]
            else:
            # Keep existing competencies for other grades
                competency_areas = [
                "Reading Comprehension", "Mathematical Problem Solving", "Scientific Inquiry",
                "Writing Skills", "Critical Thinking", "Communication", "Creativity",
                "Time Management", "Research Skills", "Digital Literacy"
            ]
            
            target_competency = st.selectbox("Target Competency", competency_areas)
            material_title = st.text_input("Material Title")
            material_description = st.text_area("Description")
            duration_days = st.number_input("Duration (Number of Days)", min_value=1, max_value=30, value=5)

            if selected_student:
                st.write(f"Uploading material for: {get_student_info(selected_student)[0]}")

            uploaded_file = st.file_uploader("Upload PDF", type=['pdf'], key=f"material_upload_{selected_student}_{datetime.now().strftime('%Y%m%d')}")

            if uploaded_file is not None:
                if validate_file_type(uploaded_file):
                    st.success(f"File '{uploaded_file.name}' selected successfully!")
                    st.write(f"File size: {len(uploaded_file.getvalue())} bytes")
    
                if st.button("Upload Material"):
                    if material_title and target_competency:
                        try:
                            material_id = f"{selected_student}_{target_competency}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                            file_data = uploaded_file.getvalue()  # Use getvalue() instead of read()
                            save_material(material_id, selected_student, st.session_state.current_user, 
                                        target_competency, material_title, material_description, 
                                        file_data, uploaded_file.name, duration_days)
                            st.success(f"Material '{material_title}' uploaded successfully for {duration_days} days!")
                            st.rerun()  # Refresh the page after upload
                        except Exception as e:
                            st.error(f"Error uploading file: {str(e)}")
                    else:
                        st.error("Please fill all required fields!")
            else:
                st.info("Please select a PDF file to upload.")
        else:
            st.info("No students available. Please add students first.")
    
    with tab4:
        st.subheader("Track Student Progress")
        teacher_students = get_user_students(st.session_state.current_user, 'teacher')
        
        if teacher_students:
            for sid in teacher_students:
                student_info = get_student_info(sid)
                if student_info:
                    st.write(f"**{student_info[0]}** (ID: {sid})")
                    
                    # Show progress for this student
                    progress_data = get_student_progress(sid)
                    
                    if progress_data:
                        for prog in progress_data:
                            status = "✅ Completed" if prog['completed'] else "⏳ In Progress"
                            st.write(f"- {prog['competency']}: {prog['title']} - {status}")
                            if prog['completed'] and prog['completed_at']:
                                st.write(f"  Completed on: {prog['completed_at']}")
                    else:
                        st.write("No progress recorded yet.")
                    
                    st.divider()
        else:
            st.info("No students to track.")
    
    with tab5:
        st.subheader("Daily Progress & Feedback")
        teacher_students = get_user_students(st.session_state.current_user, 'teacher')

        if teacher_students:
            selected_student = st.selectbox("Select Student", teacher_students, 
                                      format_func=lambda x: f"{get_student_info(x)[0]} ({x})",
                                      key="daily_review_student")
    
            daily_progress_data = get_student_daily_progress_summary(selected_student)
    
            if daily_progress_data:
                # Group by material
                from collections import defaultdict
                materials_progress = defaultdict(list)
        
                for progress in daily_progress_data:
                    materials_progress[progress['material_id']].append(progress)
        
                for material_id, progress_list in materials_progress.items():
                    st.write(f"**{progress_list[0]['title']}** - {progress_list[0]['competency']}")
            
                    for progress in progress_list:
                        status = "✅ Completed" if progress['completed'] else "⏳ Pending"
                        st.write(f"Day {progress['day_number']}: {status}")
                
                        if progress['completed_at']:
                            st.write(f"  Completed on: {progress['completed_at']}")
                
                        if progress['parent_comments']:
                            st.write(f"  **Parent Comment:** {progress['parent_comments']}")
                
                        # Show existing feedback
                        existing_feedback = get_daily_feedback(progress['daily_progress_id'])
                        if existing_feedback:
                            for fb in existing_feedback:
                                st.write(f"  **Your Feedback:** {fb['feedback']} ({fb['date']})")
                
                        # Provide feedback
                        feedback_key = f"feedback_{progress['daily_progress_id']}"
                        new_feedback = st.text_input(f"Add feedback for Day {progress['day_number']}", key=feedback_key)
                
                        if st.button(f"Submit Feedback", key=f"submit_{progress['daily_progress_id']}"):
                            if new_feedback:
                                feedback_id = f"{progress['daily_progress_id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                                save_daily_feedback(feedback_id, progress['daily_progress_id'], 
                                                st.session_state.current_user, new_feedback)
                                st.success("Feedback submitted!")
                                st.rerun()
                
                        st.write("---")
                    st.divider()
            else:
                st.info("No daily progress data available.")
        else:
            st.info("No students available.")


def parent_dashboard():
    st.header("Parent Dashboard")
    
    tab1, tab2, tab3 = st.tabs([
        "My Children", 
        "View Assessments", 
        "Learning Materials & Progress"
    ])
    
    with tab1:
        st.subheader("My Children")
        parent_students = get_user_students(st.session_state.current_user, 'parent')
        
        if parent_students:
            for sid in parent_students:
                student_info = get_student_info(sid)
                if student_info:
                    teacher_info = get_user_info(student_info[2])
                    st.write(f"**{student_info[0]}** (ID: {sid})")
                    st.write(f"Grade: {student_info[1]}")
                    st.write(f"Teacher: {teacher_info[0] if teacher_info else student_info[2]}")
                    st.divider()
        else:
            st.info("No children linked to your account. Please contact your child's teacher.")
    
    with tab2:
        st.subheader("View Competency Assessments")
        parent_students = get_user_students(st.session_state.current_user, 'parent')
        
        if parent_students:
            for sid in parent_students:
                student_info = get_student_info(sid)
                if student_info:
                    st.write(f"**{student_info[0]}** (ID: {sid})")
                    
                    # Find latest assessment for this student
                    assessment = get_latest_assessment(sid)
                    
                    if assessment:
                        st.write(f"Latest Assessment Date: {assessment['date']}")
                        
                        # Display competency scores
                        for competency, score in assessment['competencies'].items():
                            st.progress(score / 100, f"{competency}: {score}%")
                        
                        if assessment['notes']:
                            st.write(f"**Teacher's Notes:** {assessment['notes']}")
                    else:
                        st.write("No assessments available yet.")
                    
                    st.divider()
        else:
            st.info("No children linked to your account.")
    
    with tab3:
        st.subheader("Learning Materials")
        parent_students = get_user_students(st.session_state.current_user, 'parent')
    
        if parent_students:
            for sid in parent_students:
                student_info = get_student_info(sid)
                if student_info:
                    st.write(f"**{student_info[0]}** (ID: {sid})")
                
                    # Find materials for this student
                    materials = get_student_materials(sid)
                
                    if materials:
                        for material in materials:
                            st.write(f"**{material['title']}** - {material['competency']}")
                            st.write(f"Description: {material['description']}")
                            st.write(f"Duration: {material['duration_days']} days")
                        
                            # Download link
                            st.download_button(
                                label=f"📥 Download {material['filename']}",
                                data=material['file_data'],
                                file_name=material['filename'],
                                mime='application/octet-stream'
                            )
                        
                            # Daily progress tracking
                            st.write("**Daily Progress:**")
                        
                            daily_progress = get_daily_progress(material['material_id'], sid)
                            progress_dict = {dp['day_number']: dp for dp in daily_progress}
                        
                            for day in range(1, material['duration_days'] + 1):
                                col1, col2, col3 = st.columns([1, 3, 1])
                            
                                with col1:
                                    st.write(f"Day {day}")
                            
                                with col2:
                                    # Check if this day already has progress
                                    existing_progress = progress_dict.get(day)
                                
                                    if existing_progress:
                                        if existing_progress['completed']:
                                            st.success(f"✅ Completed on {existing_progress['completed_at']}")
                                            if existing_progress['parent_comments']:
                                                st.write(f"Your comment: {existing_progress['parent_comments']}")
                                        
                                            # Show teacher feedback
                                            daily_feedback = get_daily_feedback(existing_progress['daily_progress_id'])
                                            if daily_feedback:
                                                for fb in daily_feedback:
                                                    st.info(f"Teacher feedback: {fb['feedback']}")
                                        else:
                                            st.warning("⏳ In Progress")
                                            if existing_progress['parent_comments']:
                                                st.write(f"Your comment: {existing_progress['parent_comments']}")
                                    else:
                                        st.write("Not started")
                                
                                    # Comments input
                                    comment_key = f"comment_{material['material_id']}_day_{day}"
                                    existing_comment = existing_progress['parent_comments'] if existing_progress else ""
                                    parent_comment = st.text_input(f"Add comment for Day {day}", 
                                                             value=existing_comment, 
                                                             key=comment_key)
                            
                                with col3:
                                    if not existing_progress or not existing_progress['completed']:
                                        if st.button(f"Complete", key=f"complete_{material['material_id']}_day_{day}"):
                                            daily_progress_id = f"{material['material_id']}_day_{day}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                                            save_daily_progress(daily_progress_id, material['material_id'], sid, 
                                                          st.session_state.current_user, day, 
                                                          completed=True, parent_comments=parent_comment)
                                            st.success(f"Day {day} marked as completed!")
                                            st.rerun()
                                
                                    # Save comment button (for when not marking as complete)
                                    if st.button(f"Save Comment", key=f"save_comment_{material['material_id']}_day_{day}"):
                                        if parent_comment:
                                            daily_progress_id = f"{material['material_id']}_day_{day}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                                            save_daily_progress(daily_progress_id, material['material_id'], sid, 
                                                          st.session_state.current_user, day, 
                                                          completed=False, parent_comments=parent_comment)
                                            st.success("Comment saved!")
                                            st.rerun()
                        
                            st.divider()
                    else:
                        st.write("No materials available yet.")
                
                    st.divider()
        else:
            st.info("No children linked to your account.")
    

if __name__ == "__main__":
    main()
