> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/es.md)

El nodo SamplerDPMPP_2S_Ancestral crea un muestreador que utiliza el método de muestreo DPM++ 2S Ancestral para generar imágenes. Este muestreador combina elementos deterministas y estocásticos para producir resultados variados manteniendo cierta consistencia. Permite controlar la aleatoriedad y los niveles de ruido durante el proceso de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | Sí | 0.0 - 100.0 | Controla la cantidad de ruido estocástico añadido durante el muestreo (valor por defecto: 1.0) |
| `s_ruido` | FLOAT | Sí | 0.0 - 100.0 | Controla la escala del ruido aplicado durante el proceso de muestreo (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Devuelve un objeto muestreador configurado que puede utilizarse en el pipeline de muestreo |