Gera modelos 3D de forma síncrona com base em um prompt de texto usando a API da Tripo. Este nó recebe uma descrição textual e cria um modelo 3D com propriedades opcionais de textura e material.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual para gerar o modelo 3D (entrada multilinha) | STRING | Sim | - |
| `prompt_negativo` | Descrição textual do que evitar no modelo gerado (entrada multilinha) | STRING | Não | - |
| `versão_do_modelo` | Versão do modelo Tripo a ser usada para geração (padrão: v2.5-20250123) | COMBO | Não | Múltiplas opções disponíveis |
| `estilo` | Configuração de estilo para o modelo gerado (padrão: "Nenhum") | COMBO | Não | Múltiplas opções disponíveis |
| `textura` | Se deve gerar texturas para o modelo (padrão: Verdadeiro) | BOOLEAN | Não | - |
| `pbr` | Se deve gerar materiais PBR (Renderização Baseada em Física) (padrão: Verdadeiro) | BOOLEAN | Não | - |
| `semente_da_imagem` | Semente aleatória para geração de imagem (padrão: 42) | INT | Não | - |
| `semente_do_modelo` | Semente aleatória para geração do modelo (padrão: 42) | INT | Não | - |
| `semente_da_textura` | Semente aleatória para geração de textura (padrão: 42) | INT | Não | - |
| `qualidade_da_textura` | Nível de qualidade para geração de textura (padrão: "padrão") | COMBO | Não | "padrão"<br>"detalhado" |
| `limite_de_faces` | Número máximo de faces no modelo gerado, -1 para sem limite (padrão: -1) | INT | Não | -1 a 2000000 |
| `quad` | Se deve gerar geometria baseada em quads em vez de triângulos (padrão: Falso) | BOOLEAN | Não | - |
| `qualidade_da_geometria` | Nível de qualidade para geração de geometria (padrão: "padrão") | COMBO | Não | "padrão"<br>"detalhado" |

**Nota:** O parâmetro `prompt` é obrigatório e não pode estar vazio. Se nenhum prompt for fornecido, o nó gerará um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O arquivo do modelo 3D gerado (apenas para compatibilidade reversa) | STRING |
| `model task_id` | O identificador único da tarefa para o processo de geração do modelo | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
