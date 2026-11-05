# Pika H3 Flex Video

Este nó gera um vídeo com áudio sincronizado a partir de um prompt de texto, opcionalmente ancorado por um primeiro quadro, um último quadro, ou ambos. O Pika H3 Flex é o modelo MiniMax H3 pós-treinado da Pika: ele renderiza a imagem e seu som em uma única passagem, e você define a resolução, a proporção e a duração. Sem nenhum quadro conectado, o nó executa texto para vídeo; conectar um quadro o alterna para imagem para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | O que acontece no vídeo, incluindo o som que você deseja. Não pode estar vazio. Padrão: "" (string vazia). | STRING | Sim | 1 a 8000 caracteres |
| `first_frame` | Imagem opcional usada como quadro de abertura. Conectá-la executa imagem para vídeo em vez de texto para vídeo. | IMAGE | Não | - |
| `last_frame` | Imagem opcional usada como quadro de encerramento. Pode ser usada junto com `first_frame` ou sozinha. | IMAGE | Não | - |
| `resolution` | Resolução de saída. `"1080p"` e acima renderizam em 768p e fazem upscale uma vez. A mesma seed em 480p gera um vídeo diferente. Padrão: `"768p"`. | COMBO | Sim | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Proporção de saída. `"auto"` segue o primeiro quadro conectado; caso contrário, o prompt. Padrão: `"auto"`. | COMBO | Sim | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Duração do clipe em segundos. O comprimento da saída segue uma grade de quadros: 5 segundos resultam em 124 quadros, cerca de 5,17 segundos. Padrão: 5. | INT | Sim | 5 a 15 segundos |
| `rewrite_prompt` | Permitir que a Pika expanda o prompt primeiro. A mesma seed então gera um vídeo diferente a cada execução. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `seed` | Seed para amostragem. Com `rewrite_prompt` desativado, a mesma seed repete o vídeo exatamente, embora uma execução local com a mesma seed dê um resultado diferente. Padrão: 42. | INT | Sim | 0 a 2147483647 |

**Restrições:**

* O prompt deve ter entre 1 e 8000 caracteres.
* A cobrança segue a resolução selecionada e a duração do clipe, contada por segundo de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O clipe gerado com seu áudio sincronizado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `63a90fc5874ed861db3c0821e702cfcd1a14650f09459b242b4ec5e3ba5b0cd5`
