import importlib.metadata
packages = [
    "langchain",
    "langchain_core",
    "python-dotenv",
    "streamlit",
    "fastapi"
]
for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")