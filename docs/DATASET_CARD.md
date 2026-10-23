# Dataset Card — Unidad 04

## 1. Origen y finalidad

El archivo `data/territorial_risk_synthetic.csv` contiene datos territoriales sintéticos generados para fines académicos mediante una semilla fija.

No representa personas, localidades ni estadísticas oficiales de República Dominicana. Su finalidad es practicar validación de datos, clasificación, auditoría de equidad y gobernanza de un DSS.

## 2. Inventario de datos

El dataset contiene 640 registros sintéticos y nueve columnas.

| Columna | Descripción |
|---|---|
| `case_id` | Identificador del caso. |
| `received_date` | Fecha de registro utilizada para el corte temporal. |
| `zone` | Característica territorial del caso sintético. |
| `protected_group` | Atributo utilizado para la auditoría de equidad. |
| `age_band` | Rango de edad utilizado en el análisis interseccional. |
| `previous_incidents` | Antecedentes registrados en el caso sintético. |
| `infrastructure_score` | Indicador sintético de infraestructura. |
| `exposure` | Indicador sintético de exposición. |
| `target` | Variable objetivo de clasificación binaria. |

La variable `target` presenta un 55.2 % de casos positivos
y un 44.8 % de casos negativos.

Los grupos protegidos se distribuyen en G1 (396 registros)
y G2 (244 registros).

## 3. Minimización y privacidad

Se excluyen del entrenamiento `case_id`, `received_date`, `protected_group` y `target` como variable predictora. La variable objetivo se utiliza únicamente como etiqueta para el aprendizaje y la evaluación.

Los atributos protegidos se conservan para auditar resultados. Su acceso debe limitarse a los responsables autorizados.

La política del proyecto prohíbe incorporar identificadores directos como nombres, números de documento, correos electrónicos o teléfonos.

## 4. Retención y acceso

**Política propuesta para el ejercicio:**

- Conservar el dataset sintético mientras sea necesario para la evaluación académica y su reproducibilidad.
- Restringir el acceso de modificación a los responsables del proyecto.
- No incorporar datos personales reales al repositorio.
- Revisar la necesidad de conservación al finalizar el proyecto y aplicar las reglas institucionales correspondientes.

Estas medidas constituyen una propuesta de gobernanza; no representan controles de retención ya verificados.

## 5. Limitaciones y usos prohibidos

Los datos no permiten inferir riesgos, características o comportamientos de poblaciones reales.

Se prohíbe utilizarlos para perfiles operativos, decisiones de elegibilidad, intervenciones automáticas o declaraciones de emergencia.

**Evidencia:** `scripts/check_environment.py`, `scripts/describe_dataset.py`, `configs/governance.yml` y pruebas del proyecto.
