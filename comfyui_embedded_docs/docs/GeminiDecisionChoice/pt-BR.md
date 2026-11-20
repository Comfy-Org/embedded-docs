# Google Gemini Decision (Choice)

Escolha uma das suas próprias opções para o texto, imagens, áudio ou vídeo que você conectar e receba de volta a opção escolhida, sua posição e uma confiança. Conecte `choice` a um nó Branch cujas entradas tenham os mesmos nomes de opção, ou roteie por `option_index` quando um nó Branch não estiver disponível.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a usar (padrão: `"gemini-decision-1"`). | COMBO | Sim | `"gemini-decision-1"` |
| `question` | A pergunta que as opções respondem, com até 5000 caracteres (padrão: "What style is the image?"). | STRING | Sim | 1 a 5000 caracteres |
| `options` | Uma opção por linha, usada exatamente como digitada, com até 128 caracteres cada. Adicione uma opção como `other` para entradas que não se encaixam em nenhuma delas (padrão: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Sim | 2 a 255 opções |
| `images` | Imagens a classificar, até 16 nos slots expansíveis (`image_1` ... `image_16`). Uma imagem em lote é contada uma vez por imagem. | IMAGE | Não | Até 16 imagens |
| `audio` | Clipe de áudio a classificar. | AUDIO | Não | - |
| `video` | Clipe de vídeo a classificar. | VIDEO | Não | - |
| `text` | Texto sobre o qual a pergunta trata, como um prompt ou uma resposta de LLM, com até 20000 caracteres. | STRING | Não | Até 20000 caracteres |

Forneça pelo menos 2 e no máximo 255 opções, e não liste nenhuma delas duas vezes; caso contrário, o nó gera um erro. Conecte pelo menos um entre `text`, `images`, `audio` ou `video`, e nomeie várias imagens como `image_1`, `image_2` e assim por diante dentro da pergunta.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `choice` | A opção escolhida, exatamente como foi escrita em `options`. | STRING |
| `option_index` | Posição da opção escolhida em `options`, começando em 0. | INT |
| `confidence` | Confiança na escolha, entre 0 e 1. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
