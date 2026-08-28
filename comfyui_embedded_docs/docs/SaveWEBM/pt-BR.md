# Salvar WEBM

O nó SaveWEBM salva uma sequência de imagens como um arquivo de vídeo WEBM. Ele recebe múltiplas imagens de entrada e as codifica em um vídeo usando o codec VP9 ou AV1, com configurações de qualidade e taxa de quadros ajustáveis. O arquivo de vídeo resultante é salvo no diretório de saída com metadados que incluem informações do prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagens` | Imagens RGBA são salvas com seu canal alpha como transparência (somente codec vp9). | IMAGE | Sim | - |
| `prefixo_do_arquivo` | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI"). | STRING | Não | - |
| `codec` | Codec de vídeo a ser usado na codificação. | COMBO | Sim | "vp9"<br>"av1" |
| `fps` | Taxa de quadros para o vídeo de saída (padrão: 24.0). | FLOAT | Não | 0.01-1000.0 |
| `crf` | Valores maiores de crf significam qualidade menor com tamanho de arquivo menor; valores menores de crf significam qualidade maior e tamanho de arquivo maior (padrão: 32.0). | FLOAT | Não | 0-63.0 |

**Nota sobre o canal alpha:** O canal alpha de imagens RGBA é preservado apenas quando o codec VP9 é usado. Ao usar o codec AV1, o canal alpha é ignorado e somente os dados RGB são codificados.

**Nota sobre a nomeação de arquivos:** Os vídeos são salvos no diretório de saída como `{filename_prefix}_{counter:05}_.webm`, onde o contador é incrementado automaticamente para evitar a sobrescrita de arquivos existentes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `imagens` | As imagens de entrada, passadas adiante inalteradas após o vídeo ser salvo. | IMAGE |
| UI preview | Pré-visualização do vídeo mostrando o arquivo WEBM salvo. | PREVIEW |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`
