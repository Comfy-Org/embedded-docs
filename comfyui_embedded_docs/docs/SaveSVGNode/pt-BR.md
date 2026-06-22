# Salvar Nó SVG

Salva arquivos SVG no disco. Este nó recebe dados SVG como entrada e os salva no diretório de saída, com incorporação opcional de metadados. O nó gerencia automaticamente a nomeação de arquivos com sufixos numéricos e pode incorporar informações do fluxo de trabalho diretamente no arquivo SVG.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `svg` | Os dados SVG a serem salvos no disco | SVG | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` para incluir valores de nós. (padrão: "svg/ComfyUI") | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `ui` | Retorna informações do arquivo, incluindo nome, subpasta e tipo para exibição na interface do ComfyUI | DICT |

**Nota:** Este nó incorpora automaticamente metadados do fluxo de trabalho (informações do prompt e dados extras PNG) no arquivo SVG quando disponíveis. Os metadados são inseridos como uma seção CDATA dentro do elemento de metadados do SVG.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a294103d8d2306ce6765912a98c5572323bb5394909ee384591534b0b404ea70`
