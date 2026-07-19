# MoonvalleyImg2VideoNode

Voici la traduction en français de la documentation du nœud ComfyUI Moonvalley Marey Image to Video :

Le nœud Moonvalley Marey Image to Video transforme une image de référence en vidéo à l'aide de l'API Moonvalley. Il prend une image d'entrée et un texte d'invite pour générer une vidéo avec une résolution, des paramètres de qualité et des contrôles créatifs spécifiés. Le nœud gère l'ensemble du processus, du téléchargement de l'image à la génération et au téléchargement de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Image de référence utilisée pour générer la vidéo | IMAGE | Oui | - |
| `prompt` | Description textuelle pour la génération vidéo (saisie multiligne) | STRING | Oui | - |
| `negative_prompt` | Texte d'invite négative pour exclure les éléments indésirables (par défaut : liste étendue d'invites négatives) | STRING | Non | - |
| `resolution` | Résolution de la vidéo de sortie (par défaut : "16:9 (1920 x 1080)") | COMBO | Non | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" |
| `prompt_adherence` | Échelle de guidage pour le contrôle de la génération (par défaut : 4,5, pas : 1,0) | FLOAT | Non | 1.0 - 20.0 |
| `seed` | Valeur de graine aléatoire (par défaut : 9, contrôle après génération activé) | INT | Non | 0 - 4294967295 |
| `steps` | Nombre d'étapes de débruitage (par défaut : 33, pas : 1) | INT | Non | 1 - 100 |

**Contraintes :**

- L'image d'entrée doit avoir des dimensions comprises entre 300x300 pixels et la hauteur/largeur maximale autorisée
- La longueur du texte de l'invite et de l'invite négative est limitée à la longueur maximale d'invite de Moonvalley Marey

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée en sortie | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `674e69a7f106f6f961f10c179008b7bb1147bf0e569c72d207a105f3fab2aaf5`
