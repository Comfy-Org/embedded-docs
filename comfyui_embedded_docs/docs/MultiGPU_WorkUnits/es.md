> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, no dude en contribuir. [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_WorkUnits/es.md)

## Resumen general

El nodo MultiGPU CFG Split permite que el trabajo de difusión se reparta entre varias GPU instaladas en la misma computadora. La mejora de velocidad depende del flujo de trabajo, pero en flujos comunes se han medido aumentos de hasta 1.95x.

## Detalles importantes

No se admite mezclar tipos de GPU diferentes. Las GPU instaladas deben ser iguales, por ejemplo 2x 5090 o 2x 5080.

ComfyUI detecta automáticamente varias GPU instaladas cuando se inicia.

## GPUs compatibles

Cualquier configuración homogénea de dos GPU con arquitectura Ampere o superior, por ejemplo 2 x 3090 o 2 x RTX6000 Pro.

## Modelos compatibles

* LTX-2.3  
* WAN 2.2  
* FLUX.2 Klein - versiones base  
* Z-Image  
* Stable Diffusion 3.5 Large  
* Hunyuan Video  
* Qwen-Image-Edit-2511  
* Hunyuan-3D-v2.1  
* SDXL

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | N/A | El modelo que se preparará para usar MultiGPU CFG Split antes del muestreo. |
| `max_gpus` | INT | Sí | Mínimo: 1<br>Paso: 1<br>Predeterminado: 2 | La cantidad máxima de GPU idénticas que se usarán para repartir la carga. Ajústelo al número de GPU iguales instaladas en su sistema. |

## Salidas

| Nombre de salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `MODEL` | MODEL | El modelo preparado para MultiGPU CFG Split, listo para un muestreo acelerado. |

## Ubicación del nodo y notas del flujo de trabajo

![image1.png](./asset/image1.png)

El campo `max_gpus` debe configurarse con la cantidad máxima de GPU idénticas instaladas en el sistema.

**Ubicación del nodo:** MultiGPU CFG Split debe colocarse entre el nodo de carga del modelo y el nodo de muestreo. Si hay otros nodos conectados a la salida del modelo del cargador, MultiGPU CFG Split debe ser el último nodo de esa cadena antes del nodo de muestreo.

![image2.png](./asset/image2.png)

**Requisitos del flujo de trabajo:** Este nodo divide el flujo de difusión a nivel de CFG. Por eso, el CFG del flujo debe ser mayor que 1. Los flujos destilados que necesitan CFG = 1 no mostrarán una mejora de rendimiento al usar MultiGPU CFG Split con varias GPU.

## Verificación del uso de varias GPU

Cuando ejecute un flujo con MultiGPU CFG Split activado, puede abrir el Administrador de tareas de Windows y entrar en la categoría de rendimiento.

![image3.png](./asset/image3.png)

![image4.png](./asset/image4.png)

Mientras el sampler esté funcionando en el flujo, debería ver actividad en las dos GPU instaladas.

## Problemas conocidos

Pendiente de definición.

## Flujo de trabajo de ejemplo con varias GPU: (Wan 2.2 FP8)

[https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive_link](https://drive.google.com/file/d/1VORVx7rMPSH9rY1HD2hCujcHa2vB9rzv/view?usp=drive_link)

---
**Source fingerprint (SHA-256):** `7293ee785e29aea9a1a70a10444b99e89fb23c866505628ec57c209a2b8aaee0`
