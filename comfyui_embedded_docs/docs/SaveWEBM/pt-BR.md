# Salvar WEBM

O nó SaveWEBM salva uma sequência de imagens como um arquivo de vídeo WEBM. Ele codifica as imagens de entrada em um vídeo usando o codec VP9 ou AV1, com taxa de quadros e configurações de qualidade configuráveis, e salva o arquivo no diretório de saída. Os metadados de prompt e workflow são incorporados ao arquivo de vídeo quando disponíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | A sequência de imagens a ser codificada no vídeo. Imagens RGBA são salvas com seu canal alfa como transparência (somente codec vp9). | IMAGE | Sim | - |
| `filename_prefix` | Prefixo para o nome do arquivo de saída; um contador e a extensão .webm são adicionados automaticamente (padrão: "ComfyUI") | STRING | Não | - |
| `codec` | Codec de vídeo usado para codificação | COMBO | Sim | "vp9"<br>"av1" |
| `fps` | Taxa de quadros para o vídeo de saída (padrão: 24.0) | FLOAT | Não | 0.01-1000.0 |
| `crf` | crf mais alto significa qualidade inferior com tamanho de arquivo menor; crf mais baixo significa qualidade superior e arquivo maior (padrão: 32.0) | FLOAT | Não | 0-63.0 |

**Nota sobre canal alfa:** O canal alfa de imagens RGBA é preservado apenas quando se usa o codec vp9. Ao usar o codec av1, o canal alfa é ignorado e apenas os dados RGB são codificados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | A sequência de imagens de entrada, repassada inalterada | IMAGE |
| `ui` | Pré-visualização de vídeo mostrando o arquivo WEBM salvo | PREVIEW |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
