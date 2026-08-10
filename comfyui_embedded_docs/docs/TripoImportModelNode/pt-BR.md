# Tripo: Importar Modelo

Este nó importa um modelo 3D externo para o Tripo para que outros nós de pós-processamento do Tripo, como Texture, Rig e Convert, possam usá-lo. O nó envia o modelo e retorna um ID de tarefa que identifica o modelo importado. GLB é recomendado porque as texturas são preservadas apenas quando incorporadas no arquivo, e texturizar um modelo importado requer um prompt de textura.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `model_3d` | Modelo 3D a ser importado (GLB / FBX / OBJ / STL, até 150 MB). Arquivos OBJ e STL não possuem texturas incorporadas. | FILE3D | Sim | GLB<br>FBX<br>OBJ<br>STL<br>Qualquer formato 3D |

**Observação:** Apenas os formatos GLB, FBX, OBJ e STL são suportados. GLTF (.gltf) não pode ser importado porque referencia arquivos externos; use um GLB de arquivo único. O arquivo de modelo deve ter 150 MB ou menos. GLB é recomendado porque as texturas sobrevivem à importação apenas quando incorporadas no arquivo. Arquivos OBJ e STL não contêm texturas incorporadas. Texturizar um modelo importado requer um prompt de textura.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `model task_id` | Um ID de tarefa que identifica o modelo importado para uso com os nós de pós-processamento do Tripo | MODEL_TASK_ID |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
