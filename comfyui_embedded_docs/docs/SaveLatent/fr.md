# EnregistrerLatent

Le nœud SaveLatent enregistre les tenseurs latents sur le disque sous forme de fichiers pour une utilisation ultérieure ou un partage. Il prend des échantillons latents et les sauvegarde dans le répertoire de sortie avec des métadonnées optionnelles, y compris les informations de prompt. Le nœud gère automatiquement la dénomination et l'organisation des fichiers tout en préservant la structure des données latentes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | Les échantillons latents à sauvegarder sur le disque | LATENT | Oui | - |
| `préfixe_du_nom_de_fichier` | Le préfixe du nom de fichier de sortie (par défaut : "latents/ComfyUI") | STRING | Non | - |
| `prompt` | Informations de prompt à inclure dans les métadonnées (paramètre caché) | PROMPT | Non | - |
| `extra_pnginfo` | Informations PNG supplémentaires à inclure dans les métadonnées (paramètre caché) | EXTRA_PNGINFO | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `ui` | Fournit les informations d'emplacement du fichier pour le latent sauvegardé dans l'interface ComfyUI | UI |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/fr.md)

---
**Source fingerprint (SHA-256):** `dc7fd101c8dd93e2bcc39de64e0c39abe8e056c9e5932587fc6ce80e2fd143e8`
