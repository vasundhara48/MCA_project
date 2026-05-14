SKILL_CATEGORIES = {
    'Programming Languages': [
        'Python', 'JavaScript', 'Java', 'C++', 'C#', 'Go', 'Rust',
        'Ruby', 'PHP', 'Swift', 'Kotlin', 'TypeScript', 'R', 'Scala',
        'Dart', 'MATLAB', 'Perl', 'Haskell', 'Elixir', 'Clojure',
    ],
    'Web Frontend': [
        'HTML5', 'CSS3', 'React', 'Angular', 'Vue.js', 'Next.js',
        'Nuxt.js', 'Svelte', 'SvelteKit', 'Tailwind CSS', 'Bootstrap',
        'Sass/SCSS', 'Webpack', 'Vite', 'Responsive Design',
        'Accessibility', 'PWA', 'SEO',
    ],
    'Web Backend': [
        'Node.js', 'Express.js', 'Django', 'Flask', 'FastAPI',
        'Spring Boot', 'ASP.NET', 'Laravel', 'Ruby on Rails',
        'REST APIs', 'GraphQL', 'WebSockets', 'Microservices',
        'Serverless', 'API Design', 'Authentication',
    ],
    'Databases': [
        'MySQL', 'PostgreSQL', 'MongoDB', 'Redis', 'SQLite',
        'Oracle DB', 'Cassandra', 'DynamoDB', 'Elasticsearch',
        'Neo4j', 'Firebase', 'Supabase', 'CouchDB', 'MariaDB',
    ],
    'Cloud & DevOps': [
        'AWS', 'Google Cloud', 'Microsoft Azure', 'Docker',
        'Kubernetes', 'Terraform', 'Ansible', 'Jenkins',
        'GitHub Actions', 'GitLab CI', 'CI/CD', 'Nginx',
        'Apache', 'Linux', 'Prometheus', 'Grafana', 'ELK Stack',
        'Helm', 'Vault', 'Consul',
    ],
    'Data Science & AI': [
        'Machine Learning', 'Deep Learning', 'NLP', 'Computer Vision',
        'TensorFlow', 'PyTorch', 'Scikit-learn', 'Pandas', 'NumPy',
        'Matplotlib', 'Seaborn', 'Tableau', 'Power BI', 'Apache Spark',
        'Hadoop', 'Feature Engineering', 'A/B Testing', 'Statistics',
        'Data Visualization', 'Time Series Analysis',
    ],
    'Mobile Development': [
        'React Native', 'Flutter', 'Swift', 'Kotlin',
        'iOS Development', 'Android Development', 'Xamarin',
        'Ionic', 'Capacitor', 'App Store Deployment',
        'Mobile UI/UX', 'Push Notifications',
    ],
    'Design & UX': [
        'UI Design', 'UX Research', 'Figma', 'Adobe XD',
        'Sketch', 'Prototyping', 'Wireframing', 'Design Systems',
        'User Testing', 'Information Architecture', 'Interaction Design',
        'Visual Design', 'Adobe Photoshop', 'Adobe Illustrator',
    ],
    'Security': [
        'Cybersecurity', 'Penetration Testing', 'OWASP Top 10',
        'Encryption', 'OAuth/JWT', 'Network Security', 'Security Auditing',
        'Compliance (GDPR/HIPAA)', 'Threat Modeling', 'SIEM',
        'Incident Response', 'Vulnerability Assessment',
    ],
    'Testing & QA': [
        'Unit Testing', 'Integration Testing', 'E2E Testing',
        'Selenium', 'Jest', 'Cypress', 'Playwright', 'PyTest',
        'JMeter', 'Load Testing', 'TDD', 'BDD',
    ],
    'Soft Skills & Methods': [
        'Agile/Scrum', 'Kanban', 'Communication', 'Team Collaboration',
        'Problem Solving', 'Project Management', 'Technical Writing',
        'Leadership', 'Critical Thinking', 'Time Management',
        'Presentation Skills', 'Mentoring',
    ],
    'Other Tools': [
        'Git', 'GitHub', 'GitLab', 'Bitbucket', 'Jira',
        'Confluence', 'Slack', 'Postman', 'VS Code',
        'IntelliJ IDEA', 'Vim/Neovim', 'Algorithms',
        'Data Structures', 'System Design', 'Performance Optimization',
    ],
}

ROLES = {
    'Frontend Developer': {
        'core_skills': [
            'HTML5', 'CSS3', 'JavaScript', 'React', 'Responsive Design',
            'Git', 'REST APIs',
        ],
        'nice_to_have': [
            'TypeScript', 'Vue.js', 'Angular', 'Next.js', 'Tailwind CSS',
            'Sass/SCSS', 'Webpack', 'Jest', 'Accessibility', 'SEO',
            'PWA', 'Performance Optimization', 'Figma',
        ],
        'description': 'Build modern, responsive user interfaces and interactive web experiences.',
    },
    'Backend Developer': {
        'core_skills': [
            'Python', 'Node.js', 'REST APIs', 'PostgreSQL', 'Git',
            'Authentication', 'Linux',
        ],
        'nice_to_have': [
            'Django', 'FastAPI', 'Express.js', 'GraphQL', 'Docker',
            'Redis', 'MongoDB', 'Microservices', 'CI/CD',
            'WebSockets', 'API Design', 'Nginx',
        ],
        'description': 'Design and build server-side applications, APIs, and data pipelines.',
    },
    'Full Stack Developer': {
        'core_skills': [
            'HTML5', 'CSS3', 'JavaScript', 'React', 'Node.js',
            'PostgreSQL', 'REST APIs', 'Git', 'Authentication',
        ],
        'nice_to_have': [
            'TypeScript', 'Next.js', 'Django', 'Docker', 'MongoDB',
            'Redis', 'CI/CD', 'AWS', 'GraphQL', 'Tailwind CSS',
            'Unit Testing',
        ],
        'description': 'Work across the entire stack from frontend UI to backend services and databases.',
    },
    'Data Scientist': {
        'core_skills': [
            'Python', 'Machine Learning', 'Statistics', 'Pandas',
            'NumPy', 'Data Visualization', 'SQL',
        ],
        'nice_to_have': [
            'Deep Learning', 'NLP', 'TensorFlow', 'PyTorch',
            'Scikit-learn', 'Apache Spark', 'A/B Testing',
            'Feature Engineering', 'Tableau', 'Time Series Analysis',
            'Computer Vision', 'Jupyter Notebook',
        ],
        'description': 'Extract insights from data using statistical methods and machine learning.',
    },
    'Data Analyst': {
        'core_skills': [
            'SQL', 'Python', 'Excel', 'Data Visualization', 'Statistics',
        ],
        'nice_to_have': [
            'Tableau', 'Power BI', 'Pandas', 'A/B Testing',
            'Google Analytics', 'R', 'Data Cleaning', 'Matplotlib',
            'Seaborn', 'ETL',
        ],
        'description': 'Analyze data to help organizations make better business decisions.',
    },
    'DevOps Engineer': {
        'core_skills': [
            'Linux', 'Docker', 'Kubernetes', 'CI/CD', 'AWS',
            'Python', 'Git',
        ],
        'nice_to_have': [
            'Terraform', 'Ansible', 'Prometheus', 'Grafana',
            'ELK Stack', 'Jenkins', 'GitHub Actions', 'Helm',
            'Nginx', 'Vault', 'Google Cloud', 'Microsoft Azure',
        ],
        'description': 'Automate infrastructure, deployment pipelines, and ensure system reliability.',
    },
    'Mobile App Developer': {
        'core_skills': [
            'JavaScript', 'React Native', 'Flutter', 'Git',
            'REST APIs', 'Mobile UI/UX',
        ],
        'nice_to_have': [
            'Swift', 'Kotlin', 'iOS Development', 'Android Development',
            'TypeScript', 'Push Notifications', 'Firebase',
            'App Store Deployment', 'Dart', 'GraphQL',
        ],
        'description': 'Build native and cross-platform mobile applications for iOS and Android.',
    },
    'Cloud Engineer': {
        'core_skills': [
            'AWS', 'Docker', 'Kubernetes', 'Linux', 'Terraform',
            'Python', 'Networking',
        ],
        'nice_to_have': [
            'Google Cloud', 'Microsoft Azure', 'Ansible', 'CI/CD',
            'Prometheus', 'Grafana', 'Serverless', 'Helm',
            'Vault', 'Elasticsearch',
        ],
        'description': 'Design, deploy, and manage cloud infrastructure and services.',
    },
    'Cybersecurity Analyst': {
        'core_skills': [
            'Cybersecurity', 'Network Security', 'Linux', 'Python',
            'OWASP Top 10', 'Encryption',
        ],
        'nice_to_have': [
            'Penetration Testing', 'SIEM', 'Threat Modeling',
            'Incident Response', 'Vulnerability Assessment',
            'OAuth/JWT', 'Compliance (GDPR/HIPAA)', 'Docker',
            'Cloud Security', 'Forensics',
        ],
        'description': 'Protect systems and networks from security threats and vulnerabilities.',
    },
    'Machine Learning Engineer': {
        'core_skills': [
            'Python', 'Machine Learning', 'Deep Learning', 'TensorFlow',
            'PyTorch', 'SQL', 'Git',
        ],
        'nice_to_have': [
            'NLP', 'Computer Vision', 'Scikit-learn', 'Docker',
            'AWS', 'Kubernetes', 'Feature Engineering', 'MLOps',
            'Apache Spark', 'Model Deployment', 'Data Structures',
            'Algorithms',
        ],
        'description': 'Build and deploy machine learning models at scale in production systems.',
    },
    'UI/UX Designer': {
        'core_skills': [
            'UI Design', 'UX Research', 'Figma', 'Wireframing',
            'Prototyping', 'User Testing',
        ],
        'nice_to_have': [
            'Adobe XD', 'Sketch', 'Design Systems', 'Interaction Design',
            'Information Architecture', 'Visual Design', 'HTML5', 'CSS3',
            'Accessibility', 'Adobe Photoshop', 'Adobe Illustrator',
        ],
        'description': 'Design intuitive, beautiful user experiences and interfaces for digital products.',
    },
    'Product Manager': {
        'core_skills': [
            'Agile/Scrum', 'Communication', 'Problem Solving',
            'Project Management', 'Data Visualization', 'SQL',
        ],
        'nice_to_have': [
            'A/B Testing', 'Tableau', 'Jira', 'Confluence',
            'Technical Writing', 'Leadership', 'User Testing',
            'Wireframing', 'Google Analytics', 'Roadmapping',
        ],
        'description': 'Define product vision, prioritize features, and coordinate cross-functional teams.',
    },
    'QA Engineer': {
        'core_skills': [
            'Unit Testing', 'Integration Testing', 'Selenium', 'Python',
            'Git', 'Agile/Scrum',
        ],
        'nice_to_have': [
            'Cypress', 'Playwright', 'Jest', 'PyTest', 'JMeter',
            'Load Testing', 'TDD', 'BDD', 'E2E Testing',
            'Docker', 'CI/CD', 'Postman',
        ],
        'description': 'Ensure software quality through systematic testing strategies and automation.',
    },
    'Blockchain Developer': {
        'core_skills': [
            'JavaScript', 'Solidity', 'Ethereum', 'Web3.js',
            'Git', 'Smart Contracts',
        ],
        'nice_to_have': [
            'Python', 'Go', 'Rust', 'Hyperledger', 'DeFi',
            'NFT Standards', 'Cryptography', 'Docker',
            'React', 'Node.js',
        ],
        'description': 'Build decentralized applications and smart contracts on blockchain platforms.',
    },
    'Game Developer': {
        'core_skills': [
            'C++', 'C#', 'Unity', 'Unreal Engine', 'Algorithms',
            'Data Structures',
        ],
        'nice_to_have': [
            'Python', 'JavaScript', '3D Math', 'Physics Engines',
            'Shader Programming', 'AI Programming', 'Git',
            'Performance Optimization', 'Mobile UI/UX', 'Networking',
        ],
        'description': 'Create interactive gaming experiences using game engines and graphics programming.',
    },
    'Technical Writer': {
        'core_skills': [
            'Technical Writing', 'Communication', 'Git', 'Markdown',
            'Research Skills',
        ],
        'nice_to_have': [
            'HTML5', 'CSS3', 'JavaScript', 'Confluence', 'Jira',
            'Figma', 'API Documentation', 'SEO', 'Agile/Scrum',
            'Video Editing',
        ],
        'description': 'Create clear, comprehensive documentation for software products and APIs.',
    },
    'Database Administrator': {
        'core_skills': [
            'PostgreSQL', 'MySQL', 'SQL', 'Linux', 'Backup & Recovery',
            'Performance Tuning',
        ],
        'nice_to_have': [
            'Oracle DB', 'MongoDB', 'Redis', 'Elasticsearch',
            'Docker', 'Python', 'Shell Scripting', 'AWS',
            'Replication', 'Monitoring',
        ],
        'description': 'Manage, optimize, and maintain database systems for performance and reliability.',
    },
    'System Administrator': {
        'core_skills': [
            'Linux', 'Networking', 'Bash/Shell', 'Python', 'AWS',
            'Monitoring',
        ],
        'nice_to_have': [
            'Docker', 'Ansible', 'Terraform', 'Nginx', 'Prometheus',
            'Grafana', 'Jenkins', 'Virtualization', 'DNS',
            'Security Hardening',
        ],
        'description': 'Manage and maintain IT infrastructure, servers, and system operations.',
    },
    'AI Research Scientist': {
        'core_skills': [
            'Python', 'Deep Learning', 'Machine Learning', 'TensorFlow',
            'PyTorch', 'Algorithms', 'Statistics',
        ],
        'nice_to_have': [
            'NLP', 'Computer Vision', 'Reinforcement Learning',
            'Mathematical Modeling', 'Research Publication',
            'C++', 'CUDA', 'Distributed Computing', 'Scikit-learn',
            'Feature Engineering',
        ],
        'description': 'Conduct cutting-edge research in artificial intelligence and publish findings.',
    },
}

ALL_SKILLS = []
for skills in SKILL_CATEGORIES.values():
    ALL_SKILLS.extend(skills)
ALL_SKILLS = sorted(set(ALL_SKILLS))


def get_role_data(role_name):
    return ROLES.get(role_name, {})


def analyze_gap(user_skills, target_role):
    role_data = get_role_data(target_role)
    if not role_data:
        return None

    core = role_data.get('core_skills', [])
    nice = role_data.get('nice_to_have', [])

    user_set = set(s.lower().strip() for s in user_skills)
    core_set = set(s.lower().strip() for s in core)
    nice_set = set(s.lower().strip() for s in nice)

    original_core = {s.lower().strip(): s for s in core}
    original_nice = {s.lower().strip(): s for s in nice}

    matched_core_lower = user_set & core_set
    missing_core_lower = core_set - user_set
    matched_nice_lower = user_set & nice_set
    missing_nice_lower = nice_set - user_set

    matched_core = sorted([original_core[s] for s in matched_core_lower])
    missing_core = sorted([original_core[s] for s in missing_core_lower])
    matched_nice = sorted([original_nice[s] for s in matched_nice_lower])
    missing_nice = sorted([original_nice[s] for s in missing_nice_lower])

    total_weight = len(core_set) + len(nice_set) * 0.5
    matched_weight = len(matched_core_lower) + len(matched_nice_lower) * 0.5
    percentage = (matched_weight / total_weight * 100) if total_weight > 0 else 0

    return {
        'match_percentage': round(percentage, 1),
        'matched_core': matched_core,
        'missing_core': missing_core,
        'matched_nice': matched_nice,
        'missing_nice': missing_nice,
    }


def generate_roadmap(missing_core, missing_nice, target_role):
    skill_difficulty = {
        'HTML5': 1, 'CSS3': 1, 'Git': 1, 'SQL': 1, 'Linux': 1,
        'Communication': 1, 'Agile/Scrum': 1, 'Markdown': 1,
        'JavaScript': 2, 'Python': 2, 'React': 2, 'Node.js': 2,
        'Docker': 2, 'REST APIs': 2, 'TypeScript': 2,
        'PostgreSQL': 2, 'MongoDB': 2, 'Redis': 2,
        'Responsive Design': 2, 'Figma': 2, 'Wireframing': 2,
        'Authentication': 2, 'Tailwind CSS': 2, 'Sass/SCSS': 2,
        'Vue.js': 2, 'Angular': 2, 'Django': 2, 'Flask': 2,
        'Express.js': 2, 'Unit Testing': 2, 'Selenium': 2,
        'Kubernetes': 3, 'Terraform': 3, 'CI/CD': 3,
        'AWS': 3, 'GraphQL': 3, 'Microservices': 3,
        'Next.js': 3, 'Machine Learning': 3, 'Deep Learning': 3,
        'TensorFlow': 3, 'PyTorch': 3, 'NLP': 3,
        'Computer Vision': 3, 'Cybersecurity': 3, 'Penetration Testing': 3,
        'Flutter': 3, 'React Native': 3, 'System Design': 3,
        'Performance Optimization': 3, 'Kotlin': 3, 'Swift': 3,
        'OWASP Top 10': 3, 'ELK Stack': 3, 'Prometheus': 3,
        'Helm': 3, 'Ansible': 3, 'Jenkins': 3,
        'Scikit-learn': 2, 'Pandas': 2, 'NumPy': 2,
        'Tableau': 2, 'Power BI': 2, 'Statistics': 2,
        'Data Visualization': 2, 'A/B Testing': 2,
        'Feature Engineering': 3, 'Time Series Analysis': 3,
        'Design Systems': 3, 'Interaction Design': 3,
        'UX Research': 2, 'Prototyping': 2, 'User Testing': 2,
        'Jest': 2, 'Cypress': 2, 'Playwright': 2, 'PyTest': 2,
        'Accessibility': 2, 'SEO': 2, 'PWA': 3,
        'WebSockets': 3, 'API Design': 3, 'Nginx': 3,
        'Google Cloud': 3, 'Microsoft Azure': 3, 'Serverless': 3,
        'Elasticsearch': 3, 'Grafana': 3, 'Vault': 3,
        'Technical Writing': 1, 'Jira': 1, 'Confluence': 1,
        'C++': 3, 'Go': 3, 'Rust': 3, 'Solidity': 3,
    }

    all_missing = [(s, skill_difficulty.get(s, 2)) for s in missing_core + missing_nice]
    all_missing.sort(key=lambda x: x[1])

    phases = [
        {
            'name': 'Foundation',
            'duration': '4 - 6 weeks',
            'icon': '1',
            'color': '#10B981',
            'description': f'Start with the fundamentals needed for {target_role}',
            'skills': [],
        },
        {
            'name': 'Core Skills',
            'duration': '6 - 8 weeks',
            'icon': '2',
            'color': '#3B82F6',
            'description': 'Build the essential skills that define this role',
            'skills': [],
        },
        {
            'name': 'Advanced Concepts',
            'duration': '6 - 8 weeks',
            'icon': '3',
            'color': '#8B5CF6',
            'description': 'Level up with advanced tools and techniques',
            'skills': [],
        },
        {
            'name': 'Projects & Mastery',
            'duration': '4 - 6 weeks',
            'icon': '4',
            'color': '#F59E0B',
            'description': 'Apply everything through real-world projects',
            'skills': [],
        },
    ]

    n = len(all_missing)
    if n == 0:
        return phases

    phase_limits = [
        max(1, n // 4),
        max(1, n // 4),
        max(1, n // 4),
        n - 3 * max(1, n // 4),
    ]

    idx = 0
    for i, limit in enumerate(phase_limits):
        count = 0
        while idx < n and count < limit:
            phases[i]['skills'].append(all_missing[idx][0])
            idx += 1
            count += 1

    while idx < n:
        phases[-1]['skills'].append(all_missing[idx][0])
        idx += 1

    # Remove empty phases
    phases = [p for p in phases if p['skills']]

    return phases