# MiniMax Hailuo Vidéo

Génère des vidéos à partir de prompts textuels à l'aide du modèle MiniMax Hailuo-02. Vous pouvez éventuellement fournir une image de départ comme première image pour créer une vidéo qui se poursuit à partir de cette image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt_text` | Prompt textuel pour guider la génération de la vidéo. | STRING | Oui | - |
| `seed` | La graine aléatoire utilisée pour créer le bruit (par défaut : 0). | INT | Non | 0 à 18446744073709551615 |
| `first_frame_image` | Image facultative à utiliser comme première image pour générer une vidéo. | IMAGE | Non | - |
| `prompt_optimizer` | Optimiser le prompt pour améliorer la qualité de génération si nécessaire (par défaut : True). | BOOLEAN | Non | - |
| `duration` | La durée de la vidéo de sortie en secondes (par défaut : 6). | COMBO | Non | `6`<br>`10` |
| `resolution` | Les dimensions de l'affichage de la vidéo. La 1080p correspond à 1920x1080, la 768p à 1366x768 (par défaut : "768P"). | COMBO | Non | `"768P"`<br>`"1080P"` |

**Remarques :**
- `prompt_text` doit être une chaîne non vide lorsqu'aucun `first_frame_image` n'est fourni.
- Lors de l'utilisation du modèle MiniMax-Hailuo-02 avec une résolution 1080P, la durée est limitée à 6 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
