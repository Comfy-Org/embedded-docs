# LTXVCropGuides

O nó LTXVCropGuides processa entradas de conditioning e latent para geração de vídeo, removendo informações de quadros-chave e ajustando as dimensões do latent. Ele recorta a imagem latente e o mapa de ruído para excluir seções de quadros-chave, ao mesmo tempo que limpa os índices de quadros-chave e as entradas de atenção de orientação tanto no conditioning positivo quanto no negativo. Isso prepara os dados para fluxos de trabalho de geração de vídeo que não exigem orientação por quadros-chave.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de conditioning positiva contendo informações de orientação para a geração. Seus índices de quadros-chave determinam quantos quadros são recortados do latent. | CONDITIONING | Sim | - |
| `negativo` | A entrada de conditioning negativa contendo informações de orientação sobre o que evitar na geração. Seus dados de quadros-chave são limpos juntamente com os do conditioning positivo. | CONDITIONING | Sim | - |
| `latent` | A representação latente que contém as amostras de imagem e os dados do mapa de ruído. Quando há quadros-chave no conditioning positivo, os quadros do último quadro-chave são removidos tanto das amostras quanto do mapa de ruído. | LATENT | Sim | - |

Nota: O recorte ocorre somente quando o conditioning positivo contém índices de quadros-chave. Se nenhum quadro-chave for detectado, os conditionings positivo e negativo passam inalterados, juntamente com o latent.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O conditioning positivo processado, com os índices de quadros-chave e as entradas de atenção de orientação removidos | CONDITIONING |
| `negativo` | O conditioning negativo processado, com os índices de quadros-chave e as entradas de atenção de orientação removidos | CONDITIONING |
| `latent` | A representação latente recortada, com as amostras e o mapa de ruído ajustados, onde as seções de quadros-chave foram removidas | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/pt-BR.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
