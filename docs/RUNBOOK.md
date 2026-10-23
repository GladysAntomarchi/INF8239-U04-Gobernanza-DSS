
# Incident Runbook — LAB13

## 1. Detección y clasificación

El DSS debe monitorear desempeño, equidad, privacidad y funcionamiento.

Se considera una alerta cuando:
- Recall global < 0.68.
- Brecha de recall > 0.16.
- Brecha de FPR > 0.16.
- Latencia > 500 ms.
- Tamaño del modelo > 1024 KB.
- Se detectan datos prohibidos o uso no autorizado.

Clasificación propuesta:
- Alta: exposición de datos o decisiones automáticas no autorizadas.
- Media: incumplimiento de métricas o cambios relevantes en los datos.
- Baja: anomalías sin impacto confirmado.

## 2. Autoridad y contención

El ML Engineer ejecuta las medidas técnicas de contención.

El Institutional Owner es responsable final de la respuesta al incidente y autoriza la suspensión o reanudación del sistema.

Ante un incidente crítico, se suspende el uso operativo del DSS y se mantiene la revisión manual.

## 3. Preservación de evidencias

Registrar fecha, descripción, métricas, alertas, versión del modelo, configuración y acciones realizadas.

Conservar los reportes técnicos y el registro del incidente, evitando incorporar datos personales o credenciales.

## 4. Comunicación

El ML Engineer informa al Institutional Owner y consulta al equipo de datos y al área legal cuando corresponda.

El responsable institucional determina si deben notificarse operadores o personas afectadas, según el incidente y las obligaciones aplicables.

Toda comunicación debe quedar documentada.

## 5. Rollback o alternativa segura

Ante un incumplimiento crítico, detener el uso del modelo y regresar a la última versión validada, si existe.

Si no hay una versión segura disponible, utilizar la alternativa no predictiva: revisión y priorización manual mediante criterios documentados.

La reanudación requiere nuevas pruebas y autorización institucional.

## 6. Postmortem, responsable y plazo

Después del incidente, documentar:
- Causa identificada o hipótesis pendiente.
- Consecuencias y alcance.
- Acciones correctivas.
- Responsable de implementación.
- Fecha límite acordada.
- Evidencia de verificación y cierre.

El Institutional Owner supervisa el cierre y el ML Engineer coordina las acciones técnicas.

El plazo se establece según la gravedad del incidente y debe registrarse expresamente.

## Alcance

Este Runbook establece procedimientos propuestos para el DSS sintético.

Su eficacia operativa deberá evaluarse mediante el simulacro de LAB13.

