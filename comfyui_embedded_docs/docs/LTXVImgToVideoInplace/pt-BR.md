O nó LTXVImgToVideoInplace condiciona uma representação latente de vídeo codificando uma imagem de entrada em seus quadros iniciais. Ele funciona usando um VAE para codificar a imagem no espaço latente e, em seguida, mesclando-a com as amostras latentes existentes com base em uma intensidade especificada. Isso permite que uma imagem sirva como ponto de partida ou sinal de condicionamento para a geração de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar a imagem de entrada no espaço latente. | VAE | Sim | - |
| `image` | A imagem de entrada a ser codificada e usada para condicionar o latente de vídeo. | IMAGE | Sim | - |
| `latent` | A representação latente de vídeo de destino a ser modificada. | LATENT | Sim | - |
| `strength` | Controla a intensidade da mesclagem da imagem codificada no latente. Um valor de 1.0 substitui completamente os quadros iniciais, enquanto valores menores fazem a mesclagem. (padrão: 1.0) | FLOAT | Não | 0.0 - 1.0 |
| `bypass` | Ignora o condicionamento. Quando ativado, o nó retorna o latente de entrada inalterado. (padrão: Falso) | BOOLEAN | Não | - |

**Observação:** A `image` será redimensionada automaticamente para corresponder às dimensões espaciais exigidas pelo `vae` para codificação, com base na largura e altura da entrada `latent`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latent` | A representação latente de vídeo modificada. Contém as amostras atualizadas e um `noise_mask` que aplica a intensidade de condicionamento aos quadros iniciais. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/pt-BR.md)

---
**Source fingerprint (SHA-256):** `49df511591071f51e2b86f2302cfb438d18b5e1ade7ef228345f65fddf88dbcc`
