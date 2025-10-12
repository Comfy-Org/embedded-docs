> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/fr.md)

Le nœud Moonvalley Marey Image to Video transforme une image de référence en vidéo en utilisant l'API Moonvalley. Il prend une image d'entrée et une invite textuelle pour générer une vidéo avec une résolution, des paramètres de qualité et des contrôles créatifs spécifiés. Le nœud gère l'intégralité du processus, du téléchargement de l'image à la génération et au téléchargement de la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image de référence utilisée pour générer la vidéo |
| `prompt` | STRING | Oui | - | Description textuelle pour la génération de vidéo (saisie multiligne) |
| `negative_prompt` | STRING | Non | - | Invite négative pour exclure les éléments indésirables (par défaut : liste étendue d'invites négatives) |
| `resolution` | COMBO | Non | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" | Résolution de la vidéo de sortie (par défaut : "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | Non | 1.0 - 20.0 | Échelle de guidage pour le contrôle de la génération (par défaut : 4.5, pas : 1.0) |
| `seed` | INT | Non | 0 - 4294967295 | Valeur de seed aléatoire (par défaut : 9, contrôle après génération activé) |
| `steps` | INT | Non | 1 - 100 | Nombre d'étapes de débruitage (par défaut : 33, pas : 1) |

**Contraintes :**
- L'image d'entrée doit avoir des dimensions comprises entre 300x300 pixels et la hauteur/largeur maximale autorisée
- La longueur du texte de l'invite et de l'invite négative est limitée à la longueur maximale d'invite de Moonvalley Marey

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée en sortie |