import logo from "./logo.svg";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Atlant - <code>computer assistant</code> <br /> Development in
          progress.
        </p>
        <a
          className="App-link"
          href="https://github.com/artegoser/Atlant"
          target="_blank"
          rel="noopener noreferrer"
        >
          Home
        </a>
      </header>
    </div>
  );
}

export default App;
