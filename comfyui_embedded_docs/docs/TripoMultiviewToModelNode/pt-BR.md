> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/en.md)

Este nó gera modelos 3D de forma síncrona usando a API da Tripo, processando até quatro imagens que mostram diferentes vistas de um objeto. É necessário fornecer uma imagem frontal e pelo menos uma vista adicional (esquerda, traseira ou direita) para criar um modelo 3D completo com opções de textura e material.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `image` | IMAGE | Sim | - | Imagem da vista frontal do objeto (obrigatória) |
| `image_left` | IMAGE | Não | - | Imagem da vista esquerda do objeto |
| `image_back` | IMAGE | Não | - | Imagem da vista traseira do objeto |
| `image_right` | IMAGE | Não | - | Imagem da vista direita do objeto |
| `model_version` | COMBO | Não | Múltiplas opções disponíveis | Versão do modelo a ser usada na geração |
| `orientation` | COMBO | Não | Múltiplas opções disponíveis | Configuração de orientação para o modelo 3D (padrão: "default") |
| `texture` | BOOLEAN | Não | - | Se deve gerar texturas para o modelo (padrão: True) |
| `pbr` | BOOLEAN | Não | - | Se deve gerar materiais PBR (Renderização Baseada em Física) (padrão: True) |
| `model_seed` | INT | Não | - | Semente aleatória para geração do modelo (padrão: 42) |
| `texture_seed` | INT | Não | - | Semente aleatória para geração de textura (padrão: 42) |
| `texture_quality` | COMBO | Não | `"standard"`<br>`"detailed"` | Nível de qualidade para geração de textura (padrão: "standard") |
| `texture_alignment` | COMBO | Não | `"original_image"`<br>`"geometry"` | Método para alinhar texturas ao modelo (padrão: "original_image") |
| `face_limit` | INT | Não | -1 a 500000 | Número máximo de faces no modelo gerado. Defina como -1 para sem limite (padrão: -1) |
| `quad` | BOOLEAN | Não | - | Este parâmetro está obsoleto e não tem efeito (padrão: False) |
| `geometry_quality` | COMBO | Não | `"standard"`<br>`"detailed"` | Nível de qualidade para geração da geometria (padrão: "standard") |

**Observação:** A imagem frontal (`image`) é sempre obrigatória. Pelo menos uma imagem de vista adicional (`image_left`, `image_back` ou `image_right`) deve ser fornecida para o processamento multivista.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | Caminho do arquivo ou identificador do modelo 3D gerado (apenas para compatibilidade reversa) |
| `model task_id` | MODEL_TASK_ID | Identificador da tarefa para rastrear o processo de geração do modelo |
| `GLB` | FILE3DGLB | Arquivo do modelo 3D gerado no formato GLB |

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
