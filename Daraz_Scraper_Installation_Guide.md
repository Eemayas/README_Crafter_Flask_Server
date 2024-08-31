# Project Overview

The project is a product data scraper and database management system that utilizes Mongoose for MongoDB interaction, Next.js caching library, Daraz scraper, and Email sending using Nodemailer to collect and store product information. The system is designed to scrape products from Daraz, update price history, retrieve individual products, return all stored products, find similar products, and add user emails with welcome email notifications. This project showcases an efficient integration of multiple technologies, including Mongoose for MongoDB interaction, Next.js caching library, Daraz scraper, and Email sending using Nodemailer, to create a comprehensive product data management system featuring key features such as product scraping, price history updates, and personalized user engagement through email notifications.

---
# Key Features
* **Product Model Creation**: A Mongoose model is created to store product data with various fields related to pricing, ratings, reviews, and product information.
* **Pricing and Rating Features**: The product model includes fields for current and original prices, price history, discount rate, description, ratings and reviews counts, product quantity, stars, and out-of-stock status.
* **Scraping Functionality**: Five functions are exported to interact with a MongoDB database using Mongoose and a Next.js application, enabling scraping of product data from Daraz.
* **Email Notification Feature**: The code includes functionality to send email notifications to users for products they have shown interest in.
* **Product Retrieval and Filtering**: Functions are provided to retrieve a product by its ID, return all products stored in the database, and find similar products based on a given product's ID.
* **User Management**: A feature is included to add a user's email to a product's list of users and send a welcome email.

---
# Folder Structure
```sh
Daraz_Scraper/
├── app/
│   ├── favicon.ico
│   ├── products/
│   │   └── [id]/
│   │       └── page.tsx
│   ├── page.tsx
│   ├── api/
│   │   └── cron/
│   │       └── route.ts
│   ├── layout.tsx
│   └── globals.css
├── types/
│   └── index.ts
├── package.json
├── vercel.json
├── next.config.js
├── README.md
├── components/
│   ├── Modal.tsx
│   ├── HeroCarousel.tsx
│   ├── Navbar.tsx
│   ├── PriceInfoCard.tsx
│   ├── Searchbar.tsx
│   └── ProductCard.tsx
├── tsconfig.json
├── .gitignore
├── lib/
│   ├── scrapper/
│   │   └── index.ts
│   ├── nodemailer/
│   │   └── index.ts
│   ├── models/
│   │   └── product.model.ts
│   ├── action/
│   │   └── index.ts
│   ├── utils.ts
│   └── mongoose.ts
├── tailwind.config.ts
├── package-lock.json
├── public/
│   ├── demo/
│   │   ├── track-product.png
│   │   ├── home-page.png
│   │   └── product-page.png
│   ├── vercel.svg
│   ├── assets/
│   │   ├── icons/
│   │   │   ├── check.svg
│   │   │   ├── arrow-right.svg
│   │   │   ├── user.svg
│   │   │   ├── comment.svg
│   │   │   ├── star.svg
│   │   │   ├── x-close.svg
│   │   │   ├── bookmark.svg
│   │   │   ├── chart.svg
│   │   │   ├── share.svg
│   │   │   ├── black-heart.svg
│   │   │   ├── price-tag.svg
│   │   │   ├── hand-drawn-arrow.svg
│   │   │   ├── mail.svg
│   │   │   ├── red-heart.svg
│   │   │   ├── search.svg
│   │   │   ├── logo.svg
│   │   │   ├── bag.svg
│   │   │   ├── chevron-down.svg
│   │   │   ├── arrow-down.svg
│   │   │   ├── square.svg
│   │   │   ├── arrow-up.svg
│   │   │   └── frame.svg
│   │   └── images/
│   │       ├── hero-5.svg
│   │       ├── hero-3.svg
│   │       ├── trending.svg
│   │       ├── hero-4.svg
│   │       ├── details.svg
│   │       ├── hero-1.svg
│   │       └── hero-2.svg
│   └── next.svg
├── .env.local.copy
└── postcss.config.js

17 directories, 63 files
```

---
# Getting Started
Welcome to Daraz Scraper! This guide will walk you through the process of setting up the project on your local machine.

## Prerequisites
Before installing the project, make sure you have:

* Node.js (14.x or higher) installed on your system. You can download it from [here](https://nodejs.org/en/download/).
* A code editor or IDE (Integrated Development Environment) of your choice.
* Git installed on your system to clone the repository.

## Installation

### Step 1: Clone the Repository
Clone the Daraz Scraper repository using the following command:
```bash
git clone https://github.com/Eemayas/Daraz_Scraper.git
```
Change into the project directory:
```bash
cd Daraz_Scraper
```

### Step 2: Install Dependencies

In your terminal, run the following command to install all dependencies required by the project:
```bash
npm install
```
or if you're using yarn:
```bash
yarn install
```

### Step 3: Configure Environment Variables

Create a new file named `.env` in the root directory of your project and add the following variables:

* `MONGO_URI`: Your MongoDB connection string.
* `NEXT_PUBLIC_API_KEY`: Your API key for Daraz.
* `EMAIL_HOST`: Your email host (e.g., Gmail).
* `EMAIL_PORT`: Your email port.
* `EMAIL_USER`: Your email username.
* `EMAIL_PASSWORD`: Your email password.

Example:
```makefile
MONGO_URI=mongodb://localhost:27017/
NEXT_PUBLIC_API_KEY=your-api-key-here
EMAIL_HOST=gmail.com
EMAIL_PORT=587
EMAIL_USER=your-email-username
EMAIL_PASSWORD=your-email-password
```
### Step 4: Run the Project

In your terminal, run the following command to start the Next.js development server:
```bash
npm run dev
```

or if you're using yarn:
```bash
yarn dev
```
Your project is now running on [http://localhost:3000](http://localhost:3000).

## Running the Project

To run the project, follow these steps:

1. Run `npm start` or `yarn start` to start the development server.
2. Open your web browser and navigate to [http://localhost:3000](http://localhost:3000).
3. You can now interact with the project's API endpoints using tools like Postman.

## Tests
To run tests, follow these steps:

1. Run `npm test` or `yarn test` to execute all unit tests.
2. If you want to run specific tests, use the following command: `jest <test-file-name>` (e.g., `jest api/cron/route.test.ts`).

## Troubleshooting

### Common Issues and Solutions

* **npm install** hangs:
	+ Solution: Run `npx npm-force-cache && npm install`.
* **Can't find variable: process**:
	+ Solution: Make sure you're running the command in a Node.js environment (e.g., run `node -v` to check).
* **TypeError: Cannot read property 'length' of undefined**:
	+ Solution: Check your MongoDB connection string and ensure it's correct.

If you encounter any other issues, feel free to ask on [Stack Overflow](https://stackoverflow.com/questions/tagged/daraz-scraper).

---
# API Reference
#### Get product by ID and similar products

```http
  GET /api/product/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{id}`    | `string` | **Required**. The product ID |

Note: There is no API reference for getting all similar products, only a specific product by ID and its similar products.
#### Update products and send email notifications

```http
POST /api/products/update-and-send-email-notifications
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`      | `string` | **Required**. The URL of the product to update            |
| `users`    | `array`  | **Optional**. An array of user emails to send email notifications to |

Note: There is only one API endpoint in this code, and it's a POST request to `/api/products/update-and-send-email-notifications`.
#### Add user email to product

```http
  POST /api/product/{productId}/add-email
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**. Email address of the user |
| `productId`| `string`| **Required**. ID of the product |

Note: The `/api/product/{productId}/add-email` endpoint is not a standard API endpoint, but rather a custom endpoint created by the `addUserEmailToProduct` function in the code.
#### Scrape and store product information from Daraz URL

```http
POST /api/scrapeProduct
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`      | `string` | **Required**. The Daraz product URL to scrape |
#### Scrape Daraz Product Information

```http
GET /api/scrape-daraz-product
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`      | `string` | **Required**. URL of the product to scrape |
| `username` | `string` | **Required**. Bright Data username |
| `password` | `string` | **Required**. Bright Data password |
| `port`     | `integer`| **Required**. Proxy port number |
#### Product Operations

```http
POST /api/products/scrapeAndStoreProduct
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productUrl` | `string` | **Required**. The URL of the product to scrape and store |

---

#### Get Product by ID

```http
GET /api/products/getProductById/:productId
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productId` | `string` | **Required**. The ID of the product to retrieve |

---

#### Get All Products

```http
GET /api/products/getAllProducts
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `limit`   | `integer`| **Optional**. Limit the number of products (default: 10) |

---

#### Get Similar Products

```http
GET /api/products/getSimilarProducts/:productId
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productId` | `string` | **Required**. The ID of the product to find similar products for |

---

#### Add User Email to Product

```http
POST /api/products/addUserEmailToProduct/:productId
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productId` | `string` | **Required**. The ID of the product to add a user email to |
| `userEmail`  | `string` | **Required**. The email address of the user to add |

---

#### Note:
The code provided contains API endpoints for performing various operations related to products, such as scraping and storing products, retrieving products by ID or all products, finding similar products, and adding user emails to products.
#### Get product by ID and similar products

```http
  GET /api/product/{id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{id}`    | `string` | **Required**. The product ID |

Note: There is no API reference for getting all similar products, only a specific product by ID and its similar products.
#### Update products and send email notifications

```http
POST /api/products/update-and-send-email-notifications
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`      | `string` | **Required**. The URL of the product to update            |
| `users`    | `array`  | **Optional**. An array of user emails to send email notifications to |

Note: There is only one API endpoint in this code, and it's a POST request to `/api/products/update-and-send-email-notifications`.
#### Add user email to product

```http
  POST /api/product/{productId}/add-email
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `email`   | `string` | **Required**. Email address of the user |
| `productId`| `string`| **Required**. ID of the product |

Note: The `/api/product/{productId}/add-email` endpoint is not a standard API endpoint, but rather a custom endpoint created by the `addUserEmailToProduct` function in the code.
#### Scrape and store product information from Daraz URL

```http
POST /api/scrapeProduct
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`      | `string` | **Required**. The Daraz product URL to scrape |
#### Scrape Daraz Product Information

```http
GET /api/scrape-daraz-product
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `url`      | `string` | **Required**. URL of the product to scrape |
| `username` | `string` | **Required**. Bright Data username |
| `password` | `string` | **Required**. Bright Data password |
| `port`     | `integer`| **Required**. Proxy port number |
#### Product Operations

```http
POST /api/products/scrapeAndStoreProduct
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productUrl` | `string` | **Required**. The URL of the product to scrape and store |

---

#### Get Product by ID

```http
GET /api/products/getProductById/:productId
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productId` | `string` | **Required**. The ID of the product to retrieve |

---

#### Get All Products

```http
GET /api/products/getAllProducts
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `limit`   | `integer`| **Optional**. Limit the number of products (default: 10) |

---

#### Get Similar Products

```http
GET /api/products/getSimilarProducts/:productId
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productId` | `string` | **Required**. The ID of the product to find similar products for |

---

#### Add User Email to Product

```http
POST /api/products/addUserEmailToProduct/:productId
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `productId` | `string` | **Required**. The ID of the product to add a user email to |
| `userEmail`  | `string` | **Required**. The email address of the user to add |

---

#### Note:
The code provided contains API endpoints for performing various operations related to products, such as scraping and storing products, retrieving products by ID or all products, finding similar products, and adding user emails to products.


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
6. **Commit Your Changes**: Commit with a clear message describing your updates.
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

# License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.



---
