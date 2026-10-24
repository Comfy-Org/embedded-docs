# Flux.2 [max] Imagem

Gera uma imagem com Flux.2 [max] por meio da API BFL a partir de um prompt e dimensões de saída explícitas, opcionalmente guiado por imagens de referência. Expõe as mesmas entradas que Flux.2 [pro] Image.

**Observação:** Este nó está marcado como obsoleto no código-fonte.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração ou edição da imagem. | STRING | Sim | - |
| `largura` | Largura da imagem gerada em pixels (padrão: 1024). | INT | Sim | 256 a 2048 (passo 32) |
| `altura` | Altura da imagem gerada em pixels (padrão: 768). | INT | Sim | 256 a 2048 (passo 32) |
| `semente` | A semente aleatória usada para criar o ruído (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `upsampling do prompt` | Se deve realizar upsampling no prompt. Se ativo, o prompt é modificado automaticamente para uma geração mais criativa (padrão: `True`). Esta é uma configuração avançada. | BOOLEAN | Sim | True / False |
| `imagens` | Imagens de referência opcionais para geração imagem para imagem. Cada imagem é reduzida para no máximo 2048x2048 pixels antes do upload. | IMAGE | Não | 0 a 9 imagens |

**Restrições:**

* Conectar mais de 9 imagens de referência gera um erro.
* O tamanho da saída é cobrado por megapixel, portanto valores maiores de `width` e `height` custam mais.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2MaxImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cd540606835e7808861d9a96584731100b1bf9c996f18586fed39e8a2d32a29f`
