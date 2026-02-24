> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/pt-BR.md)

Gera modelos 3D de forma síncrona com base em um prompt de texto usando a API do Tripo. Este nó recebe uma descrição textual e cria um modelo 3D com propriedades opcionais de textura e material.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Descrição textual para gerar o modelo 3D (entrada de múltiplas linhas) |
| `negative_prompt` | STRING | Não | - | Descrição textual do que evitar no modelo gerado (entrada de múltiplas linhas) |
| `model_version` | COMBO | Não | Múltiplas opções disponíveis | A versão do modelo Tripo a ser usada para a geração |
| `style` | COMBO | Não | Múltiplas opções disponíveis | Configuração de estilo para o modelo gerado (padrão: "None") |
| `texture` | BOOLEAN | Não | - | Se deve gerar texturas para o modelo (padrão: True) |
| `pbr` | BOOLEAN | Não | - | Se deve gerar materiais PBR (Physically Based Rendering) (padrão: True) |
| `image_seed` | INT | Não | - | Semente aleatória para geração de imagem (padrão: 42) |
| `model_seed` | INT | Não | - | Semente aleatória para geração do modelo (padrão: 42) |
| `texture_seed` | INT | Não | - | Semente aleatória para geração de textura (padrão: 42) |
| `texture_quality` | COMBO | Não | "standard"<br>"detailed" | Nível de qualidade para geração de textura (padrão: "standard") |
| `face_limit` | INT | Não | -1 a 500000 | Número máximo de faces no modelo gerado, -1 para sem limite (padrão: -1) |
| `quad` | BOOLEAN | Não | - | Se deve gerar geometria baseada em quadriláteros em vez de triângulos (padrão: False) |

**Observação:** O parâmetro `prompt` é obrigatório e não pode estar vazio. Se nenhum prompt for fornecido, o nó retornará um erro.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | O arquivo do modelo 3D gerado |
| `model task_id` | MODEL_TASK_ID | O identificador único da tarefa para o processo de geração do modelo |
