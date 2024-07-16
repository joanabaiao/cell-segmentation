# Cell Segmentation and Classification Using YOLOv8

## Project Summary

This project focuses on the segmentation and classification of red and white blood cells in microscopic images using the YOLOv8 model. It employs Flask for the backend, integrates YOLOv8 for image processing, and provides a user-friendly web interface.

The project's goal is to offer an efficient and automated pipeline for deploying the cell segmentation and classification model on Azure. It utilizes Docker for containerization and GitHub Actions for continuous integration and continuous deployment (CI/CD).

https://github.com/user-attachments/assets/a8002e48-269e-4156-b3f1-9baa7a370ff6

## Dataset

The dataset used in this project consists of microscopic images containing red and white blood cells.

The dataset is divided into three subsets:

- **Training Set**: 213 images
- **Validation Set**: 57 images
- **Test Set**: 71 images

Each subset is structured into the following directories:

- `images/`: Contains the raw microscopic images of blood samples.
- `annotations/`: Contains the corresponding annotation files in YOLO format, specifying the bounding boxes and class labels for red and white blood cells.

## Features

- **Data Ingestion:** Automated process to ingest and prepare data for training.
- **Data Validation:** Ensures the quality and integrity of the data before training.
- **Model Training:** Trains the YOLOv8 model for cell segmentation and classification of red and white blood cells.
- **Web Interface:** A simple and interactive UI for training the model and making predictions.
- **Docker Integration**: Containerization of the application for ease of deployment and scalability.
- **Azure Deployment**: Hosting the application on Azure for accessibility and performance.
- **CI/CD with GitHub Actions**: Automated building, testing, and deployment pipelines.

## Requirements

- Python 3.x
- Flask
- YOLOv8
- Additional requirements are listed in requirements.txt.
- Azure Account

## Steps

1. Clone the repository: `git clone https://github.com/joanabaiao/cell-segmentation`

2. Install the required packages: `pip install -r requirements.txt`

3. Start the Flask server:
   `python app.py`

4. Access the web interface at `http://localhost:8080`. Follow the on-screen instructions to make predictions.

### Deployment:

1. Build the Docker Image: Create a Dockerfile and use the `docker build` command to build your image.
2. Push the Docker Image to ACR: Use the `docker push` command to upload your image to Azure Container Registry.
3. Deploy to Azure Web App: Create an Azure Web App for Containers and configure it to pull and run your Docker image from ACR.

```
docker build -t cellseg.azurecr.io/cell:latest .

docker login cellseg.azurecr.io

docker push cellseg.azurecr.io/cell:latest
```
