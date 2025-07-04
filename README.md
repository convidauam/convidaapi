# CONVIDA (Back-end API conection wrapper)

## Setup for client

```bash
cd client # from the root directory of the project
npm install
```


## Setup for backend

```bash
cd backend # from the root directory of the project
uv sync
cd dummy
uv run setup.py develop
```

## 1. Run the backend

```bash
cd backend/dummy
uv run pserve dummy.ini --reload
```

>[!NOTE]
> Go to [http://localhost:6543/example](http://localhost:6543/example) to see the service.

## 2. Run the client

```bash
cd client
node example.js
```