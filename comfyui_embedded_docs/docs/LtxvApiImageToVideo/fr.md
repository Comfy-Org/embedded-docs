# LTXV Image vers Vidéo

Le nœud LTXV Image To Video génère une vidéo de qualité professionnelle à partir d'une seule image de départ. Il utilise une API externe pour créer une séquence vidéo basée sur votre invite textuelle, vous permettant de personnaliser la durée, la résolution et la fréquence d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Première image à utiliser pour la vidéo. | IMAGE | Oui | - |
| `modèle` | Le modèle d'IA à utiliser pour la génération vidéo. Le modèle "Fast" est optimisé pour la vitesse, tandis que le modèle "Quality" privilégie la fidélité visuelle. | COMBO | Oui | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"` |
| `prompt` | Une description textuelle qui guide le contenu et le mouvement de la vidéo générée. | STRING | Oui | - |
| `durée` | La durée de la vidéo en secondes (par défaut : 8). | COMBO | Oui | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `résolution` | La résolution de sortie de la vidéo générée. | COMBO | Oui | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `ips` | Le nombre d'images par seconde pour la vidéo (par défaut : 25). | COMBO | Oui | `25`<br>`50` |
| `générer_audio` | Lorsque cette option est activée, la vidéo générée inclura un son généré par IA correspondant à la scène (par défaut : Faux). | BOOLEAN | Non | - |

**Contraintes importantes :**

* L'entrée `image` doit contenir exactement une image.
* Le `prompt` doit contenir entre 1 et 10 000 caractères.
* Si vous sélectionnez une `duration` supérieure à 10 secondes, vous devez utiliser le modèle **"LTX-2 (Fast)"**, une résolution **"1920x1080"** et **25** FPS. Cette combinaison est requise pour les vidéos plus longues.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `af891b45997173c3210d3de4f7b6bd05b14e9d3bf8a94dcb2c1ce08038b7d99d`
