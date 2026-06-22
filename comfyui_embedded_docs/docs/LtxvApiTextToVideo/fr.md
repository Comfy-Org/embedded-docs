# LTXV Texte vers Vidéo

Le nœud LTXV Texte vers Vidéo génère des vidéos de qualité professionnelle à partir d'une description textuelle. Il se connecte à une API externe pour créer des vidéos avec une durée, une résolution et une fréquence d'images personnalisables. Vous pouvez également choisir d'ajouter un son généré par IA à la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour la génération vidéo. Les modèles disponibles sont mappés à partir de la `MODELS_MAP` du code source. | COMBO | Oui | `"LTX-2 (Rapide)"`<br>`"LTX-2 (Qualité)"`<br>`"LTX-2 (Turbo)"` |
| `prompt` | La description textuelle que l'IA utilisera pour générer la vidéo. Ce champ prend en charge plusieurs lignes de texte. | STRING | Oui | - |
| `durée` | La durée de la vidéo générée en secondes (par défaut : 8). | COMBO | Oui | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `résolution` | Les dimensions en pixels (largeur x hauteur) de la vidéo de sortie. | COMBO | Oui | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `ips` | Le nombre d'images par seconde de la vidéo (par défaut : 25). | COMBO | Oui | `25`<br>`50` |
| `générer_audio` | Lorsqu'il est activé, la vidéo générée inclura un son généré par IA correspondant à la scène (par défaut : Faux). | BOOLEAN | Non | - |

**Contraintes importantes :**

* Le `prompt` doit contenir entre 1 et 10 000 caractères.
* Si vous sélectionnez une `duration` supérieure à 10 secondes, vous devez également utiliser le modèle `"LTX-2 (Rapide)"`, une résolution de `"1920x1080"` et un `fps` de `25`. Cette combinaison est requise pour les vidéos plus longues.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `a0c16995a07d879113bd3ca8fea64be414feee96bd8293a3e7737ede7d30e11d`
