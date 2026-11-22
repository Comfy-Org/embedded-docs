# HeyGen Decision (Choice)

Escolha uma das suas próprias opções para o texto, imagens, áudio ou vídeo que você conectar e receba de volta a opção escolhida, sua posição e uma confiança. Conecte `choice` a um nó Branch cujas entradas carregam os mesmos nomes de opção, ou faça o roteamento com base em `option_index`. Um nó Branch aceita no máximo 32 entradas, então faça o roteamento de conjuntos maiores de opções com `option_index`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado. `heygen-decision-1-turbo` é mais rápido e custa menos que `heygen-decision-1` (padrão: `"heygen-decision-1"`). | COMBO | Sim | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | A pergunta que as opções respondem, com até 5000 caracteres (padrão: "What style is the image?"). | STRING | Sim | 1 a 5000 caracteres |
| `options` | Uma opção por linha, usada exatamente como digitada, com até 128 caracteres cada. Adicione uma opção como `other` para entradas que não se encaixem em nenhuma delas (padrão: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Sim | 2 a 255 opções |
| `images` | Imagens a classificar, até 4 no total, contando cada quadro de um lote. Elas são numeradas de `image_1` a `image_4` em ordem entre os soquetes. | IMAGE | Não | Até 4 imagens |
| `audio_1` | Áudio a classificar, até 30 minutos. | AUDIO | Não | Até 30 minutos |
| `video_1` | Vídeo a classificar, até 60 segundos. | VIDEO | Não | Até 60 segundos |
| `text` | Texto sobre o qual a pergunta se refere, como um prompt ou uma resposta de LLM, com até 20000 caracteres. | STRING | Não | Até 20000 caracteres |

Forneça de 2 a 255 opções, nenhuma delas repetida e nenhuma diferindo apenas por maiúsculas/minúsculas, ou o nó gera um erro. Conecte pelo menos uma entrada para classificar e nomeie-as pelo soquete dentro da pergunta, por exemplo "Qual estação é mostrada em image_1?".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `choice` | A opção escolhida, exatamente como foi escrita em `options`. | STRING |
| `option_index` | Posição da opção escolhida em `options`, começando em 0. | INT |
| `confidence` | Confiança na escolha, entre 0 e 1. | FLOAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
