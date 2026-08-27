# SalvarLatent

SaveLatent salva tensores latentes no disco como arquivos `.latent` para que possam ser reutilizados ou compartilhados posteriormente. Ele recebe amostras latentes, grava-as na pasta de saída com um nome gerado automaticamente e pode incorporar metadados do fluxo de trabalho, como o prompt, no arquivo salvo. As mesmas amostras latentes também são repassadas inalteradas para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `amostras` | As amostras latentes a serem salvas no disco. | LATENT | Sim | - |
| `prefixo_do_arquivo` | O prefixo usado para montar o nome do arquivo de saída. Pode incluir subpastas, por exemplo "latents/ComfyUI" (padrão: "latents/ComfyUI"). | STRING | Sim | - |
| `prompt` | O prompt do fluxo de trabalho, serializado como JSON e armazenado nos metadados do arquivo salvo (parâmetro oculto, fornecido automaticamente). | PROMPT | Não | - |
| `extra_pnginfo` | Informações adicionais do fluxo de trabalho, serializadas como JSON e armazenadas nos metadados do arquivo salvo (parâmetro oculto, fornecido automaticamente). | EXTRA_PNGINFO | Não | - |

Observação: Cada arquivo salvo é nomeado usando o prefixo e um contador de 5 dígitos, por exemplo `ComfyUI_00001_.latent`, e é colocado no diretório de saída. O arquivo contém o tensor latente e um marcador de versão do formato latente. Os metadados são incorporados ao arquivo salvo apenas quando o suporte a metadados está habilitado, ou seja, quando o ComfyUI não é iniciado com a opção `--disable-metadata`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `amostras` | As mesmas amostras latentes fornecidas como entrada, repassadas inalteradas. | LATENT |
| `ui` | Dados de exibição da interface que descrevem o arquivo salvo: seu nome de arquivo, subpasta e tipo de saída ("output"). | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
