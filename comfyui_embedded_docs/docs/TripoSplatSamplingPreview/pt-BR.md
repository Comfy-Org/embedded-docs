# Pré-visualização de Amostragem TripoSplat

Este nó modifica um modelo TripoSplat para que, quando usado com o nó padrão KSampler, uma pré-visualização ao vivo do gaussian splat decodificado seja exibida a cada etapa de amostragem. Ele funciona encapsulando o callback do amostrador para decodificar a saída do modelo em uma imagem de pré-visualização após cada etapa.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo TripoSplat a ser modificado para pré-visualização ao vivo | MODEL | Sim | |
| `vae` | Decodificador VAE do TripoSplat | VAE | Sim | |
| `nível_octree` | Profundidade do octree para a decodificação da pré-visualização (menor = mais barato/mais grosseiro). Padrão: 5 | INT | Não | 2 a 8 |
| `número_de_gaussianos` | Número de gaussianos a serem gerados para a pré-visualização (arredondado para um múltiplo de 32). Padrão: 16384 | INT | Não | 1024 a 262144 (passo: 32) |
| `yaw` | Rotação horizontal (yaw) da câmera de pré-visualização em graus. Padrão: 90.0 | FLOAT | Não | -360.0 a 360.0 (passo: 1.0) |
| `pitch` | Rotação vertical (pitch) da câmera de pré-visualização em graus. Padrão: 15.0 | FLOAT | Não | -89.0 a 89.0 (passo: 1.0) |
| `tamanho_do_ponto` | Raio máximo do splat em pixels. Cada gaussiano é dimensionado a partir de sua escala e limitado a este valor; menor = mais fino/mais pontual, maior = mais grosso. Padrão: 3 | INT | Não | 1 a 16 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O modelo TripoSplat modificado com funcionalidade de pré-visualização ao vivo adicionada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/pt-BR.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
