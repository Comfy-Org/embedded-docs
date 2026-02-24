> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/pt-BR.md)

O nó ElevenLabs Text to Sound Effects gera efeitos sonoros em áudio a partir de uma descrição em texto. Ele utiliza a API da ElevenLabs para criar efeitos sonoros com base no seu prompt, permitindo controlar a duração, o comportamento de loop e o quão fielmente o som segue o texto.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | Sim | N/A | Descrição em texto do efeito sonoro a ser gerado. Este é um campo obrigatório. |
| `model` | COMBO | Sim | `"eleven_sfx_v2"` | Modelo a ser usado para a geração do efeito sonoro. Selecionar este modelo revela parâmetros adicionais: `duration` (padrão: 5.0, intervalo: 0.5 a 30.0 segundos), `loop` (padrão: False) e `prompt_influence` (padrão: 0.3, intervalo: 0.0 a 1.0). |
| `output_format` | COMBO | Sim | `"mp3_44100_192"`<br>`"opus_48000_192"` | Formato de saída do áudio. |

**Detalhes dos Parâmetros:**
*   **`model["duration"]`**: Duração do som gerado em segundos. O padrão é 5.0, com um mínimo de 0.5 e um máximo de 30.0.
*   **`model["loop"]`**: Quando ativado, cria um efeito sonoro com loop suave. O padrão é False.
*   **`model["prompt_influence"]`**: Controla o quão fielmente a geração segue o prompt de texto. Valores mais altos fazem o som seguir o texto mais de perto. O padrão é 0.3, com um intervalo de 0.0 a 1.0.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O arquivo de áudio do efeito sonoro gerado. |