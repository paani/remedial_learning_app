import streamlit as st

html_content = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>D.P. Public School - Remedial Sessions Platform</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            overflow-x: hidden;
        }

        /* Navigation */
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            z-index: 1000;
            padding: 1rem 0;
            transition: all 0.3s ease;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }

        .navbar.scrolled {
            background: rgba(255, 255, 255, 0.98);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .nav-links a:hover {
            color: #667eea;
        }

        .cta-button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 0.8rem 2rem;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
        }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="50%" cy="50%" r="50%"><stop offset="0%" style="stop-color:%23ffffff;stop-opacity:0.1"/><stop offset="100%" style="stop-color:%23ffffff;stop-opacity:0"/></radialGradient></defs><circle cx="200" cy="200" r="100" fill="url(%23a)"/><circle cx="800" cy="300" r="150" fill="url(%23a)"/><circle cx="400" cy="700" r="80" fill="url(%23a)"/></svg>');
            animation: float 20s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }

        .hero-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: 1fr 1fr;
            align-items: center;
            gap: 4rem;
            position: relative;
            z-index: 2;
        }

        .hero-content h1 {
            font-size: 4rem;
            font-weight: 800;
            color: white;
            margin-bottom: 1.5rem;
            line-height: 1.2;
            animation: slideInUp 1s ease-out;
        }

        .hero-content .subtitle {
            font-size: 1.3rem;
            color: rgba(255, 255, 255, 0.9);
            margin-bottom: 2rem;
            animation: slideInUp 1s ease-out 0.2s both;
        }

        .hero-content .description {
            font-size: 1.1rem;
            color: rgba(255, 255, 255, 0.8);
            margin-bottom: 3rem;
            animation: slideInUp 1s ease-out 0.4s both;
        }

        .hero-buttons {
            display: flex;
            gap: 1rem;
            animation: slideInUp 1s ease-out 0.6s both;
        }

        .btn-primary {
            background: white;
            color: #667eea;
            padding: 1rem 2.5rem;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
        }

        .btn-secondary {
            background: transparent;
            color: white;
            padding: 1rem 2.5rem;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50px;
            font-weight: 600;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.5);
        }

        .hero-visual {
            display: flex;
            justify-content: center;
            align-items: center;
            animation: slideInRight 1s ease-out 0.8s both;
        }

        .hero-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 3rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            text-align: center;
            color: white;
            transform: perspective(1000px) rotateY(-10deg);
            transition: transform 0.3s ease;
        }

        .hero-card:hover {
            transform: perspective(1000px) rotateY(0deg);
        }

        .hero-card i {
            font-size: 4rem;
            margin-bottom: 1rem;
            color: rgba(255, 255, 255, 0.9);
        }

        .hero-card h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
        }

        .hero-card p {
            color: rgba(255, 255, 255, 0.8);
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        /* Stats Section */
        .stats {
            padding: 5rem 0;
            background: #f8fafc;
            position: relative;
        }

        .stats::before {
            content: '';
            position: absolute;
            top: -50px;
            left: 0;
            right: 0;
            height: 100px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            clip-path: polygon(0 0, 100% 0, 100% 50%, 0 100%);
        }

        .stats-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
        }

        .stat-item {
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }

        .stat-item:hover {
            transform: translateY(-10px);
        }

        .stat-number {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }

        .stat-label {
            font-size: 1.2rem;
            color: #666;
            font-weight: 500;
        }

        /* Features Section */
        .features {
            padding: 8rem 0;
            background: white;
        }

        .section-header {
            text-align: center;
            margin-bottom: 5rem;
        }

        .section-header h2 {
            font-size: 3rem;
            font-weight: 700;
            color: #333;
            margin-bottom: 1rem;
        }

        .section-header p {
            font-size: 1.2rem;
            color: #666;
            max-width: 600px;
            margin: 0 auto;
        }

        .features-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 3rem;
        }

        .feature-card {
            background: white;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border: 1px solid rgba(102, 126, 234, 0.1);
            position: relative;
            overflow: hidden;
        }

        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .feature-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 30px 80px rgba(0, 0, 0, 0.15);
        }

        .feature-icon {
            width: 80px;
            height: 80px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 2rem;
            font-size: 2rem;
            color: white;
        }

        .feature-card h3 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #333;
            margin-bottom: 1rem;
        }

        .feature-card p {
            color: #666;
            line-height: 1.7;
            font-size: 1.1rem;
        }

        /* Testimonials */
        .testimonials {
            padding: 8rem 0;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            position: relative;
        }

        .testimonials::before {
            content: '';
            position: absolute;
            top: -50px;
            left: 0;
            right: 0;
            height: 100px;
            background: white;
            clip-path: polygon(0 0, 100% 0, 100% 50%, 0 100%);
        }

        .testimonials-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .testimonials .section-header h2 {
            color: white;
        }

        .testimonials .section-header p {
            color: rgba(255, 255, 255, 0.9);
        }

        .testimonials-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 3rem;
        }

        .testimonial-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            border-radius: 20px;
            padding: 3rem;
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white;
            transition: transform 0.3s ease;
        }

        .testimonial-card:hover {
            transform: translateY(-10px);
        }

        .testimonial-text {
            font-size: 1.2rem;
            line-height: 1.7;
            margin-bottom: 2rem;
            font-style: italic;
        }

        .testimonial-author {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .author-avatar {
            width: 60px;
            height: 60px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }

        .author-info h4 {
            font-size: 1.1rem;
            margin-bottom: 0.2rem;
        }

        .author-info p {
            color: rgba(255, 255, 255, 0.8);
        }

        /* CTA Section */
        .cta {
            padding: 8rem 0;
            background: #1a1a1a;
            color: white;
            text-align: center;
        }

        .cta-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .cta h2 {
            font-size: 3.5rem;
            font-weight: 700;
            margin-bottom: 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .cta p {
            font-size: 1.3rem;
            margin-bottom: 3rem;
            color: #ccc;
            line-height: 1.7;
        }

        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
        }

        /* Footer */
        .footer {
            background: #0a0a0a;
            color: white;
            padding: 3rem 0;
        }

        .footer-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 3rem;
        }

        .footer-section h3 {
            font-size: 1.3rem;
            margin-bottom: 1rem;
            color: #667eea;
        }

        .footer-section p,
        .footer-section a {
            color: #ccc;
            text-decoration: none;
            line-height: 1.7;
        }

        .footer-section a:hover {
            color: #667eea;
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid #333;
            color: #666;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-container {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .hero-content h1 {
                font-size: 2.5rem;
            }

            .nav-links {
                display: none;
            }

            .hero-buttons {
                flex-direction: column;
                align-items: center;
            }

            .testimonials-grid {
                grid-template-columns: 1fr;
            }

            .cta h2 {
                font-size: 2.5rem;
            }
        }

        /* Scroll animations */
        .scroll-fade-in {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.6s ease;
        }

        .scroll-fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <div class="logo">🎓 D.P. Public School</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#features">Features</a></li>
                <li><a href="#testimonials">Reviews</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <a href="#" class="cta-button">Get Started</a>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-container">
            <div class="hero-content">
                <h1>Transform Your Child's Learning Journey</h1>
                <p class="subtitle">Remedial Sessions Platform</p>
                <p class="description">
                    Bridging the gap between classroom and home with our innovative parent-teacher 
                    collaborative platform. Personalized learning, real-time progress tracking, 
                    and seamless communication for every child's success.
                </p>
                <div class="hero-buttons">
                    <a href="#" class="btn-primary">Launch Platform</a>
                    <a href="#features" class="btn-secondary">Learn More</a>
                </div>
            </div>
            <div class="hero-visual">
                <div class="hero-card">
                    <i class="fas fa-graduation-cap"></i>
                    <h3>Empowering Education</h3>
                    <p>Where every child's potential meets opportunity</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Stats Section -->
    <section class="stats">
        <div class="stats-container">
            <div class="stat-item scroll-fade-in">
                <div class="stat-number">150+</div>
                <div class="stat-label">Students Supported</div>
            </div>
            <div class="stat-item scroll-fade-in">
                <div class="stat-number">75+</div>
                <div class="stat-label">Teachers Connected</div>
            </div>
            <div class="stat-item scroll-fade-in">
                <div class="stat-number">300+</div>
                <div class="stat-label">Parents Engaged</div>
            </div>
            <div class="stat-item scroll-fade-in">
                <div class="stat-number">98%</div>
                <div class="stat-label">Satisfaction Rate</div>
            </div>
        </div>
    </section>

    <!-- Features Section -->
    <section class="features" id="features">
        <div class="section-header scroll-fade-in">
            <h2>Powerful Features for Modern Education</h2>
            <p>Discover how our platform revolutionizes the way teachers and parents collaborate to support student success</p>
        </div>
        <div class="features-container">
            <div class="feature-card scroll-fade-in">
                <div class="feature-icon">
                    <i class="fas fa-bullseye"></i>
                </div>
                <h3>Personalized Assessment</h3>
                <p>Advanced competency tracking across all subjects with detailed analytics and progress visualization for targeted learning interventions.</p>
            </div>
            <div class="feature-card scroll-fade-in">
                <div class="feature-icon">
                    <i class="fas fa-book-open"></i>
                </div>
                <h3>Smart Learning Materials</h3>
                <p>AI-powered content recommendations and customized worksheets tailored to each student's learning style and pace.</p>
            </div>
            <div class="feature-card scroll-fade-in">
                <div class="feature-icon">
                    <i class="fas fa-chart-line"></i>
                </div>
                <h3>Real-time Analytics</h3>
                <p>Comprehensive dashboard with live progress tracking, completion rates, and predictive insights for proactive support.</p>
            </div>
            <div class="feature-card scroll-fade-in">
                <div class="feature-icon">
                    <i class="fas fa-comments"></i>
                </div>
                <h3>Seamless Communication</h3>
                <p>Integrated messaging system with instant notifications, file sharing, and video conferencing capabilities.</p>
            </div>
            <div class="feature-card scroll-fade-in">
                <div class="feature-icon">
                    <i class="fas fa-trophy"></i>
                </div>
                <h3>Achievement Tracking</h3>
                <p>Gamified learning experience with badges, certificates, and milestone celebrations to keep students motivated.</p>
            </div>
            <div class="feature-card scroll-fade-in">
                <div class="feature-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <h3>Enterprise Security</h3>
                <p>Bank-level security with end-to-end encryption, secure authentication, and GDPR-compliant data protection.</p>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials" id="testimonials">
        <div class="testimonials-container">
            <div class="section-header scroll-fade-in">
                <h2>What Our Community Says</h2>
                <p>Real stories from teachers and parents who have transformed their educational experience</p>
            </div>
            <div class="testimonials-grid">
                <div class="testimonial-card scroll-fade-in">
                    <p class="testimonial-text">
                        "This platform has completely revolutionized how I connect with my students' families. 
                        The real-time progress tracking and instant communication have made my teaching more 
                        effective and rewarding than ever before."
                    </p>
                    <div class="testimonial-author">
                        <div class="author-avatar">
                            <i class="fas fa-user"></i>
                        </div>
                        <div class="author-info">
                            <h4>Mrs. Priya Sharma</h4>
                            <p>Grade 3 Teacher</p>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card scroll-fade-in">
                    <p class="testimonial-text">
                        "As a parent, I love being able to see exactly what my daughter is working on and 
                        how she's progressing. The detailed feedback from her teacher helps me provide 
                        the right support at home. It's truly a game-changer!"
                    </p>
                    <div class="testimonial-author">
                        <div class="author-avatar">
                            <i class="fas fa-user"></i>
                        </div>
                        <div class="author-info">
                            <h4>Mr. Rajesh Kumar</h4>
                            <p>Parent of Grade 1 Student</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->
    <section class="cta">
        <div class="cta-container scroll-fade-in">
            <h2>Ready to Transform Education?</h2>
            <p>
                Join the D.P. Public School community in creating a collaborative educational 
                environment where every child can thrive, learn, and reach their full potential 
                through innovative technology and dedicated support.
            </p>
            <div class="cta-buttons">
                <a href="#" class="btn-primary">Start Your Journey</a>
                <a href="#" class="btn-secondary">Schedule Demo</a>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-container">
            <div class="footer-section">
                <h3>D.P. Public School</h3>
                <p>Empowering every child's educational journey through innovative technology and collaborative learning.</p>
            </div>
            <div class="footer-section">
                <h3>Quick Links</h3>
                <p><a href="#home">Home</a></p>
                <p><a href="#features">Features</a></p>
                <p><a href="#testimonials">Testimonials</a></p>
                <p><a href="#contact">Contact</a></p>
            </div>
            <div class="footer-section">
                <h3>Support</h3>
                <p><a href="#">Help Center</a></p>
                <p><a href="#">Getting Started</a></p>
                <p><a href="#">Privacy Policy</a></p>
                <p><a href="#">Terms of Service</a></p>
            </div>
            <div class="footer-section">
                <h3>Contact</h3>
                <p>📧 info@dpschool.edu</p>
                <p>📞 +91 98765 43210</p>
                <p>📍 Education District, City</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 D.P. Public School. All rights reserved. Built with ❤️ for education.</p>
        </div>
    </footer>

    <script>
        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Scroll animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.scroll-fade-in').forEach(el => {
            observer.observe(el);
        });

        // Add some interactive elements
        document.querySelectorAll('.feature-card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-15px) scale(1.02)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(-15px) scale(1)';
            });
        });

        // Simulate button clicks
        document.querySelectorAll('.btn-primary, .btn-secondary, .cta-button').forEach(button => {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Create ripple effect
                const ripple = document.createElement('div');
                ripple.style.position = 'absolute';
                ripple.style.width = '20px';
                ripple.style.height = '20px';
                ripple.style.background = 'rgba(255, 255, 255, 0.5)';
                ripple.style.borderRadius = '50%';
                ripple.style.transform = 'scale(0)';
                ripple.style.animation = 'ripple 0.6s linear';
                ripple.style.left = e.offsetX - 10 + 'px';
                ripple.style.top = e.offsetY - 10 + 'px';
                
                this.style.position = 'relative';
                this.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
                
                // Show different messages based on button
                if (this.textContent.includes('Launch Platform') || this.textContent.includes('Start Your Journey')) {
                    alert('🚀 Ready to launch! This would redirect to your main application: streamlit run app4_copy.py');
                } else if (this.textContent.includes('Schedule Demo') || this.textContent.includes('Learn More')) {
                    alert('📅 Demo scheduled! We\'ll contact you soon to arrange a personalized demonstration.');
                } else if (this.textContent.includes('Get Started')) {
                    alert('✨ Welcome aboard! Let\'s begin your educational transformation journey.');
                }
            });
        });

        // Add CSS for ripple animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes ripple {
                to {
                    transform: scale(4);
                    opacity: 0;
                }
            }
            
            .floating-elements {
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: -1;
            }
            
            .floating-element {
                position: absolute;
                width: 20px;
                height: 20px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                border-radius: 50%;
                opacity: 0.1;
                animation: floatUp 10s infinite linear;
            }
            
            @keyframes floatUp {
                0% {
                    transform: translateY(100vh) scale(0);
                    opacity: 0;
                }
                10% {
                    opacity: 0.1;
                }
                90% {
                    opacity: 0.1;
                }
                100% {
                    transform: translateY(-100px) scale(1);
                    opacity: 0;
                }
            }
            
            .hero-card {
                animation: cardFloat 6s ease-in-out infinite;
            }
            
            @keyframes cardFloat {
                0%, 100% {
                    transform: perspective(1000px) rotateY(-10deg) translateY(0px);
                }
                50% {
                    transform: perspective(1000px) rotateY(-10deg) translateY(-20px);
                }
            }
            
            .feature-icon {
                animation: iconPulse 3s ease-in-out infinite;
            }
            
            @keyframes iconPulse {
                0%, 100% {
                    transform: scale(1);
                }
                50% {
                    transform: scale(1.05);
                }
            }
            
            .stat-number {
                animation: countUp 2s ease-out;
            }
            
            @keyframes countUp {
                from {
                    opacity: 0;
                    transform: translateY(20px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            /* Mobile responsiveness improvements */
            @media (max-width: 480px) {
                .hero-content h1 {
                    font-size: 2rem;
                }
                
                .hero-content .subtitle {
                    font-size: 1.1rem;
                }
                
                .hero-content .description {
                    font-size: 1rem;
                }
                
                .btn-primary, .btn-secondary {
                    padding: 0.8rem 1.5rem;
                    font-size: 1rem;
                }
                
                .feature-card {
                    padding: 2rem;
                }
                
                .section-header h2 {
                    font-size: 2rem;
                }
                
                .cta h2 {
                    font-size: 2rem;
                }
                
                .testimonial-card {
                    padding: 2rem;
                }
            }
            
            /* Dark mode support */
            @media (prefers-color-scheme: dark) {
                .navbar {
                    background: rgba(26, 26, 26, 0.95);
                }
                
                .navbar.scrolled {
                    background: rgba(26, 26, 26, 0.98);
                }
                
                .nav-links a {
                    color: #fff;
                }
                
                .stats {
                    background: #1a1a1a;
                }
                
                .stat-item {
                    background: #2a2a2a;
                    color: #fff;
                }
                
                .features {
                    background: #0f0f0f;
                }
                
                .feature-card {
                    background: #1a1a1a;
                    color: #fff;
                    border: 1px solid rgba(102, 126, 234, 0.2);
                }
                
                .section-header h2 {
                    color: #fff;
                }
                
                .section-header p {
                    color: #ccc;
                }
                
                .feature-card p {
                    color: #ccc;
                }
            }
        `;
        document.head.appendChild(style);

        // Create floating background elements
        function createFloatingElements() {
            const container = document.createElement('div');
            container.className = 'floating-elements';
            document.body.appendChild(container);

            function createFloatingElement() {
                const element = document.createElement('div');
                element.className = 'floating-element';
                element.style.left = Math.random() * 100 + '%';
                element.style.animationDelay = Math.random() * 10 + 's';
                element.style.animationDuration = (Math.random() * 10 + 10) + 's';
                container.appendChild(element);

                setTimeout(() => {
                    element.remove();
                }, 20000);
            }

            // Create floating elements periodically
            setInterval(createFloatingElement, 2000);
        }

        // Initialize floating elements
        createFloatingElements();

        // Add loading animation
        window.addEventListener('load', function() {
            document.body.style.opacity = '0';
            document.body.style.transition = 'opacity 0.5s ease-in-out';
            
            setTimeout(() => {
                document.body.style.opacity = '1';
            }, 100);
        });

        // Parallax effect for hero section
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const parallax = document.querySelector('.hero::before');
            if (parallax) {
                parallax.style.transform = `translateY(${scrolled * 0.5}px)`;
            }
        });

        // Add typing effect to hero title
        function typeWriter(element, text, speed = 50) {
            let i = 0;
            element.innerHTML = '';
            
            function type() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            }
            
            type();
        }

        // Initialize typing effect when page loads
        window.addEventListener('load', function() {
            const heroTitle = document.querySelector('.hero-content h1');
            const originalText = heroTitle.textContent;
            
            setTimeout(() => {
                typeWriter(heroTitle, originalText, 100);
            }, 1000);
        });

        // Add progress bar for scroll
        const progressBar = document.createElement('div');
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 3px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            z-index: 9999;
            transition: width 0.1s ease;
        `;
        document.body.appendChild(progressBar);

        window.addEventListener('scroll', function() {
            const scrollTop = window.pageYOffset;
            const docHeight = document.body.scrollHeight - window.innerHeight;
            const scrollPercent = (scrollTop / docHeight) * 100;
            progressBar.style.width = scrollPercent + '%';
        });

        // Add hover effects to testimonial cards
        document.querySelectorAll('.testimonial-card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-10px) scale(1.02)';
                this.style.boxShadow = '0 30px 60px rgba(0, 0, 0, 0.2)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(-10px) scale(1)';
                this.style.boxShadow = 'none';
            });
        });

        // Add stats counter animation
        function animateStats() {
            const stats = document.querySelectorAll('.stat-number');
            
            stats.forEach(stat => {
                const target = parseInt(stat.textContent);
                const increment = target / 100;
                let current = 0;
                
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    stat.textContent = Math.floor(current) + (stat.textContent.includes('%') ? '%' : '+');
                }, 20);
            });
        }

        // Trigger stats animation when stats section comes into view
        const statsObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateStats();
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        const statsSection = document.querySelector('.stats');
        if (statsSection) {
            statsObserver.observe(statsSection);
        }

        // Add Easter egg - Konami code
        let konamiCode = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
        let konamiIndex = 0;

        document.addEventListener('keydown', function(e) {
            if (e.keyCode === konamiCode[konamiIndex]) {
                konamiIndex++;
                if (konamiIndex === konamiCode.length) {
                    // Easter egg activated
                    document.body.style.animation = 'rainbow 2s infinite';
                    setTimeout(() => {
                        document.body.style.animation = '';
                        alert('🎉 Easter egg activated! You found the secret code!');
                    }, 2000);
                    konamiIndex = 0;
                }
            } else {
                konamiIndex = 0;
            }
        });

        // Add rainbow animation for Easter egg
        const rainbowStyle = document.createElement('style');
        rainbowStyle.textContent = `
            @keyframes rainbow {
                0% { filter: hue-rotate(0deg); }
                100% { filter: hue-rotate(360deg); }
            }
        `;
        document.head.appendChild(rainbowStyle);

        console.log('🎓 D.P. Public School Landing Page loaded successfully!');
        console.log('💡 Try the Konami code: ↑↑↓↓←→←→BA');
    </script>
</body>
</html>
"""

st.markdown(html_content, unsafe_allow_html=True)
