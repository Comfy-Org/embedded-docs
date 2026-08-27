# EnregistrerLatent

SaveLatent enregistre les tenseurs latents sur le disque sous forme de fichiers `.latent` afin qu'ils puissent être réutilisés ou partagés ultérieurement. Il prend des échantillons latents, les écrit dans le dossier de sortie avec un nom généré automatiquement, et peut intégrer des métadonnées de workflow telles que le prompt dans le fichier enregistré. Les mêmes échantillons latents sont également transmis tels quels pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | Les échantillons latents à enregistrer sur le disque. | LATENT | Oui | - |
| `préfixe_du_nom_de_fichier` | Le préfixe utilisé pour construire le nom du fichier de sortie. Il peut inclure des sous-dossiers, par exemple « latents/ComfyUI » (par défaut : « latents/ComfyUI »). | STRING | Oui | - |
| `prompt` | Le prompt du workflow, sérialisé en JSON et stocké dans les métadonnées du fichier enregistré (paramètre masqué, fourni automatiquement). | PROMPT | Non | - |
| `extra_pnginfo` | Informations supplémentaires sur le workflow, sérialisées en JSON et stockées dans les métadonnées du fichier enregistré (paramètre masqué, fourni automatiquement). | EXTRA_PNGINFO | Non | - |

Remarque : chaque fichier enregistré est nommé à l'aide du préfixe et d'un compteur à 5 chiffres, par exemple `ComfyUI_00001_.latent`, et est placé dans le répertoire de sortie. Le fichier contient le tenseur latent et un marqueur de version du format latent. Les métadonnées sont intégrées dans le fichier enregistré uniquement lorsque la prise en charge des métadonnées est activée, c'est-à-dire lorsque ComfyUI n'est pas démarré avec l'option `--disable-metadata`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `échantillons` | Les mêmes échantillons latents que ceux fournis en entrée, transmis tels quels. | LATENT |
| `ui` | Données d'affichage de l'interface décrivant le fichier enregistré : son nom de fichier, son sous-dossier et son type de sortie (« output »). | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/fr.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
