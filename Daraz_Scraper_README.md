
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
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/TypeScript-3178C6.svg?style=for-the-badge&logo=TypeScript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=for-the-badge&logo=JavaScript&logoColor=black" alt="JavaScript">
  <img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white" alt="CSS">
  <img src="https://img.shields.io/badge/Electron-47848F.svg?style=for-the-badge&logo=Electron&logoColor=white" alt="Electron">
  <img src="https://img.shields.io/badge/Next.js-000000.svg?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js">
</p>
    



---
# Project Overview

The project is a Daraz e-commerce platform data scraper that extracts product information from the website. It utilizes web scraping techniques to gather relevant data, including product attributes and seller information. 

This project uses JavaScript and TypeScript technologies, as well as the PUPPETEER library for web scraping and parsing JSON-formatted data. The key features of this project include its ability to extract a wide range of product attributes, such as product rating and review count, brand and title, description and highlights, price and discount information, and availability and stock status. Additionally, it can handle errors during the scraping process by throwing informative error messages.

---
# Key Features
- **PriceHistoryItem**: An object representing a single price history item.
- **User**: A type representing a user with an email property.
- **Product**: A complex type representing various product data and properties.
- **NotificationType**: An enumeration of possible notification types.
- **EmailContent**: An object containing subject and body fields for email content.
- **Price**: An object representing price information with text and value fields.

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

Welcome to the Daraz Scraper project! This guide will walk you through the steps to install and run the project on your local machine.

**Prerequisites**
-----------------

Before we begin, make sure you have the following software installed:

* Node.js (v14 or higher) - [Download](https://nodejs.org/en/download/)
* Docker (optional) - [Download](https://www.docker.com/get-started)
* A code editor or IDE of your choice

**Installation**
---------------

### 1. Clone the repository

Open a terminal and run the following command to clone the project:

```bash
git clone https://github.com/Eemayas/Daraz_Scraper.git
```

### 2. Install dependencies

Navigate into the project directory and install the required dependencies using npm or yarn:

```bash
cd Daraz_Scraper
npm install
# or
yarn install
```

### 3. Configure environment variables (optional)

If you're planning to use Docker, create a new file called `.env.local` in the root of the project with the following content:

```makefile
DB_URL=mongodb://localhost:27017/
```

Replace `DB_URL` with your MongoDB connection string if it's different.

### 4. Build and start the project

Run the following command to build and start the project:

```bash
npm run dev
# or
yarn dev
```

This will start the development server, and you should see a message indicating that the server is running on port 3000.

**Running the Project**
----------------------

To access the project in your browser, navigate to `http://localhost:3000` .

### Testing

We use Jest for testing. To run tests, execute:

```bash
npm run test
# or
yarn test
```

**Troubleshooting**
-------------------

Common issues and their solutions:

* **Error: Cannot find module 'mongodb'**: Make sure you have MongoDB installed on your local machine.
* **Error: Cannot connect to MongoDB**: Check that the connection string in `.env.local` is correct, and try restarting the project.
* **Error: Docker container failed to start**: Try deleting the `node_modules` directory and running `npm install` again.

**Summary**
----------

That's it! You've successfully installed and run the Daraz Scraper project on your local machine. If you encounter any issues during installation, refer to the troubleshooting section above for solutions. Happy coding!

---
# API Reference
#### Get all products

```http
  GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      |          |                             |

There are no additional parameters or endpoints in this code snippet. The API endpoint `/api/products` uses the `GET` HTTP method to fetch all products from the database.

Note: This code snippet does not contain any other API methods like POST, PUT, DELETE etc.
#### Get all products

```http
  GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None      |          |                             |

There are no additional parameters or endpoints in this code snippet. The API endpoint `/api/products` uses the `GET` HTTP method to fetch all products from the database.

Note: This code snippet does not contain any other API methods like POST, PUT, DELETE etc.


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
