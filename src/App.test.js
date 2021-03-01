import { render, screen } from '@testing-library/react';
import App from './App';

test("renders the correct content", () => 
{
  // Render a React component to the DOM
  const root = document.createElement("div");
  ReactDOM.render(<App />, root);

  // Use DOM APIs (queryselector) to make assertions
  expect(root.querySelector("h1"), textContent).toBe("Header");
});
