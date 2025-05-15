# 🐳 Docker Deployment Guide for Sales Forecast App

This project is containerized using Docker, allowing you to run it effortlessly on any machine without setting up Python or dependencies.

## 📦 Docker Image

The Docker image is available publicly on Docker Hub:

👉 [https://hub.docker.com/r/abhishek11397/sales-forecast-app](https://hub.docker.com/r/abhishek11397/sales-forecast-app)

---

## 🔧 How to Pull and Run the App

### ✅ Step 1: Install Docker

If Docker is not installed on your machine, follow the official guide:  
👉 [Install Docker](https://docs.docker.com/get-docker/)

---

### ✅ Step 2: Pull the Docker Image

Use the following command to download the image from Docker Hub:

```bash
docker pull abhishek11397/sales-forecast-app:latest
````

---

### ✅ Step 3: Run the Docker Container

Start the container by mapping port `8501` (Streamlit default):

```bash
docker run -p 8501:8501 abhishek11397/sales-forecast-app:latest
```

---

### 🌐 Step 4: Access the Application

After starting the container, open your browser and visit:

```
http://localhost:8501
```

You should now see the **Sales Forecast App** running.

---

## 📁 Mount Local Model Files (Optional)

If your app depends on external files like model `.pkl` files, you can mount them from your host system:

```bash
docker run -p 8501:8501 -v $(pwd)/models:/app/models abhishek11397/sales-forecast-app:latest
```

Make sure the containerized app loads files from `/app/models`.

---

## ✍️ Author

**Abhishek**
🔗 [GitHub Profile](https://github.com/abhishek1397)


