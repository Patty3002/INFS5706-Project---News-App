import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

const rootElement = document.getElementById("root");

createRoot(rootElement).render(
  <StrictMode>
    <main>
      <h1>Personalised News Newsletter Agent</h1>
      <p>Frontend setup complete. Application screens will be added here.</p>
    </main>
  </StrictMode>,
);
