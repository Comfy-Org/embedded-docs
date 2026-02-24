> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/fr.md)

Le nœud LTXV Image To Video génère une vidéo de qualité professionnelle à partir d'une seule image de départ. Il utilise une API externe pour créer une séquence vidéo basée sur votre prompt textuel, vous permettant de personnaliser la durée, la résolution et la fréquence d'images.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Première image à utiliser pour la vidéo. |
| `model` | COMBO | Oui | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"` | Le modèle d'IA à utiliser pour la génération vidéo. Le modèle "Fast" est optimisé pour la vitesse, tandis que le modèle "Quality" privilégie la fidélité visuelle. |
| `prompt` | STRING | Oui | - | Une description textuelle qui guide le contenu et le mouvement de la vidéo générée. |
| `duration` | COMBO | Oui | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | La longueur de la vidéo en secondes (par défaut : 8). |
| `resolution` | COMBO | Oui | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | La résolution de sortie de la vidéo générée. |
| `fps` | COMBO | Oui | `25`<br>`50` | Le nombre d'images par seconde pour la vidéo (par défaut : 25). |
| `generate_audio` | BOOLEAN | Non | - | Lorsque vrai, la vidéo générée inclura un audio généré par IA correspondant à la scène (par défaut : Faux). |

**Contraintes importantes :**

* L'entrée `image` doit contenir exactement une image.
* Le `prompt` doit comporter entre 1 et 10 000 caractères.
* Si vous sélectionnez une `duration` supérieure à 10 secondes, vous devez utiliser le modèle **"LTX-2 (Fast)"**, une résolution **"1920x1080"** et **25** FPS. Cette combinaison est requise pour les vidéos plus longues.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |
