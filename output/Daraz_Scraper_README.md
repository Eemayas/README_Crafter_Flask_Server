
<p align="center">
    <img src="https://img.icons8.com/nolan/512/1A6DFF/C822FF/shopping-basket-2.png" width="200" style="border-radius: 20px;" />
</p>
    

<p align="center">
    <h1>Daraz_Scraper</h1>
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
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS">
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/Electron-47848F.svg?style=for-the-badge&logo=Electron&logoColor=white" alt="Electron">
  <img src="https://img.shields.io/badge/Next.js-000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
</p>
    



---
# Project Overview

The project is an e-commerce platform that enables users to buy and sell products, with a focus on product pricing, reviews, and stock management. It allows sellers to list their products with detailed information, such as price history, discount rates, and seller ratings, while also enabling buyers to review and rate the products they purchase. The project provides features like automatic email notifications for new orders, low stock levels, and threshold met, allowing users to stay informed about important events related to their business or purchases.

The project uses Mongoose to interact with a MongoDB database, storing products in a collection called "products". It also utilizes Node.js, Axios, Cheerio, and Nodemailer libraries to handle product scraping from Daraz website, email generation, and sending emails based on notification types. The key features of the project include automated email notifications for various events, product pricing and review management, stock level tracking, and seller information display.

---
# Key Features
* **1. Authenticates with Bright Data proxy using username and password**: Utilizes a proxy service for secure and reliable web scraping.
* **2. Retrieves HTML content from the provided URL**: Extracts webpage data using Axios, enabling access to dynamic web pages.
* **3. Extracts product information from the script tags in the HTML using Cheerio**: Parses HTML to gather product details, streamlining data collection.
* **4. Parses JSON data to extract various product attributes**: Converts JSON data into structured product info, facilitating easier analysis and use cases.
* **5. Creates a Product object with the extracted information**: Organizes scraped data into a unified Product object, promoting efficient storage and processing.
* **6. Returns the Product object or throws an error if scraping fails**: Provides a clear outcome for successful or failed web scraping attempts.
* **7. Extracted Product Attributes**: Includes essential product details such as title, description, price, ratings, and more, enabling comprehensive understanding of e-commerce data.

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
Here's a detailed installation guide:

**Getting Started**
================

Welcome to the Daraz Scraper installation guide! This guide will walk you through the process of setting up the project on your local machine.

**Prerequisites**
================

Before installing the project, make sure you have the following software and tools installed:

* Node.js (LTS version) - [Download](https://nodejs.org/en/download/)
* yarn (package manager) - [Install with npm](https://yarnpkg.com/en/docs/install)
* Docker (for testing purposes) - [Download](https://www.docker.com/get-started)
* MongoDB (database) - [Download](https://www.mongodb.com/try/download/community)

**Setup Instructions**
=====================

### Step 1: Clone the Repository

Clone the Daraz Scraper repository from GitHub using the following command:
```bash
git clone https://github.com/Eemayas/Daraz_Scraper.git
```
### Step 2: Install Dependencies

Navigate to the project directory and install dependencies using yarn:
```bash
cd Daraz_Scraper
yarn install
```
This will take a few minutes to complete.

### Step 3: Configure Environment Variables

Create a new file called `.env` in the root directory of the project. Add the following environment variables:
```makefile
MONGO_URI=mongodb://localhost:27017/
API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your actual API key.

### Step 4: Build and Start the Project

Run the following command to build and start the project:
```bash
yarn dev
```
This will start the development server, which you can access at [http://localhost:3000](http://localhost:3000).

**Running the Project**
=====================

To run the project in production mode, use the following command:
```bash
yarn build
yarn start
```
This will create a static HTML file and serve it using `next.js`.

**Tests**
========

The project uses Jest for testing. To run tests, navigate to the root directory of the project and run the following command:
```bash
yarn test
```

**Troubleshooting**
==================

### Common Issues

* **Error: Cannot find module 'node_modules'**: Make sure you have installed dependencies using yarn.
* **Error: MongoDB connection failed**: Check your MongoDB installation and ensure that it is running on the correct port (27017).
* **Error: API key not found**: Verify that you have added the API key to the `.env` file.

### Resolving Issues

If you encounter any issues during installation or while running the project, refer to the following troubleshooting steps:

* Run `yarn install` again to re-install dependencies.
* Restart MongoDB and ensure it is running on the correct port (27017).
* Verify that you have added the API key to the `.env` file.

Summary
--------

Congratulations! You have successfully installed the Daraz Scraper project. If you encounter any issues during installation or while running the project, refer to this guide for troubleshooting steps.

---
# API Reference

**File:** Github_repos\Daraz_Scraper\app\api\cron\route.ts

#### Get all products

```http
  GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      | -        | No parameters required for this API endpoint |

Note: There are no other HTTP methods (e.g., POST, PUT, DELETE) mentioned in the provided code snippet.

**File:** Github_repos\Daraz_Scraper\app\api\cron\route.ts

#### Get all products

```http
  GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      | -        | No parameters required for this API endpoint |

Note: There are no other HTTP methods (e.g., POST, PUT, DELETE) mentioned in the provided code snippet.



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
3. **Create a New Branch**:
    - Create a new branch for your changes using the command:
    ```sh
    git checkout -b your-branch-name
    ```
4. **Make Your Changes**:
    - Edit, add, or delete files as needed. Ensure your changes align with the project's contribution guidelines.
5. **Commit Your Changes**:
    - Stage your changes and commit them with a descriptive message:
      ```bash
      git add .
      git commit -m "Your descriptive message"
      ```
6. **Push Your Changes:**
    - Push your branch to your forked repository:
      ```bash
      git push origin your-branch-name
      ```
7. **Create a Pull Request (PR):**
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
