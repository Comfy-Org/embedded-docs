> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/fr.md)

Le nœud Runway Image to Video (Gen4 Turbo) génère une vidéo à partir d'une seule image de départ en utilisant le modèle Gen4 Turbo de Runway. Il prend une invite textuelle et une image initiale, puis crée une séquence vidéo basée sur les paramètres de durée et de format d'image fournis. Le nœud gère le téléchargement de l'image de départ vers l'API de Runway et retourne la vidéo générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite textuelle pour la génération (par défaut : chaîne vide) |
| `start_frame` | IMAGE | Oui | - | Image de départ à utiliser pour la vidéo |
| `duration` | COMBO | Oui | Plusieurs options disponibles | Sélection de la durée de la vidéo parmi les options de durée disponibles |
| `ratio` | COMBO | Oui | Plusieurs options disponibles | Sélection du format d'image parmi les options de format Gen4 Turbo disponibles |
| `seed` | INT | Non | 0 à 4294967295 | Graine aléatoire pour la génération (par défaut : 0) |

**Contraintes des paramètres :**

- L'image `start_frame` doit avoir des dimensions ne dépassant pas 7999x7999 pixels
- L'image `start_frame` doit avoir un format d'image compris entre 0,5 et 2,0
- Le `prompt` doit contenir au moins un caractère

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée basée sur l'image d'entrée et l'invite |
