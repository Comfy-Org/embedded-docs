> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/pt-BR.md)

O nó Moonvalley Marey Text to Video gera conteúdo de vídeo a partir de descrições de texto usando a API Moonvalley. Ele recebe um prompt de texto e o converte em um vídeo com configurações personalizáveis para resolução, qualidade e estilo. O nó gerencia todo o processo, desde o envio da solicitação de geração até o download do vídeo final.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Descrição textual do conteúdo do vídeo a ser gerado |
| `negative_prompt` | STRING | Não | - | Texto do prompt negativo (padrão: lista extensa de elementos excluídos, como sintético, corte de cena, artefatos, ruído, etc.) |
| `resolution` | STRING | Não | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" | Resolução do vídeo de saída (padrão: "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | Não | 1.0-20.0 | Escala de orientação para controle da geração (padrão: 4.0) |
| `seed` | INT | Não | 0-4294967295 | Valor da semente aleatória (padrão: 9) |
| `steps` | INT | Não | 1-100 | Passos de inferência (padrão: 33) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O vídeo gerado com base no prompt de texto |
