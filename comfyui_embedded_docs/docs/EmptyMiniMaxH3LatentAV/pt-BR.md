# Latente AV MiniMax H3 Vazio

Este nó cria um latent vazio que combina informações de vídeo e áudio para o modelo MiniMax H3. Você define a largura, a altura e o comprimento do conteúdo, e o nó produz um latent em branco que o modelo pode usar como ponto de partida para a geração. A duração (comprimento) é ajustada automaticamente para se encaixar na grade de quadros exigida pelo modelo, de 17k+5 quadros a 24 fps.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `largura` | A largura do latent em pixels. Os valores devem ser múltiplos de 32. Padrão: 1344. | INT | Sim | 32 - MAX_RESOLUTION (passo 32) |
| `altura` | A altura do latent em pixels. Os valores devem ser múltiplos de 32. Padrão: 768. | INT | Sim | 32 - MAX_RESOLUTION (passo 32) |
| `duração` | Contagem de quadros a 24 fps, arredondada para cima para a grade 17k+5 do modelo (124 = ~5s; a faixa treinada é ~124-362, valores maiores não foram testados). Padrão: 124. | INT | Sim | 5 - 3600 (passo 17) |

Nota: O valor de `length` é arredondado para cima para a próxima contagem de quadros que se encaixa na grade 17k+5 do modelo (17 x k + 5 quadros, como 5, 22, 39, 56, 73, 90, 107, 124, e assim por diante). Os valores de `width` e `height` devem ser múltiplos de 32. A resolução máxima é o valor definido pelo sistema no ComfyUI.

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `latent` | O latent vazio combinado de vídeo+áudio gerado para o MiniMax H3, dimensionado de acordo com a largura, a altura e o comprimento de entrada. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxH3LatentAV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ee24f4ac630858d87b9b98bb402689a5790e0ed882ec47dffe7b497216e37a5c`
