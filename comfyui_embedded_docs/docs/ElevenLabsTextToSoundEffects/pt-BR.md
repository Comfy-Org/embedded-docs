# ElevenLabs Texto para Efeitos Sonoros

O nó ElevenLabs Text to Sound Effects gera efeitos sonoros a partir de uma descrição em texto. Ele usa a API ElevenLabs para criar efeitos sonoros com base no seu prompt, permitindo controlar a duração, o comportamento de loop e o quão fielmente o som segue o texto.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a ser usado para a geração de efeitos sonoros. Apenas um modelo está disponível atualmente: `eleven_sfx_v2`. | DYNAMIC_COMBO | Sim | `"eleven_sfx_v2"` |
| `texto` | Descrição em texto do efeito sonoro a ser gerado. (padrão: vazio) | STRING | Sim | N/A |
| `formato_saida` | Formato de saída de áudio. | COMBO | Sim | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas do eleven_sfx_v2

Estes parâmetros são exibidos quando o modelo `eleven_sfx_v2` é selecionado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duração do som gerado em segundos. (padrão: 5.0) | FLOAT | Sim | 0.5 a 30.0 |
| `loop` | Cria um efeito sonoro em loop suave. (padrão: False) | BOOLEAN | Não | True<br>False |
| `prompt_influence` | O quão fielmente a geração segue o prompt. Valores mais altos fazem o som seguir o texto mais de perto. (padrão: 0.3) | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** O parâmetro `text` não deve estar vazio; ele é validado antes do envio da solicitação de geração de som.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | O arquivo de áudio do efeito sonoro gerado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/pt-BR.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
