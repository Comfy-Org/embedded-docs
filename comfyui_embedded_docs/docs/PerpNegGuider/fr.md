> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle à utiliser pour la génération du guidage |
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif qui guide la génération vers le contenu souhaité |
| `négative` | CONDITIONING | Oui | - | Le conditionnement négatif qui éloigne la génération du contenu indésirable |
| `conditionnement vide` | CONDITIONING | Oui | - | Le conditionnement vide ou neutre utilisé comme référence de base |
| `cfg` | FLOAT | Non | 0.0 - 100.0 | L'échelle de guidage sans classifieur qui contrôle la force d'influence du conditionnement sur la génération (par défaut : 8.0) |
| `échelle nég` | FLOAT | Non | 0.0 - 100.0 | Le facteur d'échelle négative qui ajuste la force du conditionnement négatif (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `guider` | GUIDER | Un système de guidage configuré prêt à être utilisé dans le pipeline de génération |