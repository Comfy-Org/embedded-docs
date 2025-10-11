> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/es.md)

El nodo SamplerER_SDE proporciona métodos de muestreo especializados para modelos de difusión, ofreciendo diferentes tipos de solucionadores que incluyen enfoques ER-SDE, SDE de tiempo inverso y ODE. Permite controlar el comportamiento estocástico y las etapas computacionales del proceso de muestreo. El nodo ajusta automáticamente los parámetros según el tipo de solucionador seleccionado para garantizar un funcionamiento adecuado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Sí | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" | El tipo de solucionador a utilizar para el muestreo. Determina el enfoque matemático para el proceso de difusión. |
| `max_stage` | INT | Sí | 1-3 | El número máximo de etapas para el proceso de muestreo (por defecto: 3). Controla la complejidad computacional y la calidad. |
| `eta` | FLOAT | Sí | 0.0-100.0 | Fuerza estocástica de SDE de tiempo inverso (por defecto: 1.0). Cuando eta=0, se reduce a ODE determinista. Esta configuración no se aplica al tipo de solucionador ER-SDE. |
| `s_noise` | FLOAT | Sí | 0.0-100.0 | Factor de escala de ruido para el proceso de muestreo (por defecto: 1.0). Controla la cantidad de ruido aplicado durante el muestreo. |

**Restricciones de Parámetros:**
- Cuando `solver_type` está configurado como "ODE" o cuando se usa "Reverse-time SDE" con `eta`=0, tanto `eta` como `s_noise` se establecen automáticamente en 0 independientemente de los valores ingresados por el usuario.
- El parámetro `eta` solo afecta al tipo de solucionador "Reverse-time SDE" y no tiene efecto en el tipo de solucionador "ER-SDE".

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Un objeto sampler configurado que puede usarse en el pipeline de muestreo con los ajustes de solucionador especificados. |