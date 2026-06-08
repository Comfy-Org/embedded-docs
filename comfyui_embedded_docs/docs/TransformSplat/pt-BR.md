# Transform Splat

O nó Transform Splat aplica transformações de translação, rotação e escala a um splat gaussiano. Ele move, rotaciona e redimensiona todo o splat como um único objeto e, quando uma escala não uniforme é aplicada, também remodela cada splat gaussiano individual para obter resultados precisos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `splat` | O splat gaussiano a ser transformado | SPLAT | Sim | - |
| `transladar_x` | Translação ao longo do eixo X (padrão: 0.0) | FLOAT | Sim | -100.0 a 100.0 |
| `transladar_y` | Translação ao longo do eixo Y (padrão: 0.0) | FLOAT | Sim | -100.0 a 100.0 |
| `transladar_z` | Translação ao longo do eixo Z (padrão: 0.0) | FLOAT | Sim | -100.0 a 100.0 |
| `rotacionar_x` | Rotação ao redor do eixo X em graus (padrão: 0.0) | FLOAT | Sim | -360.0 a 360.0 |
| `rotacionar_y` | Rotação ao redor do eixo Y em graus (padrão: 0.0) | FLOAT | Sim | -360.0 a 360.0 |
| `rotacionar_z` | Rotação ao redor do eixo Z em graus (padrão: 0.0) | FLOAT | Sim | -360.0 a 360.0 |
| `escala_x` | Fator de escala ao longo do eixo X (padrão: 1.0) | FLOAT | Sim | 0.01 a 100.0 |
| `escala_y` | Fator de escala ao longo do eixo Y (padrão: 1.0) | FLOAT | Sim | 0.01 a 100.0 |
| `escala_z` | Fator de escala ao longo do eixo Z (padrão: 1.0) | FLOAT | Sim | 0.01 a 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `splat` | O splat gaussiano transformado com posições, escalas e rotações atualizadas | SPLAT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TransformSplat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19e6a7da7b4f0d8c9674ead2d35d742df460576b01c4ab4108dd59a2d08dfcb0`
