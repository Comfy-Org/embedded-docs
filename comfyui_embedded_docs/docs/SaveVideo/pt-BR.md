# Salvar Vídeo

O nó SaveVideo salva o conteúdo de vídeo de entrada no diretório de saída do seu ComfyUI. Ele permite especificar o prefixo do nome do arquivo, o formato do vídeo e o codec para o arquivo salvo. O nó gerencia automaticamente a nomeação dos arquivos com incrementos de contador e pode incluir metadados do fluxo de trabalho no vídeo salvo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo a ser salvo. | VIDEO | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação como %date:yyyy-MM-dd% ou %Empty Latent Image.width% para incluir valores de nós (padrão: "video/ComfyUI"). | STRING | Não | - |
| `formato` | O formato para salvar o vídeo (padrão: "auto"). | COMBO | Não | `"auto"`<br>`"mp4"`<br>`"webm"`<br>`"mkv"`<br>`"gif"` |
| `codec` | O codec a ser usado para o vídeo (padrão: "auto"). | COMBO | Não | `"auto"`<br>`"h264"`<br>`"h265"`<br>`"vp9"`<br>`"av1"`<br>`"prores"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| *Nenhuma saída* | Este nó não retorna nenhum dado de saída. | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `506ddc8820924688cccb9fd838ff9c0f5217a38f708f28f15a060be9325cea61`
