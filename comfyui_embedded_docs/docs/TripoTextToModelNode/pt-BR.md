> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/pt-BR.md)

Gera modelos 3D de forma síncrona com base em um prompt de texto usando a API da Tripo. Este nó recebe uma descrição textual e cria um modelo 3D com propriedades opcionais de textura e material.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Descrição textual para gerar o modelo 3D (entrada multilinha) |
| `prompt_negativo` | STRING | Não | - | Descrição textual do que evitar no modelo gerado (entrada multilinha) |
| `versão_do_modelo` | COMBO | Não | Múltiplas opções disponíveis | Versão do modelo Tripo a ser usada para geração (padrão: v2.5-20250123) |
| `estilo` | COMBO | Não | Múltiplas opções disponíveis | Configuração de estilo para o modelo gerado (padrão: "Nenhum") |
| `textura` | BOOLEAN | Não | - | Se deve gerar texturas para o modelo (padrão: Verdadeiro) |
| `pbr` | BOOLEAN | Não | - | Se deve gerar materiais PBR (Renderização Baseada em Física) (padrão: Verdadeiro) |
| `semente_da_imagem` | INT | Não | - | Semente aleatória para geração de imagem (padrão: 42) |
| `semente_do_modelo` | INT | Não | - | Semente aleatória para geração do modelo (padrão: 42) |
| `semente_da_textura` | INT | Não | - | Semente aleatória para geração de textura (padrão: 42) |
| `qualidade_da_textura` | COMBO | Não | "padrão"<br>"detalhado" | Nível de qualidade para geração de textura (padrão: "padrão") |
| `limite_de_faces` | INT | Não | -1 a 2000000 | Número máximo de faces no modelo gerado, -1 para sem limite (padrão: -1) |
| `quad` | BOOLEAN | Não | - | Se deve gerar geometria baseada em quads em vez de triângulos (padrão: Falso) |
| `qualidade_da_geometria` | COMBO | Não | "padrão"<br>"detalhado" | Nível de qualidade para geração de geometria (padrão: "padrão") |

**Nota:** O parâmetro `prompt` é obrigatório e não pode estar vazio. Se nenhum prompt for fornecido, o nó gerará um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | O arquivo do modelo 3D gerado (apenas para compatibilidade reversa) |
| `model task_id` | MODEL_TASK_ID | O identificador único da tarefa para o processo de geração do modelo |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB |

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
