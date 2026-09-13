# Wan Texte vers Image

Le nœud Wan Text to Image génère des images à partir de descriptions textuelles. Il utilise des modèles d'IA pour créer du contenu visuel à partir de prompts écrits, en prenant en charge les saisies en anglais et en chinois. Le nœud offre divers contrôles pour ajuster la taille, la qualité et les préférences de style de l'image de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser (par défaut : "wan2.5-t2i-preview") | STRING | Oui | "wan2.5-t2i-preview" |
| `prompt` | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois (par défaut : vide) | STRING | Oui | - |
| `negative_prompt` | Prompt négatif décrivant ce qu'il faut éviter (par défaut : vide) | STRING | Non | - |
| `width` | Largeur de l'image en pixels (par défaut : 1024, pas : 32) | INT | Non | 768-1440 |
| `height` | Hauteur de l'image en pixels (par défaut : 1024, pas : 32) | INT | Non | 768-1440 |
| `seed` | Graine à utiliser pour la génération (par défaut : 0) | INT | Non | 0-2147483647 |
| `prompt_extend` | Indique s'il faut améliorer le prompt avec l'assistance de l'IA (par défaut : True) | BOOLEAN | Non | - |
| `watermark` | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : False) | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | L'image générée à partir du prompt textuel | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `208b7c839da45316aeb1a14a3e9d176eeb09b2f931f764fb8a296da15ae3bd4e`
