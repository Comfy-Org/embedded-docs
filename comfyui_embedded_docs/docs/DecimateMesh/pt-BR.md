# DecimateMesh

DecimateMesh simplifica uma malha 3D para uma contagem alvo de faces usando simplificação por métrica de erro quadrático (QEM), executando o cálculo no dispositivo de computação ativo. O modo de posicionamento `"midpoint"` é a predefinição fiel ao cumesh, que oferece a melhor qualidade ao preservar características finas, como cabelos, enquanto `"qem"` posiciona vértices na posição ótima por QEM, com controles opcionais de linhas e arestas de características. A malha de saída permanece soldada.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D a ser simplificada. | MESH | Sim | - |
| `target_face_count` | Número máximo de faces alvo. 0 desativa. (padrão: 200000) | INT | Sim | 0 a 50000000 |
| `placement_mode` | midpoint: fiel ao cumesh (recomendado). qem: posicionamento ótimo por QEM. (padrão: `"midpoint"`) | DYNAMIC_COMBO | Sim | `"midpoint"`<br>`"qem"` |

### Entradas do Midpoint

O modo de posicionamento `"midpoint"` não expõe subparâmetros adicionais; ele usa a predefinição padrão de posicionamento midpoint.

### Entradas do QEM

Os seguintes subparâmetros aparecem na interface somente quando `placement_mode` está definido como `"qem"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | Peso da quadrática de linha por aresta; preserva cristas/vales acentuados. 0 = desativado. (padrão: 0.0) | FLOAT | Não | 0.0 a 100.0 |
| `feature_edge_quadric_weight` | Peso quadrático extra em arestas de características diedrais (vincos). 0 = desativado. (padrão: 0.0) | FLOAT | Não | 0.0 a 1000.0 |
| `feature_edge_min_dihedral_deg` | Ângulo diedral mínimo (em graus) para uma aresta ser considerada aresta de característica. (padrão: 30.0) | FLOAT | Não | 0.0 a 180.0 |
| `clamp_v_to_edge` | Projeta a posição ótima por QEM no segmento de aresta colapsado. (padrão: true) | BOOLEAN | Não | `true`<br>`false` |

Observação: a decimação é ignorada quando `target_face_count` é 0 ou quando a malha já tem menos faces que o alvo. O nó exibe um resumo da redução de faces nele mesmo, por exemplo `faces: 1.23M → 200K (-84%)`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha simplificada com a contagem reduzida de faces; a conectividade permanece soldada. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
