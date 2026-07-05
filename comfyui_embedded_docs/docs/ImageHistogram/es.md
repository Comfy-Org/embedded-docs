# Histograma de imagen

El nodo ImageHistogram analiza la distribución de color de una imagen de entrada. Calcula y genera varios histogramas, que son gráficos que muestran cuántos píxeles en la imagen tienen cada valor de intensidad posible. Genera histogramas separados para los canales de color rojo, verde y azul, un histograma RGB compuesto y un histograma de luminancia basado en una fórmula estándar de brillo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada a analizar. El nodo procesa la primera imagen del lote. | IMAGE | Sí | N/A |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `luminancia` | Un histograma compuesto que representa la intensidad promedio de píxeles en los canales rojo, verde y azul. | HISTOGRAM |
| `rojo` | Un histograma del brillo percibido de la imagen, calculado utilizando la fórmula de luminancia estándar ITU-R BT.709. | HISTOGRAM |
| `verde` | Un histograma que muestra la distribución de intensidades de píxeles en el canal de color rojo. | HISTOGRAM |
| `azul` | Un histograma que muestra la distribución de intensidades de píxeles en el canal de color verde. | HISTOGRAM |
| `blue` | Un histograma que muestra la distribución de intensidades de píxeles en el canal de color azul. | HISTOGRAM |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/es.md)

---
**Source fingerprint (SHA-256):** `9bfcdb2907ab1e5cb2a9a736671fb9286b0e6ce6439fab95187f691b969ea53d`
