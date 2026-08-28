# Pré-visualizar Áudio

O nó Preview Audio cria uma pré-visualização de áudio temporária que pode ser reproduzida diretamente na interface, sem salvar o áudio no diretório de saída do ComfyUI. Ele recebe dados de áudio como entrada e gera um widget de pré-visualização, permitindo que os usuários ouçam as saídas de áudio sem salvar arquivos permanentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `audio` | Os dados de áudio para pré-visualizar. Este nó gerará um erro se o áudio de entrada for None, o que pode acontecer quando o vídeo de origem não possui trilha de áudio. | AUDIO | Sim | - |

**Nota:** Se o `audio` de entrada for None, o nó gera um ValueError. Isso pode ocorrer quando o vídeo de origem não possui trilha de áudio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `áudio` | Os dados de áudio repassados da entrada, usados para a pré-visualização. | AUDIO |
| `ui` | Exibe um widget de reprodutor de áudio na interface para pré-visualizar o áudio. | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
