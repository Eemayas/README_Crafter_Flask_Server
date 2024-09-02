# ### Ignore List
#
# This section defines the list of directories, files, and file extensions to be ignored when processing the repository.
#


# List of file extensions to be ignored when constructuing folder structure,
# as they are unlikely to contain relevant information.
ignore_list_folder_structure = [
    # General
    ".git",  # Git repository metadata
    "node_modules",  # Node.js modules
    ".idea",  # JetBrains IDE project files
    ".vscode",  # Visual Studio Code settings
    "__pycache__",  # Python bytecode cache
    ".DS_Store",  # macOS directory metadata
    ".env",  # Environment variable files
    "venv",  # Python virtual environment
    "build",  # Build output directories
    "dist",  # Distribution directories
    "target",  # Output from Java and Rust builds
    ".pytest_cache",  # Pytest cache files
    "*.log",  # Log files
    "*.tmp",  # Temporary files
    # Python
    "*.pyc",  # Compiled Python files
    ".mypy_cache",  # Mypy type checker cache
    ".tox",  # Tox environment
    # JavaScript/Node.js
    "npm-debug.log",  # NPM debug logs
    "yarn-error.log",  # Yarn error logs
    ".parcel-cache",  # Parcel bundler cache
    "coverage",  # Code coverage reports
    ".next",  # Next.js build directory
    "out",  # Output directory for Next.js
    # Java
    "*.class",  # Compiled Java classes
    "*.jar",  # JAR files
    "*.war",  # WAR files
    ".settings",  # Eclipse settings
    ".classpath",  # Eclipse classpath
    ".project",  # Eclipse project file
    # C/C++
    "*.o",  # Object files
    "*.a",  # Static libraries
    "*.so",  # Shared libraries
    "*.out",  # Executable files
    "*.exe",  # Windows executables
    "CMakeFiles",  # CMake build files
    "CMakeCache.txt",  # CMake cache
    "*.dSYM",  # macOS debug symbols
    "*.pdb",  # Windows debug symbols
    # Rust
    "*.rlib",  # Rust libraries
    "Cargo.lock",  # Cargo lock file
    # Go
    "bin",  # Binary output directory
    "pkg",  # Package output directory
    "*.test",  # Go test binaries
    "vendor",  # Vendor directory (if not used)
    # Ruby
    ".bundle",  # Bundler directory
    "vendor/bundle",  # Bundled gems
    "log",  # Log files
    "tmp",  # Temporary files
    ".gem",  # RubyGems metadata
    # PHP
    "vendor",  # Composer dependencies
    ".phpunit.result.cache",  # PHPUnit result cache
    # Android
    ".gradle",  # Gradle files
    "*.apk",  # Android package
    "*.ap_ ",  # Android resources package
    "local.properties",  # Android SDK settings
    # .NET/C#
    "bin",  # Binary output directory
    "obj",  # Object files directory
    "*.dll",  # DLL files
    "*.user",  # User settings
    "packages",  # NuGet packages
    # LaTeX
    "*.aux",  # Auxiliary files
    "*.toc",  # Table of contents
    "*.out",  # Auxiliary output files
    "*.synctex.gz",  # SyncTeX file
    "*.fls",  # LaTeX build files
    "*.fdb_latexmk",  # LaTeX build files
]


# List of file extensions to be ignored based on file types:
ignore_list_extensions = [
    # Image formats
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".svg",
    ".tiff",
    ".webp",
    ".heif",
    ".heic",
    ".ico",
    ".raw",
    ".psd",
    # Audio formats
    ".mp3",
    ".wav",
    ".flac",
    ".aac",
    ".ogg",
    ".m4a",
    ".wma",
    ".aiff",
    ".alac",
    ".pcm",
    # Video formats
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    ".m4v",
    ".mpg",
    ".mpeg",
    ".3gp",
    ".ogv",
    ".rm",
    ".swf"
    # Binary files
    ".exe",
    ".dll",
    ".bin",
    ".iso",
    ".img",
    # System files
    ".sys",
    ".log",
    ".bak",
    ".tmp",
    ".ini",
    # Font files
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    # Miscellaneous
    ".ico",
    ".svg",
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
]

# List of additional file extensions to be ignored when searching for API references,
# as they are unlikely to contain relevant API information.

api_additional_extensions = [
    # Text and document formats
    ".copy",
    ".local",
    ".json",
    ".config",
    ".md",
    ".txt",
    ".log",
    ".yml",
    ".yaml",
    ".xml",
    ".ini",
    ".pdf",
    ".csv",
    ".tsv",
    # Font formats
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".otf",
    # Configuration and map files
    ".config.ts",
    ".map",
    ".lock",
    # Styling files
    ".css",
    ".scss",
    ".sass",
    ".less",
    ".styl",
    ".pcss",
    ".postcss",
]

# Combine ignore_extensions and api_additional_extensions

api_ignore_extensions = ignore_list_extensions + api_additional_extensions

# Additional specific ignores for API references
specific_ignores_api = [".gitignore", ".config.js", ".config.ts"]


# ### Project Icons
#
# This section defines the map of the project type and project icons


# %%
project_icons = {
    "ecommerce": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/shopping-basket-2.png"
    },
    "banking": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/bank.png"},
    "school": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/school.png"},
    "education": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/graduation-cap.png"
    },
    "work": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/briefcase.png"},
    "healthcare": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/hospital-room.png"
    },
    "real_estate": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/home.png"},
    "travel": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/passport.png"},
    "social_media": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/share.png"
    },
    "fitness": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/dumbbell.png"},
    "news": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/news.png"},
    "entertainment": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/clapperboard.png"
    },
    "food_delivery": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/food-delivery.png"
    },
    "finance": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/money.png"},
    "transportation": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/bus.png"
    },
    "hospitality": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/hotel.png"},
    "music": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/musical-notes.png"
    },
    "gaming": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/controller.png"},
    "environment": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/earth-planet.png"
    },
    "nonprofit": {"icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/charity.png"},
    "photography": {
        "icon": "https://img.icons8.com/nolan/512/1A6DFF/C822FF/camera.png"
    },
}


# ### Language, Framework, Tools Extension List
#
# This section defines the list of Language, Framework, Tools Extension List
#


# Define known file extensions and configurations for different languages and tools
extensions = {
    "Python": [".py"],
    "JavaScript": [".js", ".jsx", ".ts", ".tsx"],
    "Java": [".java", ".class", ".jar", ".xml"],
    "C++": [".c", ".cpp", ".h", ".hpp", ".cc", ".cxx"],
    "C#": [".cs", ".csproj"],
    "Ruby": [".rb", ".gemspec", ".ru"],
    "PHP": [".php", ".phtml"],
    "Swift": [".swift"],
    "Go": [".go"],
    "Rust": [".rs"],
    "Kotlin": [".kt", ".kts"],
    "R": [".R", ".r", ".rmd"],
    "SQL": [".sql"],
    "HTML5": [".html", ".htm", ".css"],
    "CSS3": [".css"],
    "TypeScript": [".ts", ".tsx"],
    "Scala": [".scala", ".sbt"],
    "Perl": [".pl", ".pm"],
    "Objective-C": [".m", ".h"],
    "Shell": [".sh", ".bash", ".zsh"],
    "PowerShell": [".ps1"],
    "Haskell": [".hs", ".cabal"],
    "Lua": [".lua"],
    "Erlang": [".erl", ".hrl"],
    "Groovy": [".groovy", ".gvy"],
    "VHDL": [".vhdl", ".vhd"],
}
frameworks_extensions = {
    "React": [".jsx", ".tsx"],
    "Angular": ["angular.json"],
    "Vue.js": [".vue"],
    "Django": ["settings.py", "urls.py"],
    "Flask": [".py"],
    "Spring": [".xml"],
    "Maven": ["pom.xml"],
    "Gradle": ["build.gradle", "settings.gradle"],
    "Rails": ["Gemfile", "config.ru"],
    "Laravel": ["composer.json"],
    "Symfony": ["composer.json"],
    "Next.js": ["next.config.js"],
    "Gatsby": ["gatsby-config.js", "gatsby-node.js"],
    "Svelte": [".svelte"],
    "Bootstrap": ["bootstrap.min.css", "bootstrap.min.js"],
    "Jasmine": ["jasmine.json"],
    "Mocha": ["mocha.opts"],
    "Express": ["app.js", "server.js"],
    "Sails.js": ["config/", "api/"],
    "ASP.NET": [".cshtml", ".vbhtml", "web.config"],
    "Spring Boot": ["application.properties", "application.yml"],
    "Quasar": ["quasar.conf.js"],
    "Electron": ["main.js", "package.json"],
}
tools_extensions = {
    "Webpack": ["webpack.config.js"],
    "Docker": ["Dockerfile"],
    "CI/CD": [".github/workflows/ci.yml", ".gitlab-ci.yml", "Jenkinsfile"],
    "Babel": [".babelrc", "babel.config.json"],
    "ESLint": [".eslintrc", ".eslintrc.js", ".eslintrc.json"],
    "Prettier": [".prettierrc", ".prettierrc.json"],
    "Jest": ["jest.config.js", "jest.config.json"],
    "Travis CI": [".travis.yml"],
    "CircleCI": [".circleci/config.yml"],
    "Appveyor": ["appveyor.yml"],
    "Composer": ["composer.json", "composer.lock"],
    "Puppet": ["manifest.pp", "Puppetfile"],
    "Ansible": ["ansible.cfg", "playbook.yml"],
    "Kubernetes": ["deployment.yaml", "service.yaml"],
    "Terraform": [".tf", "main.tf"],
}
