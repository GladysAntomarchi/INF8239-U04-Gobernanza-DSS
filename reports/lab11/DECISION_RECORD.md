# Decision Record — LAB11

## 1. Decisión

**REVIEW — Revisión antes del despliegue.**

Se recomienda continuar con la evaluación técnica y ética del DSS sintético, sin autorizar su utilización para decisiones reales.

## 2. Evidencia

La evaluación de impacto identificó ocho riesgos documentados. Los tres de mayor prioridad fueron:

| Riesgo | Prioridad | Responsable |
|---|---:|---|
| R02 — Datos incompletos o incorrectos | 9 | Equipo de datos |
| R01 — Priorización desigual entre grupos | 8 | Equipo de datos |
| R07 — Exposición de atributos sensibles | 8 | Responsable de privacidad |

El script `lab11_impact.py` se ejecutó correctamente y las pruebas específicas finalizaron con **3 pruebas aprobadas**.

## 3. Incertidumbres y limitaciones

- Los datos utilizados son sintéticos y no representan estadísticas reales de República Dominicana.
- Las puntuaciones de riesgo corresponden a estimaciones preliminares.
- Todavía no se dispone de los resultados de equidad de LAB12.
- No se ha comprobado la eficacia operativa de todos los controles de gobernanza.

## 4. Controles y acciones requeridas

- Validar la calidad e integridad de los datos antes de utilizarlos.
- Auditar las diferencias de desempeño entre grupos.
- Restringir el acceso a los atributos protegidos.
- Mantener la supervisión humana y el mecanismo de apelación.
- Documentar los resultados y las decisiones antes de cualquier despliegue.

## 5. Responsable de la decisión

El responsable institucional del DSS debe revisar la evidencia, autorizar cualquier cambio de estado y documentar su decisión.

## 6. Condición de suspensión o retiro

El DSS debe suspenderse cuando se incumplan los límites aprobados de desempeño, equidad o privacidad, o cuando no exista supervisión humana efectiva.

**Conclusión:** continuar con LAB12 y LAB13 bajo evaluación controlada. No autorizar despliegue operativo hasta comprobar los controles y completar la evidencia pendiente.
