> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/fr.md)

Le nœud StableCascade_StageB_Conditioning prépare les données de conditionnement pour la génération du Stage B de Stable Cascade en combinant les informations de conditionnement existantes avec les représentations latentes antérieures du Stage C. Il modifie les données de conditionnement pour inclure les échantillons latents du Stage C, permettant au processus de génération de tirer parti des informations antérieures pour produire des résultats plus cohérents.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Oui | - | Les données de conditionnement à modifier avec les informations antérieures du Stage C |
| `stage_c` | LATENT | Oui | - | La représentation latente du Stage C contenant les échantillons antérieurs pour le conditionnement |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées avec les informations antérieures du Stage C intégrées |