# Tripo: Importar Modelo

Este nó importa um arquivo de modelo 3D externo para o sistema do Tripo, permitindo que você o utilize com os nós de pós-processamento do Tripo, como Texture, Rig e Convert. Ele faz o upload do seu modelo e retorna um ID de tarefa que outros nós do Tripo podem usar para referenciar o modelo importado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `model_3d` | Modelo 3D a ser importado (GLB / FBX / OBJ / STL, até 150 MB). Arquivos OBJ e STL não possuem texturas incorporadas. | FILE3D | Sim | GLB<br>FBX<br>OBJ<br>STL<br>Qualquer formato 3D |

**Observação:** O formato GLB é recomendado, pois as texturas são preservadas apenas quando incorporadas diretamente no arquivo. Arquivos OBJ e STL não suportam texturas incorporadas. O formato GLTF (.gltf) não é suportado, pois faz referência a arquivos externos; use um GLB de arquivo único. O tamanho do arquivo não deve exceder 150 MB.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `model task_id` | Um ID de tarefa que identifica o modelo importado para uso com os nós de pós-processamento do Tripo | MODEL_TASK_ID |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
