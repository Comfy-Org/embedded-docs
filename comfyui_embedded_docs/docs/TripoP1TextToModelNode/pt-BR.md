Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/en.md)

## Visão Geral

Este nó gera um modelo 3D a partir de uma descrição textual usando a API Tripo P1. Ele é otimizado para criar malhas low-poly prontas para jogos, com topologia estável, sendo adequado para aplicações em tempo real.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | A descrição textual do modelo 3D que você deseja gerar. | STRING | Sim | Até 1024 caracteres |
| `negative_prompt` | Uma descrição textual do que você não deseja no modelo gerado. | STRING | Não | Até 255 caracteres |
| `output_mode` | Controla as configurações de qualidade e textura do modelo de saída. Este parâmetro é um dicionário com as seguintes chaves:<br><br>`texture_quality`: STRING, Faixa: `"standard"`<br>`pbr`: BOOLEAN, padrão: True<br>`texture`: BOOLEAN, padrão: True<br>`subdivision`: INT, padrão: 0, Faixa: 0 a 2<br>`texture_size`: INT, padrão: 2048, Faixa: 512 a 4096 (deve ser uma potência de 2)<br>`texture_format`: STRING, Faixa: `"png"`<br>`texture_clean`: BOOLEAN, padrão: False<br>`texture_seamless`: BOOLEAN, padrão: False<br><br>Padrão: `{"texture_quality": "standard", "pbr": True, "texture": True, "subdivision": 0, "texture_size": 2048, "texture_format": "png", "texture_clean": False, "texture_seamless": False}` | DICT | Sim | Ver descrição |
| `image_seed` | Um valor de semente para a geração de imagem, usado para controlar a aleatoriedade. Padrão: 42. | INT | Não |  |
| `face_limit` | O número máximo de faces para a malha gerada. Um valor de -1 significa sem limite. Padrão: -1. | INT | Não |  |
| `model_seed` | Um valor de semente para a geração do modelo, usado para controlar a aleatoriedade. | INT | Não |  |
| `auto_size` | Se ativado, o nó determinará automaticamente o tamanho ideal do modelo. Padrão: False. | BOOLEAN | Não |  |
| `export_uv` | Se ativado, o modelo incluirá coordenadas UV para mapeamento de textura. Padrão: True. | BOOLEAN | Não |  |
| `compress_geometry` | Se ativado, a geometria será comprimida para reduzir o tamanho do arquivo. Padrão: False. | BOOLEAN | Não |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O caminho do arquivo para o modelo 3D gerado (apenas para compatibilidade reversa). | STRING |
| `model task_id` | O ID de tarefa único para a solicitação de geração do modelo. | MODEL_TASK_ID |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `154e75209d65c823d5681b74cd12fe7b2ed37d7b94bf51cac86f343c68f85722`
