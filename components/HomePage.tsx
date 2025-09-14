import { useState } from "react";
import axios from "axios";
import styles from "../styles/Home.module.css";

interface ApiResponse {
  message?: string;
  status?: string;
  name?: string;
  description?: string;
  uptime_seconds?: number;
}

export default function HomePage() {
  const [apiData, setApiData] = useState<ApiResponse>({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchApiData = async (endpoint: string) => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get(`/api${endpoint}`);
      setApiData(response.data);
    } catch (err) {
      setError(
        `Failed to fetch ${endpoint}: ${
          err instanceof Error ? err.message : "Unknown error"
        }`
      );
    } finally {
      setLoading(false);
    }
  };

  const testEndpoints = [
    { path: "/", label: "Root" },
    { path: "/healthz", label: "Health Check" },
    { path: "/service-info", label: "Service Info" },
  ];

  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>Webservice Test Sandbox</h1>

        <p className={styles.description}>
          A simple web app for testing practice with Pytest
        </p>

        <div className={styles.grid}>
          {testEndpoints.map((endpoint) => (
            <div key={endpoint.path} className={styles.card}>
              <h2>{endpoint.label}</h2>
              <p>Test the {endpoint.path} endpoint</p>
              <button
                className={styles.button}
                onClick={() => fetchApiData(endpoint.path)}
                disabled={loading}
              >
                {loading ? "Testing..." : `Test ${endpoint.label}`}
              </button>
            </div>
          ))}
        </div>

        {Object.keys(apiData).length > 0 && (
          <div className={styles.response}>
            <h3>API Response:</h3>
            <pre className={styles.code}>
              {JSON.stringify(apiData, null, 2)}
            </pre>
          </div>
        )}

        {error && (
          <div className={styles.error}>
            <h3>Error:</h3>
            <p>{error}</p>
          </div>
        )}

        <div className={styles.info}>
          <h2>Testing Instructions</h2>
          <p>
            This app provides a simple backend API for testing practice. Use
            Pytest to write tests against the available endpoints:
          </p>
          <ul>
            <li>
              <code>GET /</code> - Root endpoint
            </li>
            <li>
              <code>GET /healthz</code> - Health check endpoint
            </li>
            <li>
              <code>GET /service-info</code> - Service information endpoint
            </li>
          </ul>
          <p>
            Start the services with: <code>docker compose up</code>
          </p>
          <p>
            Run tests with: <code>pytest</code>
          </p>
        </div>
      </main>
    </div>
  );
}
