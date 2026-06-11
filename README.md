# 🩸 BloodLink AI

**BloodLink AI** is a production-grade backend system designed to revolutionize blood bank management. Built with **FastAPI**, **PostgreSQL**, and **Clean Architecture**, it provides a robust platform for managing blood inventory, donor information, and urgent blood requests.

The system features an intelligent emergency blood matching engine and predictive analytics to monitor expiry and proactively manage shortages.

---

## 🚀 Key Features

-   **🔐 Secure Authentication**: JWT-based authentication with Role-Based Access Control (RBAC).
-   **📦 Inventory Management**: Real-time tracking of blood units, types, and stock levels.
-   **🩸 Donor Management**: Comprehensive donor profiles, donation history, and eligibility tracking.
-   **⚡ Urgent Matching Engine**: Intelligent matching of blood requests with available donors and inventory for emergency situations.
-   **📊 Smart Analytics**: 
    -   **Shortage Prediction**: AI-powered forecasts for blood supply needs using `scikit-learn`.
    -   **Expiry Monitoring**: Proactive alerts for blood units approaching their expiration date.
-   **📲 Notifications**: Automated system alerts for critical events and requests.
-   **🔄 Facility Transfers**: Logistical management of blood unit transfers between different centers.

---

## 🛠 Tech Stack

-   **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python 3.10+)
-   **Database**: [PostgreSQL](https://www.postgresql.org/)
-   **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) (Async)
-   **Migrations**: [Alembic](https://alembic.sqlalchemy.org/)
-   **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
-   **ML/Analytics**: [scikit-learn](https://scikit-learn.org/)
-   **Auth**: JWT (jose), Passlib (bcrypt)

---

## 📂 Project Structure

```text
logistics-transit/
├── app/
│   ├── api/          # API Routes (v1)
│   ├── core/         # Configuration, Security, Constants
│   ├── db/           # Database sessions and migrations
│   ├── models/       # SQLAlchemy models
│   ├── repositories/ # Data access abstraction
│   ├── schemas/      # Pydantic schemas (Request/Response)
│   ├── services/     # Business logic (Matching, Analytics, Expiry)
├── main.py           # Application entry point
├── create_tables.py  # Utility for DB initialization
├── requirements.txt  # Project dependencies
└── .env              # Environment variables
```

---

## ⚙️ Getting Started

### Prerequisites

-   Python 3.10 or higher
-   PostgreSQL database

### Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd logistics-transit
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    SECRET_KEY=your_secret_key
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=bloodlink_db
    ```

5.  **Initialize the database**:
    ```bash
    python create_tables.py
    # Or using Alembic
    alembic upgrade head
    ```

### Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main.py:app --reload
```

The API will be available at `http://localhost:8000`.
You can access the interactive Swagger documentation at `http://localhost:8000/docs`.

---

## 🍎 API Endpoints Overview (v1)

| Tag | Description |
| :--- | :--- |
| **Authentication** | Sign up, login, and token management. |
| **Inventory** | Manage blood types, units, and stock levels. |
| **Donors** | Register and query donor information. |
| **Requests** | Handle and process urgent blood requests. |
| **Transfers** | Manage logistical transfers between facilities. |
| **Analytics** | Access expiry monitoring and shortage predictions. |
| **Donations** | Log new blood donations. |
| **Notifications** | Manage system and user alerts. |

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
