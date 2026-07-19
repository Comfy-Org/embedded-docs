# Decodificar TripoSplat

Decodifica uma representação latente do TripoSplat em um splat gaussiano 3D. Este nó recebe o latente amostrado de um modelo TripoSplat e o reconstrói como um conjunto de gaussianas 3D, cuja densidade pode ser ajustada modificando o número de gaussianas produzidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `amostras` | As amostras latentes a serem decodificadas | LATENT | Sim | - |
| `vae` | Modelo decodificador VAE do TripoSplat | VAE | Sim | - |
| `número_de_gaussianos` | Número de gaussianas a serem produzidas (arredondado para um múltiplo de 32). 262144 corresponde à densidade de pontos da octree; valores maiores superamostram os mesmos pontos (mais denso, mas sem novos detalhes) e custam proporcionalmente mais VRAM/tempo. Padrão: 262144 | INT | Sim | 32 a 1048576 (passo: 32) |
| `semente` | Semeia o amostrador de pontos da octree (RNG global) para decodificações determinísticas. Padrão: 0 | INT | Sim | 0 a 18446744073709551615 |

**Nota:** O valor de `num_gaussians` é automaticamente arredondado para um múltiplo da configuração de gaussianas-por-ponto do decodificador VAE. O número real utilizado pode diferir ligeiramente do valor inserido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `splat` | O splat gaussiano 3D decodificado contendo posições, escalas, rotações, opacidades e coeficientes de harmônicos esféricos | SPLAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTripoSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `60fff70ade38bc820eaea9db26b714daf84a111fb3563477f56f4e8ffa96ff5b`
