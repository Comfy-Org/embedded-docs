> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxGuidance/fr.md)

## Entrées

| Paramètre | Type de données | Description |
|----------------|-----------|-------------|
| conditioning | CONDITIONING | Données de conditionnement en entrée, généralement issues d'étapes précédentes d'encodage ou de traitement |
| guidance | FLOAT | Contrôle l'influence des invites textuelles sur la génération d'images, plage ajustable de 0,0 à 100,0 |

## Sorties

| Paramètre | Type de données | Description |
|----------------|-----------|-------------|
| CONDITIONING | CONDITIONING | Données de conditionnement mises à jour, contenant la nouvelle valeur de guidance |