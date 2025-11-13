# ADK Workshop

This project is for YourSurprise's workshop about Google's ADK (Agent Development Kit).

## Setup

This project uses `uv` for package management.

To install the dependencies from the lock file, run:

```bash
uv sync
```

To add a new dependency, run:

```bash
uv add <package-name>
```

## Running the application

To run the web interface, use the following command:

```bash
adk web
```

You can access the running application through the "Ports" tab in your Cloud Workstation's VSCode interface. A new entry should appear for the port the application is running on.

## Documentation

For more information on the Agent Development Kit (ADK), please refer to the [official Google Cloud documentation](https://cloud.google.com/vertex-ai/docs/agent-builder/overview).
