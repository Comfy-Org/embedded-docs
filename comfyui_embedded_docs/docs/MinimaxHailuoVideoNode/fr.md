> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/fr.md)

Voici la traduction de la documentation du nœud ComfyUI **MinimaxHailuoVideoNode** :

Génère des vidéos à partir de descriptions textuelles en utilisant le modèle MiniMax Hailuo-02. Vous pouvez éventuellement fournir une image de départ comme première image pour créer une vidéo qui se poursuit à partir de cette image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `texte_prompt` | STRING | Oui | - | Description textuelle pour guider la génération vidéo. |
| `graine` | INT | Non | 0 à 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit (par défaut : 0). |
| `image_premiere_frame` | IMAGE | Non | - | Image facultative à utiliser comme première image pour générer une vidéo. |
| `optimiseur_prompt` | BOOLEAN | Non | - | Optimiser la description pour améliorer la qualité de génération si nécessaire (par défaut : True). |
| `durée` | COMBO | Non | `6`<br>`10` | La durée de la vidéo de sortie en secondes (par défaut : 6). |
| `résolution` | COMBO | Non | `"768P"`<br>`"1080P"` | Les dimensions de l'affichage vidéo. 1080p correspond à 1920x1080, 768p à 1366x768 (par défaut : "768P"). |

**Remarque :** Lors de l'utilisation du modèle MiniMax-Hailuo-02 avec une résolution 1080P, la durée est limitée à 6 secondes.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `5466b9cda979a30158b818743de0e0cf30eb3e27015d431eb04a370029250a4c`
