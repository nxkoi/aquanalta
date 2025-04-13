import React, { useEffect, useState } from "react";
import { getVizinhos } from "../api/mar";

export default function OceanMap({ barcoId }) {
  const [vizinhos, setVizinhos] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      getVizinhos(barcoId).then((res) => setVizinhos(res.data));
    }, 1000);
    return () => clearInterval(interval);
  }, [barcoId]);

  return (
    <div style={{ border: "1px solid #ccc", padding: "1rem" }}>
      <h2>Barcos próximos</h2>
      <ul>
        {vizinhos.map((b) => (
          <li key={b.id}>
            {b.id} - {b.dist} unidades - {b.direcao}° - {b.velocidade} u/s
          </li>
        ))}
      </ul>
    </div>
  );
}
