# Tripo: Multiview para Modelo

Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/en.md)

Este nó gera modelos 3D de forma síncrona usando a API da Tripo, processando até quatro imagens que mostram diferentes vistas de um objeto. É necessário fornecer uma imagem frontal e pelo menos uma vista adicional (esquerda, traseira ou direita) para criar um modelo 3D completo com opções de textura e material.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | Imagem da vista frontal do objeto (obrigatória) | IMAGE | Sim | - |
| `imagem_esquerda` | Imagem da vista esquerda do objeto | IMAGE | Não | - |
| `imagem_traseira` | Imagem da vista traseira do objeto | IMAGE | Não | - |
| `imagem_direita` | Imagem da vista direita do objeto | IMAGE | Não | - |
| `versão_do_modelo` | Versão do modelo a ser usada na geração | COMBO | Não | Múltiplas opções disponíveis |
| `orientação` | Configuração de orientação para o modelo 3D (padrão: "default") | COMBO | Não | Múltiplas opções disponíveis |
| `textura` | Se deve gerar texturas para o modelo (padrão: True) | BOOLEAN | Não | - |
| `pbr` | Se deve gerar materiais PBR (Renderização Baseada em Física) (padrão: True) | BOOLEAN | Não | - |
| `semente_do_modelo` | Semente aleatória para geração do modelo (padrão: 42) | INT | Não | - |
| `semente_da_textura` | Semente aleatória para geração de textura (padrão: 42) | INT | Não | - |
| `qualidade_da_textura` | Nível de qualidade para geração de textura (padrão: "standard") | COMBO | Não | `"standard"`<br>`"detailed"` |
| `alinhamento_da_textura` | Método para alinhar texturas ao modelo (padrão: "original_image") | COMBO | Não | `"original_image"`<br>`"geometry"` |
| `limite_de_faces` | Número máximo de faces no modelo gerado. Defina como -1 para sem limite (padrão: -1) | INT | Não | -1 a 500000 |
| `quad` | Este parâmetro está obsoleto e não tem efeito (padrão: False) | BOOLEAN | Não | - |
| `qualidade_da_geometria` | Nível de qualidade para geração da geometria (padrão: "standard") | COMBO | Não | `"standard"`<br>`"detailed"` |

**Observação:** A imagem frontal (`image`) é sempre obrigatória. Pelo menos uma imagem de vista adicional (`image_left`, `image_back` ou `image_right`) deve ser fornecida para o processamento multivista.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | Caminho do arquivo ou identificador do modelo 3D gerado (apenas para compatibilidade reversa) | STRING |
| `model task_id` | Identificador da tarefa para rastrear o processo de geração do modelo | MODEL_TASK_ID |
| `GLB` | Arquivo do modelo 3D gerado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
