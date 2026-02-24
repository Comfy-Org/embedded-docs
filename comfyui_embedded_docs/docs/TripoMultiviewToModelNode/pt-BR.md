> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/pt-BR.md)

Este nó gera modelos 3D de forma síncrona usando a API da Tripo, processando até quatro imagens que mostram diferentes vistas de um objeto. Ele requer uma imagem frontal e pelo menos uma vista adicional (esquerda, traseira ou direita) para criar um modelo 3D completo com opções de textura e material.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | Imagem da vista frontal do objeto (obrigatória) |
| `image_left` | IMAGE | Não | - | Imagem da vista esquerda do objeto |
| `image_back` | IMAGE | Não | - | Imagem da vista traseira do objeto |
| `image_right` | IMAGE | Não | - | Imagem da vista direita do objeto |
| `model_version` | COMBO | Não | Múltiplas opções disponíveis | Versão do modelo Tripo a ser usada para a geração |
| `orientation` | COMBO | Não | Múltiplas opções disponíveis | Configuração de orientação para o modelo 3D |
| `texture` | BOOLEAN | Não | - | Se deve gerar texturas para o modelo (padrão: Verdadeiro) |
| `pbr` | BOOLEAN | Não | - | Se deve gerar materiais PBR (*Physically Based Rendering*) (padrão: Verdadeiro) |
| `model_seed` | INT | Não | - | Semente aleatória para geração do modelo (padrão: 42) |
| `texture_seed` | INT | Não | - | Semente aleatória para geração de textura (padrão: 42) |
| `texture_quality` | COMBO | Não | "standard"<br>"detailed" | Nível de qualidade para geração de textura (padrão: "standard") |
| `texture_alignment` | COMBO | Não | "original_image"<br>"geometry" | Método para alinhar texturas ao modelo (padrão: "original_image") |
| `face_limit` | INT | Não | -1 a 500000 | Número máximo de faces no modelo gerado, -1 para sem limite (padrão: -1) |
| `quad` | BOOLEAN | Não | - | Se deve gerar geometria baseada em quadriláteros em vez de triângulos (padrão: Falso) |

**Observação:** A imagem frontal (`image`) é sempre obrigatória. Pelo menos uma imagem de vista adicional (`image_left`, `image_back` ou `image_right`) deve ser fornecida para o processamento multivista.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model_file` | STRING | Caminho do arquivo ou identificador para o modelo 3D gerado |
| `model task_id` | MODEL_TASK_ID | Identificador da tarefa para rastrear o processo de geração do modelo |
