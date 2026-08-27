# LTXV Dual CFG Guider

Ce nœud crée un objet d’échantillonnage guidé (guider CFG) pour les modèles LTXV-AV. Il applique une échelle de guidage distincte à la partie vidéo et à la partie audio du latent groupé, ce qui permet de contrôler indépendamment l’influence du conditionnement sur chaque modalité. Si les deux échelles sont égales, ou si le latent ne contient pas de composants vidéo et audio séparés, une échelle globale unique est utilisée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser lors de l’échantillonnage. | MODEL | Oui | - |
| `positif` | Conditionnement positif pour guider la génération vers la cible souhaitée. | CONDITIONING | Oui | - |
| `négatif` | Conditionnement négatif pour éloigner la génération de la cible indésirable. | CONDITIONING | Oui | - |
| `video_cfg` | Intensité du guidage appliquée à la modalité vidéo du latent (par défaut : 3.0). | FLOAT | Oui | 0.0 à 100.0 |
| `audio_cfg` | Intensité du guidage appliquée à la modalité audio du latent (par défaut : 7.0). | FLOAT | Oui | 0.0 à 100.0 |

Remarque : Lorsque `video_cfg` et `audio_cfg` sont égaux ou très proches en valeur, le guider utilise cette valeur comme échelle CFG unique pour l’ensemble du latent. Si le latent n’est pas un latent LTXV-AV groupé, seule la valeur de `video_cfg` est utilisée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `guider` | Le guider CFG configuré, à transmettre à un nœud d’échantillonnage. | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/fr.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
