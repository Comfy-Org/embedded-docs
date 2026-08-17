# Définir le Type de Réseau de Contrôle d'Union

Le nœud SetUnionControlNetType vous permet de définir le type de contrôle d'un réseau de contrôle utilisé pour le conditionnement. Il prend un réseau de contrôle existant, crée une copie modifiée de celui-ci et stocke le type de contrôle sélectionné dans cette copie, de sorte que l'original reste inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `control_net` | Le réseau de contrôle à copier et à modifier avec le type de contrôle sélectionné | CONTROL_NET | Oui | - |
| `type` | Le type de contrôle à appliquer au réseau de contrôle copié. Sélectionnez « auto » pour laisser le type de contrôle non défini, ou choisissez un type spécifique parmi les types de réseau de contrôle union disponibles (par défaut : « auto ») | COMBO | Oui | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

Remarque : lorsque `type` est « auto », la liste des types de contrôle sur le réseau de contrôle copié est effacée. Lorsqu'un type spécifique est sélectionné, le réseau de contrôle copié stocke le numéro de type correspondant.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `control_net` | La copie modifiée du réseau de contrôle avec le type de contrôle sélectionné appliqué | CONTROL_NET |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/fr.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
