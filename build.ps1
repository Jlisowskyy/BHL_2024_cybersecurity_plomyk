python -m venv .venv
./.venv/Scripts/activate
pip install -r ConnectionSolution/requirements.txt
cd AdministratorUI
dotnet build
cd ..