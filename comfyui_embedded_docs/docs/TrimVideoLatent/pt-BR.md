> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/pt-BR.md)

O nó TrimVideoLatent remove quadros do início de uma representação latente de vídeo. Ele recebe uma amostra latente de vídeo e corta um número especificado de quadros do início, retornando a porção restante do vídeo. Isso permite encurtar sequências de vídeo removendo os quadros iniciais.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | A representação latente de vídeo de entrada contendo os quadros a serem cortados |
| `trim_amount` | INT | Não | 0 a 99999 | O número de quadros a serem removidos do início do vídeo (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | A representação latente de vídeo cortada, com o número especificado de quadros removidos do início |
