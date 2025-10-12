> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/fr.md)

Le nœud Runway Image to Video (Gen3a Turbo) génère une vidéo à partir d'une seule image de départ en utilisant le modèle Gen3a Turbo de Runway. Il prend une invite textuelle et une image initiale, puis crée une séquence vidéo basée sur la durée et le format d'image spécifiés. Ce nœud se connecte à l'API de Runway pour traiter la génération à distance.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite textuelle pour la génération (par défaut : "") |
| `start_frame` | IMAGE | Oui | N/A | Image de départ à utiliser pour la vidéo |
| `duration` | COMBO | Oui | Plusieurs options disponibles | Sélection de la durée de la vidéo parmi les options disponibles |
| `ratio` | COMBO | Oui | Plusieurs options disponibles | Sélection du format d'image parmi les options disponibles |
| `seed` | INT | Non | 0-4294967295 | Graine aléatoire pour la génération (par défaut : 0) |

**Contraintes des paramètres :**
- La `start_frame` doit avoir des dimensions ne dépassant pas 7999x7999 pixels
- La `start_frame` doit avoir un format d'image compris entre 0,5 et 2,0
- Le `prompt` doit contenir au moins un caractère (ne peut pas être vide)

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La séquence vidéo générée |