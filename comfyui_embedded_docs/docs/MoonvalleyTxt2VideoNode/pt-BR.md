> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/en.md)

O nó Moonvalley Marey Text to Video gera conteúdo de vídeo a partir de descrições textuais usando a API Moonvalley. Ele recebe um prompt de texto e o converte em um vídeo com configurações personalizáveis para resolução, qualidade e estilo. O nó gerencia todo o processo, desde o envio da requisição de geração até o download do arquivo de vídeo final.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Descrição textual do conteúdo de vídeo a ser gerado |
| `negative_prompt` | STRING | Não | - | Texto do prompt negativo (padrão: lista extensa de elementos excluídos como sintético, corte de cena, artefatos, ruído, etc.) |
| `resolution` | STRING | Não | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" | Resolução do vídeo de saída (padrão: "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | Não | 1.0-20.0 | Escala de orientação para controle de geração (padrão: 4.0) |
| `seed` | INT | Não | 0-4294967295 | Valor da semente aleatória (padrão: 9) |
| `steps` | INT | Não | 1-100 | Etapas de inferência (padrão: 33) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O vídeo gerado como saída com base no prompt de texto |

---
**Source fingerprint (SHA-256):** `3654043567d7aca3af741d706ee07a8d2e28dbeb4b5b8755514b790aa7c1bd41`
