El nodo `BasicScheduler` está diseñado para calcular una secuencia de valores sigma para modelos de difusión basándose en el programador, el modelo y los parámetros de eliminación de ruido proporcionados. Ajusta dinámicamente el número total de pasos según el factor de eliminación de ruido para afinar el proceso de difusión, proporcionando "recetas" precisas para diferentes etapas en procesos de muestreo avanzados que requieren un control detallado (como el muestreo en múltiples etapas).

## Entradas

| Parámetro | Descripción Metafórica | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Propósito Técnico |
| --- | --- | --- | --- | --- | --- | --- |
| `modelo` | **Tipo de Lienzo**: Diferentes materiales de lienzo necesitan diferentes fórmulas de pintura | MODEL | Entrada | - | - | Objeto del modelo de difusión, determina la base de cálculo de sigma |
| `programador` | **Técnica de Mezcla**: Elige cómo cambia la concentración de pintura | COMBO[STRING] | Widget | - | 9 opciones | Algoritmo de programación, controla el modo de disminución del ruido |
| `pasos` | **Cantidad de Mezclas**: Diferencia de precisión entre 20 y 50 mezclas | INT | Widget | 20 | 1-10000 | Pasos de muestreo, afecta la calidad y velocidad de generación |
| `desruido` | **Intensidad de Creación**: Controla el nivel desde ajuste fino hasta repintado | FLOAT | Widget | 1.0 | 0.0-1.0 | Fuerza de eliminación de ruido, admite escenarios de repintado parcial |

### Tipos de Programador

Basado en el código fuente `comfy.samplers.SCHEDULER_NAMES`, admite los siguientes 9 programadores:

| Nombre del Programador | Características      | Casos de Uso                    | Patrón de Disminución de Ruido |
| ---------------------- | -------------------- | ------------------------------- | ------------------------------ |
| **normal**             | Lineal estándar      | Escenarios generales, equilibrado | Disminución uniforme           |
| **karras**             | Transición suave     | Alta calidad, rico en detalles  | Disminución no lineal suave    |
| **exponential**        | Disminución exponencial | Generación rápida, eficiencia | Disminución exponencial rápida |
| **sgm_uniform**        | Uniforme SGM         | Optimización de modelos específicos | Disminución optimizada SGM     |
| **simple**             | Programación simple  | Pruebas rápidas, uso básico     | Disminución simplificada       |
| **ddim_uniform**       | Uniforme DDIM        | Optimización de muestreo DDIM   | Disminución específica DDIM    |
| **beta**               | Distribución Beta    | Necesidades de distribución especial | Disminución por función Beta   |
| **linear_quadratic**   | Lineal cuadrático    | Optimización de escenarios complejos | Disminución por función cuadrática |
| **kl_optimal**         | Óptimo KL            | Optimización teórica            | Disminución optimizada por divergencia KL |

## Salidas

| Parámetro | Descripción Metafórica | Tipo de Dato | Tipo de Salida | Significado Técnico |
| --- | --- | --- | --- | --- |
| `sigmas` | **Tabla de Recetas de Pintura**: Lista detallada de concentraciones de pintura para usar paso a paso | SIGMAS | Salida | Secuencia de niveles de ruido, guía el proceso de eliminación de ruido del modelo de difusión |

## Función del Nodo: Asistente de Mezcla de Colores del Artista

Imagina que eres un artista creando una imagen clara a partir de una mezcla caótica de pintura (ruido). `BasicScheduler` actúa como tu **asistente profesional de mezcla de colores**, cuyo trabajo es preparar una serie de recetas precisas de concentración de pintura:

### Flujo de Trabajo

- **Paso 1**: Usa pintura al 90% de concentración (nivel alto de ruido)
- **Paso 2**: Usa pintura al 80% de concentración
- **Paso 3**: Usa pintura al 70% de concentración
- **...**
- **Paso Final**: Usa pintura al 0% de concentración (lienzo limpio, sin ruido)

### Habilidades Especiales del Asistente de Color

**Diferentes métodos de mezcla (programador)**:

- **Método de mezcla "karras"**: La concentración de pintura cambia de manera muy suave, como la técnica de degradado de un artista profesional
- **Método de mezcla "exponential"**: La concentración de pintura disminuye rápidamente, adecuado para creación rápida
- **Método de mezcla "linear"**: La concentración de pintura disminuye uniformemente, estable y controlable

**Control fino (pasos)**:

- **20 mezclas**: Pintura rápida, prioriza la eficiencia
- **50 mezclas**: Pintura detallada, prioriza la calidad

**Intensidad de creación (eliminación de ruido)**:

- **1.0 = Creación completamente nueva**: Comienza desde un lienzo en blanco
- **0.5 = Media transformación**: Mantén la mitad de la pintura original, transforma la otra mitad
- **0.2 = Ajuste fino**: Solo realiza ajustes sutiles a la pintura original

### Colaboración con Otros Nodos

`BasicScheduler` (Asistente de Color) → Prepara Receta → `SamplerCustom` (Artista) → Pintura Real → Obra Completada

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/es.md)
