# Salvar Imagem

O nó SaveImage salva as imagens recebidas no diretório `ComfyUI/output`. Ele salva cada imagem como um arquivo PNG e pode incorporar metadados do workflow, como o prompt, no arquivo salvo para referência futura.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | As imagens a serem salvas. | IMAGE | Sim | - |
| `filename_prefix` | O prefixo do arquivo a ser salvo. Pode incluir informações de formatação, como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`, para incluir valores de nós (padrão: "ComfyUI"). | STRING | Sim | - |
| `prompt` | Entrada oculta, fornecida automaticamente pelo ComfyUI: os dados do prompt incorporados como metadados no arquivo PNG salvo. | PROMPT | Não | - |
| `extra_pnginfo` | Entrada oculta, fornecida automaticamente pelo ComfyUI: informações adicionais do workflow incorporadas como metadados no arquivo PNG salvo. | EXTRA_PNGINFO | Não | - |

Cada imagem é salva como um arquivo PNG. No nome do arquivo salvo, `%batch_num%` no prefixo é substituído pelo número do lote da imagem, e um contador com zeros à esquerda é anexado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | As mesmas imagens que foram salvas, repassadas para que possam ser usadas por outros nós. | IMAGE |
| `ui` | Resultado da interface contendo uma lista das imagens salvas com seus nomes de arquivo, subpastas e tipo, exibidos na interface do ComfyUI. | UI_RESULT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
