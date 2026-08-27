# BriaIncreaseResolution

Bria Increase Resolution agrandit une image d'entrée par un facteur 2 ou 4 en utilisant le service d'agrandissement d'image de Bria, en préservant le contenu d'origine. Il télécharge l'image, la traite sur le service Bria et renvoie le résultat agrandi sous forme d'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à agrandir. | IMAGE | Oui | Image unique |
| `desired_increase` | Multiplicateur de résolution. La sortie doit tenir dans 8192 pixels de chaque côté. | COMBO | Oui | "2"<br>"4" |
| `auto_downscale` | Réduit automatiquement le multiplicateur, et réduit la résolution de l'image d'entrée si cela ne suffit toujours pas, lorsque la sortie dépasserait la limite. (défaut : False) | BOOLEAN | Oui | True<br>False |
| `moderation` | Paramètres de modération. Lorsqu'elle est réglée sur « true », active les sous-options `visual_input_moderation` et `visual_output_moderation`, toutes deux définies par défaut sur False. | DYNAMIC_COMBO | Oui | "false"<br>"true" |

Remarques :
- Lorsque `moderation` est définie sur « true », les sous-options `visual_input_moderation` et `visual_output_moderation` deviennent disponibles, toutes deux définies par défaut sur False. Elles contrôlent la modération de l'image d'entrée et du contenu de l'image de sortie.
- Le nœud impose une taille maximale de 8192 pixels pour la sortie. Si le multiplicateur sélectionné dépasse cette limite et que `auto_downscale` est désactivé, une erreur est levée. L'activation de `auto_downscale` permet au nœud d'utiliser automatiquement un multiplicateur inférieur ou de réduire la résolution de l'image d'entrée à la place.
- Bria agrandit d'abord le petit côté de l'image d'entrée à au moins 224 pixels avant l'agrandissement. Les images trop allongées peuvent déclencher une erreur demandant de les recadrer pour obtenir une forme plus carrée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image agrandie renvoyée par l'API Bria. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/fr.md)

---
**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`
