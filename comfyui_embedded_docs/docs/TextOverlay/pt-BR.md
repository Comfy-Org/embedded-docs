# Desenhar Sobreposição de Texto

Este nó desenha texto sobre uma imagem ou um lote de imagens. Ele cria uma sobreposição de texto usando tamanho de fonte, cor, posição vertical, alinhamento horizontal e contorno preto opcional configuráveis, e então combina a sobreposição com os pixels da imagem original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagens` | A imagem de entrada ou lote de imagens sobre o qual desenhar o texto | IMAGE | Sim | |
| `texto` | O texto a ser sobreposto na imagem (padrão: ""). Suporta múltiplas linhas: as sequências de escape `\n` e `\t` são convertidas em quebras de linha e tabulações, e linhas longas são quebradas automaticamente para caber na largura da imagem. | STRING | Sim | |
| `tamanho_da_fonte` | Tamanho da fonte como porcentagem da altura da imagem (padrão: 5.0) | FLOAT | Sim | 0.5 a 50.0 (passo 0.5) |
| `cor` | Cor do texto (padrão: "#ffffff") | COLOR | Sim | |
| `posição` | Posição vertical do texto na imagem (padrão: "top") | COMBO | Sim | "top"<br>"bottom" |
| `alinhamento` | Alinhamento horizontal do texto (padrão: "left") | COMBO | Sim | "left"<br>"center"<br>"right" |
| `contorno` | Desenhar um contorno preto ao redor do texto (padrão: True) | BOOLEAN | Sim | |

Nota: Se `text` estiver vazio ou contiver apenas espaços em branco, o nó retorna as imagens de entrada inalteradas. A sobreposição de texto é renderizada uma vez e aplicada a cada imagem do lote. Se o bloco de texto renderizado for mais alto que a área disponível da imagem, o tamanho da fonte é reduzido automaticamente até caber ou atingir um tamanho mínimo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | As imagens de entrada com a sobreposição de texto composta por cima | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
