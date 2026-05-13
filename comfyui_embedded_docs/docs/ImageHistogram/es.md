> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/es.md)

El nodo ImageHistogram analiza la distribución de color de una imagen de entrada. Calcula y genera varios histogramas, que son gráficos que muestran cuántos píxeles en la imagen tienen cada valor de intensidad posible. Genera histogramas separados para los canales de color rojo, verde y azul, un histograma RGB compuesto y un histograma de luminancia basado en una fórmula estándar de brillo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | N/A | La imagen de entrada a analizar. El nodo procesa la primera imagen del lote. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `luminancia` | HISTOGRAM | Un histograma compuesto que representa la intensidad promedio de píxeles en los canales rojo, verde y azul. |
| `rojo` | HISTOGRAM | Un histograma del brillo percibido de la imagen, calculado utilizando la fórmula de luminancia estándar ITU-R BT.709. |
| `verde` | HISTOGRAM | Un histograma que muestra la distribución de intensidades de píxeles en el canal de color rojo. |
| `azul` | HISTOGRAM | Un histograma que muestra la distribución de intensidades de píxeles en el canal de color verde. |
| `blue` | HISTOGRAM | Un histograma que muestra la distribución de intensidades de píxeles en el canal de color azul. |

---
**Source fingerprint (SHA-256):** `9bfcdb2907ab1e5cb2a9a736671fb9286b0e6ce6439fab95187f691b969ea53d`
