> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/fr.md)

Le nœud Runway First-Last-Frame to Video génère des vidéos en chargeant des images clés de début et de fin accompagnées d'une invite textuelle. Il crée des transitions fluides entre les images de départ et de fin fournies en utilisant le modèle Gen-3 de Runway. Ceci est particulièrement utile pour les transitions complexes où l'image de fin diffère significativement de l'image de départ.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Invite textuelle pour la génération (par défaut : chaîne vide) |
| `start_frame` | IMAGE | Oui | N/A | Image de départ à utiliser pour la vidéo |
| `end_frame` | IMAGE | Oui | N/A | Image de fin à utiliser pour la vidéo. Pris en charge pour gen3a_turbo uniquement. |
| `duration` | COMBO | Oui | Plusieurs options disponibles | Sélection de la durée de la vidéo parmi les options Durée disponibles |
| `ratio` | COMBO | Oui | Plusieurs options disponibles | Sélection du format d'image parmi les options RunwayGen3aAspectRatio disponibles |
| `seed` | INT | Non | 0-4294967295 | Graine aléatoire pour la génération (par défaut : 0) |

**Contraintes des paramètres :**
- Le `prompt` doit contenir au moins 1 caractère
- `start_frame` et `end_frame` doivent avoir des dimensions maximales de 7999x7999 pixels
- `start_frame` et `end_frame` doivent avoir des formats d'image compris entre 0,5 et 2,0
- Le paramètre `end_frame` est uniquement pris en charge lors de l'utilisation du modèle gen3a_turbo

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée effectuant la transition entre les images de début et de fin |