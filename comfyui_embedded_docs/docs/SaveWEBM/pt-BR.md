> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/pt-BR.md)

O nó SaveWEBM salva uma sequência de imagens como um arquivo de vídeo WEBM. Ele recebe múltiplas imagens de entrada e as codifica em um vídeo usando os codecs VP9 ou AV1, com configurações de qualidade e taxa de quadros ajustáveis. O arquivo de vídeo resultante é salvo no diretório de saída com metadados que incluem informações do prompt.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | Sequência de imagens de entrada para codificar como quadros do vídeo |
| `filename_prefix` | STRING | Não | - | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI") |
| `codec` | COMBO | Sim | "vp9"<br>"av1" | Codec de vídeo a ser usado para a codificação |
| `fps` | FLOAT | Não | 0.01-1000.0 | Taxa de quadros para o vídeo de saída (padrão: 24.0) |
| `crf` | FLOAT | Não | 0-63.0 | Configuração de qualidade, onde um valor de `crf` mais alto significa qualidade menor com tamanho de arquivo reduzido, e um valor mais baixo significa qualidade maior com tamanho de arquivo maior (padrão: 32.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `ui` | PREVIEW | Prévia do vídeo mostrando o arquivo WEBM salvo |
