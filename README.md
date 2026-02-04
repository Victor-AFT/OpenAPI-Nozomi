
# 🛰️ OpenAPI-Nozomi – Scripts de Automatización para Nozomi Networks

Este repositorio contiene una colección de scripts diseñados para interactuar con la **OpenAPI de Nozomi Networks**, permitiendo consultar, extraer y procesar información desde sensores Guardian o CMC.

Los scripts están orientados a facilitar la integración con sistemas externos, automatizar consultas y mejorar la visibilidad de activos y eventos en entornos OT/ICS.

---
## 🚀 Funcionalidades

Los scripts de este repositorio permiten:

- Realizar **consultas HTTP** al endpoint OpenAPI de Nozomi.
- Ejecutar queries personalizadas para obtener datos como:
  - Nodos
  - Alertas
  - Dispositivos
  - Conexiones
- Interactuar con el endpoint `/api/open/query/do`.
- Autenticación básica (Basic Auth) según las recomendaciones de Nozomi Networks.
- Exportar resultados en formatos más manejables (JSON / TXT).

---
## 📌 ¿Qué es la OpenAPI de Nozomi Networks?

Según la documentación oficial de Nozomi, la OpenAPI proporciona un endpoint **HTTP** que permite realizar queries avanzadas sobre los sensores Guardian o CMC. Estas consultas permiten obtener información en tiempo real o histórica sobre los nodos, conexiones, eventos, alertas y más.

La API utiliza **autenticación Basic Auth** y admite queries complejas siempre que estén correctamente codificadas (URI encoding).  
Más detalles en la documentación oficial.

---
## 📁 Contenido del repositorio

```
OpenAPI-Nozomi/
├── consultas_basicas.py      # Ejemplos de consultas simples
├── consultas_avanzadas.py    # Queries complejas con filtros
├── autenticacion.py          # Gestión de credenciales y conexión
├── utils.py                  # Funciones auxiliares (exportar, formatear, etc.)
└── README.md                 # Este archivo
```

*Nota: La estructura es orientativa, dependiendo de los nombres reales en tu repo.*

---
## 🧠 Ejemplo de uso

```bash
python consultas_basicas.py
```

Un ejemplo común es consultar los nodos:

```python
curl -H "Authorization: Basic <TOKEN>"      "https://<sensor>/api/open/query/do?query=nodes"
```

El resultado contiene:
- `header`: columnas
- `result`: datos obtenidos
- `total`: número total de objetos

---
## 🔧 Requisitos

- Python 3.x
- Librerías necesarias:

```bash
pip install requests
```

- Credenciales OpenAPI con permisos de **queries y exportación**.

---
## 🛡️ Seguridad

- Se recomienda crear un usuario específico para el uso de OpenAPI (según Nozomi Networks). 
- Evita guardar credenciales en texto plano. Usa variables de entorno.
- No uses `curl -k` salvo en entornos de laboratorio.

---
## 🧩 Futuras mejoras

- Añadir soporte para exportación automática en CSV.
- Dashboard en tiempo real con consultas programadas.
- Integración con sistemas SIEM.

---
## 🤝 Contribuciones

¡Tus aportes son bienvenidos! Si deseas mejorar queries, optimizar código o añadir funcionalidades, abre un **pull request**.

---
## 📜 Licencia

Libre para uso personal y profesional.

