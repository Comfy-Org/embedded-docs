# Salvar Áudio (Opus)

O nó SaveAudioOpus salva dados de áudio em um arquivo no formato Opus, permitindo escolher a qualidade de codificação (bitrate) e o prefixo do nome do arquivo para o arquivo exportado. Este nó está obsoleto e pode ser removido em versões futuras.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `áudio` | Os dados de áudio a serem salvos como um arquivo Opus. Um ValueError é gerado se isto for None (por exemplo, quando o vídeo de origem não tem faixa de áudio). | AUDIO | Sim | - |
| `prefixo_do_arquivo` | O prefixo usado para o nome do arquivo de saída (padrão: "audio/ComfyUI"). | STRING | Não | - |
| `qualidade` | O bitrate usado para codificar o arquivo Opus; valores mais altos produzem melhor qualidade, mas arquivos maiores (padrão: "128k"). | COMBO | Não | `"64k"`<br>`"96k"`<br>`"128k"`<br>`"192k"`<br>`"320k"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `audio` | Os dados de áudio que foram salvos no arquivo Opus. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
