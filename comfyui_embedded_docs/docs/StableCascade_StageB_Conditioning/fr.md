> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/fr.md)

Le nœud **StableCascade_StageB_Conditioning** prépare les données de conditionnement pour la génération de l'étape B de Stable Cascade en combinant les informations de conditionnement existantes avec les représentations latentes préalables de l'étape C. Il modifie les données de conditionnement pour inclure les échantillons latents de l'étape C, permettant ainsi au processus de génération d'exploiter les informations préalables pour des résultats plus cohérents.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `conditionnement` | CONDITIONING | Oui | - | Les données de conditionnement à modifier avec les informations préalables de l'étape C |
| `stage_c` | LATENT | Oui | - | La représentation latente de l'étape C contenant les échantillons préalables pour le conditionnement |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement modifiées avec les informations préalables de l'étape C intégrées |

---
**Source fingerprint (SHA-256):** `f6ee524889aa324151a91c200fdc2692754cbd1348e32fbc05a26fd7ba27c755`
