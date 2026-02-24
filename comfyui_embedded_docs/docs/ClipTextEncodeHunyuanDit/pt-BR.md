> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/pt-BR.md)

O nó `CLIPTextEncodeHunyuanDiT` tem como função principal converter texto de entrada em uma forma que o modelo possa compreender. É um nó de condicionamento avançado, projetado especificamente para a arquitetura de codificador de texto duplo do modelo HunyuanDiT.
Seu papel principal é semelhante ao de um tradutor, convertendo nossas descrições textuais em "linguagem de máquina" que o modelo de IA possa entender. As entradas `bert` e `mt5xl` preferem tipos diferentes de entrada de prompt.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-----------|-------------|
| `clip` | CLIP | Uma instância do modelo CLIP usada para tokenização e codificação de texto, sendo essencial para gerar as condições. |
| `bert` | STRING | Entrada de texto para codificação, prefere frases e palavras-chave, suporta múltiplas linhas e prompts dinâmicos. |
| `mt5xl` | STRING | Outra entrada de texto para codificação, suporta múltiplas linhas e prompts dinâmicos (multilíngue), pode usar frases completas e descrições complexas. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | A saída condicional codificada, usada para processamento posterior em tarefas de geração. |
