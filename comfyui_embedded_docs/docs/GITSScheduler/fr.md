# GITSScheduler

Le nœud GITSScheduler génère les sigmas du planning de bruit pour la méthode d’échantillonnage GITS (Generative Iterative Time Steps). Il calcule les valeurs sigma à partir d’un paramètre de coefficient et du nombre d’étapes, avec un facteur de débruitage optionnel qui peut réduire le nombre total d’étapes utilisées. Le nœud utilise des niveaux de bruit prédéfinis et une interpolation pour créer le planning de sigma final.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `coeff` | La valeur du coefficient qui contrôle la courbe du planning de bruit (défaut : 1.20). La valeur est arrondie à deux décimales et sélectionne la table de niveaux de bruit prédéfinie utilisée. | FLOAT | Oui | 0.80 - 1.50 (step 0.05) |
| `étapes` | Le nombre total d’étapes d’échantillonnage pour lesquelles générer les sigmas (défaut : 10) | INT | Oui | 2 - 1000 |
| `débruitage` | Facteur de débruitage qui réduit le nombre d’étapes utilisées (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

**Remarque :** Lorsque `denoise` est inférieur ou égal à 0.0, le nœud renvoie un tenseur vide. Lorsque `denoise` est inférieur à 1.0, le nombre réel d’étapes utilisées est calculé comme `round(steps * denoise)`, et seule la dernière partie correspondante du planning est conservée. Pour des étapes comprises entre 2 et 20, le nœud sélectionne un planning de bruit prédéfini correspondant. Pour plus de 20 étapes, le nœud utilise une interpolation log-linéaire pour étendre les niveaux de bruit prédéfinis au nombre d’étapes souhaité.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `sigmas` | Les valeurs sigma générées pour le planning de bruit. Pour N étapes, N+1 valeurs sigma sont renvoyées, et la dernière sigma est définie à 0. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
