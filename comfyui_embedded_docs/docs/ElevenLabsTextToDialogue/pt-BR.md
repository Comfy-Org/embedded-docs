> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/pt-BR.md)

O nó ElevenLabs Text to Dialogue gera um áudio de diálogo com múltiplos falantes a partir de texto. Ele permite que você crie uma conversa especificando diferentes linhas de texto e vozes distintas para cada participante. O nó envia a solicitação de diálogo para a API da ElevenLabs e retorna o áudio gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `stability` | FLOAT | Não | 0.0 - 1.0 | Estabilidade da voz. Valores mais baixos proporcionam uma gama emocional mais ampla, valores mais altos produzem uma fala mais consistente, mas potencialmente monótona. (padrão: 0.5) |
| `apply_text_normalization` | COMBO | Não | `"auto"`<br>`"on"`<br>`"off"` | Modo de normalização de texto. 'auto' deixa o sistema decidir, 'on' sempre aplica normalização, 'off' ignora. |
| `model` | COMBO | Não | `"eleven_v3"` | Modelo a ser usado para geração do diálogo. |
| `inputs` | DYNAMICCOMBO | Sim | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | Número de entradas de diálogo. Selecionar um número gerará essa quantidade de campos de entrada para texto e voz. |
| `language_code` | STRING | Não | - | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática. (padrão: vazio) |
| `seed` | INT | Não | 0 - 4294967295 | Semente para reprodutibilidade. (padrão: 1) |
| `output_format` | COMBO | Não | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de saída do áudio. |

**Observação:** O parâmetro `inputs` é dinâmico. Quando você seleciona um número (ex.: "3"), o nó exibirá três campos de entrada `text` e `voice` correspondentes (ex.: `text1`, `voice1`, `text2`, `voice2`, `text3`, `voice3`). Cada campo `text` deve conter pelo menos um caractere.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O áudio do diálogo com múltiplos falantes gerado, no formato de saída selecionado. |