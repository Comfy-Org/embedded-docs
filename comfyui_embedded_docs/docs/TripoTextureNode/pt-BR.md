> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/pt-BR.md)

O TripoTextureNode gera modelos 3D texturizados usando a API Tripo. Ele recebe um ID de tarefa de modelo e aplica a geração de textura com várias opções, incluindo materiais PBR, configurações de qualidade de textura e métodos de alinhamento. O nó se comunica com a API Tripo para processar a solicitação de geração de textura e retorna o arquivo de modelo resultante e o ID da tarefa.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Sim | - | O ID da tarefa do modelo ao qual aplicar as texturas |
| `texture` | BOOLEAN | Não | - | Se deve gerar texturas (padrão: Verdadeiro) |
| `pbr` | BOOLEAN | Não | - | Se deve gerar materiais PBR (Renderização Baseada em Física) (padrão: Verdadeiro) |
| `texture_seed` | INT | Não | - | Semente aleatória para a geração de textura (padrão: 42) |
| `texture_quality` | COMBO | Não | "standard"<br>"detailed" | Nível de qualidade para a geração de textura (padrão: "standard") |
| `texture_alignment` | COMBO | Não | "original_image"<br>"geometry" | Método para alinhar as texturas (padrão: "original_image") |

*Nota: Este nó requer tokens de autenticação e chaves de API que são gerenciados automaticamente pelo sistema.*

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | O arquivo de modelo gerado com as texturas aplicadas |
| `model task_id` | MODEL_TASK_ID | O ID da tarefa para rastrear o processo de geração de textura |
