> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/pt-BR.md)

O nó SaveWEBM salva uma sequência de imagens como um arquivo de vídeo WEBM. Ele recebe múltiplas imagens de entrada e as codifica em um vídeo usando o codec VP9 ou AV1, com configurações ajustáveis de qualidade e taxa de quadros. O arquivo de vídeo resultante é salvo no diretório de saída com metadados incluindo informações do prompt.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | - | Sequência de imagens de entrada para codificar como quadros de vídeo |
| `filename_prefix` | STRING | Não | - | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI") |
| `codec` | COMBO | Sim | "vp9"<br>"av1" | Codec de vídeo a ser usado para codificação |
| `fps` | FLOAT | Não | 0.01-1000.0 | Taxa de quadros para o vídeo de saída (padrão: 24.0) |
| `crf` | FLOAT | Não | 0-63.0 | Configuração de qualidade onde um crf mais alto significa qualidade inferior com tamanho de arquivo menor, e um crf mais baixo significa qualidade superior com tamanho de arquivo maior (padrão: 32.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `ui` | PREVIEW | Visualização do vídeo mostrando o arquivo WEBM salvo |

---
**Source fingerprint (SHA-256):** `761ce5148c273ffe3789be75c2a00268241d3ec7ecebd5b10efd1b1cc98d85ea`
