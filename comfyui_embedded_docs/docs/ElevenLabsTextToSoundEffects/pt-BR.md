# ElevenLabs Texto para Efeitos Sonoros

O nó ElevenLabs Text to Sound Effects gera efeitos sonoros a partir de uma descrição em texto. Ele usa a API ElevenLabs para criar efeitos sonoros com base no seu prompt, permitindo controlar a duração, o comportamento de loop e o quão fielmente o som segue o texto.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a ser usado para a geração de efeitos sonoros. Dois modelos estão disponíveis: `eleven_sfx_v3` (padrão) e `eleven_sfx_v2`. | DYNAMIC_COMBO | Sim | `"eleven_sfx_v3"`<br>`"eleven_sfx_v2"` |
| `texto` | Descrição em texto do efeito sonoro a ser gerado. Escreva em inglês, com no máximo 450 caracteres; prompts em outros idiomas costumam ser falados em voz alta em vez de virarem som. (padrão: vazio) | STRING | Sim | 1 a 450 caracteres |
| `formato_saida` | Formato de saída de áudio. | COMBO | Sim | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas do eleven_sfx_v3 e eleven_sfx_v2

Estes parâmetros são exibidos quando qualquer um dos dois modelos é selecionado; ambos usam as mesmas configurações.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duração do som gerado em segundos. (padrão: 5.0) | FLOAT | Sim | 0.5 a 30.0 |
| `loop` | Cria um efeito sonoro em loop suave. (padrão: False) | BOOLEAN | Não | True<br>False |
| `prompt_influence` | O quão fielmente a geração segue o prompt. Valores mais altos fazem o som seguir o texto mais de perto. (padrão: 0.3) | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** O parâmetro `text` deve conter de 1 a 450 caracteres; ele é validado antes do envio da solicitação de geração de som.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | O arquivo de áudio do efeito sonoro gerado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bf7735aed642b2d795a18f7ca2631cab6856a2e0980f4c9e7a8699f08784177c`
