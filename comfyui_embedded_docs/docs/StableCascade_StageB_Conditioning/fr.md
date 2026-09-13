# StableCascade_StageB_Conditioning

Le nœud StableCascade_StageB_Conditioning prépare les données de conditionnement pour la génération Stable Cascade Stage B en combinant les informations de conditionnement existantes avec la représentation latente préalable produite par Stage C. Il copie chaque entrée de conditionnement et y stocke les échantillons latents de Stage C, afin que les étapes de génération ultérieures puissent utiliser ces informations préalables pour obtenir des résultats plus cohérents.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `conditioning` | Les données de conditionnement à modifier avec les informations préalables de Stage C. Chaque entrée de la liste est copiée et se voit attribuer les échantillons de Stage C. | CONDITIONING | Oui | - |
| `stage_c` | La représentation latente issue de Stage C. Sa valeur `samples` est utilisée comme information préalable ajoutée au conditionnement. | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `CONDITIONING` | Les données de conditionnement modifiées avec les informations préalables de Stage C intégrées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/fr.md)

---
**Source fingerprint (SHA-256):** `3154457773465e5b93221b6d83d2064b565cb653403e12e88615652c7832d1e8`
