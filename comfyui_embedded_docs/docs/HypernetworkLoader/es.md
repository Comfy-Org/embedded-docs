Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/hypernetworks`, y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml. A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo HypernetworkLoader está diseñado para mejorar o modificar las capacidades de un modelo dado aplicando un hypernetwork. Carga un hypernetwork especificado y lo aplica al modelo, alterando potencialmente su comportamiento o rendimiento basado en el parámetro de fuerza. Este proceso permite ajustes dinámicos a la arquitectura o parámetros del modelo, habilitando sistemas de IA más flexibles y adaptativos.

## Entradas

| Campo                 | Comfy dtype       | Descripción                                                                                  |
|-----------------------|-------------------|----------------------------------------------------------------------------------------------|
| `model`               | `MODEL`           | El modelo base al que se aplicará el hypernetwork, determinando la arquitectura a mejorar o modificar. |
| `hypernetwork_name`  | `COMBO[STRING]`   | El nombre del hypernetwork que se cargará y aplicará al modelo, impactando el comportamiento o rendimiento modificado del modelo. |
| `strength`            | `FLOAT`           | Un escalar que ajusta la intensidad del efecto del hypernetwork en el modelo, permitiendo un ajuste fino de las alteraciones. |

## Salidas

| Campo   | Data Type | Descripción                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | El modelo modificado después de que el hypernetwork ha sido aplicado, mostrando el impacto del hypernetwork en el modelo original. |
