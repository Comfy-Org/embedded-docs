# Batch Cameras

Une câmeras e órbitas de câmera em uma única lista de câmeras, na ordem de entrada. Render Mesh e Render Splat renderizam uma imagem por câmera na lista, que é como uma renderização multivisão é construída.

## Entradas

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `cameras` | Slot expansível de câmeras, provenientes de Create Camera Info, Create Camera Orbit ou de um visualizador. Uma lista de câmeras conta como todas as câmeras nela. | AUTOGROW | Sim | 1 a 50 câmeras |

## Saídas

| Nome da saída | Descrição | Tipo de dado |
| --- | --- | --- |
| `camera_info` | Uma lista de câmeras contendo todas as câmeras de entrada, na ordem de entrada. | LOAD3D_CAMERA |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchCameras/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a5ddae7f539a2d70efc1b156f7b4ec4b219d7cf78544b882f7b8f9538ae9a88d`
