[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=Bakkym_fastAPI--devco)](https://sonarcloud.io/summary/new_code?id=Bakkym_fastAPI--devco)

# Arquitectura despliegue
![image](https://github.com/Bakkym/fastAPI--devco/assets/92707871/00074275-3e67-4382-9643-f5ff4884d18c)


# Comandos
## Instalar dependencias
`pip install --no-cache-dir --upgrade -r requirements.txt`
## Ejecutar el servicio
`uvicorn app.main:app --host 0.0.0.0 --port 8000`
## Ejecutar pruebas unitarias
`python -m unittest discover tests`
## Compilar Docker
`docker build -t devco/fast-api-example:latest .`
