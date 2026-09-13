# Tripo P1: Texto para Modelo

Tripo P1 de texto para 3D. Este nó gera um modelo 3D a partir de uma descrição textual usando a API do Tripo P1. Ele é otimizado para criar malhas low-poly prontas para jogos, com topologia estável, o que o torna adequado para aplicações em tempo real.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `output_mode` | Controla se o modelo gerado contém apenas geometria ou também texturas de cor/PBR. "Geometry only" retorna uma malha sem textura. "Textured" adiciona mapas de cor/PBR e revela as opções de textura abaixo. | DYNAMIC_COMBO | Sim | `"Geometry only"`<br>`"Textured"` |
| `prompt` | A descrição textual do modelo 3D que você deseja gerar. Até 1024 caracteres. Obrigatório e não pode ficar vazio. | STRING | Sim | Até 1024 caracteres |
| `negative_prompt` | Uma descrição textual do que você não deseja no modelo gerado. Até 255 caracteres. Padrão: não definido. | STRING | Não | Até 255 caracteres |
| `image_seed` | Um valor de semente usado para controlar a aleatoriedade. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `face_limit` | Contagem alvo de faces, 48-20000. -1 permite que o Tripo escolha de forma adaptativa. Padrão: -1. | INT | Não | -1 a 20000 |
| `model_seed` | Um valor de semente usado para controlar a aleatoriedade. Padrão: 42. | INT | Não | 0 a 2147483647 |
| `auto_size` | Escala a saída para aproximar metros do mundo real. Padrão: False. | BOOLEAN | Não | True / False |
| `export_uv` | Desdobramento de UV durante a geração. Desative para execuções mais rápidas de apenas geometria. Padrão: True. | BOOLEAN | Não | True / False |
| `compress_geometry` | Aplica compressão de geometria meshopt (EXT_meshopt_compression). Arquivos menores, mas a visualização 3D do ComfyUI não consegue exibi-los; descompacte antes de editar. Padrão: False. | BOOLEAN | Não | True / False |

### Entradas de apenas geometria

Nenhuma entrada extra está disponível quando `output_mode` está definido como `"Geometry only"`. Parâmetros relacionados a textura não são enviados ao Tripo neste modo.

### Entradas com textura

Estas entradas aparecem apenas quando `output_mode` está definido como `"Textured"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Inclui mapas PBR. Quando ativado, a textura base também é forçada. Padrão: True. | BOOLEAN | Sim | True / False |
| `texture_quality` | Predefinição de qualidade de textura. detailed = texturas HD, extreme = texturas Ultra 8K. Padrão: "standard". | COMBO | Sim | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Um valor de semente para a geração de textura, usado para controlar a aleatoriedade. Padrão: 42. | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `model_file` | O nome do arquivo de modelo gerado, mantido apenas para compatibilidade retroativa. | STRING |
| `model task_id` | O ID exclusivo da tarefa para a solicitação de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
