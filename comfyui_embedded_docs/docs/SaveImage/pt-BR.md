> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/pt-BR.md)

O nó SaveImage salva as imagens que recebe no diretório `ComfyUI/output` do seu sistema. Ele salva cada imagem como um arquivo PNG e pode incorporar metadados do fluxo de trabalho, como o prompt, no arquivo salvo para referência futura.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | As imagens a serem salvas. |
| `filename_prefix` | STRING | Sim | - | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação, como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`, para incluir valores de outros nós (padrão: "ComfyUI"). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `ui` | UI_RESULT | Este nó gera um resultado de interface do usuário contendo uma lista das imagens salvas com seus nomes de arquivo e subpastas. Ele não emite dados para conexão com outros nós. |
