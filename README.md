# Backgammon - Proyecto Final

## 🐳 Despliegue con Docker

Este proyecto incluye configuración de Docker para facilitar la ejecución tanto del juego como de los tests.

## 📋 Requisitos previos

* Docker instalado ([Instalar Docker](https://docs.docker.com/get-docker/))
* Docker Compose instalado ([Instalar Docker Compose](https://docs.docker.com/compose/install/))

## 🎮 Modo Juego (CLI)

Para ejecutar el juego en modo consola:

```bash
# Construir la imagen (solo la primera vez)
docker-compose build cli

# Ejecutar el juego
docker-compose run --rm cli
```

El juego se ejecutará en modo interactivo en la terminal.

## 🧪 Modo Testing

Para ejecutar todos los tests con pytest y coverage:

```bash
# Construir la imagen (solo la primera vez)
docker-compose build test

# Ejecutar los tests con coverage
docker-compose run --rm test
```

Esto ejecutará:
* Todos los tests con pytest
* Reporte de cobertura en terminal
* Reporte HTML en la carpeta `htmlcov/`

## 🎨 Modo Pygame (Interfaz Gráfica)

Para ejecutar la interfaz gráfica con Pygame:

### Linux:

```bash
# 1. Permitir conexión X11 (IMPORTANTE)
xhost +local:docker

# 2. Construir la imagen (solo la primera vez)
docker-compose build pygame

# 3. Ejecutar pygame
docker-compose run --rm pygame

# 4. Revocar permisos después (opcional, por seguridad)
xhost -local:docker
```

### Windows/Mac: 

Docker no soporta nativamente la interfaz gráfica en estos sistemas. Se recomienda ejecutar localmente:

```bash
# Activar entorno virtual (si lo usas)
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Ejecutar pygame
python -m ui.pygame_ui
```

## 🛠️ Comandos útiles

```bash
# Ver todas las imágenes
docker images

# Ver contenedores en ejecución
docker ps

# Limpiar contenedores detenidos
docker-compose down

# Reconstruir después de cambios en el código
docker-compose build

# Reconstruir desde cero (sin caché)
docker-compose build --no-cache

# Ver logs de un servicio
docker-compose logs pygame
```

## 📦 Estructura de archivos Docker

```
.
├── Dockerfile              # Definición de la imagen
├── docker-compose.yml      # Configuración de servicios (cli, test, pygame)
├── requirements.txt        # Dependencias Python
└── README.md              # Este archivo
```

## ⚙️ Personalización

Para modificar los comandos de ejecución, edita el archivo `docker-compose.yml` en la sección `command` del servicio correspondiente.

## 🚀 Ejecución sin Docker (alternativa)

Si prefieres no usar Docker, puedes ejecutar directamente:

### Instalar dependencias:

```bash
pip install -r requirements.txt
```

### Jugar (CLI):

```bash
python -m cli.cli
```

### Tests:

```bash
pytest --cov=. --cov-report=term-missing --cov-report=html
```

### Pygame:

```bash
python -m pygame_ui.pygameui
```

## 🐛 Solución de problemas

### Pygame no muestra ventana en Linux:

```bash
# Verificar que DISPLAY esté configurado
echo $DISPLAY

# Si está vacío, configurarlo
export DISPLAY=:0

# Dar permisos X11
xhost +local:docker
```

### Error "cannot open display":

Asegúrate de haber ejecutado `xhost +local:docker` antes de correr pygame.

### Tests fallan por permisos:

```bash
# Limpiar contenedores y volúmenes
docker-compose down -v

# Reconstruir
docker-compose build --no-cache
```

## 📝 Notas

* La primera ejecución puede tardar mientras se descargan las imágenes y se instalan dependencias
* Los cambios en el código se reflejan automáticamente gracias a los volúmenes montados
* El servicio pygame requiere acceso al servidor X11 en Linux
* Para Windows/Mac, pygame debe ejecutarse localmente fuera de Docker

## 🎯 Servicios disponibles

| Servicio | Descripción | Comando |
|----------|-------------|---------|
| `cli` | Juego en modo consola | `docker-compose run --rm cli` |
| `test` | Tests con pytest y coverage | `docker-compose run --rm test` |
| `pygame` | Interfaz gráfica (solo Linux) | `docker-compose run --rm pygame` |