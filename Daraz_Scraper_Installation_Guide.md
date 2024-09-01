# Project Overview

This project is a Daraz product scraper, designed to extract product information from Daraz URLs using Axios and Cheerio. It sends a GET request to the provided URL with authentication headers, parses the response HTML content to extract script tags containing product data, extracts product information from the parsed JSON object, and constructs a Product object with the extracted information. The project returns a Promise that resolves to the scraped product data or undefined if no data is found.

The technologies used in this project are TypeScript, Axios, Cheerio, and Bright Data proxy server for authentication. The key features of this project include its ability to scrape product information from Daraz URLs, use of authentication headers for secure access, parsing of HTML content using Cheerio, extraction of product details from JSON objects, and construction of a Product object with the extracted information.

---
# Key Features
- **Product Management**: Comprehensive object containing product details such as ID, URL, currency, image, title, category, price history, reviews, ratings, and more.
- **Price History Management**: Item in the product's price history, consisting of a single price value.
- **User Authentication**: Simple object representing a user with an email address.
- **Notification System**: Enum specifying four types of notifications: welcome, stock change, lowest price, and threshold met.
- **Email Generation**: Object containing the subject and body of an email.
- **Integration**: Integration with user and notification systems.

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
**Daraz_Scraper Installation Guide**
=====================================

# Getting Started
---------------

Welcome to the Daraz_Scraper installation guide! This project is built using Next.js and TypeScript. Before you start, make sure you have a basic understanding of these technologies.

## Prerequisites
-----------------

To run this project, you'll need:

1. **Node.js**: Download and install Node.js from [https://nodejs.org/en/download/](https://nodejs.org/en/download/)
2. **npm** (Node Package Manager): Should come bundled with Node.js
3. **yarn**: Optional, but recommended for faster installation times
4. **Docker** (for development): If you plan to use Docker for local development, install it from [https://www.docker.com/get-started](https://www.docker.com/get-started)
5. **Git**: Clone the project repository using `git clone` command

## Installation
-----------------

### Step 1: Clone the Repository

Clone the Daraz_Scraper repository from GitHub:

```bash
git clone https://github.com/Eemayas/Daraz_Scraper.git
```

### Step 2: Install Dependencies

Navigate to the project directory and install dependencies using npm or yarn:

```bash
npm install
# or
yarn install
```

### Step 3: Configure Environment Variables

Copy `.env.local.copy` file and name it as `.env.local`. Then, add your environment variables (e.g., API keys) in this file.

### Step 4: Build the Project

Run the following command to build the project:

```bash
npm run build
# or
yarn build
```

## Running the Project
------------------------

To run the project locally, execute the following command:

```bash
npm start
# or
yarn start
```

This will start the development server. You can now access the project at [http://localhost:3000](http://localhost:3000).

### Step 5: Run Tests (Optional)

If you want to run tests, navigate to the `lib` directory and execute:

```bash
npm test
# or
yarn test
```

## Troubleshooting
-------------------

### Common Issues

* **Error installing dependencies**: Make sure your Node.js version is compatible with Next.js. You can check this by running `node -v`.
* **Build fails due to missing modules**: Check if all dependencies are installed correctly.
* **Development server not starting**: Ensure that you have the necessary environment variables set up.

### Resolving Issues

1. **Check logs**: Look for errors in the console or terminal output.
2. **Google search**: Search online forums and documentation for specific error messages.
3. **GitHub issues**: Check if there are existing issues reported by others.

**Summary**
--------------

Congratulations! You have successfully installed the Daraz_Scraper project. If you encounter any difficulties, refer to this guide or reach out to the community for help. Happy coding!

---
# API Reference
#### Get all products with latest price history and send email notification

```http
GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

Note: There is only one parameter, which is the API key required for authentication. The rest of the parameters are internally handled by the function, such as product URL and email notification type.
#### Get product details by ID

```http
GET /api/products/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`       | `string` | **Required**. The ID of the product to retrieve |

The API endpoint is `/api/products/{id}`, where `{id}` is a required parameter of type `string`. This endpoint returns the details of a specific product by its ID.

Note: There are no other parameters or query strings in this API endpoint. The endpoint only expects the `id` parameter to be passed as part of the URL.
#### Add user email to product

```http
  POST /api/products/{productId}/add-email
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**. User's email address |
| `productId` | `string` | **Path parameter**. The ID of the product to add email to |

Note: There is only one API endpoint in this code snippet, which is used to add a user's email address to a specific product. It uses a POST request and expects two parameters: `email` and `productId`.
#### Connect to MongoDB

```http
POST /api/db/connect
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `MONGODB_URI`| `string`| **Required**. Your MongoDB connection string |
| `strictQuery`| `boolean`| **Optional**. Enable strict query mode |
#### Product Management API

```http
POST /api/products/scrapeAndStoreProduct
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productUrl` | `string` | **Required**. URL of the product to scrape and store |

#### Get Product by ID API

```http
GET /api/products/getProductById/{productId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{productId}` | `string` | **Path parameter**. ID of the product to retrieve |
| `api_key` | `string` | **Optional**. Your API key |

#### Get All Products API

```http
GET /api/products/getAllProducts
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Optional**. Your API key |
| `limit`   | `integer`| **Optional**. Limit the number of products |

#### Get Similar Products API

```http
GET /api/products/getSimilarProducts/{productId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{productId}` | `string` | **Path parameter**. ID of the product to retrieve similar products for |

#### Add User Email to Product API

```http
POST /api/products/addUserEmailToProduct/{productId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{productId}` | `string` | **Path parameter**. ID of the product to add user email to |
| `userEmail`   | `string` | **Required**. Email address of the user to add |
#### Scraping Daraz Products

```http
GET /api/daraz/scrape
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`     | `string` | **Required**. The URL of the product to scrape |
| `username`| `string` | **Required**. Your Bright Data username |
| `password`| `string` | **Required**. Your Bright Data password |
| `port`    | `integer`| **Required**. The port number for the Bright Data proxy (default: 22225) |
| `session_id`| `integer` | **Required**. A random session ID |

Note: This API reference is specific to the scrapingDarazProduct function in the provided code snippet.
#### Get all products with latest price history and send email notification

```http
GET /api/products
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

Note: There is only one parameter, which is the API key required for authentication. The rest of the parameters are internally handled by the function, such as product URL and email notification type.
#### Get product details by ID

```http
GET /api/products/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id`       | `string` | **Required**. The ID of the product to retrieve |

The API endpoint is `/api/products/{id}`, where `{id}` is a required parameter of type `string`. This endpoint returns the details of a specific product by its ID.

Note: There are no other parameters or query strings in this API endpoint. The endpoint only expects the `id` parameter to be passed as part of the URL.
#### Add user email to product

```http
  POST /api/products/{productId}/add-email
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**. User's email address |
| `productId` | `string` | **Path parameter**. The ID of the product to add email to |

Note: There is only one API endpoint in this code snippet, which is used to add a user's email address to a specific product. It uses a POST request and expects two parameters: `email` and `productId`.
#### Connect to MongoDB

```http
POST /api/db/connect
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `MONGODB_URI`| `string`| **Required**. Your MongoDB connection string |
| `strictQuery`| `boolean`| **Optional**. Enable strict query mode |
#### Product Management API

```http
POST /api/products/scrapeAndStoreProduct
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productUrl` | `string` | **Required**. URL of the product to scrape and store |

#### Get Product by ID API

```http
GET /api/products/getProductById/{productId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{productId}` | `string` | **Path parameter**. ID of the product to retrieve |
| `api_key` | `string` | **Optional**. Your API key |

#### Get All Products API

```http
GET /api/products/getAllProducts
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Optional**. Your API key |
| `limit`   | `integer`| **Optional**. Limit the number of products |

#### Get Similar Products API

```http
GET /api/products/getSimilarProducts/{productId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{productId}` | `string` | **Path parameter**. ID of the product to retrieve similar products for |

#### Add User Email to Product API

```http
POST /api/products/addUserEmailToProduct/{productId}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{productId}` | `string` | **Path parameter**. ID of the product to add user email to |
| `userEmail`   | `string` | **Required**. Email address of the user to add |
#### Scraping Daraz Products

```http
GET /api/daraz/scrape
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`     | `string` | **Required**. The URL of the product to scrape |
| `username`| `string` | **Required**. Your Bright Data username |
| `password`| `string` | **Required**. Your Bright Data password |
| `port`    | `integer`| **Required**. The port number for the Bright Data proxy (default: 22225) |
| `session_id`| `integer` | **Required**. A random session ID |

Note: This API reference is specific to the scrapingDarazProduct function in the provided code snippet.


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
    - Replace your-username and repository-name with your GitHub username.
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
