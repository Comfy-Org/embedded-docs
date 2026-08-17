# GITSScheduler

Le nœud GITSScheduler génère le planning de sigmas (niveaux de bruit) utilisé par la méthode d'échantillonnage GITS. Il sélectionne une table de niveaux de bruit prédéfinie en fonction du paramètre `coeff` et du nombre de `steps`, en réduisant éventuellement le planning lorsqu'une valeur de `denoise` inférieure à 1.0 est utilisée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `coeff` | Le coefficient qui détermine quelle table de niveaux de bruit prédéfinie est utilisée pour construire le planning. La valeur est arrondie à 2 décimales (par défaut : 1,20) | FLOAT | Oui | 0.80 - 1.50 |
| `steps` | Le nombre total d'étapes d'échantillonnage pour lequel générer les sigmas (par défaut : 10) | INT | Oui | 2 - 1000 |
| `denoise` | Facteur de débruitage qui réduit le nombre d'étapes utilisées (par défaut : 1,0) | FLOAT | Oui | 0.0 - 1.0 |

**Remarque :** Lorsque `denoise` est défini sur 0.0, le nœud renvoie un tenseur vide. Lorsque `denoise` est inférieur à 1.0, le nombre réel d'étapes utilisées est calculé comme suit : `round(steps * denoise)`. Pour un nombre d'étapes allant jusqu'à 20, le nœud utilise directement les niveaux de bruit prédéfinis ; pour un nombre d'étapes supérieur à 20, il utilise une interpolation log-linéaire pour étendre les niveaux de bruit prédéfinis au nombre d'étapes souhaité.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `sigmas` | Les valeurs de sigma générées pour le planning de bruit | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
