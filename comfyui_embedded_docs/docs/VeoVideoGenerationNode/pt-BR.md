Gera vídeos a partir de prompts de texto usando a API Google Veo 2. Este nó pode criar vídeos a partir de descrições textuais e entradas de imagem opcionais, com controle sobre parâmetros como proporção de aspecto, duração e outros.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual do vídeo (padrão: vazio) | STRING | Sim | - |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída (padrão: "16:9") | COMBO | Sim | "16:9"<br>"9:16" |
| `negative_prompt` | Prompt textual negativo para orientar o que evitar no vídeo (padrão: vazio) | STRING | Não | - |
| `duration_seconds` | Duração do vídeo de saída em segundos (padrão: 5) | INT | Não | 5-8 |
| `enhance_prompt` | Se deve aprimorar o prompt com assistência de IA (padrão: Verdadeiro). Este é um parâmetro avançado. | BOOLEAN | Não | - |
| `person_generation` | Se deve permitir a geração de pessoas no vídeo (padrão: "ALLOW"). Este é um parâmetro avançado. | COMBO | Não | "ALLOW"<br>"BLOCK" |
| `seed` | Semente para geração do vídeo (0 para aleatório) (padrão: 0). Este é um parâmetro avançado. | INT | Não | 0-4294967295 |
| `image` | Imagem de referência opcional para orientar a geração do vídeo | IMAGE | Não | - |
| `model` | Modelo Veo 2 a ser usado para geração de vídeo (padrão: "veo-2.0-generate-001") | COMBO | Não | "veo-2.0-generate-001" |

**Nota:** O parâmetro `generate_audio` está disponível apenas para modelos Veo 3.0 e é tratado automaticamente pelo nó com base no modelo selecionado. Ao usar modelos Veo 3.0, o parâmetro `enhance_prompt` é forçado para Verdadeiro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
