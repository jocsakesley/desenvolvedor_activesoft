import React, { useState } from 'react';
import { FaStar } from 'react-icons/fa';

function NotaField({ maxNota, value, onClick }) {
  const [nota, setNota] = useState(null);

  return (
    <div>
      {[...Array(maxNota)].map((star, i) => {
        const ratingValue = i + 1;
        return (
          <label>
            <input type="radio" value={ratingValue} name="rating" onClick={() => setNota(ratingValue)} />
            <FaStar size={50} color={ratingValue <= nota ? "#FFC107" : "#E4E5E9"} className="star" />

          </label>
        );
      })}

    </div>
  );
}

export default NotaField;
