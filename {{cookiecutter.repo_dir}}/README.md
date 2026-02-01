<div align="center">
  <img src=".github/docs/logo.png?raw=true" width="150" alt="{{ cookiecutter.project_name }}'s logo" />
  <h1 align="center">{{ cookiecutter.project_name}}</h1>
</div>

<div align="center">
  <sub>Created by <a href="#">{{cookiecutter.author_name}}</a></sub>
</div>

<br /><br />

`{{cookiecutter.project_name}}` is .. lorem ipsum

<br>

### Installation

#### Prerequisites
- A local distribution of Python 3.12 or later.
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- [poetry](https://python-poetry.org/) (see [instructions](https://python-poetry.org/docs/#installing-with-pipx))

#### Setup

1. Clone the repository and `cd` into your local copy through your terminal emulator.
2. Install the Python dependencies via poetry:

   ```shell
   poetry install --with dev
   ```

3. Install the [pre-commit](https://pre-commit.com/)

   ```shell
   pre-commit install
   ```

4. Create a copy of the `env.sample` file as `.env`:

   ```shell
   cp env.sample .env
   ```

Then edit `.env` with your actual configuration values.

5. Run the app locally without Docker

   ```shell
   uvicorn {{cookiecutter.package_dir}}.main:app --reload
   ```

#### Docker (using Make)

1. Build and start services:

   ```shell
   make build
   make start
   ```

2. The application will be available at http://localhost:8000.


3. To stop the services:

   ```shell
   make stop
   ```

List all available commands:

   ```shell
   make help
   ```

<br>

### API Documentation

Interactive API documentation is available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

In production, the same `/docs` and `/redoc` paths are available at the production base URL.

<br>

### Testing

If your service integrates with downstream or third-party systems, mock external dependencies in your tests to ensure reliability and avoid flaky results.

Run tests

```shell
make test
```