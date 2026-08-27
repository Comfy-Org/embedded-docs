# BriaGenFill

Ce nœud génère des objets ou des décors dans une région masquée d'une image à l'aide de l'API Bria. Il télécharge l'image et le masque, envoie le prompt au service de remplissage génératif Bria, attend la fin de l'opération, puis renvoie l'image modifiée. Cette opération d'API est payante (0,0429 $US par requête).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à modifier. | IMAGE | Oui | - |
| `masque` | Les zones blanches sont remplies avec le contenu généré, les zones noires sont préservées. Le masque est binarisé avant l'envoi, donc les zones partiellement peintes sont considérées comme blanches. Il doit avoir le même rapport hauteur-largeur que l'image. | MASK | Oui | - |
| `texte d’invite` | Description de ce qui doit être généré dans la région masquée. Doit contenir au moins 1 caractère. (défaut : "") | STRING | Oui | - |
| `negative_prompt` | Un prompt décrivant le contenu à éviter dans le résultat généré. S'il est laissé vide, il n'est pas envoyé à l'API. (défaut : "") | STRING | Oui | - |
| `refine_prompt` | Ajuste automatiquement le prompt pour de meilleurs résultats ; désactivez pour utiliser le prompt exactement tel qu'il a été écrit. (défaut : true) | BOOLEAN | Oui | true<br>false |
| `graine` | Graine (seed) pour le processus de génération. (défaut : 42) | INT | Oui | 1 à 2147483647 |
| `moderation` | Paramètres de modération. Lorsqu'ils sont définis sur "true", les options de modération ci-dessous sont appliquées. (défaut : "false") | DYNAMIC_COMBO | Oui | "false"<br>"true" |

### Entrées de modération (lorsque `moderation` = "true")

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_content_moderation` | Applique une modération de contenu au prompt. (défaut : false) | BOOLEAN | Non | true<br>false |
| `visual_input_moderation` | Applique une modération de contenu à l'image d'entrée. (défaut : false) | BOOLEAN | Non | true<br>false |
| `visual_output_moderation` | Applique une modération de contenu à l'image de sortie. (défaut : false) | BOOLEAN | Non | true<br>false |

**Remarque :** Le `prompt` ne doit pas être vide. Le `mask` doit avoir le même rapport hauteur-largeur que l'`image`. Le masque est binarisé à 50 % d'opacité, donc les zones peintes à moins de la moitié de l'opacité sont ignorées ; si le masque ne contient aucune zone blanche après la binarisation, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image résultante avec la région masquée remplie par le contenu généré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/fr.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
