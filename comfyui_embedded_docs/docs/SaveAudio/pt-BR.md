> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/pt-BR.md)

O nó SaveAudio salva dados de áudio em um arquivo no formato FLAC. Ele recebe uma entrada de áudio e a grava no diretório de saída especificado com o prefixo de nome de arquivo fornecido. O nó gerencia automaticamente a nomeação dos arquivos e garante que o áudio seja salvo corretamente para uso posterior.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `áudio` | AUDIO | Sim | - | Os dados de áudio a serem salvos |
| `prefixo_do_arquivo` | STRING | Não | - | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") |

*Nota: Os parâmetros `prompt` e `extra_pnginfo` são ocultos e gerenciados automaticamente pelo sistema.*

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| *Nenhum* | - | Este nó não retorna nenhum dado de saída, mas salva o arquivo de áudio no diretório de saída |

---
**Source fingerprint (SHA-256):** `16242dfc45d0f2808a5615e9c1bfe4de4d19e2f5f6b28370f631439021dc72e5`
