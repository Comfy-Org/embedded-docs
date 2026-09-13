# Remplissage génératif Bria

Ce nœud génère des objets ou des éléments de décor à l'intérieur d'une région masquée d'une image à l'aide de Bria. Il téléverse l'image et le masque, envoie le prompt au service de remplissage génératif de Bria, attend la fin de l'opération et renvoie l'image modifiée. Il s'agit d'une opération API payante (0,0429 $ US par requête).

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à modifier. | IMAGE | Oui | - |
| `mask` | Les zones blanches sont remplies avec le contenu généré, les zones noires sont préservées. Le masque est binarisé avant envoi avec un seuil de 50 % : seules les zones peintes à plus de 50 % d'opacité sont considérées comme blanches. Doit avoir le même rapport d'aspect que l'image. | MASK | Oui | - |
| `prompt` | Description de ce qu'il faut générer à l'intérieur de la région masquée. Doit contenir au moins 1 caractère. (par défaut : "") | STRING | Oui | - |
| `negative_prompt` | Un prompt décrivant le contenu à éviter dans le résultat généré. S'il est laissé vide, il n'est pas envoyé à l'API. (par défaut : "") | STRING | Oui | - |
| `refine_prompt` | Ajuste automatiquement le prompt pour de meilleurs résultats ; désactivez cette option pour utiliser le prompt exactement tel qu'il est écrit. (par défaut : true) | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour le processus de génération. (par défaut : 42) | INT | Oui | 1 à 2147483647 |
| `moderation` | Paramètres de modération. Lorsqu'ils sont définis sur "true", les options de modération ci-dessous sont appliquées. (par défaut : "false") | DYNAMIC_COMBO | Oui | "false"<br>"true" |

### Entrées de modération (lorsque `moderation` = "true")

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_content_moderation` | Applique la modération de contenu au prompt. (par défaut : false) | BOOLEAN | Non | true<br>false |
| `visual_input_moderation` | Applique la modération de contenu à l'image d'entrée. (par défaut : false) | BOOLEAN | Non | true<br>false |
| `visual_output_moderation` | Applique la modération de contenu à l'image de sortie. (par défaut : false) | BOOLEAN | Non | true<br>false |

**Remarque :** Le `prompt` ne doit pas être vide. Le `mask` doit avoir le même rapport d'aspect que l'`image`. Le masque est binarisé à 50 % d'opacité, donc les zones peintes à moins de la moitié d'opacité sont ignorées ; si le masque ne contient aucune zone blanche après binarisation, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image résultante avec la région masquée remplie par le contenu généré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/fr.md)

---
**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`
