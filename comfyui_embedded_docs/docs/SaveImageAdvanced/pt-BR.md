# SaveImageAdvanced

O nó **SaveImageAdvanced** salva imagens no diretório de saída do ComfyUI com controle avançado sobre formato de arquivo, profundidade de bits e espaço de cores. Ele suporta salvar como arquivos PNG ou EXR e pode incorporar metadados do fluxo de trabalho nos arquivos salvos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | As imagens a serem salvas. | IMAGE | Sim | - |
| `prefixo_do_nome_do_arquivo` | O prefixo para o arquivo a ser salvo. Pode incluir tokens de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (padrão: "ComfyUI") | STRING | Sim | - |
| `formato` | O formato de arquivo no qual salvar a imagem. Selecionar um formato revela opções adicionais para aquele formato. | COMBO | Sim | `"png"`<br>`"exr"` |
| `bit_depth` | A profundidade de bits para o formato selecionado. Este parâmetro aparece quando um formato é escolhido. (padrão: "8-bit" para PNG, "32-bit float" para EXR) | COMBO | Sim (condicional) | Para PNG: `"8-bit"`<br>`"16-bit"`<br>Para EXR: `"32-bit float"` |
| `input_color_space` | Espaço de cores do tensor de entrada. Para PNG, apenas sRGB está disponível. Para EXR, a imagem é sempre gravada como cena-linear no gamute correspondente. (padrão: "sRGB") | COMBO | Sim (condicional) | Para PNG: `"sRGB"`<br>Para EXR: `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Observações sobre Dependências de Parâmetros:**
- Os parâmetros `bit_depth` e `input_color_space` estão disponíveis apenas quando um `format` específico é selecionado.
- Para o formato PNG, apenas profundidades de bits "8-bit" e "16-bit" estão disponíveis, e apenas o espaço de cores "sRGB".
- Para o formato EXR, apenas a profundidade de bits "32-bit float" está disponível, com espaços de cores "sRGB", "HDR" ou "linear".
- O parâmetro `input_color_space` para EXR determina como o tensor de entrada é interpretado:
  - `"sRGB"` — a entrada é sRGB codificada em Rec.709; a EOTF sRGB inversa é aplicada.
  - `"HDR"` — a entrada é HLG codificada em Rec.2020 (BT.2100); a OETF HLG inversa é aplicada para obter luz cena-linear.
  - `"linear"` — a entrada já é cena-linear (primárias Rec.709); gravada sem alterações. Use esta opção para saída de renderizadores/compositores.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | Uma lista de resultados de imagens salvas, cada um contendo o nome do arquivo, subpasta e tipo ("output"). Esta saída é usada para fins de exibição na interface do usuário. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/pt-BR.md)

---
**Source fingerprint (SHA-256):** `61e52bab8c28437cf648e4790823c15dbe0f758478635b0bd8b5cce785421fe5`
