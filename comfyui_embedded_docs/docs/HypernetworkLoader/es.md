> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/es.md)

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/hypernetworks`, y también lee modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo de la carpeta correspondiente.

El nodo HypernetworkLoader está diseñado para mejorar o modificar las capacidades de un modelo determinado mediante la aplicación de una hiperred. Carga una hiperred específica y la aplica al modelo, alterando potencialmente su comportamiento o rendimiento según el parámetro de intensidad. Este proceso permite realizar ajustes dinámicos en la arquitectura o los parámetros del modelo, posibilitando sistemas de IA más flexibles y adaptativos.

## Entradas

| Campo                | Tipo Comfy        | Descripción                                                                                  |
|----------------------|-------------------|----------------------------------------------------------------------------------------------|
| `model`              | `MODEL`           | El modelo base al que se aplicará la hiperred, determinando la arquitectura que se mejorará o modificará. |
| `hypernetwork_name`  | `COMBO[STRING]`   | El nombre de la hiperred que se cargará y aplicará al modelo, afectando el comportamiento o rendimiento modificado del modelo. |
| `strength`           | `FLOAT`           | Un escalar que ajusta la intensidad del efecto de la hiperred sobre el modelo, permitiendo un ajuste fino de las alteraciones. |

## Salidas

| Campo    | Tipo de Dato | Descripción                                                              |
|----------|--------------|--------------------------------------------------------------------------|
| `model`  | `MODEL`      | El modelo modificado después de aplicar la hiperred, mostrando el impacto de la hiperred sobre el modelo original. |