# Agent Workshop

This is a workshop for building agents with the Google AI Development Kit.

## Getting Started

1.  **Set up your environment file.**

    Copy the `env.dist` file to `.env` and add your Google API key:

    ```bash
    cp app/.env.dist app/.env
    ```

    Then, edit `app/.env` to add your API key:

    ```
    GOOGLE_API_KEY="YOUR_API_KEY"
    ```

2.  **Build and run the Docker container.**

    ```bash
    docker-compose up --build -d
    ```



3.  **Access the web interface.**

    Open your web browser to `http://localhost:8000`.
