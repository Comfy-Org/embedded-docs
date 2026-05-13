> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewImage/fr.md)

Voici la traduction en français de la documentation du nœud PreviewImage :

Le nœud PreviewImage est conçu pour créer des images d'aperçu temporaires. Il génère automatiquement un nom de fichier temporaire unique pour chaque image, compresse l'image à un niveau spécifié et l'enregistre dans un répertoire temporaire. Cette fonctionnalité est particulièrement utile pour générer des aperçus d'images pendant le traitement sans affecter les fichiers d'origine.

## Entrées

| Paramètre | Type de données | Description |
|-----------|-----------------|-------------|
| `images`  | `IMAGE`         | L'entrée 'images' spécifie les images à traiter et à enregistrer en tant qu'images d'aperçu temporaires. Il s'agit de l'entrée principale du nœud, qui détermine les images qui subiront le processus de génération d'aperçu. |

## Sorties

Le nœud ne possède pas de types de sortie.