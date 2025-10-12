> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicGuider/fr.md)

Le nœud BasicGuider crée un mécanisme de guidage simple pour le processus d'échantillonnage. Il prend un modèle et des données de conditionnement en entrée et produit un objet guideur qui peut être utilisé pour orienter le processus de génération pendant l'échantillonnage. Ce nœud fournit la fonctionnalité de guidage fondamentale nécessaire pour une génération contrôlée.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `modèle` | MODEL | requis | - | - | Le modèle à utiliser pour le guidage |
| `conditionnement` | CONDITIONING | requis | - | - | Les données de conditionnement qui guident le processus de génération |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Un objet guideur qui peut être utilisé pendant le processus d'échantillonnage pour orienter la génération |
