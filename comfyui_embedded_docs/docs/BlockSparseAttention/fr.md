# Attention clairsemée par blocs du modèle

Le nœud **Block Sparse Attention** modifie un modèle afin que ses couches d'attention se concentrent uniquement sur les parties les plus pertinentes de l'entrée plutôt que sur tout à la fois, ce qui réduit le travail de calcul nécessaire pour les longues séquences. Les économies augmentent avec la longueur de séquence, car les séquences courtes sont généralement plus rapides avec une attention normale (dense).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle à patcher. | MODEL | Oui | N/A |
| `selection` | Méthode utilisée pour choisir les blocs de clés pour une attention complète au niveau des tokens (affichée comme `method`). <br>`sol-attn` : Sparsifying Online Attention utilise un seuil adaptatif sans entraînement pour chaque tête d'attention et bloc de requêtes.<br>`sla` : Sparse-Linear Attention conserve un pourcentage fixe des blocs de clés les mieux notés ; à utiliser uniquement avec des poids de modèle entraînés pour ce schéma.<br>`vsa` : Video Sparse Attention (FastVideo) utilise un pavage 3D en cubes vidéo et une branche d'attention grossière apprise ; nécessite des poids de modèle FastH3. | DYNAMIC_COMBO | Oui | `"sol-attn"`<br>`"sla"`<br>`"vsa"` |
| `start_percent` | Point de pourcentage où commence l'attention parcimonieuse. Avant ce point, l'attention reste dense. Par défaut : 0.2. | FLOAT | Non | min: 0.0, max: 1.0, step: 0.01 |
| `end_percent` | Point de pourcentage où se termine l'attention parcimonieuse. Après ce point, l'attention redevient dense. Par défaut : 1.0. | FLOAT | Non | min: 0.0, max: 1.0, step: 0.01 |
| `dense_blocks` | Blocs Transformer qui fonctionnent toujours en dense, par ex. '0, 1, 47-49'. Par défaut : "" (vide). Entrée avancée. | STRING | Non | Par défaut : "" |
| `min_tokens` | Les séquences plus courtes que cette valeur restent denses. Par défaut : 12288. Entrée avancée. | INT | Non | min: 0, max: 1048576, step: 512 |
| `extra_tokens` | Tokens supplémentaires les mieux notés auxquels chaque bloc de requêtes prête attention au-delà de ses blocs sélectionnés. Une valeur plus proche du dense offre plus de temps d'attention ; 256 recommandé, 0 désactive. Ignoré pour VSA. Par défaut : 256. Entrée avancée. | INT | Non | min: 0, max: 256, step: 64 |
| `sink_conditioning` | MiniMax-H3 uniquement. `exact_kv` : chaque requête prête exactement attention aux lignes empaquetées de texte/audio/référence (environ 3 % de coût). `exact_kv_and_rows` : exécute en plus les lignes de requêtes de l'audio cible en dense (préserve l'audio généré intact). `off` désactive ce comportement. Par défaut : "exact_kv_and_rows". Entrée avancée. | COMBO | Non | `"exact_kv"`<br>`"exact_kv_and_rows"`<br>`"off"` |
| `verbose` | Journalise si chaque forme d'attention a utilisé l'attention parcimonieuse ou pourquoi elle est restée dense. Par défaut : False. Entrée avancée. | BOOLEAN | Non | Par défaut : False |

### Entrées sol-attn

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `tau` | Seuil en écarts-types de la distribution des scores. Plus la valeur est élevée, plus l'attention est parcimonieuse : 1.0 conserve environ 16 % des blocs de clés exacts, 1.5 environ 7 %, 2.0 environ 2,7 %. Par défaut : 1.3. | FLOAT | Non | min: 0.0, max: 4.0, step: 0.05 |

### Entrées sla

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `keep_percent` | Pourcentage de blocs de clés que chaque bloc de requêtes conserve exactement (les sinks et la diagonale s'ajoutent par-dessus). Les LoRA de style SLA pour la sélection sont distillées pour ce schéma ; sans un tel LoRA, une valeur plus élevée est plus proche du dense. Par défaut : 10.0. | FLOAT | Non | min: 0.5, max: 95.0, step: 0.5 |

### Entrées vsa

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `keep_percent` | Pourcentage de cubes vidéo que chaque cube de requêtes conserve ; les checkpoints FastH3-VSA sont entraînés à 10. Utilise les couches `to_gate_compress` du modèle pour la branche grossière lorsqu'elles sont présentes. Par défaut : 10.0. | FLOAT | Non | min: 0.5, max: 95.0, step: 0.5 |

**Remarque :** Seuls les paramètres appartenant à la méthode actuellement sélectionnée sont affichés dans l'interface.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle avec attention parcimonieuse par blocs appliquée. | MODEL |

## Contraintes et limitations

- Les séquences plus courtes que `min_tokens`, les blocs listés dans `dense_blocks` et les étapes d'échantillonnage en dehors de la fenêtre `start_percent` à `end_percent` reviennent au backend d'attention dense du modèle sélectionné par le nœud Model Attention Backend.
- `extra_tokens` est ignoré lorsque la méthode `vsa` est sélectionnée. Un message est journalisé, car les poids VSA ont été entraînés selon leur schéma parcimonieux.
- La méthode `vsa` nécessite un modèle MiniMax-H3 ; tout autre modèle déclenche une erreur. Si le modèle ne possède pas les couches `to_gate_compress`, l'étape fine s'exécute sans la branche grossière et un avertissement est journalisé.
- `dense_blocks` est ignoré pour les modèles qui ne rapportent pas d'indices de blocs, ce qui est indiqué dans le journal lorsque `verbose` est activé.
- `sink_conditioning` s'applique uniquement aux modèles MiniMax-H3 qui rapportent une disposition correspondant à la longueur de séquence actuelle.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BlockSparseAttention/fr.md)

---
**Source fingerprint (SHA-256):** `0c34876b49a04db0ab265526e2bb5f784e150591aab631713ad2ab420a3327c4`
