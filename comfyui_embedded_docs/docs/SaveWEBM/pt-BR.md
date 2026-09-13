# Salvar WEBM

O nó SaveWEBM salva uma sequência de imagens como um arquivo de vídeo WEBM. Ele recebe várias imagens de entrada e as codifica em um vídeo usando o codec VP9 ou AV1, com configurações de qualidade e taxa de quadros configuráveis. O arquivo de vídeo resultante é salvo no diretório de saída com metadados que incluem informações do prompt.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagens RGBA são salvas com seu canal alfa como transparência (somente codec vp9). | IMAGE | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI"). | STRING | Não | - |
| `codec` | Codec de vídeo a ser usado para codificação. | COMBO | Sim | "vp9"<br>"av1" |
| `fps` | Taxa de quadros para o vídeo de saída (padrão: 24.0). | FLOAT | Não | 0.01-1000.0 |
| `crf` | CRF mais alto significa qualidade menor com tamanho de arquivo menor; CRF mais baixo significa qualidade maior com tamanho de arquivo maior (padrão: 32.0). | FLOAT | Não | 0-63.0 |

**Nota sobre o canal alfa:** O canal alfa de imagens RGBA só é preservado ao usar o codec VP9. Ao usar o codec AV1, o canal alfa é ignorado e apenas os dados RGB são codificados.

**Nota sobre nomenclatura de arquivos:** Os vídeos são salvos no diretório de saída como `{filename_prefix}_{counter:05}_.webm`, onde o contador é incrementado automaticamente para evitar sobrescrever arquivos existentes.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `images` | As imagens de entrada, repassadas sem alteração após o vídeo ser salvo. | IMAGE |
| UI preview | Pré-visualização do vídeo mostrando o arquivo WEBM salvo. | PREVIEW |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
