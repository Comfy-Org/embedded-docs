# MiniMax Hailuo Vidéo

Voici la traduction de la documentation du nœud ComfyUI **MinimaxHailuoVideoNode** :

Génère des vidéos à partir de descriptions textuelles en utilisant le modèle MiniMax Hailuo-02. Vous pouvez éventuellement fournir une image de départ comme première image pour créer une vidéo qui se poursuit à partir de cette image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `texte_prompt` | Description textuelle pour guider la génération vidéo. | STRING | Oui | - |
| `graine` | La graine aléatoire utilisée pour créer le bruit (par défaut : 0). | INT | Non | 0 à 18446744073709551615 |
| `image_premiere_frame` | Image facultative à utiliser comme première image pour générer une vidéo. | IMAGE | Non | - |
| `optimiseur_prompt` | Optimiser la description pour améliorer la qualité de génération si nécessaire (par défaut : True). | BOOLEAN | Non | - |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut : 6). | COMBO | Non | `6`<br>`10` |
| `résolution` | Les dimensions de l'affichage vidéo. 1080p correspond à 1920x1080, 768p à 1366x768 (par défaut : "768P"). | COMBO | Non | `"768P"`<br>`"1080P"` |

**Remarque :** Lors de l'utilisation du modèle MiniMax-Hailuo-02 avec une résolution 1080P, la durée est limitée à 6 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `5466b9cda979a30158b818743de0e0cf30eb3e27015d431eb04a370029250a4c`
