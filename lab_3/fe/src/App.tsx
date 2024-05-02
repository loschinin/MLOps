import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import {Button, TextField, Typography} from "@mui/material";

function App() {
  const [inputData, setInputData] = useState('');
  const [prediction, setPrediction] = useState('');
  const [error, setError] = useState('');

  const handlePredict = async () => {
    try {
      const features = inputData.split(',').map(Number); // Convert input string to an array of numbers
      const response = await fetch('http://127.0.0.1:5001/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ features }),
      });

      const data = await response.json();
      if (response.ok) {
        setPrediction(data.prediction);
        setError('');
      } else {
        throw new Error(data.error || 'Unknown error');
      }
    } catch (e: any) {
      setError(e.toString());
      setPrediction('');
    }
  };

  return (
    <>
      <div>
        <a href="/">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="/">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Iris Prediction</h1>
      <Typography variant={'body1'}>Request Example: 5.1, 3.5, 1.4, 0.2</Typography>
      <div className="card">
        <TextField
          type="text"
          color={'primary'}
          fullWidth
          value={inputData}
          onChange={(e) => setInputData(e.target.value)}
          placeholder="Enter features separated by commas"
          inputProps={{
            style: { color: 'white', minWidth: 300 }
          }}
          variant={'standard'}
        />
        <br/>
        <br/>
        <Button variant={'outlined'} onClick={handlePredict}>Predict</Button>
        <br/>
        <br/>
        <hr/>
        <br/>
        <p>Result: {prediction}</p>
        <br/>
        <hr/>
        {error && <p>Error: {error}</p>}
      </div>
    </>
  );
}

export default App;
