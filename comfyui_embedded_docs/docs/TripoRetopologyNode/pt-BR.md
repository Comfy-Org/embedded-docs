# TripoRetopologyNode

Tripo: Retopology pega um modelo 3D high-poly gerado por um nó Tripo anterior e o reconstrói como uma versão low-poly com topologia limpa. Ele envia o modelo para o serviço de retopologia da Tripo, aguarda a conclusão da tarefa, baixa o modelo finalizado e expõe o ID da tarefa para uso por outros nós Tripo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | ID da tarefa do modelo high-poly de origem. Aceita um ID de tarefa de modelo de um nó de geração Tripo ou um ID de tarefa de segmento do Tripo: Segment Model. | STRING | Sim | Tripo task ID |
| `face_limit` | Contagem de faces desejada: 500 a 20.000 triângulos ou 500 a 10.000 quads. -1 permite que a Tripo escolha. (padrão: -1) | INT | Sim | -1 (automatic)<br>500 a 20,000 (triangles)<br>500 a 10,000 (quads) |
| `quad` | Saída de malha quad. A Tripo entrega malhas quad como FBX, então o resultado chega na saída FBX e a saída GLB permanece vazia. (padrão: False) | BOOLEAN | Sim | True<br>False (default) |
| `bake` | Aplica (bake) as texturas de origem na malha low-poly. (padrão: True) | BOOLEAN | Não | True (default)<br>False |
| `part_names` | Nomes de partes separados por vírgula do Tripo: Segment Model. Vazio processa o modelo inteiro. (padrão: "") | STRING | Não | Model part names or empty |

Nota: Quando `face_limit` é definido como -1, a Tripo decide a contagem de faces automaticamente. Quando `quad` está habilitado, o limite máximo de faces é 10.000 quads em vez de 20.000 triângulos, e o resultado é fornecido como FBX (a saída GLB permanece vazia). Quando `part_names` está vazio, o modelo inteiro é processado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | Saída compatível com versões anteriores que identifica o arquivo do modelo concluído. Fluxos de trabalho mais recentes devem usar as saídas GLB ou FBX. | STRING |
| `task_id do modelo` | ID da tarefa do resultado de retopologia concluído. Pode ser passado para outros nós Tripo para referenciar este modelo. | STRING |
| `GLB` | Modelo low-poly retopologizado no formato GLB. Vazio quando `quad` está habilitado. | GLB FILE |
| `FBX` | Modelo low-poly retopologizado no formato FBX. Só é preenchido quando `quad` está habilitado. | FBX FILE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetopologyNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dc15f469b160a1d738e8089cf18de4a8262721bc77ebafa45bf194f04c7726b6`
