> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/en.md)

## Visão Geral

Este nó gera um modelo 3D a partir de uma descrição textual usando a API Tripo P1. Ele é otimizado para criar malhas low-poly prontas para jogos, com topologia estável, sendo adequado para aplicações em tempo real.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | Até 1024 caracteres | A descrição textual do modelo 3D que você deseja gerar. |
| `negative_prompt` | STRING | Não | Até 255 caracteres | Uma descrição textual do que você não deseja no modelo gerado. |
| `output_mode` | DICT | Sim | Ver descrição | Controla as configurações de qualidade e textura do modelo de saída. Este parâmetro é um dicionário com as seguintes chaves:<br><br>`texture_quality`: STRING, Faixa: `"standard"`<br>`pbr`: BOOLEAN, padrão: True<br>`texture`: BOOLEAN, padrão: True<br>`subdivision`: INT, padrão: 0, Faixa: 0 a 2<br>`texture_size`: INT, padrão: 2048, Faixa: 512 a 4096 (deve ser uma potência de 2)<br>`texture_format`: STRING, Faixa: `"png"`<br>`texture_clean`: BOOLEAN, padrão: False<br>`texture_seamless`: BOOLEAN, padrão: False<br><br>Padrão: `{"texture_quality": "standard", "pbr": True, "texture": True, "subdivision": 0, "texture_size": 2048, "texture_format": "png", "texture_clean": False, "texture_seamless": False}` |
| `image_seed` | INT | Não |  | Um valor de semente para a geração de imagem, usado para controlar a aleatoriedade. Padrão: 42. |
| `face_limit` | INT | Não |  | O número máximo de faces para a malha gerada. Um valor de -1 significa sem limite. Padrão: -1. |
| `model_seed` | INT | Não |  | Um valor de semente para a geração do modelo, usado para controlar a aleatoriedade. |
| `auto_size` | BOOLEAN | Não |  | Se ativado, o nó determinará automaticamente o tamanho ideal do modelo. Padrão: False. |
| `export_uv` | BOOLEAN | Não |  | Se ativado, o modelo incluirá coordenadas UV para mapeamento de textura. Padrão: True. |
| `compress_geometry` | BOOLEAN | Não |  | Se ativado, a geometria será comprimida para reduzir o tamanho do arquivo. Padrão: False. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | STRING | O caminho do arquivo para o modelo 3D gerado (apenas para compatibilidade reversa). |
| `model task_id` | MODEL_TASK_ID | O ID de tarefa único para a solicitação de geração do modelo. |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB. |

---
**Source fingerprint (SHA-256):** `154e75209d65c823d5681b74cd12fe7b2ed37d7b94bf51cac86f343c68f85722`
