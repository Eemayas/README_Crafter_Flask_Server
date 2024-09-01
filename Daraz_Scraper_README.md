
<p align="center">
    <img src="https://img.icons8.com/nolan/512/1A6DFF/C822FF/shopping-basket-2.png" width="200" style="border-radius: 20px;" />
</p>
    

<p align="center">
    <h1 align="center">Daraz_Scraper</h1>
</p>
    

<p align="center">
  <img src="https://img.shields.io/github/license/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="license">
  <img src="https://img.shields.io/github/last-commit/Eemayas/Daraz_Scraper?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
  <img src="https://img.shields.io/github/languages/top/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="repo-top-language">
  <img src="https://img.shields.io/github/languages/count/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="repo-language-count">
  <img src="https://img.shields.io/github/actions/workflow/status/Eemayas/Daraz_Scraper/build.yml?branch=main&style=flat&color=0080ff" alt="build-status">
  <img src="https://img.shields.io/github/issues/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="open-issues">
  <img src="https://img.shields.io/github/forks/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="forks">
  <img src="https://img.shields.io/github/stars/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="stars">
  <img src="https://img.shields.io/github/issues-pr/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="pull-requests">
  <img src="https://img.shields.io/github/contributors/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="contributors">
  <img src="https://img.shields.io/github/commit-activity/m/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="commit-activity">
  <img src="https://img.shields.io/github/languages/code-size/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="code-size">
  <img src="https://img.shields.io/github/repo-size/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="repo-size">
  <img src="https://img.shields.io/github/downloads/Eemayas/Daraz_Scraper/total?style=flat&color=0080ff" alt="downloads">
  <img src="https://img.shields.io/github/sponsors/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="sponsors">
  <img src="https://img.shields.io/github/v/release/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="release-version">
  <img src="https://img.shields.io/codecov/c/github/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="coverage">
  <img src="https://img.shields.io/codeclimate/quality/a/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="code-quality">
  <img src="https://img.shields.io/david/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="dependencies">
  <img src="https://img.shields.io/david/dev/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="dev-dependencies">
  <img src="https://img.shields.io/snyk/vulnerabilities/github/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="security">
  <img src="https://img.shields.io/website?style=flat&color=0080ff&url=https%3A%2F%2Fexample.com" alt="performance">
  <img src="https://img.shields.io/github/commit-activity/y/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="activity">
  <img src="https://img.shields.io/docsify/docs?style=flat&color=0080ff" alt="documentation">
  <img src="https://img.shields.io/github/v/tag/Eemayas/Daraz_Scraper?style=flat&color=0080ff" alt="version">
</p>
    

<p align="center">
	<em>Constructed using the following tools and technologies:</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS">
  <img src="https://img.shields.io/badge/Next.js-000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
  <img src="https://img.shields.io/badge/Electron-47848F.svg?style=for-the-badge&logo=Electron&logoColor=white" alt="Electron">
</p>
    



---
# Project Overview

The project appears to be a web scraping script, likely for extracting product information from Daraz, a Pakistani e-commerce platform. It uses Axios and Cheerio libraries to fetch and parse HTML content from product pages, then extracts relevant data using regular expressions.

This script defines a set of types for a product catalog system in TypeScript, including price-related, product-related, notification-related, and email-related types. The project utilizes environment variables for authentication with Bright Data and uses a random session ID to avoid rate limiting. It also returns the extracted product information as a Product object, which can be used by other parts of the application.

The technologies used in this project include TypeScript, Axios, Cheerio, and Bright Data for web scraping. The key features of the project are its ability to fetch and parse HTML content, extract relevant data using regular expressions, and return the product information as a Product object. Additionally, it defines a set of types for a product catalog system in TypeScript, making it a comprehensive solution for managing products and notifications.

---
# Key Features
- **Daraz Product Scraper**: A function that extracts product information from a specified URL on the Daraz e-commerce platform using Axios and Cheerio.
- **Product Catalog System Types**: A set of types defined in TypeScript for a product catalog system, including price-related, product-related, notification-related, and email-related types.
- **Price History**: The ability to track price history for products, with each item containing a single 'price' property.
- **User Information**: The capacity to represent users with an email address.
- **Product Metadata**: The capability to describe products with various properties, including title, category, image, pricing information, ratings/reviews data, and more.
- **Notification Types**: Four possible notification types: welcome, change of stock, lowest price, and threshold met.

---
# Folder Structure
```sh
Daraz_Scraper/
├── .env.local.copy
├── .gitignore
├── app/
│   ├── api/
│   │   └── cron/
│   │       └── route.ts
│   ├── favicon.ico
│   ├── globals.css
│   ├── layout.tsx
│   ├── page.tsx
│   └── products/
│       └── [id]/
│           └── page.tsx
├── components/
│   ├── HeroCarousel.tsx
│   ├── Modal.tsx
│   ├── Navbar.tsx
│   ├── PriceInfoCard.tsx
│   ├── ProductCard.tsx
│   └── Searchbar.tsx
├── lib/
│   ├── action/
│   │   └── index.ts
│   ├── models/
│   │   └── product.model.ts
│   ├── mongoose.ts
│   ├── nodemailer/
│   │   └── index.ts
│   ├── scrapper/
│   │   └── index.ts
│   └── utils.ts
├── next.config.js
├── package-lock.json
├── package.json
├── postcss.config.js
├── public/
│   ├── assets/
│   │   ├── icons/
│   │   │   ├── arrow-down.svg
│   │   │   ├── arrow-right.svg
│   │   │   ├── arrow-up.svg
│   │   │   ├── bag.svg
│   │   │   ├── black-heart.svg
│   │   │   ├── bookmark.svg
│   │   │   ├── chart.svg
│   │   │   ├── check.svg
│   │   │   ├── chevron-down.svg
│   │   │   ├── comment.svg
│   │   │   ├── frame.svg
│   │   │   ├── hand-drawn-arrow.svg
│   │   │   ├── logo.svg
│   │   │   ├── mail.svg
│   │   │   ├── price-tag.svg
│   │   │   ├── red-heart.svg
│   │   │   ├── search.svg
│   │   │   ├── share.svg
│   │   │   ├── square.svg
│   │   │   ├── star.svg
│   │   │   ├── user.svg
│   │   │   └── x-close.svg
│   │   └── images/
│   │       ├── details.svg
│   │       ├── hero-1.svg
│   │       ├── hero-2.svg
│   │       ├── hero-3.svg
│   │       ├── hero-4.svg
│   │       ├── hero-5.svg
│   │       └── trending.svg
│   ├── demo/
│   │   ├── home-page.png
│   │   ├── product-page.png
│   │   └── track-product.png
│   ├── next.svg
│   └── vercel.svg
├── README.md
├── tailwind.config.ts
├── tsconfig.json
├── types/
│   └── index.ts
└── vercel.json

17 directories, 63 files
```

---
**Getting Started**
====================

Welcome to the Daraz Scraper installation guide! This guide will walk you through setting up the project on your local machine.

**Prerequisites**
----------------

Before installing the project, make sure you have the following:

* **Node.js**: Download and install Node.js from [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
* **npm**: The package manager for Node.js should be installed automatically with Node.js.
* **Git**: Make sure Git is installed on your machine. You can download it from [https://git-scm.com/downloads](https://git-scm.com/downloads)
* **Next.js**: A popular React-based framework for building server-rendered applications. Install it using npm by running `npm install next` in the terminal.
* **Typescript**: A superset of JavaScript that adds optional static typing and other features. You can install it using npm with `npm install typescript --save-dev`
* **Tailwind CSS**: A utility-first CSS framework for building custom UI components. Install it by running `npx tailwindcss init` in the terminal.
* **Vercel CLI**: A command-line interface for deploying and managing Next.js applications on Vercel. You can install it using npm with `npm install vercel --save-dev`

**Installation**
---------------

### Step 1: Clone the repository

Clone the Daraz Scraper repository from GitHub:

```bash
git clone https://github.com/Eemayas/Daraz_Scraper.git daraz-scraper
```

### Step 2: Install dependencies

Navigate to the project directory and install the dependencies using npm:

```bash
cd daraz-scraper
npm install
```

### Step 3: Configure environment variables

Create a new file called `.env` in the root of the project with your desired environment variables. For example:

```makefile
NODE_ENV=development
NEXT_PUBLIC_API_URL=https://api.example.com/
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=password
```

### Step 4: Configure Next.js

Configure Next.js by running `npx next` in the terminal.

**Running the Project**
----------------------

To run the project locally, follow these steps:

1. **Start Next.js**: Run `npx next dev` to start the development server.
2. **Open browser**: Open your web browser and navigate to [http://localhost:3000](http://localhost:3000) to see the Daraz Scraper interface.

**Tests**
-------

To run tests, use Jest:

```bash
npm test
```

**Troubleshooting**
------------------

### Common issues

* **"Cannot find module 'next'"**: Make sure you have installed Next.js using npm.
* **"Could not start server..."**: Run `npx next dev` with the `--debug` flag to get more detailed error messages.

Summary
--------

Congratulations! You have successfully set up and run the Daraz Scraper project. If you encounter any issues or have questions, feel free to reach out to me on GitHub.

---
# API Reference
#### Get all products

```http
  GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      |          |                            |

Note: There are no parameters required or optional for this API endpoint. It simply retrieves all products from the database.

#### Update a product

```http
  PUT /api/products/:id
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`      | `string` | **Required**. ID of the product to update |

Note: This endpoint is used to update a specific product in the database, identified by its unique ID.

#### Send email notification

```http
  POST /api/send-email-notification
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      |          |                            |

Note: This endpoint sends an email notification to users who have subscribed to updates for a specific product. It does not require any parameters.

No other API references with HTTP methods were found in the provided code.
#### Get all products

```http
  GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      |          |                            |

Note: There are no parameters required or optional for this API endpoint. It simply retrieves all products from the database.

#### Update a product

```http
  PUT /api/products/:id
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`      | `string` | **Required**. ID of the product to update |

Note: This endpoint is used to update a specific product in the database, identified by its unique ID.

#### Send email notification

```http
  POST /api/send-email-notification
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      |          |                            |

Note: This endpoint sends an email notification to users who have subscribed to updates for a specific product. It does not require any parameters.

No other API references with HTTP methods were found in the provided code.


---

# Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/Eemayas/Daraz_Scraper/pulls)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/Eemayas/Daraz_Scraper/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/Eemayas/Daraz_Scraper/issues)**: Submit bugs found or log feature requests for Daraz_Scraper.

### Contributing Guidelines

1. **Fork the Repository**:
    - Start by forking the project repository to your GitHub account.
2. **Clone the Repository**:
    - Clone your forked repository to your local machine using the command:
    ```sh
    git clone https://github.com/your-username/Daraz_Scraper.git
    ```
    - Replace ``your-username`` with your GitHub username.
4. **Create a New Branch**:
    - Create a new branch for your changes using the command:
    ```sh
    git checkout -b your-branch-name
    ```
5. **Make Your Changes**:
    - Edit, add, or delete files as needed. Ensure your changes align with the project's contribution guidelines.
6. **Commit Your Changes**:
    - Stage your changes and commit them with a descriptive message:
      ```bash
      git add .
      git commit -m "Your descriptive message"
      ```
7. **Push Your Changes:**
    - Push your branch to your forked repository:
      ```bash
      git push origin your-branch-name
      ```
8. **Create a Pull Request (PR):**
    - Go to the original repository on GitHub and click “Compare & pull request.” Provide a clear description of the changes and submit the PR.

Once your PR is reviewed and approved, it will be merged into the main branch.
        

---

# Contributors

| Avatar | Contributor | GitHub Profile | No of Contributions |
|:--------:|:--------------:|:----------------:|:-------------------:|
| <img src='https://avatars.githubusercontent.com/u/100434825?v=4' width='40' height='40' style='border-radius:50%;'/> | Eemayas | [@Eemayas](https://github.com/Eemayas) | 14 |

    

---

# License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.



---
