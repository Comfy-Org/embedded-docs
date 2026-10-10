# Quiver Text to SVG

Générez un graphique vectoriel évolutif (SVG) à partir d'une invite textuelle avec Quiver AI. Des images de référence et des instructions de style facultatives peuvent guider la génération.

La sélection d'un `model` révèle les paramètres spécifiques au modèle listés ci-dessous, et le nombre maximal d'images de référence dépend également du modèle sélectionné.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération SVG. | DYNAMIC_COMBO | Oui | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `prompt` | Description textuelle de la sortie SVG souhaitée. Doit contenir au moins un caractère (par défaut : vide). | STRING | Oui | Tout texte |
| `instructions` | Conseils supplémentaires de style ou de formatage. Paramètre avancé facultatif (par défaut : vide). | STRING | Non | Tout texte |
| `reference_images` | Emplacement extensible : connectez une ou plusieurs images de référence facultatives (`ref_1`, `ref_2`, ...) qui guident la génération. Le nombre maximal d'images dépend du modèle sélectionné. | IMAGE | Non | Jusqu'à 14<br>Jusqu'à 4 |
| `width` | Largeur du canevas SVG de sortie (viewBox), en unités utilisateur. Définissez à la fois `width` et `height` pour contrôler la taille et le rapport d'aspect de la sortie ; laissez l'un ou l'autre à 0 pour laisser le modèle choisir, ce qui donne généralement un canevas carré. Paramètre avancé (par défaut : 0). | INT | Oui | 0 à 8192 |
| `height` | Hauteur du canevas SVG de sortie (viewBox), en unités utilisateur. Définissez à la fois `width` et `height` pour contrôler la taille et le rapport d'aspect de la sortie ; laissez l'un ou l'autre à 0 pour laisser le modèle choisir, ce qui donne généralement un canevas carré. Paramètre avancé (par défaut : 0). | INT | Oui | 0 à 8192 |
| `seed` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la valeur de la graine. Ce paramètre dispose de la fonctionnalité « contrôle après génération » (par défaut : 42). | INT | Oui | 0 à 2147483647 |

### Entrées spécifiques au modèle

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reasoning_effort` | Quantité de raisonnement que le modèle effectue avant de dessiner. Des niveaux plus élevés améliorent les détails et coûtent plus de jetons. Utilisé uniquement par les modèles `"arrow-2"` et `"arrow-2-telos"` (par défaut : `"high"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Contrôle de l'aléatoire. Des valeurs plus élevées augmentent l'aléatoire. Non utilisé par le modèle `"arrow-2-telos"`. Paramètre avancé (par défaut : 1.0). | FLOAT | Oui | 0.0 à 2.0 (pas de 0.1) |
| `top_p` | Paramètre d'échantillonnage nucleus. Non utilisé par le modèle `"arrow-2-telos"`. Paramètre avancé (par défaut : 1.0). | FLOAT | Oui | 0.05 à 1.0 (pas de 0.05) |
| `presence_penalty` | Pénalité de présence des jetons. Non utilisé par le modèle `"arrow-2-telos"`. Paramètre avancé (par défaut : 0.0). | FLOAT | Oui | -2.0 à 2.0 (pas de 0.1) |

**Remarque :** Le nombre maximal de `reference_images` est de 14 pour `"arrow-2"`, `"arrow-2-telos"` et `"arrow-1.1-max"`, et de 4 pour `"arrow-1.1"` et `"arrow-preview"`. Laissez `width` ou `height` à 0 pour laisser le modèle choisir la taille du canevas.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SVG` | La sortie SVG générée. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverTextToSVGNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `809d2e5bd62386723e36b7649af2f8dda40b437dc39bac9236529db5b52d32e9`
