> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"`<br>`"LTX-2 (Turbo)"` | Le modèle d'IA à utiliser pour la génération de vidéo. Les modèles disponibles sont mappés depuis le `MODELS_MAP` du code source. |
| `prompt` | STRING | Oui | - | La description textuelle que l'IA utilisera pour générer la vidéo. Ce champ prend en charge plusieurs lignes de texte. |
| `duration` | COMBO | Oui | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | La durée de la vidéo générée en secondes (par défaut : 8). |
| `resolution` | COMBO | Oui | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | Les dimensions en pixels (largeur x hauteur) de la vidéo de sortie. |
| `fps` | COMBO | Oui | `25`<br>`50` | Le nombre d'images par seconde pour la vidéo (par défaut : 25). |
| `generate_audio` | BOOLEAN | Non | - | Lorsqu'activé, la vidéo générée inclura un audio généré par IA correspondant à la scène (par défaut : Faux). |

**Contraintes importantes :**

* Le `prompt` doit contenir entre 1 et 10 000 caractères.
* Si vous sélectionnez une `duration` supérieure à 10 secondes, vous devez également utiliser le modèle `"LTX-2 (Fast)"`, une résolution de `"1920x1080"` et un `fps` de `25`. Cette combinaison est requise pour les vidéos plus longues.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |
