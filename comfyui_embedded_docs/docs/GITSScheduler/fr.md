# GITSScheduler

Le nœud GITSScheduler génère des sigmas de planification du bruit pour la méthode d’échantillonnage GITS (Generative Iterative Time Steps). Il calcule les valeurs sigma à partir d’un paramètre de coefficient et du nombre d’étapes, avec un facteur de débruitage qui peut réduire le nombre total d’étapes utilisées. Le nœud utilise des niveaux de bruit prédéfinis et une interpolation pour créer la planification finale des sigmas.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `coeff` | Paramètre avancé. Valeur du coefficient qui contrôle la courbe de planification du bruit (par défaut : 1.20). La valeur est arrondie à deux décimales et détermine quelle table de niveaux de bruit prédéfinis est utilisée. | FLOAT | Oui | 0.80 - 1.50 (pas 0.05) |
| `steps` | Nombre total d’étapes d’échantillonnage pour lesquelles générer des sigmas (par défaut : 10). | INT | Oui | 2 - 1000 |
| `denoise` | Facteur de débruitage qui réduit le nombre d’étapes utilisées (par défaut : 1.0). | FLOAT | Oui | 0.0 - 1.0 (pas 0.01) |

**Remarque :** Lorsque `denoise` est inférieur ou égal à 0.0, le nœud renvoie un tenseur vide. Lorsque `denoise` est inférieur à 1.0, le nombre réel d’étapes utilisées est calculé par `round(steps * denoise)`, et seule la dernière partie correspondante de la planification est conservée. Pour des étapes comprises entre 2 et 20, le nœud sélectionne une planification de bruit prédéfinie correspondante. Pour des étapes supérieures à 20, le nœud utilise une interpolation log-linéaire pour étendre les niveaux de bruit prédéfinis au nombre d’étapes souhaité.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `sigmas` | Valeurs sigma générées pour la planification du bruit. Pour N étapes d’échantillonnage, N+1 valeurs sigma sont renvoyées, et le dernier sigma est défini à 0. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
