> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/fr.md)

Le nœud CFGGuider crée un système de guidage pour contrôler le processus d'échantillonnage dans la génération d'images. Il prend un modèle ainsi que des conditionnements positifs et négatifs en entrée, puis applique une échelle de guidage sans classificateur pour orienter la génération vers le contenu souhaité tout en évitant les éléments indésirables. Ce nœud produit en sortie un objet guideur qui peut être utilisé par les nœuds d'échantillonnage pour contrôler la direction de la génération d'images.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `modèle` | MODEL | Requis | - | - | Le modèle à utiliser pour le guidage |
| `positive` | CONDITIONING | Requis | - | - | Le conditionnement positif qui guide la génération vers le contenu souhaité |
| `négative` | CONDITIONING | Requis | - | - | Le conditionnement négatif qui éloigne la génération du contenu indésirable |
| `cfg` | FLOAT | Requis | 8.0 | 0.0 - 100.0 | L'échelle de guidage sans classificateur qui contrôle la force d'influence du conditionnement sur la génération |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | Un objet guideur qui peut être transmis aux nœuds d'échantillonnage pour contrôler le processus de génération |
