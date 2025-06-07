El nodo `ProgramadorBásico` está diseñado para calcular una secuencia de valores sigma para modelos de difusión basados en el programador, modelo y parámetros de reducción de ruido proporcionados. Ajusta dinámicamente el número total de pasos según el factor de reducción de ruido para afinar el proceso de difusión, proporcionando "recetas" precisas para diferentes etapas en procesos de muestreo avanzados que requieren control fino (como el muestreo por etapas).

## Entradas

| Parámetro   | Tipo de Dato  | Tipo de Entrada | Por Defecto | Rango     | Descripción Metafórica   | Propósito Técnico   |
| ----------- | ------------- | --------------- | ----------- | --------- | ------------------------ | ------------------- |
| `modelo`     | MODEL         | Input           | -           | -         | **Tipo de Lienzo**: Diferentes materiales de lienzo necesitan diferentes fórmulas de pintura | Objeto del modelo de difusión, determina la base del cálculo sigma |
| `programador` | COMBO[STRING] | Widget          | -           | 9 opciones| **Técnica de Mezcla**: Elegir cómo cambia la concentración de pintura | Algoritmo de programación, controla el modo de decaimiento del ruido |
| `pasos`     | INT           | Widget          | 20          | 1-10000   | **Conteo de Mezclas**: Diferencia de precisión entre 20 vs 50 mezclas | Pasos de muestreo, afecta la calidad y velocidad de generación |
| `desruido`   | FLOAT         | Widget          | 1.0         | 0.0-1.0   | **Intensidad de Creación**: Nivel de control desde ajuste fino hasta repintado | Fuerza de reducción de ruido, soporta escenarios de repintado parcial |

### Tipos de Programadores

Basado en el código fuente `comfy.samplers.SCHEDULER_NAMES`, soporta los siguientes 9 programadores:

| Nombre del Programador | Características        | Casos de Uso                      | Patrón de Decaimiento del Ruido    |
| ---------------------- | ---------------------- | --------------------------------- | ---------------------------------- |
| **normal**             | Lineal estándar        | Escenarios generales, equilibrado | Decaimiento uniforme               |
| **karras**             | Transición suave       | Alta calidad, rico en detalles    | Decaimiento no lineal suave        |
| **exponential**        | Decaimiento exponencial| Generación rápida, eficiencia     | Decaimiento rápido exponencial     |
| **sgm_uniform**        | SGM uniforme           | Optimización de modelo específico | Decaimiento optimizado SGM         |
| **simple**             | Programación simple    | Pruebas rápidas, uso básico       | Decaimiento simplificado           |
| **ddim_uniform**       | DDIM uniforme          | Optimización de muestreo DDIM     | Decaimiento específico DDIM        |
| **beta**               | Distribución Beta      | Necesidades de distribución especial | Decaimiento de función Beta      |
| **linear_quadratic**   | Cuadrático lineal      | Optimización de escenarios complejos | Decaimiento de función cuadrática |
| **kl_optimal**         | KL óptimo              | Optimización teórica              | Decaimiento optimizado de divergencia KL |

## Salidas

| Parámetro | Tipo de Dato | Tipo de Salida | Descripción Metafórica           | Significado Técnico                              |
| --------- | ------------ | -------------- | -------------------------------- | ----------------------------------------------- |
| `sigmas`  | SIGMAS       | Output         | **Tabla de Recetas de Pintura**: Lista detallada de concentración de pintura para uso paso a paso | Secuencia de niveles de ruido, guía el proceso de reducción de ruido del modelo de difusión |

## Rol del Nodo: Asistente de Mezcla de Colores del Artista

Imagina que eres un artista creando una imagen clara a partir de una mezcla caótica de pintura (ruido). `ProgramadorBásico` actúa como tu **asistente profesional de mezcla de colores**, cuyo trabajo es preparar una serie de recetas precisas de concentración de pintura:

### Flujo de Trabajo

- **Paso 1**: Usar pintura de concentración 90% (nivel de ruido alto)
- **Paso 2**: Usar pintura de concentración 80%  
- **Paso 3**: Usar pintura de concentración 70%
- **...**
- **Paso Final**: Usar concentración 0% (lienzo limpio, sin ruido)

### Habilidades Especiales del Asistente de Colores

**Diferentes métodos de mezcla (scheduler)**:

- **Método de mezcla "karras"**: La concentración de pintura cambia muy suavemente, como la técnica de gradiente de un artista profesional
- **Método de mezcla "exponential"**: La concentración de pintura disminuye rápidamente, adecuado para creación rápida
- **Método de mezcla "linear"**: La concentración de pintura disminuye uniformemente, estable y controlable

**Control fino (steps)**:

- **20 mezclas**: Pintura rápida, prioridad en eficiencia
- **50 mezclas**: Pintura fina, prioridad en calidad

**Intensidad de creación (denoise)**:

- **1.0 = Creación completamente nueva**: Comenzar completamente desde lienzo en blanco
- **0.5 = Media transformación**: Mantener la mitad de la pintura original, transformar la mitad
- **0.2 = Ajuste fino**: Solo hacer ajustes sutiles a la pintura original

### Colaboración con Otros Nodos

`ProgramadorBásico` (Asistente de Colores) → Preparar Receta → `ÉchantillonneurPersonnalisé` (Artista) → Pintura Real → Trabajo Completado
