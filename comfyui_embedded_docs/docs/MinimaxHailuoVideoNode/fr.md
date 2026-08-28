# MiniMax Hailuo Vidéo

Génère des vidéos à partir de prompts textuels à l'aide du modèle MiniMax Hailuo-02. Vous pouvez éventuellement fournir une image de départ comme première image pour créer une vidéo qui continue à partir de cette image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `texte_prompt` | Prompt textuel pour guider la génération de la vidéo. | STRING | Oui | - |
| `graine` | Graine aléatoire utilisée pour créer le bruit (défaut : 0). | INT | Non | 0 à 18446744073709551615 |
| `image_premiere_frame` | Image facultative à utiliser comme première image pour générer une vidéo. | IMAGE | Non | - |
| `optimiseur_prompt` | Optimise le prompt pour améliorer la qualité de génération si nécessaire (défaut : True). | BOOLEAN | Non | True<br>False |
| `durée` | Durée de la vidéo de sortie en secondes (défaut : 6). | COMBO | Non | 6<br>10 |
| `résolution` | Dimensions de l'affichage vidéo. Le 1080p correspond à 1920x1080, le 768p à 1366x768 (défaut : « 768P »). | COMBO | Non | « 768P »<br>« 1080P » |

**Remarque :** Lorsque `resolution` est défini sur « 1080P », `duration` est limité à 6 secondes. Lorsque `first_frame_image` n'est pas fournie, `prompt_text` ne doit pas être vide.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
