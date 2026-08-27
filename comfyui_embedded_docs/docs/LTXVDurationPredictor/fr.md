# LTXVDurationPredictor

```markdown
Ce nœud prédit la durée naturelle d'un plan pour un prompt à l'aide d'une tête de durée LTX 2.4. Il convertit la durée prédite en un nombre d'images qui correspond à la grille d'images du VAE, en utilisant la cadence et les limites de durée minimale/maximale fournies.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle utilisé pour prétraiter les plongements de texte et exécuter la tête de durée. | MODEL | Oui | N/A |
| `positif` | Le conditionnement qui fournit les plongements de texte du prompt et les métadonnées pour la prédiction de durée. | CONDITIONING | Oui | N/A |
| `duration_head` | Tête de durée LTX 2.4 chargée avec ModelPatchLoader. Doit être une tête de durée LTX. | MODEL_PATCH | Oui | N/A |
| `taux d’images` | Cadence en images par seconde utilisée pour convertir les secondes en images (défaut : 24.0). | FLOAT | Oui | 1.0 à 120.0 |
| `secondes_min` | Durée minimale en secondes utilisée lors de la conversion de la prédiction en nombre d'images (défaut : 1.0). | FLOAT | Oui | 0.5 à 120.0 |
| `secondes_max` | Durée maximale en secondes utilisée lors de la conversion de la prédiction en nombre d'images (défaut : 20.0). | FLOAT | Oui | 0.5 à 120.0 |

Note : L'entrée `duration_head` doit être une tête de durée LTX 2.4 chargée avec ModelPatchLoader. Si le patch de modèle connecté n'est pas une tête de durée LTX, le nœud lève une ValueError.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `nombre_de_frames` | La durée prédite convertie en nombre d'images et ajustée à la grille d'images 8k+1 du VAE. | INT |
| `secondes` | Durée prédite brute (non écrêtée). Il s'agit de la valeur avant l'ajustement à la grille d'images. | FLOAT |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/fr.md)

---
**Source fingerprint (SHA-256):** `ebbf6a2601a955122ab9862142aa475524c1f38403f4ef8dc9ffee6456ee8ce5`
