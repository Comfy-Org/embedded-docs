> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/pt-BR.md)

O nó TextEncodeQwenImageEditPlus processa prompts de texto e imagens opcionais para gerar dados de condicionamento para tarefas de geração ou edição de imagens. Ele utiliza um template especializado para analisar imagens de entrada e compreender como as instruções de texto devem modificá-las, codificando essas informações para uso em etapas subsequentes de geração. O nó pode lidar com até três imagens de entrada e, opcionalmente, gerar latentes de referência quando um VAE é fornecido.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | - | O modelo CLIP usado para tokenização e codificação |
| `prompt` | STRING | Sim | - | Instrução de texto descrevendo a modificação de imagem desejada (suporta entrada multilinha e prompts dinâmicos) |
| `vae` | VAE | Não | - | Modelo VAE opcional para gerar latentes de referência a partir das imagens de entrada |
| `image1` | IMAGE | Não | - | Primeira imagem de entrada opcional para análise e modificação |
| `image2` | IMAGE | Não | - | Segunda imagem de entrada opcional para análise e modificação |
| `image3` | IMAGE | Não | - | Terceira imagem de entrada opcional para análise e modificação |

**Observação:** Quando um VAE é fornecido, o nó gera latentes de referência a partir de todas as imagens de entrada. O nó pode processar até três imagens simultaneamente, e as imagens são redimensionadas automaticamente para dimensões apropriadas para o processamento.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Dados de condicionamento codificados contendo tokens de texto e latentes de referência opcionais para geração de imagem |
