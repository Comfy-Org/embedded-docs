> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/pt-BR.md)

Gera vídeos a partir de prompts de texto usando a API Veo 3 do Google. Este nó suporta dois modelos Veo 3: veo-3.0-generate-001 e veo-3.0-fast-generate-001. Ele estende o nó base Veo com recursos específicos do Veo 3, incluindo geração de áudio e uma duração fixa de 8 segundos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Range | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Descrição textual do vídeo (padrão: "") |
| `aspect_ratio` | COMBO | Sim | "16:9"<br>"9:16" | Proporção de aspecto do vídeo de saída (padrão: "16:9") |
| `negative_prompt` | STRING | Não | - | Prompt de texto negativo para orientar o que evitar no vídeo (padrão: "") |
| `duration_seconds` | INT | Não | 8-8 | Duração do vídeo de saída em segundos (o Veo 3 suporta apenas 8 segundos) (padrão: 8) |
| `enhance_prompt` | BOOLEAN | Não | - | Se deve aprimorar o prompt com assistência de IA (padrão: True) |
| `person_generation` | COMBO | Não | "ALLOW"<br>"BLOCK" | Se deve permitir a geração de pessoas no vídeo (padrão: "ALLOW") |
| `seed` | INT | Não | 0-4294967295 | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) |
| `image` | IMAGE | Não | - | Imagem de referência opcional para orientar a geração do vídeo |
| `model` | COMBO | Não | "veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | Modelo Veo 3 a ser usado para a geração do vídeo (padrão: "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | Não | - | Gerar áudio para o vídeo. Suportado por todos os modelos Veo 3. (padrão: False) |

**Observação:** O parâmetro `duration_seconds` é fixo em 8 segundos para todos os modelos Veo 3 e não pode ser alterado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |
