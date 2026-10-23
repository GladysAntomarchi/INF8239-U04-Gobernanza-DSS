# Model Card — LAB13

## 1. Intended use — Uso previsto

El modelo de regresión logística apoya la priorización de casos territoriales sintéticos para revisión humana. Su función es recomendar prioridades, sin sustituir las decisiones de los responsables institucionales.

## 2. Out-of-scope use — Usos prohibidos

No está autorizado para ejecutar intervenciones automáticas, determinar elegibilidad, declarar emergencias ni tomar decisiones definitivas sobre personas o comunidades.

## 3. Data and split — Datos y partición

Se utilizaron 640 registros sintéticos con nueve columnas. La evaluación se realizó mediante una partición temporal:

- Entrenamiento: registros hasta el 24/09/2026.
- Prueba: registros desde el 25/09/2026 (160 observaciones).
- Variables excluidas del modelo: `case_id`, `received_date`, `protected_group` y `target`.

Los atributos protegidos se conservaron para evaluar diferencias entre grupos, sin incorporarlos directamente a las variables predictoras.

## 4. Global and subgroup evaluation — Evaluación del modelo

**Resultados globales de Logistic:**

| Métrica | Resultado |
|---|---:|
| Accuracy | 71.88 % |
| Recall | 71.74 % |
| Precisión | 77.65 % |
| FPR | 27.94 % |

**Resultados por grupo:**

| Grupo | Registros | Recall | FPR |
|---|---:|---:|---:|
| G1 | 101 | 65.3 % | 25.0 % |
| G2 | 59 | 79.1 % | 37.5 % |

Las brechas observadas fueron de 13.76 puntos porcentuales para recall y 12.50 para FPR.

En LAB13, las cinco puertas técnicas configuradas se superaron y el DSS generó `GO`. Esta decisión técnica requiere aprobación humana y no autoriza su aplicación a datos reales.

## 5. Green AI evidence — Evidencia computacional

En LAB12, Logistic registró un tiempo de entrenamiento de 0.0299 segundos y un tamaño de 3.56 KB, frente a 0.0340 segundos y 7.87 KB del árbol de decisión.

En LAB13, el entrenamiento registró 0.2849 segundos y una latencia de 0.0190 ms.

Son mediciones puntuales. No permiten concluir que exista un ahorro energético demostrado.

## 6. Limitations, human oversight and appeal — Limitaciones y supervisión

- El dataset es sintético y no representa poblaciones reales.
- Las diferencias entre grupos no demuestran discriminación causal.
- Algunos subgrupos interseccionales tienen pocas observaciones.
- Excluir atributos protegidos no elimina posibles sesgos indirectos.
- Toda recomendación requiere revisión humana y registro de la decisión.
- Debe existir un mecanismo para solicitar revisión o impugnar recomendaciones.

El sistema debe suspenderse si incumple los límites aprobados de desempeño, equidad o privacidad, o si no existe supervisión humana efectiva.

## 7. Owner and review date — Responsable y revisión

**Responsable propuesto:** Product Owner, con supervisión del Institutional Owner para decisiones de gobernanza e incidentes.

**Fecha de documentación:** 23/10/2026.

**Próxima revisión:** antes de cualquier despliegue y cuando existan cambios relevantes en datos, modelo o políticas.

**Evidencias:** `reports/lab12/`, `reports/lab13/deployment_decision.json` y `configs/governance.yml`.