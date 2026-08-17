# Int

El nodo `PrimitiveInt` proporciona una forma sencilla de trabajar con valores enteros en su flujo de trabajo. Toma una entrada entera y produce el mismo valor, lo que resulta útil para pasar parámetros enteros entre nodos o establecer valores numéricos específicos para otras operaciones.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `value` | El valor entero de salida (por defecto: 0) | INT | Sí | -9223372036854775807 a 9223372036854775807 |

Nota: El parámetro `value` está configurado con un comportamiento de control fijo posterior a la generación, por lo que el valor no cambia automáticamente después de cada generación.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | El valor entero de entrada se pasa sin cambios | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveInt/es.md)

---
**Source fingerprint (SHA-256):** `b928ec40c781043c1c8652de3aebedc755d9b63be9e2c773e3fb26ce4d594bba`
