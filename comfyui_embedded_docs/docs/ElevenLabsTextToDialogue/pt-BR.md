# ElevenLabs Texto para Diálogo

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/en.md)

O nó ElevenLabs Text to Dialogue gera um diálogo de áudio com múltiplos falantes a partir de texto. Ele permite criar uma conversa especificando diferentes linhas de texto e vozes distintas para cada participante. O nó envia a solicitação de diálogo para a API do ElevenLabs e retorna o áudio gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `estabilidade` | Estabilidade da voz. Valores mais baixos proporcionam uma gama emocional mais ampla, valores mais altos produzem uma fala mais consistente, mas potencialmente monótona. (padrão: 0.5) | FLOAT | Não | 0.0 - 1.0 |
| `aplicar_normalização_texto` | Modo de normalização de texto. 'auto' permite que o sistema decida, 'on' sempre aplica a normalização, 'off' a ignora. | COMBO | Não | `"auto"`<br>`"on"`<br>`"off"` |
| `modelo` | Modelo a ser usado para geração de diálogo. | COMBO | Não | `"eleven_v3"` |
| `entradas` | Número de entradas de diálogo. Selecionar um número gerará essa quantidade de campos de entrada de texto e voz. | DYNAMICCOMBO | Sim | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `código_idioma` | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática. (padrão: vazio) | STRING | Não | - |
| `semente` | Semente para reprodutibilidade. (padrão: 1) | INT | Não | 0 - 4294967295 |
| `formato_saida` | Formato de saída de áudio. | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Nota:** O parâmetro `inputs` é dinâmico. Ao selecionar um número (ex.: "3"), o nó exibirá três campos de entrada `text` e `voice` correspondentes (ex.: `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Cada campo `text` deve conter pelo menos um caractere.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `audio` | O áudio do diálogo com múltiplos falantes gerado no formato de saída selecionado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2e1634e90314167320d715346f8d0c691dfabe82b090391afa2b0b18a8a126d8`
