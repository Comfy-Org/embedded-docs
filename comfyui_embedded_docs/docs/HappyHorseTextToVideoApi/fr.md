> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Génère une vidéo à partir d'une invite textuelle en utilisant le modèle HappyHorse. Ce nœud envoie votre invite et vos paramètres à l'API HappyHorse, attend la génération de la vidéo, puis télécharge le résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | DICT | Oui | Voir Description | Un dictionnaire contenant la sélection du modèle et ses paramètres associés. Le modèle doit être `"happyhorse-1.0-t2v"`. Ce dictionnaire inclut les sous-paramètres suivants :<br><br>**`prompt`** (STRING) : La description textuelle de la vidéo que vous souhaitez générer. Prend en charge l'anglais et le chinois. (valeur par défaut : "").<br>**`resolution`** (COMBO) : La résolution de la vidéo de sortie. Options : `"720P"`, `"1080P"`.<br>**`ratio`** (COMBO) : Le rapport hauteur/largeur de la vidéo de sortie. Options : `"16:9"`, `"9:16"`, `"1:1"`, `"4:3"`, `"3:4"`.<br>**`duration`** (INT) : La durée de la vidéo en secondes. (valeur par défaut : 5, min : 3, max : 15, pas : 1). |
| `seed` | INT | Oui | 0 à 2147483647 | Graine à utiliser pour la génération. L'utilisation de la même graine avec les mêmes entrées produira le même résultat. (valeur par défaut : 0). |
| `watermark` | BOOLEAN | Non | True / False | Indique s'il faut ajouter un filigrane généré par IA au résultat. (valeur par défaut : False). |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `VIDEO` | VIDEO | Le fichier vidéo généré. |