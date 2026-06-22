# Tripo: Refinar Modelo Rascunho

O TripoRefineNode refina modelos 3D preliminares criados especificamente por modelos Tripo v1.4. Ele recebe um ID de tarefa de modelo e o processa através da API Tripo para gerar uma versão melhorada do modelo. Este nó foi projetado para funcionar exclusivamente com modelos preliminares produzidos por modelos Tripo v1.4.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `id_da_tarefa_do_modelo` | Deve ser um modelo Tripo v1.4 | MODEL_TASK_ID | Sim | - |

**Observação:** Este nó aceita apenas modelos preliminares criados por modelos Tripo v1.4. O uso de modelos de outras versões pode resultar em erros.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O caminho do arquivo ou referência para o modelo refinado (apenas para compatibilidade reversa) | STRING |
| `model task_id` | O identificador da tarefa para a operação do modelo refinado | MODEL_TASK_ID |
| `GLB` | O modelo 3D refinado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
