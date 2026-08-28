# Salvar Imagem

O nó SaveImage salva as imagens de entrada como arquivos PNG no diretório de saída do seu ComfyUI. Ele pode incorporar metadados do fluxo de trabalho, como o prompt, em cada arquivo salvo, e retorna as imagens inalteradas para que possam ser usadas por outros nós.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | As imagens a salvar. | IMAGE | Sim | - |
| `prefixo_do_arquivo` | O prefixo do arquivo a salvar. Isso pode incluir informações de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` para incluir valores de nós (padrão: "ComfyUI"). | STRING | Sim | - |

O nó também recebe duas entradas ocultas, `prompt` e `extra_pnginfo`, que são automaticamente preenchidas pelo ComfyUI com o prompt do fluxo de trabalho e informações PNG extras. Quando os metadados estão habilitados, essas informações são incorporadas como metadados de texto em cada arquivo PNG salvo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | As imagens de entrada originais, retornadas inalteradas após serem salvas no disco. | IMAGE |
| `ui` | Um resultado somente de interface (UI) contendo a lista de arquivos de imagem salvos (nome do arquivo, subpasta e tipo) para exibição no frontend. | UI_RESULT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
