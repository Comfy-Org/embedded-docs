> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/pt-BR.md)

O nó SaveImage salva as imagens recebidas no diretório `ComfyUI/output`. Ele salva cada imagem como um arquivo PNG e pode incorporar metadados do fluxo de trabalho, como o prompt, no arquivo salvo para referência futura.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagens` | IMAGE | Sim | - | As imagens a serem salvas. |
| `prefixo_do_arquivo` | STRING | Sim | - | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` para incluir valores de nós (padrão: "ComfyUI"). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `ui` | UI_RESULT | Este nó gera um resultado de interface contendo uma lista das imagens salvas com seus nomes de arquivo e subpastas. Ele não gera dados para conexão com outros nós. |

---
**Source fingerprint (SHA-256):** `fa88c26e5e03f788dcc545434a54124c5e9d03b559da67f0857b52faec0e97e7`
