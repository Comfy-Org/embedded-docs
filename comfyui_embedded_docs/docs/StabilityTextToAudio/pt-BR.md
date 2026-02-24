> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/pt-BR.md)

Gera música e efeitos sonoros de alta qualidade a partir de descrições textuais. Este nó utiliza a tecnologia de geração de áudio da Stability AI para criar conteúdo de áudio com base em seus prompts de texto.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `"stable-audio-2.5"` | O modelo de geração de áudio a ser utilizado (padrão: "stable-audio-2.5") |
| `prompt` | STRING | Sim | - | A descrição textual usada para gerar o conteúdo de áudio (padrão: string vazia) |
| `duration` | INT | Não | 1-190 | Controla a duração, em segundos, do áudio gerado (padrão: 190) |
| `seed` | INT | Não | 0-4294967294 | A semente aleatória usada para a geração (padrão: 0) |
| `steps` | INT | Não | 4-8 | Controla o número de etapas de amostragem (padrão: 8) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O arquivo de áudio gerado com base no prompt de texto |
