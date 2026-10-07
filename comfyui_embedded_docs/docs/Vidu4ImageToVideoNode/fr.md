# Vidu Q4 Image-to-Video Generation

Générez une vidéo à partir d'une image de départ et d'un prompt facultatif avec un modèle Vidu Q4. La sortie conserve le rapport d'aspect de l'image d'entrée.

La sélection d'un `model` révèle les paramètres spécifiques à ce modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image de départ de la vidéo générée. Le rapport d'aspect doit être compris entre 1:5 et 5:1. | IMAGE | Oui | N/A |
| `model` | Modèle à utiliser pour la génération de vidéo. La sélection d'un modèle révèle les paramètres qui lui sont spécifiques : `prompt`, `resolution`, `duration`, `audio` et `seed`. | DYNAMIC_COMBO | Oui | `"Vidu Q4 Preview"` |
| `prompt` | Prompt textuel facultatif pour la génération de vidéo, jusqu'à 5000 caractères (par défaut : vide). | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie (par défaut : `"720p"`). | COMBO | Oui | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"2K"`<br>`"4K"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 3 à 16 |
| `audio` | Lorsque cette option est activée, produit une vidéo avec du son, y compris les dialogues et les effets sonores (par défaut : True). | BOOLEAN | Oui | `True`<br>`False` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Ce paramètre dispose de la fonctionnalité « control after generate » (par défaut : 42). | INT | Oui | 1 à 2147483647 |

**Remarque :** le rapport d'aspect de `image` doit rester compris entre 1:5 et 5:1, et le `prompt` ne peut pas dépasser 5000 caractères. Le résultat conserve le rapport d'aspect de l'image d'entrée, de sorte que la taille de sortie ne suit le paramètre `resolution` que dans les limites de ce rapport.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu4ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `8778696edbdfb821afaa99dcba09cbebff57fd4cd2378273e82ad9fb18600b62`
