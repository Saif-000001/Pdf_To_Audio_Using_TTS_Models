import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [audioUrl, setAudioUrl] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setError(null);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!file) {
      setError('Please select a file');
      return;
    }
    setIsLoading(true);
    setError(null);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/pdf_to_audio', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        responseType: 'blob',
        timeout: 300000, 
      });

      if (response.headers['content-type'] === 'application/json') {
        // If the response is JSON, it's probably an error message
        const reader = new FileReader();
        reader.onload = () => {
          const errorData = JSON.parse(reader.result);
          setError(errorData.detail || 'An unknown error occurred');
        };
        reader.readAsText(response.data);
      } else {
        const blob = new Blob([response.data], { type: 'audio/wav' });
        const url = window.URL.createObjectURL(blob);
        setAudioUrl(url);
      }
    } catch (error) {
      console.error('Error:', error);
      setError(error.response?.data?.detail || error.message || 'An error occurred while processing the PDF');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>PDF to Audio Converter</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="file" 
          onChange={handleFileChange} 
          accept=".pdf" 
        />
        <button 
          type="submit" 
          disabled={!file || isLoading}
        >
          {isLoading ? 'Converting...' : 'Convert to Audio'}
        </button>
      </form>
      {error && <p className="error">{error}</p>}
      {audioUrl && (
        <div className="audio-section">
          <h2>Generated Audio:</h2>
          <audio controls src={audioUrl}>
            Your browser does not support the audio element.
          </audio>
          <br />
          <a href={audioUrl} download="converted_audio.wav">
            Download Audio
          </a>
        </div>
      )}
    </div>
  );
}

export default App;