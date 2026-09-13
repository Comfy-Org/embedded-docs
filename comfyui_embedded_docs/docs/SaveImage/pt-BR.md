# Salvar Imagem

O nó SaveImage salva as imagens de entrada como arquivos PNG no seu diretório de saída do ComfyUI. Ele pode incorporar metadados do workflow, como o prompt, em cada arquivo salvo, e retorna as imagens inalteradas para que ainda possam ser usadas por outros nós.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | As imagens a salvar. | IMAGE | Sim | - |
| `prefixo_do_arquivo` | O prefixo do arquivo a ser salvo. Isso pode incluir informações de formatação, como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`, para incluir valores de nós (padrão: "ComfyUI"). | STRING | Sim | - |

O nó também recebe duas entradas ocultas, `prompt` e `extra_pnginfo`, que são preenchidas automaticamente pelo ComfyUI com o prompt do workflow e informações PNG extras. Quando os metadados estão habilitados, essas informações são incorporadas como metadados de texto em cada arquivo PNG salvo.

O nome do arquivo para cada imagem salva é montado a partir de `filename_prefix`, um placeholder opcional `%batch_num%` que é substituído pela posição da imagem no lote, e um contador de cinco dígitos, por exemplo `ComfyUI_00001_.png`. As imagens são gravadas com nível 4 de compressão PNG.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | As imagens de entrada originais, retornadas inalteradas após serem salvas em disco. | IMAGE |
| `ui` | Um resultado apenas da UI contendo a lista de arquivos de imagem salvos (filename, subfolder e type) para exibição no frontend. | UI_RESULT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
