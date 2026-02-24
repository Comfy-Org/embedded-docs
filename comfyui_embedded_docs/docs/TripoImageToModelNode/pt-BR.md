> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/pt-BR.md)

Gera modelos 3D de forma síncrona com base em uma única imagem usando a API do Tripo. Este nó recebe uma imagem de entrada e a converte em um modelo 3D com várias opções de personalização para textura, qualidade e propriedades do modelo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Imagem de entrada usada para gerar o modelo 3D |
| `model_version` | COMBO | Não | Múltiplas opções disponíveis | A versão do modelo Tripo a ser usada para a geração |
| `style` | COMBO | Não | Múltiplas opções disponíveis | Configuração de estilo para o modelo gerado (padrão: "None") |
| `texture` | BOOLEAN | Não | - | Se deve gerar texturas para o modelo (padrão: True) |
| `pbr` | BOOLEAN | Não | - | Se deve usar Renderização Baseada em Física (padrão: True) |
| `model_seed` | INT | Não | - | Semente aleatória para a geração do modelo (padrão: 42) |
| `orientation` | COMBO | Não | Múltiplas opções disponíveis | Configuração de orientação para o modelo gerado |
| `texture_seed` | INT | Não | - | Semente aleatória para a geração de textura (padrão: 42) |
| `texture_quality` | COMBO | Não | "standard"<br>"detailed" | Nível de qualidade para a geração de textura (padrão: "standard") |
| `texture_alignment` | COMBO | Não | "original_image"<br>"geometry" | Método de alinhamento para o mapeamento de textura (padrão: "original_image") |
| `face_limit` | INT | Não | -1 a 500000 | Número máximo de faces no modelo gerado, -1 para sem limite (padrão: -1) |
| `quad` | BOOLEAN | Não | - | Se deve usar faces quadriláteras em vez de triângulos (padrão: False) |

**Observação:** O parâmetro `image` é obrigatório e deve ser fornecido para que o nó funcione. Se nenhuma imagem for fornecida, o nó levantará um RuntimeError.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | O arquivo do modelo 3D gerado |
| `model task_id` | MODEL_TASK_ID | O ID da tarefa para rastrear o processo de geração do modelo |
