> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/fr.md)

Ce nœud utilise l'API Seedance 2.0 de ByteDance pour générer une vidéo à partir d'une description textuelle. Il envoie votre prompt au modèle sélectionné, attend que la vidéo soit traitée et renvoie le résultat final.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | Le modèle à utiliser pour la génération vidéo. La sélection d'un modèle révélera des entrées supplémentaires requises pour le prompt, la résolution, le format d'image, la durée et la génération audio. "Seedance 2.0" est pour une qualité maximale ; "Seedance 2.0 Fast" est pour une optimisation de la vitesse. |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de seed (par défaut : 0). Le nœud se réexécutera si cette valeur change, mais les résultats sont non déterministes, quel que soit le seed. |
| `watermark` | BOOLEAN | Non | `True` / `False` | Indique s'il faut ajouter un filigrane à la vidéo (par défaut : False). Il s'agit d'un paramètre avancé. |

**Note :** Le paramètre `model` est un combo dynamique. Lorsque vous sélectionnez un modèle, il révélera plusieurs sous-paramètres requis qui doivent être renseignés, notamment le prompt textuel, la résolution, le format d'image, la durée et l'option de générer de l'audio. Le texte du prompt doit comporter au moins 1 caractère après suppression des espaces.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |