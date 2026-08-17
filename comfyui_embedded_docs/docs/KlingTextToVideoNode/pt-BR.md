# Kling Texto para Vídeo

O nó Kling Text to Video converte prompts de texto em videoclipes curtos usando o serviço de geração de vídeo Kling. Você fornece prompts positivos e negativos, juntamente com configurações como proporção de aspecto, escala de configuração e modo de geração, e o nó retorna o vídeo gerado com seu identificador e duração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto positivo que descreve o conteúdo de vídeo desejado. Entrada multilinha. Não pode estar vazio. | STRING | Sim | Máximo de 2500 caracteres |
| `negative_prompt` | Prompt de texto negativo que descreve o que evitar no vídeo. Entrada multilinha. Pode ser deixado vazio. | STRING | Sim | Máximo de 2500 caracteres |
| `cfg_scale` | Valor da escala de configuração que controla o quão fielmente o vídeo segue o prompt (padrão: 1.0). | FLOAT | Não | 0.0 a 1.0 |
| `aspect_ratio` | Configuração de proporção de aspecto do vídeo (padrão: "16:9"). | COMBO | Não | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | A configuração a ser usada para a geração de vídeo seguindo o formato: modo / duração / nome_do_modelo (padrão: "pro mode / 5s duration / kling-v2-5-turbo"). O modo de 5s custa USD 0,35, o modo de 10s custa USD 0,70. | COMBO | Não | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A saída de vídeo gerada. | VIDEO |
| `video_id` | Identificador único para o vídeo gerado. | STRING |
| `duration` | Informação de duração para o vídeo gerado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
