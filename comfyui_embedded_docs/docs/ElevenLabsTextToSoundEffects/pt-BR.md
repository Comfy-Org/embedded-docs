# ElevenLabs Texto para Efeitos Sonoros

O nó ElevenLabs Text to Sound Effects gera áudio de efeitos sonoros a partir de uma descrição em texto usando a API ElevenLabs. Ele envia seu prompt escrito para o serviço de geração de sons da ElevenLabs e retorna o áudio resultante, com controles de duração, comportamento de loop e o quão fielmente o som segue o texto.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a ser usado para geração de efeitos sonoros. O modelo selecionado determina os parâmetros de geração disponíveis listados abaixo. | DYNAMIC_COMBO | Sim | `"eleven_sfx_v2"` |
| `texto` | Descrição em texto do efeito sonoro a ser gerado. Deve conter pelo menos 1 caractere. (padrão: vazio) | STRING | Sim | N/A |
| `formato_saida` | Formato de saída do áudio. | COMBO | Sim | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entradas do Eleven SFX v2

Subparâmetros exibidos quando `model` está definido como `"eleven_sfx_v2"`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `duration` | Duração do som gerado em segundos. (padrão: 5.0) | FLOAT | Sim | 0.5 a 30.0 (passo: 0.1) |
| `loop` | Cria um efeito sonoro com loop suave. (padrão: Falso) | BOOLEAN | Não | True ou False |
| `prompt_influence` | O quão fielmente a geração segue o prompt. Valores mais altos fazem o som seguir o texto mais de perto. (padrão: 0.3) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `audio` | O arquivo de áudio do efeito sonoro gerado. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/pt-BR.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
