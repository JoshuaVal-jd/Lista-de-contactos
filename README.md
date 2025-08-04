# Lista de contactos

Proyecto de consola en Python que simula la gestión de una agenda de contactos, inspirado en las apps de contactos de dispositivos móviles. Permite agregar, consultar, modificar y eliminar contactos, así como organizarlos por áreas y grupos, y exportar listados en PDF.

## Descripción

Este proyecto, escrito en Python 3.12.6, emula las funcionalidades básicas de una aplicación de contactos:

- Gestión de **áreas** (códigos numéricos asociados a prefijos telefónicos).
- Gestión de **contactos** con atributos: número de teléfono, área, tipo (Móvil, Casa, Trabajo, Otro), nombre, correo electrónico, dirección física, fecha de nacimiento, pasatiempos y notas.
- Organización en **grupos** de contactos, con asignación y eliminación de miembros.
- **Exportación a PDF** de listados filtrados usando el módulo `fpdf`.
- Menú interactivo en consola con secciones de Ayuda y Acerca de.

## Requisitos

- Python 3.12.6
- Módulo externo `fpdf`
- Módulos estándar: `os`, `re`

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/lista-de-contactos.git
   cd lista-de-contactos
   ```
2. (Opcional) Crear y activar un entorno virtual:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Instalar las dependencias:
   ```bash
   pip install fpdf
   ```

## Uso

Ejecutar el script en la consola o en IDLE:

```bash
python lista_digital_de_contactos.py
```

Para una guía detallada de uso, consulta el [Manual de Usuario](manual_de_usuario_lista_digital_de_contactos.pdf).

## Configuración inicial

Antes de registrar contactos, realiza estos pasos en el menú:

1. **Registrar áreas**: añade los códigos numéricos (p. ej., 506) y sus nombres descriptivos.
2. **Configurar valores por omisión**: elige el área predeterminada y el tipo de teléfono (Móvil, Casa, Trabajo u Otro) que se aplicarán al crear nuevos contactos sin especificar.

## Menú y características principales

- **Áreas**:
  - Agregar, consultar, modificar y eliminar códigos de área.
- **Contactos**:
  - Agregar, consultar, modificar y eliminar contactos.
- **Grupos**:
  - Crear, renombrar y eliminar grupos.
  - Añadir o quitar contactos de cada grupo.
- **Listado en PDF**:
  - Generar un listado filtrado de contactos con exportación a un archivo PDF con columnas de todos los campos.
- **Ayuda**:
  - Mostrar en pantalla el manual de usuario.
- **Acerca de**:
  - Mostrar nombre del programa, versión, fecha de creación y autor.

## Autor

Joshua Valvarde Arguedas  
Versión 1.0 (15/04/2024)

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contribuciones

¡Bienvenido! Para contribuir:

1. Abre un issue detallando tu sugerencia o reporte.
2. Envía un pull request con cambios claros y descritos.

Todas las mejoras, correcciones y aportaciones son bienvenidas. ¡Gracias por tu ayuda!

