python_sources(
    name="django",  # Align with project name
    sources=["django_app/**/*.py", "manage.py"]
)
python_requirements(
    name="reqs",
    source="pyproject.toml"
)
pex_binary(
    name="manage",
    entry_point="manage:main",
    dependencies=[":django", ":reqs"]
)