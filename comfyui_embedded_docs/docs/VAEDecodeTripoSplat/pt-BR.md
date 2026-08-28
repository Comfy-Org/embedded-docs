# Decodificar TripoSplat

Decodifica uma representação latente do TripoSplat em um splat gaussiano 3D. Este nó pega o latente amostrado de um modelo TripoSplat e o reconstrói como um conjunto de gaussianas 3D, cuja densidade pode ser ajustada modificando o número de gaussianas produzidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `amostras` | As amostras latentes a decodificar. Se as amostras contiverem um fluxo de câmera aninhado junto com o latente, apenas o fluxo latente é decodificado. | LATENT | Sim | - |
| `vae` | Decodificador VAE do TripoSplat | VAE | Sim | - |
| `número_de_gaussianos` | Número de gaussianas a produzir (arredondado para um múltiplo de 32). 262144 corresponde à densidade de pontos do octree; valores maiores superamostram os mesmos pontos (mais denso, mas sem novos detalhes) e custam proporcionalmente mais VRAM/tempo. Padrão: 262144 | INT | Sim | 32 a 1048576 (step: 32) |
| `semente` | Define a semente do amostrador de pontos do octree (RNG global) para decodificações determinísticas. Padrão: 0 | INT | Sim | 0 a 18446744073709551615 |

**Nota:** O valor de `num_gaussians` é automaticamente limitado ao intervalo permitido e arredondado para um múltiplo da configuração de gaussianas por ponto do decodificador VAE. O número real usado pode diferir ligeiramente do valor de entrada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `splat` | O splat gaussiano 3D decodificado contendo posições, escalas, rotações, opacidades e coeficientes de harmônicos esféricos | SPLAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5c2b21cee31c68a6440ab4c7156e0d5c041ce7264f6467a508dc41e2eb0dc598`
