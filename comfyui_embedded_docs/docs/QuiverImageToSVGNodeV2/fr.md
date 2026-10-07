# Quiver Image to SVG

Vectorisez une image matricielle en un graphique vectoriel évolutif (SVG) avec Quiver AI. L’image est envoyée à l’API de Quiver AI, qui renvoie le résultat vectorisé.

La sélection d’un `model` affiche les paramètres spécifiques au modèle listés ci-dessous.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la vectorisation SVG. | DYNAMIC_COMBO | Oui | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `image` | Image d’entrée à vectoriser. | IMAGE | Oui | N/A |
| `auto_crop` | Recadre automatiquement sur le sujet dominant. Paramètre avancé (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |
| `target_size` | Redimensionnement carré appliqué à l’image d’entrée avant la vectorisation, en pixels, de 128 à 4096. 0 conserve la taille source, ce qui donne une vectorisation plus propre que de forcer un redimensionnement. Cela ne définit pas le canevas de sortie ; utilisez `width` et `height` pour cela. Paramètre avancé (par défaut : 0). | INT | Oui | 0 à 4096 |
| `width` | Largeur du canevas SVG de sortie (viewBox), en unités utilisateur. Définissez à la fois `width` et `height` pour contrôler la taille et le rapport d’aspect de sortie ; laissez l’un ou l’autre à 0 pour laisser le modèle choisir, ce qui donne généralement un canevas carré. Paramètre avancé (par défaut : 0). | INT | Oui | 0 à 8192 |
| `height` | Hauteur du canevas SVG de sortie (viewBox), en unités utilisateur. Définissez à la fois `width` et `height` pour contrôler la taille et le rapport d’aspect de sortie ; laissez l’un ou l’autre à 0 pour laisser le modèle choisir, ce qui donne généralement un canevas carré. Paramètre avancé (par défaut : 0). | INT | Oui | 0 à 8192 |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la valeur de la graine. Ce paramètre dispose de la fonctionnalité « control after generate » (par défaut : 42). | INT | Oui | 0 à 2147483647 |

### Entrées spécifiques au modèle

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reasoning_effort` | Quantité de raisonnement que le modèle effectue avant de dessiner. Des niveaux plus élevés améliorent les détails et consomment plus de tokens. Utilisé uniquement par les modèles `"arrow-2"` et `"arrow-2-telos"` (par défaut : `"high"`). | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |
| `temperature` | Contrôle de l’aléatoire. Des valeurs plus élevées augmentent l’aléatoire. Non utilisé par le modèle `"arrow-2-telos"`. Paramètre avancé (par défaut : 1.0). | FLOAT | Oui | 0.0 à 2.0 (pas 0.1) |
| `top_p` | Paramètre d’échantillonnage nucleus. Non utilisé par le modèle `"arrow-2-telos"`. Paramètre avancé (par défaut : 1.0). | FLOAT | Oui | 0.05 à 1.0 (pas 0.05) |
| `presence_penalty` | Pénalité de présence de token. Non utilisée par le modèle `"arrow-2-telos"`. Paramètre avancé (par défaut : 0.0). | FLOAT | Oui | -2.0 à 2.0 (pas 0.1) |

**Remarque :** `target_size` est appliqué avant la vectorisation et ne change pas le canevas de sortie. Laissez `width` ou `height` à 0 pour laisser le modèle choisir la taille du canevas.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SVG` | La sortie SVG vectorisée. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNodeV2/fr.md)

---
**Source fingerprint (SHA-256):** `186769b09bef2d2dbbfc26102f375ff80f8b324a24cd593da20afcea9cc2095b`
