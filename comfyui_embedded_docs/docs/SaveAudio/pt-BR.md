# Salvar Áudio (FLAC)

O nó SaveAudio salva dados de áudio em um arquivo no formato FLAC. Ele recebe uma entrada de áudio e a grava no diretório de saída especificado com o prefixo de nome de arquivo fornecido. O nó gerencia automaticamente a nomeação dos arquivos e garante que o áudio seja salvo corretamente para uso posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | Os dados de áudio a serem salvos | AUDIO | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "audio/ComfyUI") | STRING | Não | - |

*Nota: Os parâmetros `prompt` e `extra_pnginfo` são ocultos e gerenciados automaticamente pelo sistema.*

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| *Nenhum* | Este nó não retorna nenhum dado de saída, mas salva o arquivo de áudio no diretório de saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `16242dfc45d0f2808a5615e9c1bfe4de4d19e2f5f6b28370f631439021dc72e5`
