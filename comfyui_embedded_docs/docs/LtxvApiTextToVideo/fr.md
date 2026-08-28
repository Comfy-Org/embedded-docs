# LTXV Texte vers Vidéo

Le nœud LTXV Text To Video génère des vidéos de qualité professionnelle à partir d'une description textuelle. Il se connecte à une API externe pour créer des vidéos avec une durée, une résolution et un taux d'images par seconde personnalisables. Vous pouvez également choisir d'ajouter un audio généré par IA à la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour la génération de vidéos. « LTX-2 (Pro) » offre une qualité supérieure, tandis que « LTX-2 (Fast) » est optimisé pour la vitesse. | COMBO | Oui | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | La description textuelle que l'IA utilisera pour générer la vidéo. Ce champ prend en charge plusieurs lignes de texte et doit contenir de 1 à 10 000 caractères. | STRING | Oui | - |
| `durée` | La durée de la vidéo générée en secondes (défaut : 8). | COMBO | Oui | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `résolution` | Les dimensions en pixels (largeur x hauteur) de la vidéo de sortie. | COMBO | Oui | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `ips` | Le nombre d'images par seconde pour la vidéo (défaut : 25). | COMBO | Oui | `25`<br>`50` |
| `générer_audio` | Lorsque true, la vidéo générée inclura un audio généré par IA correspondant à la scène (défaut : False). Il s'agit d'un paramètre facultatif avancé. | BOOLEAN | Non | - |

**Contraintes importantes :**

* Le `prompt` doit contenir entre 1 et 10 000 caractères.
* Si vous sélectionnez une `duration` supérieure à 10 secondes, vous devez également utiliser le modèle `"LTX-2 (Fast)"`, une résolution de `"1920x1080"` et un `fps` de `25`. Cette combinaison est requise pour les vidéos plus longues.

**Remarque :** Ce nœud est obsolète.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`
