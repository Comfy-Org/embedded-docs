# LTXV Image vers Vidéo

Le nœud **LTXV Image To Video** génère une vidéo de qualité professionnelle à partir d’une seule image de départ. Il utilise une API externe pour créer une séquence vidéo basée sur votre invite textuelle, vous permettant de personnaliser la durée, la résolution et la fréquence d’images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Première image à utiliser pour la vidéo. | IMAGE | Oui | - |
| `model` | Modèle d’IA à utiliser pour la génération vidéo. Le modèle « Pro » est optimisé pour la qualité, tandis que le modèle « Fast » est optimisé pour la vitesse. | COMBO | Oui | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Description textuelle qui guide le contenu et le mouvement de la vidéo générée. | STRING | Oui | - |
| `duration` | La durée de la vidéo en secondes (par défaut : 8). | COMBO | Oui | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | La résolution de sortie de la vidéo générée. | COMBO | Oui | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Le nombre d’images par seconde pour la vidéo (par défaut : 25). | COMBO | Oui | `25`<br>`50` |
| `generate_audio` | Lorsque cette option est activée (`true`), la vidéo générée inclura un fichier audio généré par l’IA correspondant à la scène (par défaut : `False`). | BOOLEAN | Non | - |

**Contraintes importantes :**

* L’entrée `image` doit contenir exactement une image.
* Le `prompt` doit contenir entre 1 et 10 000 caractères.
* Si vous sélectionnez une `duration` supérieure à 10 secondes, vous devez utiliser le modèle **"LTX-2 (Fast)"**, une résolution **"1920x1080"** et **25** FPS. Cette combinaison est requise pour les vidéos plus longues.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`
