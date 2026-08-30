# Carregar Modelo de Corpo SAM3D

Carrega um modelo SAM3D Body a partir de um arquivo de checkpoint armazenado na pasta de detecção e o prepara para uso na detecção de corpo 3D. O nó carrega os pesos do modelo, detecta e aplica as configurações de quantização, se presentes, e envolve o modelo para gerenciamento automático de memória.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_file` | O arquivo de checkpoint do SAM3D Body a ser carregado. O arquivo deve estar na pasta de detecção. | COMBO | Sim | Todos os arquivos de modelo disponíveis na pasta de detecção |

Nota: O arquivo de modelo deve estar localizado na pasta de detecção. O carregamento falha com um erro se as chaves do dicionário de estado do checkpoint não corresponderem à estrutura do modelo SAM3D Body.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `sam3d_body_model` | O modelo SAM3D Body carregado, envolto para gerenciamento automático de memória entre GPU e CPU. Os pesos de detecção de mãos são removidos, portanto o modelo é especializado apenas em detecção de corpo. | SAM3D_BODY_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Loader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c66a1639b5f19dafcfb1466d68908969a4d33ab0d01c30e8b31d1f1ce41fd782`
