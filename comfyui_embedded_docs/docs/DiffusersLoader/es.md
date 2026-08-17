# Cargador de Difusores

El nodo DiffusersLoader está obsoleto. Carga modelos preentrenados guardados en el formato diffusers de Hugging Face y devuelve los tres componentes estándar necesarios para el pipeline: MODEL, CLIP y VAE. El nodo escanea automáticamente las carpetas de diffusers configuradas en busca de directorios de modelo válidos (carpetas que contienen un archivo `model_index.json`) y le permite elegir cuál cargar.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model_path` | La ruta al directorio del modelo diffusers que se va a cargar. El nodo escanea las carpetas de diffusers configuradas y lista todos los directorios que contienen un archivo `model_index.json`. | COMBO | Sí | Autocompletado desde las carpetas de diffusers configuradas (toda subcarpeta que contenga un archivo `model_index.json`) |

Nota: la ruta seleccionada se valida contra la lista de modelos descubiertos. La carga falla con un error si la ruta ya no está en la lista o si no se puede encontrar el directorio del modelo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `MODEL` | El componente de modelo cargado desde el formato diffusers | MODEL |
| `CLIP` | El componente de modelo de codificación de texto CLIP cargado desde el formato diffusers | CLIP |
| `VAE` | El componente VAE (Autoencoder Variacional) cargado desde el formato diffusers | VAE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/es.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
