
# Incident Postmortem — LAB13

## 1. Detección del incidente

- Fecha UTC: 2026-10-23T01:13:35.701613+00:00
- Escenario simulado: brecha de recall superior al límite permitido.
- Umbral establecido: 0.16 (16 puntos porcentuales).
- Clasificación propuesta: severidad media.
- Estado: incidente simulado; no se detectó un incumplimiento real.

## 2. Contención

Ante el incumplimiento simulado, se propone cambiar
la recomendación a REVIEW y suspender el uso operativo
hasta completar la investigación.

Responsable de ejecución: ML Engineer.
Responsable final: Institutional Owner.

## 3. Preservación de evidencias

Conservar la versión del modelo, configuración,
métricas y registro de decisiones.

Evidencias técnicas disponibles:
- configs/governance.yml
- reports/lab13/deployment_decision.json
- reports/lab12/logistic/global_metrics.json

La conservación de estas evidencias se documenta
como procedimiento propuesto.

## 4. Comunicación

El ML Engineer notificará al Institutional Owner
y consultará al equipo de datos para investigar
las diferencias de desempeño.

El Institutional Owner determinará las comunicaciones
necesarias a operadores y partes afectadas.

La comunicación se plantea como parte del simulacro;
no se realizaron notificaciones reales.

## 5. Rollback o alternativa segura

Se propone regresar a una versión previamente validada
si está disponible.

De lo contrario, utilizar revisión manual mediante
criterios documentados hasta corregir el problema.

No se ejecutó un rollback técnico real.

## 6. Acciones correctivas y responsables

| Acción propuesta | Responsable | Plazo simulado |
|---|---|---|
| Investigar la brecha de recall | Data Scientist | 2 días |
| Revisar calidad y distribución de datos | Data Engineer | 3 días |
| Evaluar ajustes y repetir auditoría | Data Scientist | 5 días |
| Verificar controles antes de reanudar | ML Engineer | 6 días |
| Revisar y autorizar el cierre | Institutional Owner | 7 días |

Los plazos son objetivos propuestos para el ejercicio,
no fechas de ejecución confirmadas.

## 7. Conclusión del simulacro

El escenario permitió documentar la respuesta prevista
ante una brecha de equidad fuera de tolerancia.

En la ejecución real de LAB13, el sistema obtuvo GO
y superó las cinco puertas técnicas configuradas.

El simulacro no demuestra que los mecanismos de
contención, comunicación o rollback se hayan
ejecutado automáticamente.

La reanudación operativa requeriría verificación de
controles y autorización institucional.

