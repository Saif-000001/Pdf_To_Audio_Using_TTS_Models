
#  PDF TO AUDIO USING TTS

## Project Description
This project is a web application designed to convert PDF documents into audio files using Text-to-Speech (TTS) technology. Users can upload PDF files through a React-based frontend interface, and the backend, built with FastAPI, will handle the processing. The backend extracts text from the PDF using `easyocr` for Optical Character Recognition (OCR) and generates an audio file using the `TTS` library. The entire application is containerized and deployed using Docker, ensuring consistency and ease of deployment across different environments and this project demonstrates the effective use of modern web technologies to solve a real-world problem, highlighting the integration of frontend and backend systems and the power of containerization for deployment.

## Text-to-Speech (TTS) Repository
For the Text-to-Speech (TTS) functionality used in this project, we leverage a powerful TTS engine available at [Text-to-Speech Repository](https://github.com/coqui-ai/TTS). This allows us to convert text from PDF files into high-quality audio, enhancing accessibility and usability for our users.



## Technologies Used
- **Frontend**: React
- **Backend**: FastAPI
- **Deployment**: Docker

## Project Structure

```plaintext
PDF_TO_AUDIO_USING_TTS/
├── .venv/
├── backend/
│   ├── app/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── main.py
│   ├── .dockerignore
│   ├── .gitignore
│   ├── Dockerfile
│   ├── requirements.txt
├── frontend/
│   ├── .venv/
│   ├── node_modules/
│   ├── public/
│   ├── src/
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── index.js
│   ├── .dockerignore
│   ├── .gitignore
│   ├── Dockerfile
│   ├── package-lock.json
│   ├── package.json
|   ├── README.md
├── .gitignore
├── docker-compose.yml
├── README.md
```
## Requirements
To run this project, you will need Docker and Docker Compose installed on your machine. Installation guides for Docker can be found [here](https://docs.docker.com/get-docker/) and for Docker Compose [here](https://docs.docker.com/compose/install/).


## Running the Application

#### 1. Clone the Repository 
```bash
git clone https://github.com/Saif-000001/Pdf_To_Audio_Using_TTS_Models.git
cd Pdf_To_Audio_Using_TTS_Models
```
Open your project in Visual Studio Code, then open a new terminal. In the terminal, navigate to the frontend directory using the command `cd frontend`, and then install the project dependencies by running `npm install`."

#### 2. Build and Run the Docker Containers

```bash
docker-compose up --build
```
This command builds the images for the frontend and backend if they don't exist and starts the containers. The backend is available at `http://localhost:8000/` and the frontend at `http://localhost:3000/`.

#### 3. Viewing the Application

Open a browser and navigate to `http://localhost:3000/` to view the React application. It should display a message fetched from the FastAPI backend.

## Stopping the Application
To stop the application and remove containers, networks, and volumes created by `docker-compose up`, you can use:

```bash 
docker-compose down -v
```
