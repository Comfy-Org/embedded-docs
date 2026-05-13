> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/fr.md)

Voici la traduction en français de la documentation du nœud WanTextToImageApi, en respectant vos règles :

Le nœud Wan Texte vers Image génère des images à partir de descriptions textuelles. Il utilise des modèles d'IA pour créer un contenu visuel à partir d'invites écrites, prenant en charge la saisie de texte en anglais et en chinois. Le nœud offre divers contrôles pour ajuster la taille, la qualité et les préférences de style de l'image de sortie.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | "wan2.5-t2i-preview" | Modèle à utiliser (par défaut : "wan2.5-t2i-preview") |
| `invite` | STRING | Oui | - | Invite décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois (par défaut : vide) |
| `invite négative` | STRING | Non | - | Invite négative décrivant ce qu'il faut éviter (par défaut : vide) |
| `largeur` | INT | Non | 768-1440 | Largeur de l'image en pixels (par défaut : 1024, pas : 32) |
| `hauteur` | INT | Non | 768-1440 | Hauteur de l'image en pixels (par défaut : 1024, pas : 32) |
| `graine` | INT | Non | 0-2147483647 | Graine à utiliser pour la génération (par défaut : 0) |
| `extension d'invite` | BOOLEAN | Non | - | Indique s'il faut enrichir l'invite avec l'assistance de l'IA (par défaut : True) |
| `filigrane` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane généré par l'IA au résultat (par défaut : False) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | IMAGE | L'image générée à partir de l'invite textuelle |

---
**Source fingerprint (SHA-256):** `2a59551d7ff0fc0553f41561afd94092d2d950ac3e1aa3f6402436540da7d6fb`
