# Pré-visualização de Amostragem TripoSplat

Este nó modifica um modelo TripoSplat para que, quando usado com o nó padrão KSampler, uma pré-visualização ao vivo do splat gaussiano decodificado seja exibida a cada etapa de amostragem. Ele funciona encapsulando o callback do amostrador para decodificar a saída do modelo em uma imagem de pré-visualização após cada etapa.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|--------------|-----------|
| `model` | O modelo TripoSplat a ser modificado para pré-visualização ao vivo | MODEL | Sim | |
| `vae` | Decodificador VAE do TripoSplat | VAE | Sim | |
| `octree_level` | Profundidade do octree para a decodificação da pré-visualização (menor = mais barato/mais grosseiro). Padrão: 5 | INT | Não | 2 a 8 |
| `num_gaussians` | Número de gaussianas a serem geradas para a pré-visualização (arredondado para múltiplo de 32). Padrão: 16384 | INT | Não | 1024 a 262144 (passo: 32) |
| `yaw` | Rotação horizontal (yaw) da câmera de pré-visualização em graus. Padrão: 90.0 | FLOAT | Não | -360.0 a 360.0 (passo: 1.0) |
| `pitch` | Rotação vertical (pitch) da câmera de pré-visualização em graus. Padrão: 15.0 | FLOAT | Não | -89.0 a 89.0 (passo: 1.0) |
| `point_size` | Raio máximo do splat em pixels. Cada gaussiana é dimensionada a partir de sua escala e limitada a este valor; menor = mais fino/pontiagudo, maior = mais encorpado. Padrão: 3 | INT | Não | 1 a 16 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `MODEL` | O modelo TripoSplat modificado com a funcionalidade de pré-visualização ao vivo adicionada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/pt-BR.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
