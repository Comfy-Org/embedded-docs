# Tripo: Completar Partes da Malha

Completa as partes de um modelo 3D segmentado e repara regiões ausentes ou danificadas da malha. Recebe o ID de tarefa de um resultado de segmentação de malha do Tripo, solicita o trabalho de conclusão ao Tripo e aguarda sua finalização. Opcionalmente, você pode limitar o trabalho a nomes de partes específicos. O modelo concluído é retornado como um arquivo GLB.

> **Nota:** O Tripo mantém os registros de tarefas em seus servidores por 7 dias (a partir de 1º de dezembro de 2026). Um ID de tarefa mais antigo não pode mais ser resolvido, então executar novamente um fluxo de trabalho salvo depois desse prazo falha neste nó. Para continuar, execute novamente o nó Tripo de segmentação de malha anterior para criar um novo `SEGMENT_TASK_ID`. A segmentação que parte de um modelo precisa de um `MODEL_TASK_ID`; se ele também tiver expirado, reimporte primeiro o modelo com **Tripo: Importar Modelo**. Use o arquivo com o qual você trabalhou originalmente: o modelo baixado do Tripo ou, se você criou ou importou o modelo em vez de gerá-lo com um nó Tripo, seu próprio arquivo local. Se você não tem mais esse arquivo e o modelo veio de um nó Tripo de geração de modelo, execute novamente esse nó e conecte o novo `MODEL_TASK_ID` dele ao nó de segmentação; a malha pode ser diferente da original. Um fluxo de trabalho que usa **Tripo: Smart Segment** com `source` definido como `image` não precisa de nada disso: execute novamente esse nó com a mesma imagem, porque ele mesmo gera o modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `segment_task_id` | ID de tarefa de uma tarefa de segmentação de malha do Tripo. As partes do modelo segmentado dessa tarefa são concluídas. Conecte a saída SEGMENT_TASK_ID de um nó anterior de segmentação de malha do Tripo. | SEGMENT_TASK_ID | Sim | ID de tarefa único |
| `part_names` | Nomes de partes separados por vírgula a serem concluídos. Vazio conclui todas as partes. Padrão: string vazia. Espaços extras ao redor dos nomes são removidos e nomes duplicados são ignorados. | STRING | Não | Texto livre ou vazio |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `model_file` | Nome do arquivo do modelo concluído. Esta saída existe apenas para compatibilidade com versões anteriores. | STRING |
| `model task_id` | ID de tarefa da tarefa de conclusão de malha do Tripo concluída. Pode ser usado como entrada por outros nós do Tripo que esperam um ID de tarefa de modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D concluído com as partes reparadas, baixado como um arquivo GLB. | GLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
