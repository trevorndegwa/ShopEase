# ShopEase

Welcome to ShopEase, a fully functional e-commerce platform built with Python and Django. This project is designed to provide a seamless online shopping experience for users while offering powerful management tools for administrators.

## Features

### User Features
- **User Authentication**: Secure user registration, login, and logout functionality.
- **Product Browsing**: Explore products by category, search for specific items, and view detailed product information.
- **Shopping Cart**: Add, update, or remove items in a shopping cart.
- **Order Placement**: Place orders and view order history.

### Admin Features
- **Product Management**: Add, update, or remove products.
- **Order Management**: View and manage customer orders.

## Technologies Used
- **Backend**: Python, Django (Django Admin for management).
- **Frontend**: HTML, CSS, JavaScript, Bootstrap.
- **Database**: SQLite during development, with plans to migrate to PostgreSQL for production.
- **Version Control**: Git and GitHub for source code management.

## Current State
- The core functionality, including user authentication, product management, and order processing, has been implemented.
- Payment integration (PayPal, Stripe, Mpesa) and PostgreSQL database migration are planned for future iterations.
- The app is yet to be deployed to a live hosting platform.

## Challenges Faced
- Transitioning from SQLite to PostgreSQL.
- Implementing advanced payment gateways.
- Hosting and deploying the project.

## Lessons Learned
- Importance of structuring models and views efficiently.
- Managing and documenting frequent commits during the development process.
- Understanding and debugging third-party library integrations.

## Installation

### Prerequisites
- Python (>=3.8)
- pip
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/trevorndegwa/shopease.git
   cd shopease
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Open the app in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Roadmap
- **Database Migration**: Move to PostgreSQL for enhanced scalability and performance.
- **Payment Integration**: Add support for PayPal, Stripe, and Mpesa.
- **Deployment**: Deploy the app to a live server using services like AWS, Heroku, or PythonAnywhere.

## Contribution
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Open-source libraries and the Django community for continuous support.

---

Feel free to explore, use, and contribute to ShopEase!


