# Sélectionner le périphérique du modèle

Le nœud SelectModelDevice vous permet de choisir sur quel périphérique (CPU ou GPU spécifique) un modèle de diffusion s’exécute. Selon l’option sélectionnée, il restaure le périphérique d’origine du chargeur, verrouille le modèle sur le CPU, ou le déplace vers un GPU spécifique, et il gère automatiquement les conflits avec les autres nœuds multi-GPU.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion à placer sur un périphérique spécifique. | MODEL | Oui |  |
| `device` | Le périphérique cible pour le modèle. Les options sont générées dynamiquement en fonction des GPU disponibles. (défaut : « default ») | COMBO | Oui | `"default"`<br>`"cpu"`<br>`"gpu:N"` pour chaque GPU disponible (par ex. `"gpu:0"`, `"gpu:1"`, ...) |

**Détails des paramètres :**
- `"default"` : Restaure le périphérique attribué par le chargeur de modèle, même si un nœud SelectModelDevice précédent l’a modifié.
- `"cpu"` : Verrouille à la fois le périphérique de chargement et de déchargement sur le CPU.
- `"gpu:N"` : Verrouille le périphérique de chargement sur le Nième GPU disponible (par ex., `"gpu:0"` pour le premier GPU). Le périphérique de déchargement est restauré au choix d’origine du chargeur.

**Remarques importantes :**
- Les valeurs `"gpu:N"` inconnues sont acceptées au moment de la validation afin que les workflows portables n’échouent pas sur des machines avec moins de GPU. Lors de l’exécution, un périphérique indisponible entraîne le passage du modèle tel quel avec un message de journalisation.
- Si le périphérique demandé n’existe pas sur la machine actuelle (par ex., un workflow créé sur une machine à 2 GPU est ouvert sur une machine à 1 GPU), le nœud transmet le modèle tel quel et journalise un message au lieu d’échouer.
- Si le modèle est déjà sur le périphérique demandé, le nœud emprunte un chemin rapide et ne recharge pas le modèle.
- Lorsque le périphérique demandé diffère du périphérique actuel, un nouveau modèle est créé à l’aide de la fabrique de rechargement du chargeur, de sorte que le modèle renvoyé possède des poids indépendants sur le nouveau périphérique. Les chargeurs qui ne prennent pas en charge cela entraînent le passage du modèle tel quel par le nœud, avec un avertissement.
- Si le workflow a déjà appliqué MultiGPU CFG Split et que le GPU choisi correspond à l’un des clones multigpu existants, ce clone est supprimé afin que deux patchers ne se retrouvent pas liés au même périphérique.
- Placer ce nœud *après* un nœud qui a déjà consommé le modèle (par ex., un KSampler) n’est pas recommandé, car tout état modifié par le nœud précédent sera observé si le périphérique correspond à celui d’origine.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion, désormais placé sur le périphérique sélectionné. Si le périphérique était invalide ou indisponible, le modèle est transmis tel quel. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/fr.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
