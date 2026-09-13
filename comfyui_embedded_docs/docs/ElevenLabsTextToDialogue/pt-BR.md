# ElevenLabs Texto para Diálogo

O nó ElevenLabs Text to Dialogue gera um diálogo de áudio com vários falantes a partir de texto. Ele permite criar uma conversa especificando diferentes linhas de texto e vozes distintas para cada participante. O nó envia a solicitação de diálogo para a API da ElevenLabs e retorna o áudio gerado.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `estabilidade` | Estabilidade da voz. Valores mais baixos proporcionam uma amplitude emocional mais ampla; valores mais altos produzem fala mais consistente, mas potencialmente monótona. (padrão: 0.5) | FLOAT | Sim | 0.0 - 1.0 |
| `aplicar_normalização_texto` | Modo de normalização de texto. 'auto' deixa o sistema decidir, 'on' sempre aplica a normalização, 'off' ignora essa etapa. | COMBO | Sim | `"auto"`<br>`"on"`<br>`"off"` |
| `modelo` | Modelo a ser usado para a geração de diálogo. | COMBO | Sim | `"eleven_v3"` |
| `entradas` | Número de itens de diálogo. Selecionar um número cria essa quantidade de pares de entrada de texto e voz. | DYNAMIC_COMBO | Sim | `"1"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |
| `código_idioma` | Código de idioma ISO-639-1 ou ISO-639-3 (ex.: 'en', 'es', 'fra'). Deixe vazio para detecção automática. (padrão: vazio) | STRING | Sim | - |
| `semente` | Semente para reprodutibilidade. (padrão: 1) | INT | Sim | 0 - 4294967295 |
| `formato_saida` | Formato de saída de áudio. | COMBO | Sim | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas de Itens de Diálogo

Compartilhado por todas as opções de `inputs`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `text1` ... `text10` | Conteúdo de texto para o item de diálogo correspondente. O nó cria um campo `text` para cada item de diálogo selecionado. Cada valor de texto deve conter pelo menos um caractere. | STRING | Sim | - |
| `voice1` ... `voice10` | Voz para o item de diálogo correspondente. Conecte a partir de um nó Voice Selector ou Instant Voice Clone. O nó cria um campo `voice` para cada item de diálogo selecionado. | ELEVENLABS_VOICE | Sim | - |

**Observação:** O seletor `inputs` pode criar até 10 itens de diálogo. Cada item exige tanto um campo `text` quanto um campo `voice`. O valor de `text` não pode ficar vazio. A entrada `voice` espera um ID de voz fornecido por um nó de voz ElevenLabs compatível.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | O áudio de diálogo com vários falantes gerado no formato de saída selecionado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToDialogue/pt-BR.md)

---
**Source fingerprint (SHA-256):** `95b16143391a2282c58ebc66561b85338a8ce1f87e0ec769405225599d2c76ae`
