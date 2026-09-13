# Augmenter la résolution avec Bria

Bria Increase Resolution augmente la résolution d'une image d'entrée par 2x ou 4x à l'aide du service d'agrandissement d'image de Bria, tout en préservant le contenu original. Le nœud téléverse l'image, la soumet au traitement sur le service Bria, attend le résultat, puis renvoie l'image dont la résolution a été augmentée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à agrandir. | IMAGE | Oui | Single image |
| `desired_increase` | Multiplicateur de résolution. La sortie doit tenir dans une limite de 8192 pixels de chaque côté. | COMBO | Oui | "2"<br>"4" |
| `auto_downscale` | Abaisse automatiquement le multiplicateur et réduit l'échelle de l'image d'entrée si cela ne suffit toujours pas, lorsque la sortie dépasserait la limite. (par défaut : False) | BOOLEAN | Oui | True<br>False |
| `moderation` | Paramètres de modération. Lorsqu'il est défini sur "true", active les sous-options `visual_input_moderation` et `visual_output_moderation`, toutes deux définies sur False par défaut. | DYNAMIC_COMBO | Oui | "false"<br>"true" |

Remarques :
- Lorsque `moderation` est défini sur "true", les sous-options `visual_input_moderation` et `visual_output_moderation` deviennent disponibles, toutes deux définies sur False par défaut. Elles contrôlent la modération du contenu de l'image d'entrée et de l'image de sortie.
- Le nœud impose une taille maximale de 8192 pixels sur le côté de sortie. Si le multiplicateur sélectionné devait dépasser cette limite et que `auto_downscale` est désactivé, une erreur est levée. Activer `auto_downscale` permet au nœud d'utiliser automatiquement un multiplicateur inférieur ou de réduire l'échelle de l'image d'entrée à la place.
- Bria agrandit d'abord le côté court de l'image d'entrée à au moins 224 pixels avant l'agrandissement. Les images trop allongées peuvent déclencher une erreur demandant de les recadrer sur une forme plus carrée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image agrandie renvoyée par le service Bria. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/fr.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
