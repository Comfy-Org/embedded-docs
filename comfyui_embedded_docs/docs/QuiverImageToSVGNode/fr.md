# Quiver Image vers SVG

Ce nœud convertit une image matricielle en une image vectorielle SVG à l'aide des modèles de vectorisation de Quiver AI. Il envoie l'image à une API externe qui la traite et renvoie le résultat vectorisé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image d'entrée à vectoriser. | IMAGE | Oui | N/A |
| `auto_crop` | Recadre automatiquement sur le sujet dominant (par défaut : False). | BOOLEAN | Oui | True<br>False |
| `model` | Modèle à utiliser pour la vectorisation SVG. La sélection d'un modèle révèle des paramètres supplémentaires propres à ce modèle : `target_size` (cible de redimensionnement carrée en pixels ; 0 conserve la taille de l'image source, sinon 128 à 4096), `temperature`, `top_p` et `presence_penalty`. | DYNAMIC_COMBO | Oui | `"arrow-2"`<br>`"arrow-2-telos"`<br>`"arrow-1.1"`<br>`"arrow-1.1-max"`<br>`"arrow-preview"` |
| `seed` | Graine servant à déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la valeur de la graine. Ce paramètre dispose de la fonctionnalité « contrôle après génération » (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `effort de raisonnement` | Quantité de raisonnement que le modèle consacre avant de dessiner. Des niveaux plus élevés améliorent les détails et consomment plus de tokens. Utilisé uniquement par les modèles Arrow 2 (par défaut : "high"). | COMBO | Non | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `SVG` | La sortie SVG vectorisée. | SVG |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuiverImageToSVGNode/fr.md)

---
**Source fingerprint (SHA-256):** `d32225207ede8f15fd54780778c6b23b1ce1880be8cb416c341e73afbd9b8aa0`
