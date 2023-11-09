import React, { useState, useEffect } from "react";
import './App.css'; // Make sure to import the CSS file

function App() {
  const [photos, setPhotos] = useState([]);

  useEffect(() => {
    const fetchPhotos = () => {
      fetch("/photos")
        .then((res) => res.json())
        .then(setPhotos)
        .catch(console.error); // Always good to catch potential errors
    };

    fetchPhotos();
    const interval = setInterval(fetchPhotos, 30000); // Refresh every 30 seconds

    return () => clearInterval(interval); // Clean up the interval on unmount
  }, []);

  return (
    <div className="photo-grid">
      {photos.length === 0 ? (
        <p>Loading...</p>
      ) : (
        photos.map((filename, i) => (
          <div className="photo-item" key={i}>
            <img src={`/photos/${filename}`} alt={filename} />
          </div>
        ))
      )}
    </div>
  );
}

export default App;
