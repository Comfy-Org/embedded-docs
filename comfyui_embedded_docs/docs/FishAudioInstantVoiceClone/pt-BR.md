# FishAudioInstantVoiceClone

Este nó cria uma voz clonada privada a partir das suas gravações de áudio usando a API Fish Audio. Você fornece uma ou mais amostras de áudio, e o nó constrói uma voz personalizada que pode ser usada imediatamente para conversão de texto em fala. Ele aceita de 1 a 20 gravações, com duração recomendada de 10 a 30 segundos cada e um limite total de 270 segundos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `files` | Gravações de áudio para clonagem de voz. Esta é uma entrada expansível: conecte um ou mais itens de áudio (por exemplo `audio_1`, `audio_2`, ...) para fornecer as amostras de voz. | AUDIO | Sim | 1 a 20 gravações |
| `enhance_audio_quality` | Melhora a qualidade do áudio de referência antes do treinamento (padrão: True). | BOOLEAN | Sim | True<br>False |

**Observação:** A duração total de todo o áudio de referência combinado deve ser inferior a 270 segundos. Se a duração combinada atingir ou exceder 270 segundos, o nó retorna um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `voice` | A voz clonada recém-criada, identificada por um ID de voz exclusivo retornado pela API Fish Audio. Essa voz pode ser usada para conversão de texto em fala. | FISHAUDIO_VOICE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`
