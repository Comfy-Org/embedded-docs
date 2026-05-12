> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDQuadmaskPreprocess/fr.md)

Voici la traduction en français de la documentation du nœud VOIDQuadmaskPreprocess :

## Aperçu

Le nœud VOIDQuadmaskPreprocess prépare un masque pour l'incrustation VOID en le convertissant en un "quadmasque" spécial à quatre niveaux. Il prend un masque d'entrée, dilate éventuellement la région principale, puis quantifie les valeurs du masque en quatre niveaux distincts représentant différentes régions sémantiques (objet principal, chevauchement, zone affectée et arrière-plan). Enfin, il inverse et normalise le masque de sorte que les valeurs de sortie soient dans la plage [0, 1], où 1,0 indique la zone à supprimer et 0,0 la zone à conserver.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `mask` | MASK | Oui | N/D | Le masque d'entrée à prétraiter. |
| `dilate_width` | INT | Non | 0 à 50 (pas : 1) | Rayon de dilatation pour la région du masque principal. Une valeur de 0 signifie qu'aucune dilatation n'est appliquée. (par défaut : 0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `quadmask` | MASK | Le quadmasque prétraité avec des valeurs dans [0, 1], représentant quatre niveaux discrets : 1,0 (objet principal à supprimer), ~0,75 (chevauchement du principal et de l'affecté), ~0,50 (région affectée) et 0,0 (arrière-plan à conserver). |