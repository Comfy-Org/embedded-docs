# BriaIncreaseResolution

Bria Increase Resolution agrandit une image d'entrée par 2x ou 4x en utilisant l'API d'agrandissement d'image de Bria, en préservant le contenu d'origine. Il téléverse l'image, la traite sur le service Bria, puis renvoie le résultat agrandi sous forme d'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à agrandir. | IMAGE | Oui | Single image |
| `desired_increase` | Multiplicateur de résolution. La sortie doit tenir dans 8192 pixels de chaque côté. | COMBO | Oui | "2"<br>"4" |
| `auto_downscale` | Réduit automatiquement le multiplicateur, et réduit l'image d'entrée si cela ne suffit toujours pas, lorsque la sortie dépasserait la limite. (par défaut : False) | BOOLEAN | Oui | True<br>False |
| `moderation` | Paramètres de modération. Lorsqu'elle est définie sur "true", active les sous-options `visual_input_moderation` et `visual_output_moderation`, dont la valeur par défaut est False. | DYNAMIC_COMBO | Oui | "false"<br>"true" |

Remarques :
- Le nœud impose une taille maximale de 8192 pixels pour le côté de sortie. Si le multiplicateur sélectionné dépasse cette limite et que `auto_downscale` est désactivé, une erreur est générée. L'activation de `auto_downscale` permet au nœud d'utiliser automatiquement un multiplicateur inférieur ou de réduire l'image d'entrée à la place.
- Bria agrandit d'abord le petit côté de l'image d'entrée à au moins 224 pixels avant l'agrandissement. Les images trop allongées peuvent déclencher une erreur demandant de les recadrer pour obtenir une forme plus carrée.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `IMAGE` | L'image agrandie renvoyée par l'API Bria. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/fr.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
