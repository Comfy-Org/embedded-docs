> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/pt-BR.md)

Gera vídeos a partir de prompts de texto usando a API Veo do Google. Este nó pode criar vídeos a partir de descrições de texto e entradas de imagem opcionais, com controle sobre parâmetros como proporção de tela, duração e mais.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Descrição textual do vídeo (padrão: vazio) |
| `aspect_ratio` | COMBO | Sim | "16:9"<br>"9:16" | Proporção de tela do vídeo de saída (padrão: "16:9") |
| `negative_prompt` | STRING | Não | - | Prompt de texto negativo para orientar o que evitar no vídeo (padrão: vazio) |
| `duration_seconds` | INT | Não | 5-8 | Duração do vídeo de saída em segundos (padrão: 5) |
| `enhance_prompt` | BOOLEAN | Não | - | Se deve aprimorar o prompt com assistência de IA (padrão: True) |
| `person_generation` | COMBO | Não | "ALLOW"<br>"BLOCK" | Se deve permitir a geração de pessoas no vídeo (padrão: "ALLOW") |
| `seed` | INT | Não | 0-4294967295 | Semente para geração de vídeo (0 para aleatório) (padrão: 0) |
| `image` | IMAGE | Não | - | Imagem de referência opcional para orientar a geração do vídeo |
| `model` | COMBO | Não | "veo-2.0-generate-001" | Modelo Veo 2 a ser usado para geração de vídeo (padrão: "veo-2.0-generate-001") |

**Observação:** O parâmetro `generate_audio` está disponível apenas para modelos Veo 3.0 e é tratado automaticamente pelo nó com base no modelo selecionado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |
