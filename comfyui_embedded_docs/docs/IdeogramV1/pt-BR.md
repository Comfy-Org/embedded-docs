> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/pt-BR.md)

O nó IdeogramV1 gera imagens usando o modelo Ideogram V1 por meio de uma API. Ele recebe *prompts* de texto e várias configurações de geração para criar uma ou mais imagens com base na sua entrada. O nó suporta diferentes proporções de aspecto e modos de geração para personalizar o resultado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | *Prompt* para a geração da imagem (padrão: vazio) |
| `turbo` | BOOLEAN | Sim | - | Se deve usar o modo turbo (geração mais rápida, potencialmente com qualidade inferior) (padrão: Falso) |
| `aspect_ratio` | COMBO | Não | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | A proporção de aspecto para a geração da imagem (padrão: "1:1") |
| `magic_prompt_option` | COMBO | Não | "AUTO"<br>"ON"<br>"OFF" | Determina se o MagicPrompt deve ser usado na geração (padrão: "AUTO") |
| `seed` | INT | Não | 0-2147483647 | Valor de semente aleatória para a geração (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Descrição do que excluir da imagem (padrão: vazio) |
| `num_images` | INT | Não | 1-8 | Número de imagens a serem geradas (padrão: 1) |

**Observação:** O parâmetro `num_images` tem um limite máximo de 8 imagens por solicitação de geração.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A(s) imagem(ns) gerada(s) pelo modelo Ideogram V1 |
