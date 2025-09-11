# CreditWise

proyecto/
│
├── backend/                 # Backend con FastAPI (Python)
│   ├── app/                  # Código principal
│   │   ├── api/              # Rutas/Endpoints
│   │   ├── core/             # Configuraciones y utilidades
│   │   ├── models/           # Modelos de datos (SQLAlchemy)
│   │   ├── schemas/          # Esquemas Pydantic
│   │   ├── services/         # Lógica de negocio
│   │   ├── db.py             # Conexión a MySQL
│   │   ├── main.py           # Punto de entrada FastAPI
│   ├── tests/                # Pruebas unitarias
│   ├── requirements.txt      # Dependencias Python
│   └── README.md
│
├── frontend/                 # Frontend con React
│   ├── public/               # Archivos estáticos
│   ├── src/                  # Código fuente
│   │   ├── components/       # Componentes reutilizables
│   │   ├── pages/            # Páginas
│   │   ├── services/         # Llamadas a la API
│   │   ├── App.js
│   │   └── index.js
│   ├── package.json          # Dependencias JS
│   └── README.md
│
├── db/                       # Scripts y migraciones de MySQL
│   ├── migrations/           # Archivos de migración
│   ├── init.sql              # Script inicial de base de datos
│   └── README.md
│
├── docs/                     # Documentación del proyecto
│   ├── arquitectura.md
│   ├── api.md
│   └── README.md
│
├── docker-compose.yml        # Configuración para levantar todo el stack
└── README.md
Cada uno de estos archivos se encuentra en la carpeta principal del
proyecto (nivel raíz).
