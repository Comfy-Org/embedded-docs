# Simplificar Malha

Simplifica uma malha 3D para uma contagem de faces alvo usando simplificação QEM (métrica de erro quadrática), executando o cálculo no dispositivo de computação ativo. O modo de posicionamento `"midpoint"` é a predefinição cumesh-faithful que oferece a melhor qualidade enquanto preserva recursos finos, como cabelos, ao passo que `"qem"` posiciona os vértices na posição ótima do QEM com controles opcionais de linha e arestas características. A malha de saída permanece soldada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D a ser simplificada. | MESH | Sim | - |
| `target_face_count` | Máximo de faces alvo. 0 desativa. (padrão: 200000) | INT | Sim | 0 a 50000000 |
| `placement_mode` | midpoint: fiel ao cumesh (recomendado). qem: posicionamento ótimo do QEM. (padrão: `"midpoint"`) | DYNAMIC_COMBO | Sim | `"midpoint"`<br>`"qem"` |

### Entradas do Midpoint

O modo de posicionamento `"midpoint"` não expõe subparâmetros adicionais; ele usa a predefinição padrão de posicionamento midpoint.

### Entradas do QEM

Os seguintes subparâmetros aparecem na interface somente quando `placement_mode` está definido como `"qem"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `line_quadric_weight` | Peso da quadrica de linha por aresta; preserva cristas/vales acentuados. 0 = desativado. (padrão: 0.0) | FLOAT | Não | 0.0 a 100.0 |
| `feature_edge_quadric_weight` | Peso quadrico extra em arestas características diedrais (vincos). 0 = desativado. (padrão: 0.0) | FLOAT | Não | 0.0 a 1000.0 |
| `feature_edge_min_dihedral_deg` | Ângulo diedral mínimo (grau) para contar uma aresta como aresta característica. (padrão: 30.0) | FLOAT | Não | 0.0 a 180.0 |
| `clamp_v_to_edge` | Projeta a posição ótima do QEM sobre o segmento da aresta colapsada. (padrão: true) | BOOLEAN | Não | `true`<br>`false` |

Observação: a decimação é ignorada quando `target_face_count` é 0 ou quando a malha já não tem mais faces que o alvo. O nó exibe um resumo de redução de faces nele próprio, por exemplo `faces: 1.23M → 200K (-84%)`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha simplificada com a contagem de faces reduzida; a conectividade permanece soldada. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DecimateMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55336e5b52e27d940e5402ecd74fd0ac847a1c6acd35955eccf72aab8ed940f9`
