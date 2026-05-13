> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/pt-BR.md)

O nó LTXVImgToVideoInplace condiciona uma representação latente de vídeo codificando uma imagem de entrada em seus quadros iniciais. Ele funciona usando um VAE para codificar a imagem no espaço latente e, em seguida, mesclando-a com as amostras latentes existentes com base em uma intensidade especificada. Isso permite que uma imagem sirva como ponto de partida ou sinal de condicionamento para a geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem de entrada no espaço latente. |
| `image` | IMAGE | Sim | - | A imagem de entrada a ser codificada e usada para condicionar o latente de vídeo. |
| `latent` | LATENT | Sim | - | A representação latente de vídeo de destino a ser modificada. |
| `strength` | FLOAT | Não | 0.0 - 1.0 | Controla a intensidade da mesclagem da imagem codificada no latente. Um valor de 1.0 substitui completamente os quadros iniciais, enquanto valores menores fazem a mesclagem. (padrão: 1.0) |
| `bypass` | BOOLEAN | Não | - | Ignora o condicionamento. Quando ativado, o nó retorna o latente de entrada inalterado. (padrão: Falso) |

**Observação:** A `image` será redimensionada automaticamente para corresponder às dimensões espaciais exigidas pelo `vae` para codificação, com base na largura e altura da entrada `latent`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `latent` | LATENT | A representação latente de vídeo modificada. Contém as amostras atualizadas e um `noise_mask` que aplica a intensidade de condicionamento aos quadros iniciais. |

---
**Source fingerprint (SHA-256):** `49df511591071f51e2b86f2302cfb438d18b5e1ade7ef228345f65fddf88dbcc`
